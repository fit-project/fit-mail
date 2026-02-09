#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

import json
from pathlib import Path

from fit_common.core import DEFAULT_LANG, get_system_lang

LANG_DIR = Path(__file__).parent


def load_translations(lang=None):
    lang = lang or get_system_lang()
    filename = f"{lang}.json"
    path = LANG_DIR / filename

    if not path.exists():
        path = LANG_DIR / f"{DEFAULT_LANG}.json"

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
