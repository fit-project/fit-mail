#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: GPL-3.0-only
# -----
######

import os
import re

from fit_acquisition.tasks.task import Task
from fit_acquisition.tasks.task_worker import TaskWorker
from fit_common.gui.utils import Status

from fit_mail.lang import load_translations


class TaskSaveMessagesWorker(TaskWorker):
    def start(self):
        # Create acquisition folder
        self.acquisition_mail_dir = os.path.join(
            self.options.get("acquisition_directory"), "acquisition_mail"
        )
        if not os.path.exists(self.acquisition_mail_dir):
            os.makedirs(self.acquisition_mail_dir)

        emails_to_save = self.options.get("emails_to_save")
        service = self.options.get("mail_controller")

        for folder, emails_list in emails_to_save.items():
            for emails in emails_list:
                email_id = emails.partition("UID: ")[2]
                # Create acquisition folder
                folder_stripped = re.sub(r"[^a-zA-Z0-9]+", "-", folder)
                service.write_emails(
                    email_id, self.acquisition_mail_dir, folder_stripped, folder
                )
                self.progress.emit()
        service.write_logs(self.options.get("acquisition_directory"))
        self.finished.emit()


class TaskSaveMessages(Task):
    def __init__(self, logger, progress_bar=None, status_bar=None):

        self.__translations = load_translations()

        super().__init__(
            logger,
            progress_bar,
            status_bar,
            label=self.__translations["SAVE_MESSAGES"],
        )

        self.__worker = TaskSaveMessagesWorker()
        self.__worker.started.connect(self._started)
        self.__worker.finished.connect(self._finished)
        self.__worker.error.connect(self._handle_error)

    def start(self):
        super().start_task(self.__translations["MAIL_SCRAPER_STARTED"])
        self.__worker.options = self.options
        self.__worker.start()

    def _finished(self, status=Status.SUCCESS, details=""):
        super()._finished(
            status,
            details,
            self.__translations["MAIL_SCRAPER_COMPLETED"].format(status.name),
        )
