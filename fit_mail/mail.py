# !/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

import logging

from fit_scraper.scraper import Scraper
from PySide6 import QtCore

from fit_mail.lang import load_translations
from fit_mail.mail_ui import Ui_fit_mail


class Mail(Scraper):
    def __init__(self, wizard=None):
        logger = logging.getLogger("view.scrapers.mail.mail")
        packages = []

        super().__init__(logger, "web", packages, wizard)

        if self.has_valid_case:
            self.__translations = load_translations()
            self.__init_ui()

    def __init_ui(self):
        # HIDE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui = Ui_fit_mail()
        self.ui.setupUi(self)
