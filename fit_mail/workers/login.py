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


class MailLoginWorker(TaskWorker):
    def __init__(self):
        super().__init__()
        self.__translations = load_translations()

    def start(self):
        auth_info = self.options.get("auth_info")
        service = self.options.get("mail_service")
        try:
            if service.mailbox is None:
                service.check_server(auth_info.get("server"), auth_info.get("port"))

            if service.is_logged_in is False:
                service.check_login(auth_info.get("email"), auth_info.get("password"))

            self.finished.emit()

        except Exception as e:
            self.error.emit(
                {
                    "title": self.__translations["SERVER_ERROR_TITLE"],
                    "msg": self.__translations["SERVER_ERROR_MESSAGE"],
                    "details": str(e),
                }
            )
        except Exception as e:
            self.error.emit(
                {
                    "title": self.__translations["LOGIN_ERROR_TITLE"],
                    "msg": self.__translations["LOGIN_ERROR_MESSAGE"],
                    "details": str(e),
                }
            )
