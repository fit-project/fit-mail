# !/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

import logging
from datetime import date, timedelta

from fit_acquisition.class_names import class_names
from fit_common.core import get_version
from fit_common.gui.clickable_label import ClickableLabel
from fit_common.gui.error import Error
from fit_common.gui.spinner import Spinner
from fit_scraper.scraper import Scraper
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QDate

from fit_mail.lang import load_translations
from fit_mail.mail_service import MailService
from fit_mail.mail_ui import Ui_fit_mail
from fit_mail.workers.login import MailLoginWorker
from fit_mail.workers.logout import MailLogoutWorker
from fit_mail.workers.search import MailSearchWorker


class Mail(Scraper):
    def __init__(self, wizard=None):
        logger = logging.getLogger("scraper.mail")
        packages = ["fit_mail.tasks"]

        super().__init__(logger, "email", packages, wizard)

        if self.has_valid_case:
            class_names.register("SAVE_MESSAGES", "TaskSaveMessages")
            self.acquisition.stop_tasks = [class_names.SAVE_MESSAGES]
            self.__translations = load_translations()
            self.__mail_service = None
            self._is_logged_in = False
            self.__init_ui()

    def __init_ui(self):
        # HIDE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui = Ui_fit_mail()
        self.ui.setupUi(self)
        self.__spinner = Spinner(self)

        # CUSTOM TOP BAR
        self.ui.left_box.mouseMoveEvent = self.move_window

        # MINIMIZE BUTTON
        self.ui.minimize_button.clicked.connect(self.showMinimized)

        # CLOSE BUTTON
        self.ui.close_button.clicked.connect(self.close)

        # CONFIGURATION BUTTON
        self.ui.configuration_button.clicked.connect(self.configuration_dialog)

        # CASE BUTTON
        self.ui.case_button.clicked.connect(self.show_case_info)

        # HIDE PROGRESS BAR
        self.ui.progress_bar.setHidden(True)

        # HIDE STATUS MESSAGE
        self.ui.status_message.setHidden(True)

        # SET VERSION
        self.ui.version.setText(f"v{get_version()}")

        # ADD GUIDE LINK
        self.ui.server_configuration_vlayout.addWidget(
            ClickableLabel(
                self.__translations["TWO_FACTOR_AUTH_URL"],
                self.__translations["TWO_FACTOR_AUTH"],
            )
        )

        # SERVER INPUT FIELDS
        self.ui.server_configuration_fields = self.ui.server_configuration.findChildren(
            QtWidgets.QLineEdit
        )
        for field in self.ui.server_configuration_fields:
            field.textChanged.connect(self.__enable_login_button)
            if field.objectName() == "server_port":
                field.setValidator(QtGui.QIntValidator())
            elif field.objectName() == "server_name":
                field.textEdited.connect(self.__validate_input)

        # LOGIN BUTTON
        self.ui.login_button.clicked.connect(self.__on_login_logout_clicked)
        self.ui.login_button.setEnabled(False)

        # SEARCH CRITERIA
        self.__enable_all(self.ui.search_criteria.children(), False)

        # SEARCH DATE FROM
        self.ui.search_date_from.setDate(QtCore.QDate.currentDate().addDays(-14))

        # SEARCH DATE TO
        self.ui.search_date_to.setDate(QtCore.QDate.currentDate())

        # SEARCH EMAIL FROM
        self.ui.search_email_from.textChanged.connect(self.__is_valid_search_mail)
        self.ui.search_email_from.editingFinished.connect(self.__enable_search_button)

        # SEARCH EMAIL TO
        self.ui.search_email_to.textChanged.connect(self.__is_valid_search_mail)
        self.ui.search_email_to.editingFinished.connect(self.__enable_search_button)

        # SEARCH BUTTON
        self.ui.search_button.clicked.connect(self.__search)

        # EMAIL FOUNDED
        self.__enable_all(self.ui.select_email.children(), False)
        self.ui.emails_tree.setHeaderLabel("")
        self.ui.emails_tree.itemChanged.connect(self.__on_item_changed)

        # save_messages BUTTON
        self.ui.save_messages_button.clicked.connect(self.__save_messages)
        self.ui.save_messages_button.setText(
            self.__translations["SAVE_MESSAGES_BUTTON"]
        )

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def move_window(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def __on_login_logout_clicked(self):
        if self._is_logged_in:
            self.__logout()
        else:
            self.__login()

    def __login(self):
        self.setEnabled(False)
        self.__spinner.start()
        self.__mail_service = MailService()
        self._thread: QtCore.QThread | None = None
        self._worker: MailLoginWorker | None = None

        self._thread = QtCore.QThread()
        self._worker = MailLoginWorker()

        self._worker.options = dict()

        self._worker.options = {
            "auth_info": {
                "server": self.ui.server_name.text(),
                "port": self.ui.server_port.text(),
                "email": self.ui.login.text(),
                "password": self.ui.password.text(),
            },
            "mail_service": self.__mail_service,
        }

        self._worker.moveToThread(self._thread)

        self._thread.started.connect(self._worker.start)
        self._worker.finished.connect(self.__is_logged_in)
        self._worker.error.connect(self.__handle_error)

        # Pulizia quando il thread finisce
        self._worker.finished.connect(self._thread.quit)
        self._thread.finished.connect(self._thread.deleteLater)
        self._worker.finished.connect(self._worker.deleteLater)

        self._worker.error.connect(self._thread.quit)
        self._worker.error.connect(self._worker.deleteLater)

        self._thread.start()

    def __is_logged_in(self):
        self.setEnabled(True)
        self.__spinner.stop()
        self._is_logged_in = True
        self.ui.login_button.setText(self.__translations["LOGOUT_BUTTON"])

        dialog = Error(
            QtWidgets.QMessageBox.Icon.Information,
            self.__translations["LOGIN_SUCCESS_TITLE"],
            self.__translations["LOGIN_SUCCESS_MESSAGE"],
            "",
        )
        dialog.exec()

        self.__enable_all(self.ui.server_configuration_fields, False)
        self.__enable_all(self.ui.search_criteria.children(), True)

    def __logout(self):
        self.setEnabled(False)
        self.__spinner.start()
        self._thread: QtCore.QThread | None = None
        self._worker: MailLogoutWorker | None = None

        self._thread = QtCore.QThread()
        self._worker = MailLogoutWorker()

        self._worker.options = dict()
        self._worker.options = {
            "mail_service": self.__mail_service,
        }
        self._is_logged_in = False
        self.ui.login_button.setText(self.__translations["LOGIN_BUTTON"])
        self._worker.moveToThread(self._thread)

        self._thread.started.connect(self._worker.start)
        self._worker.finished.connect(self.__is_logged_out)
        self._worker.error.connect(self.__handle_error)

        # Pulizia quando il thread finisce
        self._worker.finished.connect(self._thread.quit)
        self._thread.finished.connect(self._thread.deleteLater)
        self._worker.finished.connect(self._worker.deleteLater)

        self._worker.error.connect(self._thread.quit)
        self._worker.error.connect(self._worker.deleteLater)

        self._thread.start()

    def __is_logged_out(self):
        self.setEnabled(True)
        self.__spinner.stop()
        self._is_logged_in = False
        self.__mail_service = None
        self.ui.status_message.setText("")
        self.ui.status_message.setHidden(True)
        self.ui.login_button.setText(self.__translations["LOGIN_BUTTON"])
        self.ui.emails_tree.clear()
        self.ui.save_messages_button.setEnabled(False)
        self.__enable_all(self.ui.server_configuration_fields, True)
        self.__enable_all(self.ui.search_criteria.children(), False)

    def __handle_error(self, error):
        self.setEnabled(True)
        self.__spinner.stop()
        dialog = Error(
            QtWidgets.QMessageBox.Icon.Critical,
            error.get("title"),
            error.get("msg"),
            error.get("details"),
        )
        dialog.exec()

    def __search(self):
        self.setEnabled(False)
        self.__spinner.start()
        self.ui.emails_tree.clear()
        self._thread: QtCore.QThread | None = None
        self._worker: MailLoginWorker | None = None

        self._thread = QtCore.QThread()
        self._worker = MailSearchWorker()

        self._worker.options = dict()

        from_date = self.ui.search_date_from.date()
        to_date = self.ui.search_date_to.date()
        selected_from_date = self.__qdate_to_date(from_date)
        selected_to_date = self.__qdate_to_date(to_date) + timedelta(days=1)

        self._worker.options = {
            "search_criteria": {
                "sender": self.ui.search_email_from.text(),
                "recipient": self.ui.search_email_to.text(),
                "subject": self.ui.search_email_subject.text(),
                "from_date": selected_from_date,
                "to_date": selected_to_date,
            },
            "mail_service": self.__mail_service,
        }

        self._worker.moveToThread(self._thread)

        self._thread.started.connect(self._worker.start)
        self._worker.finished.connect(self.__search_emails_finished)
        self._worker.error.connect(self.__handle_error)

        # Pulizia quando il thread finisce
        self._worker.finished.connect(self._thread.quit)
        self._thread.finished.connect(self._thread.deleteLater)
        self._worker.finished.connect(self._worker.deleteLater)

        self._worker.error.connect(self._thread.quit)
        self._worker.error.connect(self._worker.deleteLater)

        self._thread.start()

    def __search_emails_finished(self, result):
        self.setEnabled(True)
        self.__spinner.stop()

        emails = result.get("emails", {})
        if not emails or len(emails) == 0:
            dialog = Error(
                QtWidgets.QMessageBox.Icon.Information,
                self.__translations["NO_EMAILS_TITLE"],
                self.__translations["NO_EMAILS_MESSAGE"],
                self.__translations["CHECK_SEARCH_CRITERIA"],
            )
            dialog.exec()
            self.__enable_all(self.ui.search_criteria.children(), True)
        else:
            self.ui.status_message.setHidden(False)
            fetch_time = result.get("fetch_time", {})
            total_emails = fetch_time.get("total_emails")

            if fetch_time and fetch_time.get("estimated_time"):
                self.ui.status_message.setText(
                    self.__translations["MAIL_SCRAPER_FETCH_EMAILS"].format(
                        total_emails,
                        fetch_time.get("estimated_time"),
                    )
                )
            else:
                self.ui.status_message.setText(
                    self.__translations["MAIL_SCRAPER_FETCH_EMAILS_NO_TIME"].format(
                        total_emails
                    )
                )
            self.__enable_all(self.ui.select_email.children(), True)
            self.ui.save_messages_button.setEnabled(False)
            self.__add_emails_on_tree_widget(emails)
            self.ui.emails_tree.expandAll()

    def __add_emails_on_tree_widget(self, emails):
        self.ui.emails_tree.setHeaderLabel(self.__translations["IMAP_FOUND_EMAILS"])
        self.root = QtWidgets.QTreeWidgetItem([self.__translations["IMAP_FOLDERS"]])
        self.ui.emails_tree.addTopLevelItem(self.root)

        for key in emails:
            self.folder_tree = QtWidgets.QTreeWidgetItem([key])
            self.folder_tree.setData(
                0, QtCore.Qt.ItemDataRole.UserRole, key
            )  # add identifier to the tree items
            self.folder_tree.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
            self.root.addChild(self.folder_tree)

            for value in emails[key]:
                sub_item = QtWidgets.QTreeWidgetItem([value])
                sub_item.setData(0, QtCore.Qt.ItemDataRole.UserRole, key)
                sub_item.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
                self.folder_tree.addChild(sub_item)

        self.ui.emails_tree.expandItem(self.root)

    def __is_checked(self):
        for i in range(self.root.childCount()):
            parent = self.root.child(i)
            for k in range(parent.childCount()):
                child = parent.child(k)
                if (
                    child.checkState(0) == QtCore.Qt.CheckState.Checked
                    and self.ui.save_messages_button.isEnabled() is False
                ):
                    self.ui.save_messages_button.setEnabled(True)
            if (
                parent.checkState(0) == QtCore.Qt.CheckState.Checked
                and self.ui.save_messages_button.isEnabled() is False
            ):
                parent.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

    def __on_item_changed(self, item, column):
        child_count = item.childCount()
        for i in range(child_count):
            child = item.child(i)
            child.setCheckState(column, item.checkState(column))

        self.ui.save_messages_button.setEnabled(False)
        self.__is_checked()

    def __save_messages(self):
        self.setEnabled(True)
        self.__spinner.start()

        self.__emails_to_save_messages = {}

        emails_counter = 0
        for i in range(self.root.childCount()):
            folder = self.root.child(i)
            folder_name = folder.text(0)
            for k in range(folder.childCount()):
                email = folder.child(k)
                if email.checkState(0) == QtCore.Qt.CheckState.Checked:
                    emails_counter += 1
                    if folder_name in self.__emails_to_save_messages:
                        self.__emails_to_save_messages[folder_name].append(
                            email.text(0)
                        )
                    else:
                        self.__emails_to_save_messages[folder_name] = [email.text(0)]

        self.__spinner.stop()

        if self.create_acquisition_directory():
            self.acquisition.options = {
                "type": "email",
                "case_info": self.case_info,
                "acquisition_directory": self.acquisition_directory,
                "emails_to_save": self.__emails_to_save_messages,
                "mail_service": self.__mail_service,
            }

            self.execute_start_tasks_flow()

    def on_start_tasks_finished(self):
        self.execute_stop_tasks_flow()
        self.ui.status_message.setText("")
        self.ui.status_message.setHidden(True)

    def on_post_acquisition_finished(self):
        self.ui.emails_tree.clear()
        self.ui.save_messages_button.setEnabled(False)
        return super().on_post_acquisition_finished()

    def __is_valid_search_mail(self, text):
        self.is_valid_mail = self.__validate_mail(text)
        self.search_button.setEnabled(False)
        if self.is_valid_mail is False:
            self.sender().setStyleSheet("border: 1px solid red;")
        else:
            self.sender().setStyleSheet("")
            self.search_button.setEnabled(True)

    def __validate_mail(self, mail):
        email_validator = QtGui.QRegularExpressionValidator(
            QtCore.QRegularExpression(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}")
        )
        state = email_validator.validate(mail, 0)
        return bool(state[0] == QtGui.QRegularExpressionValidator.State.Acceptable)

    def __enable_search_button(self):
        if self.sender().text() == "" and self.ui.search_button.isEnabled() is False:
            self.is_valid_email = True
            self.sender().setStyleSheet("")
            self.ui.search_button.setEnabled(True)

    def __enable_login_button(self, text):
        if self.sender().objectName() == "login":
            self.is_valid_mail = self.__validate_mail(text)
            if self.is_valid_mail is False:
                self.sender().setStyleSheet("border: 1px solid red;")
            else:
                self.sender().setStyleSheet("")

        all_fields_filled = all(
            field.text() for field in self.ui.server_configuration_fields
        )
        self.ui.login_button.setEnabled(all_fields_filled and self.is_valid_mail)

    def __validate_input(self, text):
        sender = self.sender()
        sender.setText(text.replace(" ", ""))

    def __enable_all(self, items, enable, exclude=None):
        for item in items:
            if (
                isinstance(item, QtWidgets.QLabel)
                or isinstance(item, QtWidgets.QDateEdit)
                or isinstance(item, QtWidgets.QLineEdit)
                or isinstance(item, QtWidgets.QPushButton)
                or isinstance(item, QtWidgets.QTreeView)
                and (exclude is None or item != exclude)
            ):
                item.setEnabled(enable)

    def __qdate_to_date(self, qd: QDate | None) -> date | None:
        if qd is None:
            return None
        if hasattr(qd, "toPython"):
            return qd.toPython()
        if not qd.isValid():
            return None
        return date(qd.year(), qd.month(), qd.day())
