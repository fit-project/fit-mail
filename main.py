#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

import argparse
import sys

from fit_common.core import (
    DebugLevel,
    debug,
    resolve_path,
    set_debug_level,
    set_gui_crash_handler,
)
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMessageBox

from fit_mail.mail import Mail


def parse_args():
    parser = argparse.ArgumentParser(description="FIT Web Module")
    parser.add_argument(
        "--debug",
        choices=["none", "log", "verbose"],
        default="none",
        help="Set the debug level (default: none)",
    )
    return parser.parse_args()


def show_crash_dialog(error_message: str):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle("Application Error")
    msg_box.setText("A fatal error occurred:")
    msg_box.setDetailedText(error_message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec()


def main():
    args = parse_args()
    set_debug_level(
        {
            "none": DebugLevel.NONE,
            "log": DebugLevel.LOG,
            "verbose": DebugLevel.VERBOSE,
        }[args.debug]
    )

    app = QApplication(sys.argv)

    set_gui_crash_handler(show_crash_dialog)

    app.setWindowIcon(QtGui.QIcon(resolve_path("icon.ico")))

    window = Mail()
    if window.has_valid_case:
        window.show()
        sys.exit(app.exec())
    else:
        debug(
            "User cancelled the case form. Nothing to display.", context="Main.fit_web"
        )
        sys.exit(0)


if __name__ == "__main__":
    main()
