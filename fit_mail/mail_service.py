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
from email.header import decode_header
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

    def get_mails_from_every_folder(self, search_criteria):
        # Retrieve every folder from the mailbox
        folders = []
        for folder in self.mailbox.list()[1]:
            name = folder.decode()
            if ' "/" ' in name:  # tested by zitelog on imapmail.libero.it
                name = folder.decode().split(' "/" ')[1]
            elif ' "." ' in name:  # tested by zitelog on imaps.pec.aruba.it
                name = folder.decode().split(' "." ')[1]
            else:
                name = None

            if name is not None:
                folders.append(name)

        # Scrape every message from the folders
        scraped_emails = self.fetch_messages(folders, search_criteria)
        self.__save_logs()
        return scraped_emails

    def fetch_messages(self, folders, search_criteria=None):
        scraped_emails = {}

        for folder in folders:
            try:
                self.mailbox.select(folder, readonly=True)
                type, data = self.mailbox.search(None, search_criteria)

                # Fetch every message in specified folder
                messages = data[0].split()
                for email_id in messages:
                    status, email_data = self.mailbox.fetch(
                        email_id, "BODY.PEEK[HEADER]"
                    )  # fetch just the header to speed up the process
                    email_part = email.message_from_bytes(email_data[0][1])

                    # prepare data for the dict
                    uid = str(email_id.decode("utf-8"))
                    subject = email_part.get("subject")
                    date_str = str(email_part.get("date"))
                    sender = email_part.get("from")
                    recipient = email_part.get("to")
                    dict_value = (
                        "Mittente: "
                        + sender
                        + "\nDestinatario: "
                        + recipient
                        + "\nData: "
                        + date_str
                        + "\nOggetto: "
                        + subject
                        + "\nUID: "
                        + uid
                    )
                    # add message to dict
                    if folder in scraped_emails:
                        scraped_emails[folder].append(dict_value)
                    else:
                        scraped_emails[folder] = [dict_value]
            except Exception as e:
                log_exception(e, context=get_context(self))
                debug(
                    "Logout failed",
                    str(e),
                    context=get_context(self),
                )
                raise Exception(e)
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
        # Create mail folder
        folder_dir = os.path.join(mail_dir, folder_stripped)
        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)
        self.mailbox.select(folder, readonly=True)
        try:
            status, data = self.mailbox.fetch(email_id, "(UID INTERNALDATE RFC822)")
        except Exception as e:
            log_exception(e, context=get_context(self))
            debug(
                "Logout failed",
                str(e),
                context=get_context(self),
            )
            raise Exception(e)

        if status == "OK":
            metadata = data[0][0].decode()
            raw_email = data[0][1]

            message = email.message_from_bytes(raw_email)
            sanitized_id = re.sub(r'[<>:"/\\|?*]', "", message.get("message-id")[1:-8])
            md5_hash = hashlib.md5()
            md5_hash.update(sanitized_id.encode("utf-8"))
            md5_digest = md5_hash.hexdigest()
            filename = f"{md5_digest}.eml"

            subject = self.__decode_mime_header(message.get("subject"))

            uid_start = metadata.find("UID ") + 4
            uid_end = metadata.find(" ", uid_start)
            uid = metadata[uid_start:uid_end]

            match = re.search(r'INTERNALDATE\s+"([^"]+)"', metadata)
            internal_date_str = None

            if match:
                internal_date_str = match.group(1)
            # gmail workaroud
            else:
                internal_date = self.__extract_internal_date(data)

            if internal_date_str is not None:
                internal_date = parsedate_to_datetime(internal_date_str)

            self.acquisition_emails_log += (
                "=========================================================\n"
            )
            self.acquisition_emails_log += f"Filename: {filename}\n"
            self.acquisition_emails_log += f"Subject: {subject}\n"
            self.acquisition_emails_log += f"IMAP UID: {uid}\n"
            self.acquisition_emails_log += f"Internnal Date: {internal_date}\n"

            email_path = os.path.join(folder_dir, filename)

            with open(email_path, "wb") as f:
                f.write(message.as_bytes())
            self.__save_logs()

    def __save_logs(self):
        logs_buffer = io.StringIO()
        original_stderr = sys.stderr
        sys.stderr = logs_buffer
        self.mailbox.print_log()
        self.imap_logs = self.imap_logs + "\n" + logs_buffer.getvalue()
        sys.stderr = original_stderr

    def __decode_mime_header(self, header_value):
        decoded_bytes, charset = decode_header(header_value)[0]
        if charset:
            return decoded_bytes.decode(charset)
        else:
            return decoded_bytes

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
