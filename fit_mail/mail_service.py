#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: GPL-3.0-only
# -----
######
import email
import hashlib
import imaplib
import io
import locale
import os
import re
import sys
import time
from email.header import Header, decode_header
from email.utils import parsedate_to_datetime

from fit_common.core import debug, get_context, log_exception


class MailService:
    def __init__(self):
        self.email_address = None
        self.password = None
        self.mailbox = None
        self.is_logged_in = False
        self.imap_logs = ""
        self.acquisition_emails_log = ""

    def check_server(self, server, port):
        try:
            self.mailbox = imaplib.IMAP4_SSL(server, int(port))  # imap ssl port
        except Exception as e:
            log_exception(e, context=get_context(self))
            debug(
                "Check server capture failed",
                str(e),
                context=get_context(self),
            )
            raise Exception(e)
        self.__save_logs()

    def check_login(self, email_address, password):
        self.email_address = email_address
        self.password = password
        try:
            self.mailbox.login(self.email_address, self.password)
            self.mailbox.select()
            self.is_logged_in = True
        except Exception as e:
            log_exception(e, context=get_context(self))
            debug(
                "Check login failed",
                str(e),
                context=get_context(self),
            )
            raise Exception(e)

        # Clear password after usage
        self.password = ""
        self.__save_logs()

    def logout(self):
        try:
            self.mailbox.logout()
            self.is_logged_in = False
        except Exception as e:
            log_exception(e, context=get_context(self))
            debug(
                "Logout failed",
                str(e),
                context=get_context(self),
            )
            raise Exception(e)

    def estimate_email_fetch_time(self, search_criteria):
        num_emails_test = (
            1  # number of emails used to calculate the estimated fetching time
        )
        start_time = time.time()
        self.mailbox.select(readonly=True)

        stat, email_ids = self.mailbox.search(None, search_criteria)

        emails = email_ids[0].split()
        total_emails = len(emails)

        selected_emails = email_ids[0].split()[:num_emails_test]

        for email_id in selected_emails:
            self.mailbox.fetch(email_id, "(BODY.PEEK[HEADER])")
        end_time = time.time()
        estimated_time = round(
            ((end_time - start_time) * (total_emails / num_emails_test)) / 60, 2
        )  # minutes

        self.__save_logs()
        return {"estimated_time": estimated_time, "total_emails": total_emails}

    def __quote_mailbox(self, name: str) -> str:
        if not name:
            return name
        safe = name.replace('"', r"\"")
        if re.search(r'[ (){%*"]', safe):
            return f'"{safe}"'
        return safe

    def get_mails_from_every_folder(self, search_criteria):
        typ, data = self.mailbox.list()
        if typ != "OK":
            raise Exception("LIST failed")

        def parse_list_name(raw: str) -> str | None:
            m = re.match(
                r'^\((?P<flags>[^)]*)\)\s+(?P<delim>NIL|".*?"|[^\s]+)\s+(?P<name>".*?"|[^\r\n]+)\s*$',
                raw,
            )
            if not m:
                return None
            flags = m.group("flags") or ""
            if "\\Noselect" in flags or "\\NoSelect" in flags:
                return None
            name = m.group("name").strip()

            if len(name) >= 2 and name[0] == '"' and name[-1] == '"':
                name = name[1:-1]
            return name

        folders = []
        for line in data or []:
            if not line:
                continue
            raw = line.decode("utf-8", errors="ignore")
            name = parse_list_name(raw)
            if not name:
                continue
            folders.append(name)

        scraped_emails = self.fetch_messages(folders, search_criteria or "ALL")
        self.__save_logs()
        return scraped_emails

    def fetch_messages(self, folders, search_criteria=None):
        scraped_emails = {}
        criteria = search_criteria or "ALL"

        for folder in folders or []:
            try:
                select_name = self.__quote_mailbox(folder)
                sel_typ, _ = self.mailbox.select(select_name, readonly=True)
                if sel_typ != "OK":
                    sel_typ, _ = self.mailbox.select(folder, readonly=True)
                if sel_typ != "OK":
                    debug(
                        "Impossibile selezionare la cartella",
                        folder,
                        context=get_context(self),
                    )
                    continue

                typ, data = self.mailbox.search(None, criteria)
                if typ != "OK" or not data:
                    continue

                for email_id in data[0].split():
                    status, email_data = self.mailbox.fetch(
                        email_id, "(BODY.PEEK[HEADER])"
                    )
                    if status != "OK" or not email_data:
                        continue

                    header_bytes = None
                    for part in email_data:
                        if (
                            isinstance(part, tuple)
                            and len(part) > 1
                            and isinstance(part[1], (bytes, bytearray))
                        ):
                            header_bytes = part[1]
                            break
                    if not header_bytes:
                        continue

                    email_part = email.message_from_bytes(header_bytes)

                    uid = email_id.decode("utf-8", errors="ignore")
                    subject = self.__decode_mime_header(email_part.get("subject"))
                    date_str = self.__decode_mime_header(email_part.get("date"))
                    sender = self.__decode_mime_header(email_part.get("from"))
                    recipient = self.__decode_mime_header(email_part.get("to"))

                    dict_value = (
                        f"Mittente: {sender}"
                        f"\nDestinatario: {recipient}"
                        f"\nData: {date_str}"
                        f"\nOggetto: {subject}"
                        f"\nUID: {uid}"
                    )
                    scraped_emails.setdefault(folder, []).append(dict_value)

            except Exception as e:
                log_exception(e, context=get_context(self))
                debug("fetch_messages failed", str(e), context=get_context(self))
                continue

        self.__save_logs()
        return scraped_emails

    def set_criteria(self, sender, recipient, subject, from_date, to_date):
        criteria = []
        if sender != "":
            criteria.append(f'(FROM "{sender}")')
        if recipient != "":
            criteria.append(f'(TO "{recipient}")')
        if subject != "":
            criteria.append(f'(SUBJECT "{subject}")')

        locale.setlocale(locale.LC_ALL, "en_US")

        criteria.append(
            f'(SINCE "{from_date.strftime("%d-%b-%Y")}" BEFORE "{to_date.strftime("%d-%b-%Y")}")'
        )

        # combine the search criteria
        params = " ".join(criteria)
        return params

    def write_emails(self, email_id, mail_dir, folder_stripped, folder):
        sel_typ, _ = self.mailbox.select(folder, readonly=True)
        if sel_typ != "OK":
            sel_typ, _ = self.mailbox.select(folder, readonly=False)
        if sel_typ != "OK":
            debug(
                "Impossibile selezionare la cartella", folder, context=get_context(self)
            )
            raise Exception(f"SELECT fallita per folder: {folder}")

        folder_dir = os.path.join(mail_dir, folder_stripped)
        os.makedirs(folder_dir, exist_ok=True)

        try:
            status, data = self.mailbox.fetch(email_id, "(UID INTERNALDATE RFC822)")
        except Exception as e:
            log_exception(e, context=get_context(self))
            debug(
                "fetch (UID INTERNALDATE RFC822) failed",
                str(e),
                context=get_context(self),
            )
            raise

        if status != "OK" or not data:
            raise Exception(f"FETCH fallito (status={status}, data={bool(data)})")

        meta_bytes = None
        raw_email = None
        for item in data:
            if isinstance(item, tuple) and len(item) > 1:
                meta_bytes = item[0]
                raw_email = item[1]
                break
        if not (
            isinstance(meta_bytes, (bytes, bytearray))
            and isinstance(raw_email, (bytes, bytearray))
        ):
            raise Exception("Formato FETCH inatteso: meta/raw non trovati")

        metadata = meta_bytes.decode("utf-8", errors="ignore")
        message = email.message_from_bytes(raw_email)

        subject = self.__decode_mime_header(message.get("subject"))

        m_uid = re.search(r"UID\s+(\d+)", metadata)
        uid = (
            m_uid.group(1)
            if m_uid
            else (
                email_id.decode("utf-8", errors="ignore")
                if isinstance(email_id, (bytes, bytearray))
                else str(email_id)
            )
        )

        m_date = re.search(r'INTERNALDATE\s+"([^"]+)"', metadata)
        internal_date_str = (
            m_date.group(1) if m_date else self.__extract_internal_date(data)
        )
        internal_date = None
        if internal_date_str:
            try:
                internal_date = parsedate_to_datetime(internal_date_str)
            except Exception:
                internal_date = None

        msg_id = message.get("message-id")
        if msg_id:
            sanitized_id = re.sub(r'[<>:"/\\|?*]', "", msg_id).strip()
            sanitized_id = (
                sanitized_id[:200] if len(sanitized_id) > 200 else sanitized_id
            )
            base_for_hash = sanitized_id
        else:
            base_for_hash = f"{uid}|{internal_date_str or ''}|{subject or ''}"

        md5_digest = hashlib.md5(
            base_for_hash.encode("utf-8", errors="ignore")
        ).hexdigest()
        filename = f"{md5_digest}.eml"

        email_path = os.path.join(folder_dir, filename)
        with open(email_path, "wb") as f:
            f.write(message.as_bytes())

        self.acquisition_emails_log += (
            "=========================================================\n"
        )
        self.acquisition_emails_log += f"Filename: {filename}\n"
        self.acquisition_emails_log += f"Subject: {subject}\n"
        self.acquisition_emails_log += f"IMAP UID: {uid}\n"
        self.acquisition_emails_log += f"Internal Date: {internal_date}\n"

        self.__save_logs()

    def __save_logs(self):
        logs_buffer = io.StringIO()
        original_stderr = sys.stderr
        sys.stderr = logs_buffer
        self.mailbox.print_log()
        self.imap_logs = self.imap_logs + "\n" + logs_buffer.getvalue()
        sys.stderr = original_stderr

    def __decode_mime_header(self, header_value):
        if header_value is None:
            return ""

        if isinstance(header_value, Header):
            raw = str(header_value)
        else:
            raw = str(header_value)

        try:
            parts = decode_header(raw)
        except Exception:
            return raw

        decoded = []
        for chunk, charset in parts:
            if isinstance(chunk, bytes):
                decoded.append(chunk.decode(charset or "utf-8", errors="replace"))
            else:
                decoded.append(chunk)
        return "".join(decoded)

    def write_logs(self, acquisition_directory):
        self.__write_imap_logs(acquisition_directory)
        self.__write_acquisition_emails_log(acquisition_directory)

    def __write_imap_logs(self, acquisition_directory):
        with open(os.path.join(acquisition_directory, "imap_logs.log"), "w") as f:
            f.write(self.imap_logs)

    def __write_acquisition_emails_log(self, acquisition_directory):
        with open(
            os.path.join(acquisition_directory, "acquisition_emails.log"), "w"
        ) as f:
            f.write(self.acquisition_emails_log)

    # gmail workaround
    def __extract_internal_date(self, data):
        internaldate = None
        for item in data:
            if isinstance(item, tuple):
                for part in item:
                    if isinstance(part, bytes):
                        response = part.decode("utf-8", errors="ignore")
                        match = re.search(r'INTERNALDATE\s+"([^"]+)"', response)
                        if match:
                            internaldate = match.group(1)
            elif isinstance(item, bytes):
                response = item.decode("utf-8", errors="ignore")
                match = re.search(r'INTERNALDATE\s+"([^"]+)"', response)
                if match:
                    internaldate = match.group(1)
        return internaldate
