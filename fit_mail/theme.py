#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: GPL-3.0-only
# -----
######
"""Light/dark theme support.

The UI stylesheets were authored for the dark theme with hard-coded colours.
Instead of duplicating every stylesheet, the light theme is derived by
substituting each dark colour with its light counterpart. Every stylesheet
is captured once at startup (dark) and re-rendered on theme change.
"""
import re

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QWidget

DARK = "dark"
LIGHT = "light"
_SETTINGS_KEY = "fit_mail/theme"

# dark colour -> light colour
_LIGHT_MAP = {
    "rgb(221, 221, 221)": "rgb(35, 38, 45)",  # default text
    "#ffffff": "#23262d",
    "rgb(255, 255, 255)": "rgb(35, 38, 45)",
    "rgb(23, 26, 30)": "rgb(222, 225, 230)",  # darkest bg
    "rgb(33, 37, 43)": "rgb(255, 255, 255)",  # inputs / content bg
    "rgba(33, 37, 43, 180)": "rgba(255, 255, 255, 230)",
    "rgba(39, 44, 54, 150)": "rgba(230, 233, 238, 180)",
    "rgb(40, 44, 52)": "rgb(243, 244, 247)",  # app bg
    "rgb(44, 49, 57)": "rgb(226, 229, 234)",
    "rgb(44, 49, 58)": "rgb(210, 214, 220)",  # borders
    "rgb(44, 49, 60)": "rgb(226, 229, 234)",
    "rgb(52, 59, 72)": "rgb(232, 234, 238)",
    "rgb(55, 63, 77)": "rgb(220, 223, 229)",
    "rgb(57, 65, 80)": "rgb(215, 219, 226)",
    "rgb(58, 66, 81)": "rgb(215, 219, 226)",
    "rgb(64, 71, 88)": "rgb(200, 205, 214)",
    "rgb(91, 101, 124)": "rgb(140, 150, 170)",
    "rgb(94, 106, 130)": "rgb(140, 150, 170)",
    "rgb(113, 126, 149)": "rgb(110, 120, 140)",
    # accent (#e06133) is kept in both themes
}

_PATTERN = re.compile(
    "|".join(re.escape(k) for k in sorted(_LIGHT_MAP, key=len, reverse=True))
)


def to_light(stylesheet: str) -> str:
    return _PATTERN.sub(lambda m: _LIGHT_MAP[m.group(0)], stylesheet)


def load_theme() -> str:
    return QSettings().value(_SETTINGS_KEY, DARK)


def save_theme(theme: str):
    QSettings().setValue(_SETTINGS_KEY, theme)


class ThemeManager:
    """Snapshots the dark stylesheets of a widget tree and switches theme."""

    def __init__(self, root: QWidget):
        self.__root = root
        self.__dark_sheets = {}
        for w in [root] + root.findChildren(QWidget):
            sheet = w.styleSheet()
            if sheet:
                self.__dark_sheets[w] = sheet
        self.theme = DARK

    def apply(self, theme: str):
        for widget, dark_sheet in self.__dark_sheets.items():
            widget.setStyleSheet(dark_sheet if theme == DARK else to_light(dark_sheet))
        self.theme = theme
        save_theme(theme)

    def toggle(self) -> str:
        self.apply(LIGHT if self.theme == DARK else DARK)
        return self.theme
