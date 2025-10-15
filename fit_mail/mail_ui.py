#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_fit_mail(object):
    def setupUi(self, fit_mail):
        fit_mail.setObjectName("fit_mail")
        fit_mail.resize(800, 600)
        fit_mail.setMinimumSize(QtCore.QSize(800, 600))
        self.styleSheet = QtWidgets.QWidget(parent=fit_mail)
        self.styleSheet.setStyleSheet(
            "\n"
            "\n"
            "QWidget{\n"
            "    color: rgb(221, 221, 221);\n"
            "    font: 13px;\n"
            "}\n"
            "\n"
            "/* Tooltip */\n"
            "QToolTip {\n"
            "    color: #e06133;\n"
            "    background-color: rgba(33, 37, 43, 180);\n"
            "    border: 1px solid rgb(44, 49, 58);\n"
            "    background-image: none;\n"
            "    background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "    border: none;\n"
            "    border-left: 2px solid rgb(224, 97, 51);\n"
            "    text-align: left;\n"
            "    padding-left: 8px;\n"
            "    margin: 0px;\n"
            "}\n"
            "\n"
            "/* Bg App*/\n"
            "#bg_app {    \n"
            "    background-color: rgb(40, 44, 52);\n"
            "    border: 1px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Title Menu */\n"
            "#title_right_info { font: 13px; }\n"
            "#title_right_info { padding-left: 10px; }\n"
            "\n"
            "/* Content App */\n"
            "#content_top_bg{    \n"
            "    background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#content_bottom{\n"
            "    border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Top Buttons */\n"
            "#right_buttons_container .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#right_buttons_container .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
            "#right_buttons_container .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "\n"
            "/* Bottom Bar */\n"
            "#bottom_bar { background-color: rgb(44, 49, 58); }\n"
            "#bottom_bar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "\n"
            "\n"
            "#content .QLabel:disabled {color: rgba(255, 255, 255, 10%) }\n"
            "#content .QDateEdit:disabled {color: rgba(255, 255, 255, 10%) }\n"
            "#content .QLineEdit:disabled {color: rgba(255, 255, 255, 10%) }\n"
            "\n"
            "#content .QPushButton:disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }\n"
            "#content .QPushButton:hover { background-color: rgb(44, 49, 57);}\n"
            "#content .QPushButton:pressed { background-color: rgb(44, 49, 57);}\n"
            "#content .QPushButton {background-color: rgb(52, 59, 72); }\n"
            "\n"
            "#content .QDateEdit {\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-left: 10px;\n"
            "}\n"
            "\n"
            "#content .QDateEdit:hover {\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "#content .QDateEdit:focus {\n"
            "    border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "#content .QDateEdit::up-button, QDateEdit::down-button {\n"
            "    border: none;\n"
            "    padding-right: 5px;\n"
            "}\n"
            "\n"
            "QDateEdit::up-button {\n"
            "    subcontrol-position: top right;\n"
            "}\n"
            "\n"
            "QDateEdit::down-button {\n"
            "    subcontrol-position: bottom right;\n"
            "}\n"
            "\n"
            "/* now, the magic begins */\n"
            "\n"
            "#content .QDateEdit::up-arrow, QDateEdit::down-arrow {\n"
            '    /* a default color for the "border" (aka, the arrow) */\n'
            "    border: 5px solid white;\n"
            "\n"
            "    /* right and left borders will be transparent */\n"
            "    border-left-color: rgba(255, 255, 255, 0);\n"
            "    border-right-color: rgba(255, 255, 255, 0);\n"
            "\n"
            '    /* basic "null" size as above */\n'
            "    width: 0;\n"
            "    height: 0;\n"
            "}\n"
            "\n"
            "/* set up the up arrow states */\n"
            "\n"
            "#content .QDateEdit::up-arrow {\n"
            "    /*\n"
            '        we want to show the "down border" alone, so we make the \n'
            "        opposite one (the top) invisible and **empty**\n"
            "    */\n"
            "    border-top: none;\n"
            "}\n"
            "\n"
            "#content .QDateEdit::up-arrow:hover {\n"
            "    border-bottom-color: rgb(57, 65, 80);\n"
            "}\n"
            "\n"
            "#content .QDateEdit::up-arrow:pressed {\n"
            "    border-bottom-color: white;\n"
            "}\n"
            "\n"
            "#content .QDateEdit::up-arrow:disabled, QDateEdit::up-arrow:off {\n"
            "    /*\n"
            '        use the "mid" color role as a disabled/invalid arrow\n'
            "        state; since this rule is stated *after*, it will take\n"
            "        precedence in case it matches;\n"
            "    */\n"
            "    border-bottom-color: rgb(52, 59, 72);\n"
            "}\n"
            "\n"
            "/*\n"
            "    set up the down arrow states, similarly to the above, but\n"
            "    using the opposite border when relevant.\n"
            "*/\n"
            "\n"
            "#content .QDateEdit::down-arrow {\n"
            "    border-bottom: none;\n"
            "}\n"
            "\n"
            "#content .QDateEdit::down-arrow:hover {\n"
            "    border-bottom-color: rgb(57, 65, 80);\n"
            "}\n"
            "\n"
            "#content .QDateEdit::down-arrow:pressed {\n"
            "    border-top-color: white;\n"
            "}\n"
            "\n"
            "#content .QDateEdit::down-arrow:disabled, QDateEdit::down-arrow:off {\n"
            "    border-top-color: rgb(52, 59, 72);\n"
            "}\n"
            "\n"
            "/* LineEdit */\n"
            "QLineEdit {\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-left: 10px;\n"
            "    selection-color: rgb(255, 255, 255);\n"
            "    selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "    border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* QDateEdit */\n"
            "QDateEdit {\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-left: 10px;\n"
            "}\n"
            "\n"
            "/* ScrollBars */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 8px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(52, 59, 72);\n"
            "    min-width: 25px;\n"
            "    border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 4px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 8px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(52, 59, 72);\n"
            "    min-height: 25px;\n"
            "    border-radius: 4px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 4px;\n"
            "    border-top-right-radius: 4px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "\n"
            "QTreeView::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "    width: 15px;\n"
            "    height: 15px;\n"
            "    border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "    margin:5px 3px 5px 3px;\n"
            "}\n"
            "QTreeView::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QTreeView::indicator:checked {\n"
            "    background: 3px solid rgb(52, 59, 72);\n"
            "    border: 3px solid rgb(52, 59, 72);    \n"
            "    background-image: url(:/icons/cil-check-alt.png);\n"
            "}\n"
            "\n"
            "QTreeView::item{\n"
            "    padding-bottom: 2px;\n"
            "}\n"
            "\n"
            "/* RadioButton */\n"
            "QRadioButton::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "    width: 15px;\n"
            "    height: 15px;\n"
            "    border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QRadioButton::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QRadioButton::indicator:checked {\n"
            "    background: 3px solid rgb(94, 106, 130);\n"
            "    border: 3px solid rgb(52, 59, 72);    \n"
            "}\n"
            "\n"
            "/* ComboBox */\n"
            "QComboBox{\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-bottom: 5px;\n"
            "    padding-top: 5px;\n"
            "    padding-left: 10px;\n"
            "\n"
            "}\n"
            "QComboBox:hover{\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 25px; \n"
            "    border-left-width: 3px;\n"
            "    border-left-color: rgba(39, 44, 54, 150);\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:/icons/cil-arrow-bottom.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "\n"
            "QComboBox:!editable{\n"
            "    selection-background-color: rgb(33, 37, 43);\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    border: none;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "     padding:10px;\n"
            "    selection-background-color: rgb(33, 37, 43);\n"
            "}\n"
            ""
        )
        self.styleSheet.setObjectName("styleSheet")
        self.appMargins = QtWidgets.QVBoxLayout(self.styleSheet)
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName("appMargins")
        self.bg_app = QtWidgets.QFrame(parent=self.styleSheet)
        self.bg_app.setStyleSheet("")
        self.bg_app.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bg_app.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bg_app.setObjectName("bg_app")
        self.appLayout = QtWidgets.QHBoxLayout(self.bg_app)
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName("appLayout")
        self.content_box = QtWidgets.QFrame(parent=self.bg_app)
        self.content_box.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_box.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_box.setObjectName("content_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content_box)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.content_top_bg = QtWidgets.QFrame(parent=self.content_box)
        self.content_top_bg.setMinimumSize(QtCore.QSize(0, 50))
        self.content_top_bg.setMaximumSize(QtCore.QSize(16777215, 50))
        self.content_top_bg.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_top_bg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_top_bg.setObjectName("content_top_bg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content_top_bg)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_box = QtWidgets.QFrame(parent=self.content_top_bg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_box.sizePolicy().hasHeightForWidth())
        self.left_box.setSizePolicy(sizePolicy)
        self.left_box.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.left_box.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_box.setObjectName("left_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.left_box)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_container = QtWidgets.QFrame(parent=self.left_box)
        self.logo_container.setMinimumSize(QtCore.QSize(60, 0))
        self.logo_container.setMaximumSize(QtCore.QSize(60, 16777215))
        self.logo_container.setObjectName("logo_container")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.logo_container)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.top_logo = QtWidgets.QLabel(parent=self.logo_container)
        self.top_logo.setMinimumSize(QtCore.QSize(42, 42))
        self.top_logo.setMaximumSize(QtCore.QSize(42, 42))
        self.top_logo.setText("")
        self.top_logo.setPixmap(QtGui.QPixmap(":/images/images/logo-42x42.png"))
        self.top_logo.setObjectName("top_logo")
        self.horizontalLayout_8.addWidget(self.top_logo)
        self.horizontalLayout_3.addWidget(self.logo_container)
        self.title_right_info = QtWidgets.QLabel(parent=self.left_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.title_right_info.sizePolicy().hasHeightForWidth()
        )
        self.title_right_info.setSizePolicy(sizePolicy)
        self.title_right_info.setMaximumSize(QtCore.QSize(16777215, 45))
        self.title_right_info.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.title_right_info.setObjectName("title_right_info")
        self.horizontalLayout_3.addWidget(self.title_right_info)
        self.horizontalLayout.addWidget(self.left_box)
        self.right_buttons_container = QtWidgets.QFrame(parent=self.content_top_bg)
        self.right_buttons_container.setMinimumSize(QtCore.QSize(0, 28))
        self.right_buttons_container.setStyleSheet("font-size:18px;")
        self.right_buttons_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.right_buttons_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.right_buttons_container.setObjectName("right_buttons_container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.right_buttons_container)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.acquisition_info = QtWidgets.QPushButton(
            parent=self.right_buttons_container
        )
        self.acquisition_info.setMinimumSize(QtCore.QSize(28, 28))
        self.acquisition_info.setMaximumSize(QtCore.QSize(28, 28))
        self.acquisition_info.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.acquisition_info.setStyleSheet("QToolTip {font:13px;}")
        self.acquisition_info.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("fit_mail/ui/../icons/info-circle.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        icon.addPixmap(
            QtGui.QPixmap("fit_mail/ui/../icons/info-circle-disabled.png"),
            QtGui.QIcon.Mode.Disabled,
            QtGui.QIcon.State.On,
        )
        self.acquisition_info.setIcon(icon)
        self.acquisition_info.setIconSize(QtCore.QSize(20, 20))
        self.acquisition_info.setObjectName("acquisition_info")
        self.horizontalLayout_2.addWidget(self.acquisition_info)
        self.case_button = QtWidgets.QPushButton(parent=self.right_buttons_container)
        self.case_button.setMinimumSize(QtCore.QSize(28, 28))
        self.case_button.setMaximumSize(QtCore.QSize(28, 28))
        self.case_button.setStyleSheet("QToolTip {font:13px;}")
        self.case_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_case.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_case-disabled.png"),
            QtGui.QIcon.Mode.Disabled,
            QtGui.QIcon.State.On,
        )
        self.case_button.setIcon(icon1)
        self.case_button.setIconSize(QtCore.QSize(20, 20))
        self.case_button.setObjectName("case_button")
        self.horizontalLayout_2.addWidget(self.case_button)
        self.line = QtWidgets.QFrame(parent=self.right_buttons_container)
        self.line.setMinimumSize(QtCore.QSize(0, 40))
        self.line.setMaximumSize(QtCore.QSize(16777215, 40))
        self.line.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.configuration_button = QtWidgets.QPushButton(
            parent=self.right_buttons_container
        )
        self.configuration_button.setMinimumSize(QtCore.QSize(28, 28))
        self.configuration_button.setMaximumSize(QtCore.QSize(28, 28))
        self.configuration_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.configuration_button.setStyleSheet("QToolTip {font:13px;}")
        self.configuration_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_settings.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_settings-disabled.png"),
            QtGui.QIcon.Mode.Disabled,
            QtGui.QIcon.State.On,
        )
        self.configuration_button.setIcon(icon2)
        self.configuration_button.setIconSize(QtCore.QSize(20, 20))
        self.configuration_button.setObjectName("configuration_button")
        self.horizontalLayout_2.addWidget(self.configuration_button)
        self.minimize_button = QtWidgets.QPushButton(
            parent=self.right_buttons_container
        )
        self.minimize_button.setMinimumSize(QtCore.QSize(28, 28))
        self.minimize_button.setMaximumSize(QtCore.QSize(28, 28))
        self.minimize_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.minimize_button.setToolTip("")
        self.minimize_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_minimize.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_minimize-disabled.png"),
            QtGui.QIcon.Mode.Disabled,
            QtGui.QIcon.State.On,
        )
        self.minimize_button.setIcon(icon3)
        self.minimize_button.setIconSize(QtCore.QSize(20, 20))
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_2.addWidget(self.minimize_button)
        self.close_button = QtWidgets.QPushButton(parent=self.right_buttons_container)
        self.close_button.setMinimumSize(QtCore.QSize(28, 28))
        self.close_button.setMaximumSize(QtCore.QSize(28, 28))
        self.close_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.close_button.setToolTip("")
        self.close_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_close.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.On,
        )
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_close-disabled.png"),
            QtGui.QIcon.Mode.Disabled,
            QtGui.QIcon.State.On,
        )
        self.close_button.setIcon(icon4)
        self.close_button.setIconSize(QtCore.QSize(20, 20))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)
        self.horizontalLayout.addWidget(
            self.right_buttons_container, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout_2.addWidget(self.content_top_bg)
        self.content_bottom = QtWidgets.QFrame(parent=self.content_box)
        self.content_bottom.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_bottom.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_bottom.setObjectName("content_bottom")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.content_bottom)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.content = QtWidgets.QFrame(parent=self.content_bottom)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.left_content = QtWidgets.QFrame(parent=self.content)
        self.left_content.setMaximumSize(QtCore.QSize(370, 16777215))
        self.left_content.setObjectName("left_content")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.left_content)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.server_configuration = QtWidgets.QFrame(parent=self.left_content)
        self.server_configuration.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.server_configuration.setObjectName("server_configuration")
        self.server_configuration_vlayout = QtWidgets.QVBoxLayout(
            self.server_configuration
        )
        self.server_configuration_vlayout.setContentsMargins(-1, 5, -1, 0)
        self.server_configuration_vlayout.setObjectName("server_configuration_vlayout")
        self.sever_configuration_title = QtWidgets.QLabel(
            parent=self.server_configuration
        )
        self.sever_configuration_title.setStyleSheet("")
        self.sever_configuration_title.setObjectName("sever_configuration_title")
        self.server_configuration_vlayout.addWidget(self.sever_configuration_title)
        self.login = QtWidgets.QLineEdit(parent=self.server_configuration)
        self.login.setMinimumSize(QtCore.QSize(0, 30))
        self.login.setText("")
        self.login.setObjectName("login")
        self.server_configuration_vlayout.addWidget(self.login)
        self.password = QtWidgets.QLineEdit(parent=self.server_configuration)
        self.password.setMinimumSize(QtCore.QSize(0, 30))
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.server_configuration_vlayout.addWidget(self.password)
        self.server_name = QtWidgets.QLineEdit(parent=self.server_configuration)
        self.server_name.setMinimumSize(QtCore.QSize(0, 30))
        self.server_name.setObjectName("server_name")
        self.server_configuration_vlayout.addWidget(self.server_name)
        self.server_port = QtWidgets.QLineEdit(parent=self.server_configuration)
        self.server_port.setMinimumSize(QtCore.QSize(0, 30))
        self.server_port.setText("")
        self.server_port.setObjectName("server_port")
        self.server_configuration_vlayout.addWidget(self.server_port)
        self.login_button_layout = QtWidgets.QHBoxLayout()
        self.login_button_layout.setContentsMargins(-1, -1, -1, 10)
        self.login_button_layout.setObjectName("login_button_layout")
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.login_button_layout.addItem(spacerItem)
        self.login_button = QtWidgets.QPushButton(parent=self.server_configuration)
        self.login_button.setEnabled(True)
        self.login_button.setMinimumSize(QtCore.QSize(150, 30))
        self.login_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.login_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.login_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.login_button.setStyleSheet("")
        self.login_button.setIconSize(QtCore.QSize(0, 0))
        self.login_button.setObjectName("login_button")
        self.login_button_layout.addWidget(self.login_button)
        self.server_configuration_vlayout.addLayout(self.login_button_layout)
        self.verticalLayout_9.addWidget(self.server_configuration)
        self.search_criteria = QtWidgets.QFrame(parent=self.left_content)
        self.search_criteria.setEnabled(True)
        self.search_criteria.setMaximumSize(QtCore.QSize(16777215, 283))
        self.search_criteria.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.search_criteria.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.search_criteria.setObjectName("search_criteria")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.search_criteria)
        self.verticalLayout_11.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.search_criteria_title = QtWidgets.QLabel(parent=self.search_criteria)
        self.search_criteria_title.setEnabled(True)
        self.search_criteria_title.setStyleSheet("")
        self.search_criteria_title.setObjectName("search_criteria_title")
        self.verticalLayout_11.addWidget(self.search_criteria_title)
        self.search_date_layout = QtWidgets.QHBoxLayout()
        self.search_date_layout.setObjectName("search_date_layout")
        self.label_from_date = QtWidgets.QLabel(parent=self.search_criteria)
        self.label_from_date.setEnabled(True)
        self.label_from_date.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_from_date.setWordWrap(False)
        self.label_from_date.setObjectName("label_from_date")
        self.search_date_layout.addWidget(self.label_from_date)
        self.search_date_from = QtWidgets.QDateEdit(parent=self.search_criteria)
        self.search_date_from.setEnabled(True)
        self.search_date_from.setMinimumSize(QtCore.QSize(100, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.WindowText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(221, 221, 221))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive,
            QtGui.QPalette.ColorRole.ButtonText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.WindowText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled,
            QtGui.QPalette.ColorRole.ButtonText,
            brush,
        )
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush
        )
        self.search_date_from.setPalette(palette)
        self.search_date_from.setDateTime(
            QtCore.QDateTime(QtCore.QDate(1999, 12, 31), QtCore.QTime(12, 0, 0))
        )
        self.search_date_from.setTimeSpec(QtCore.Qt.TimeSpec.UTC)
        self.search_date_from.setObjectName("search_date_from")
        self.search_date_layout.addWidget(self.search_date_from)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.search_date_layout.addItem(spacerItem1)
        self.label_to_date = QtWidgets.QLabel(parent=self.search_criteria)
        self.label_to_date.setEnabled(True)
        self.label_to_date.setObjectName("label_to_date")
        self.search_date_layout.addWidget(self.label_to_date)
        self.search_date_to = QtWidgets.QDateEdit(parent=self.search_criteria)
        self.search_date_to.setEnabled(True)
        self.search_date_to.setMinimumSize(QtCore.QSize(100, 30))
        self.search_date_to.setCalendarPopup(False)
        self.search_date_to.setObjectName("search_date_to")
        self.search_date_layout.addWidget(self.search_date_to)
        self.verticalLayout_11.addLayout(self.search_date_layout)
        self.search_email_from = QtWidgets.QLineEdit(parent=self.search_criteria)
        self.search_email_from.setEnabled(True)
        self.search_email_from.setMinimumSize(QtCore.QSize(0, 30))
        self.search_email_from.setStyleSheet("")
        self.search_email_from.setText("")
        self.search_email_from.setObjectName("search_email_from")
        self.verticalLayout_11.addWidget(self.search_email_from)
        self.search_email_to = QtWidgets.QLineEdit(parent=self.search_criteria)
        self.search_email_to.setEnabled(True)
        self.search_email_to.setMinimumSize(QtCore.QSize(0, 30))
        self.search_email_to.setText("")
        self.search_email_to.setObjectName("search_email_to")
        self.verticalLayout_11.addWidget(self.search_email_to)
        self.search_email_subject = QtWidgets.QLineEdit(parent=self.search_criteria)
        self.search_email_subject.setEnabled(True)
        self.search_email_subject.setMinimumSize(QtCore.QSize(0, 30))
        self.search_email_subject.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.search_email_subject.setText("")
        self.search_email_subject.setReadOnly(True)
        self.search_email_subject.setObjectName("search_email_subject")
        self.verticalLayout_11.addWidget(self.search_email_subject)
        self.search_button_layout = QtWidgets.QHBoxLayout()
        self.search_button_layout.setObjectName("search_button_layout")
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.search_button_layout.addItem(spacerItem2)
        self.search_button = QtWidgets.QPushButton(parent=self.search_criteria)
        self.search_button.setEnabled(True)
        self.search_button.setMinimumSize(QtCore.QSize(150, 30))
        self.search_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.search_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.search_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.search_button.setIconSize(QtCore.QSize(0, 0))
        self.search_button.setObjectName("search_button")
        self.search_button_layout.addWidget(self.search_button)
        self.verticalLayout_11.addLayout(self.search_button_layout)
        self.verticalLayout_9.addWidget(self.search_criteria)
        self.horizontalLayout_4.addWidget(self.left_content)
        self.right_content = QtWidgets.QFrame(parent=self.content)
        self.right_content.setMinimumSize(QtCore.QSize(300, 0))
        self.right_content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.right_content.setObjectName("right_content")
        self.leftContentLayout = QtWidgets.QVBoxLayout(self.right_content)
        self.leftContentLayout.setContentsMargins(5, 5, 0, 12)
        self.leftContentLayout.setObjectName("leftContentLayout")
        self.select_email = QtWidgets.QFrame(parent=self.right_content)
        self.select_email.setStyleSheet(
            "QDateEdit::up-arraow{\n" "color:red !important;\n" "}"
        )
        self.select_email.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.select_email.setObjectName("select_email")
        self.topFrameRight = QtWidgets.QVBoxLayout(self.select_email)
        self.topFrameRight.setContentsMargins(0, 0, 0, 0)
        self.topFrameRight.setObjectName("topFrameRight")
        self.email_founded_title = QtWidgets.QLabel(parent=self.select_email)
        self.email_founded_title.setEnabled(True)
        self.email_founded_title.setStyleSheet("")
        self.email_founded_title.setObjectName("email_founded_title")
        self.topFrameRight.addWidget(self.email_founded_title)
        self.emails_tree = QtWidgets.QTreeWidget(parent=self.select_email)
        self.emails_tree.setEnabled(True)
        self.emails_tree.setMinimumSize(QtCore.QSize(0, 0))
        self.emails_tree.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.emails_tree.setObjectName("emails_tree")
        self.emails_tree.headerItem().setText(0, "1")
        self.emails_tree.header().setVisible(False)
        self.emails_tree.header().setCascadingSectionResizes(False)
        self.topFrameRight.addWidget(self.emails_tree)
        self.download_button_layout = QtWidgets.QHBoxLayout()
        self.download_button_layout.setContentsMargins(-1, -1, -1, 0)
        self.download_button_layout.setObjectName("download_button_layout")
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.download_button_layout.addItem(spacerItem3)
        self.download_button = QtWidgets.QPushButton(parent=self.select_email)
        self.download_button.setEnabled(True)
        self.download_button.setMinimumSize(QtCore.QSize(150, 30))
        self.download_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.download_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.download_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.download_button.setIconSize(QtCore.QSize(0, 0))
        self.download_button.setObjectName("download_button")
        self.download_button_layout.addWidget(self.download_button)
        self.topFrameRight.addLayout(self.download_button_layout)
        self.leftContentLayout.addWidget(self.select_email)
        self.horizontalLayout_4.addWidget(self.right_content)
        self.verticalLayout_6.addWidget(self.content)
        self.bottom_bar = QtWidgets.QFrame(parent=self.content_bottom)
        self.bottom_bar.setMinimumSize(QtCore.QSize(0, 22))
        self.bottom_bar.setMaximumSize(QtCore.QSize(16777215, 22))
        self.bottom_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bottom_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottom_bar.setObjectName("bottom_bar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.credits_label = QtWidgets.QLabel(parent=self.bottom_bar)
        self.credits_label.setMaximumSize(QtCore.QSize(120, 16))
        self.credits_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.credits_label.setObjectName("credits_label")
        self.horizontalLayout_5.addWidget(self.credits_label)
        spacerItem4 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_5.addItem(spacerItem4)
        self.progress_bar = QtWidgets.QProgressBar(parent=self.bottom_bar)
        self.progress_bar.setMinimumSize(QtCore.QSize(200, 0))
        self.progress_bar.setMaximumSize(QtCore.QSize(200, 20))
        self.progress_bar.setStyleSheet(
            "QProgressBar\n"
            "{\n"
            "    color: #ffffff;\n"
            "    border-style: outset;\n"
            "border-width: 2px;\n"
            "    border-radius: 5px;\n"
            "    text-align: left;\n"
            "}\n"
            "QProgressBar::chunk\n"
            "{\n"
            "    background-color:#e06133;\n"
            "}"
        )
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.horizontalLayout_5.addWidget(self.progress_bar)
        spacerItem5 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_5.addItem(spacerItem5)
        self.status_message = QtWidgets.QLabel(parent=self.bottom_bar)
        self.status_message.setMinimumSize(QtCore.QSize(300, 0))
        self.status_message.setStyleSheet("font-size:14px;\n" "color:#ffffff;")
        self.status_message.setObjectName("status_message")
        self.horizontalLayout_5.addWidget(self.status_message)
        spacerItem6 = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_5.addItem(spacerItem6)
        self.version = QtWidgets.QLabel(parent=self.bottom_bar)
        self.version.setMaximumSize(QtCore.QSize(120, 16777215))
        self.version.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.version.setObjectName("version")
        self.horizontalLayout_5.addWidget(self.version)
        self.frame_size_grip = QtWidgets.QFrame(parent=self.bottom_bar)
        self.frame_size_grip.setMinimumSize(QtCore.QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_5.addWidget(self.frame_size_grip)
        self.verticalLayout_6.addWidget(self.bottom_bar)
        self.verticalLayout_2.addWidget(self.content_bottom)
        self.appLayout.addWidget(self.content_box)
        self.appMargins.addWidget(self.bg_app)
        fit_mail.setCentralWidget(self.styleSheet)

        self.retranslateUi(fit_mail)
        QtCore.QMetaObject.connectSlotsByName(fit_mail)

    def retranslateUi(self, fit_mail):
        _translate = QtCore.QCoreApplication.translate
        fit_mail.setWindowTitle(_translate("fit_mail", "FIT Mail Scaper"))
        self.title_right_info.setText(_translate("fit_mail", "Mail Scraper"))
        self.acquisition_info.setToolTip(_translate("fit_mail", "Acquisition info"))
        self.case_button.setToolTip(_translate("fit_mail", "Case info"))
        self.configuration_button.setToolTip(_translate("fit_mail", "Configuration"))
        self.sever_configuration_title.setText(
            _translate("fit_mail", "Server configuration")
        )
        self.login.setPlaceholderText(_translate("fit_mail", "example@example.com"))
        self.password.setPlaceholderText(_translate("fit_mail", "password"))
        self.server_name.setPlaceholderText(_translate("fit_mail", "imap.server.com"))
        self.server_port.setPlaceholderText(_translate("fit_mail", "993"))
        self.login_button.setText(_translate("fit_mail", "Login"))
        self.search_criteria_title.setText(_translate("fit_mail", "Search criteria"))
        self.label_from_date.setText(_translate("fit_mail", "From date"))
        self.label_to_date.setText(_translate("fit_mail", "To date"))
        self.search_email_from.setPlaceholderText(_translate("fit_mail", "From:"))
        self.search_email_to.setPlaceholderText(_translate("fit_mail", "To:"))
        self.search_email_subject.setPlaceholderText(_translate("fit_mail", "Subject:"))
        self.search_button.setText(_translate("fit_mail", "Search"))
        self.email_founded_title.setText(_translate("fit_mail", "Select e-mail"))
        self.download_button.setText(_translate("fit_mail", "Download"))
        self.credits_label.setText(_translate("fit_mail", "By: fit-project.org"))
        self.status_message.setText(_translate("fit_mail", "status message"))
        self.version.setText(_translate("fit_mail", "v1.0.3"))
