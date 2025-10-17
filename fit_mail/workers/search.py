#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: GPL-3.0-only
# -----
######

from fit_acquisition.tasks.task_worker import TaskWorker
from PySide6.QtCore import Signal

from fit_mail.lang import load_translations


class MailSearchWorker(TaskWorker):
    finished = Signal(dict)

    def __init__(self):
        super().__init__()
        self.__translations = load_translations()

    def start(self):
        search_criteria = self.options.get("search_criteria")
        service = self.options.get("mail_service")
        fetch_time = None

        if search_criteria:
            search_criteria = service.set_criteria(
                search_criteria.get("sender"),
                search_criteria.get("recipient"),
                search_criteria.get("subject"),
                search_criteria.get("from_date"),
                search_criteria.get("to_date"),
            )

        try:
            fetch_time = service.estimate_email_fetch_time(search_criteria)

        except Exception as e:
            self.error.emit(
                {
                    "title": self.__translations["ESTIMATION_FETCH_TIME_ERROR_TITLE"],
                    "msg": self.__translations["ESTIMATION_FETCH_TIME_ERROR_MESSAGE"],
                    "details": str(e),
                }
            )
        else:
            try:
                emails = service.get_mails_from_every_folder(search_criteria)
                self.finished.emit({"fetch_time": fetch_time, "emails": emails})
            except Exception as e:
                self.error.emit(
                    {
                        "title": self.__translations["SEARCH_ERROR_TITLE"],
                        "msg": self.__translations["SEARCH_ERROR_MESSAGE"],
                        "details": str(e),
                    }
                )
