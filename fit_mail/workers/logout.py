#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: GPL-3.0-only
# -----
######

from fit_acquisition.tasks.task_worker import TaskWorker

from fit_mail.lang import load_translations


class MailLogoutWorker(TaskWorker):
    def __init__(self):
        super().__init__()
        self.__translations = load_translations()

    def start(self):
        service = self.options.get("mail_service")
        try:
            service.logout()
            self.finished.emit()
        except Exception as e:
            self.error.emit(
                {
                    "title": self.__translations["LOGOUT_ERROR_TILE"],
                    "msg": self.__translations["LOGOUT_ERROR_MESSAGE"],
                    "details": str(e),
                }
            )
