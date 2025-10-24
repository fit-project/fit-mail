# -*- mode: python ; coding: utf-8 -*-

import os
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, collect_dynamic_libs
from fit_common.core import get_version

# Version file (come su macOS)
version_value = get_version()
version_file_path = Path("./_version.py")
version_file_path.write_text(f'__version__ = "{version_value}"\n', encoding="utf-8")

# --- DATI E RISORSE ---
datas = [
    ('../../fit_mail/lang', 'fit_mail/lang'),
    ('./icon.png', '.'),
    ('../../_version.py', '.'),
]

# Lingue condivise (come nel tuo spec macOS)
datas += collect_data_files('fit_assets', includes=['icons/', 'images/', 'templates/'])
datas += collect_data_files('fit_common', includes=['lang/*.json'])
datas += collect_data_files('fit_cases', includes=['lang/*.json'])
datas += collect_data_files('fit_configurations', includes=['lang/*.json'])
datas += collect_data_files('fit_acquisition', includes=['lang/*.json'])
datas += collect_data_files('fit_scraper', includes=['lang/*.json'])


datas += collect_data_files('PySide6', includes=['Qt/plugins/**', 'Qt/translations/**', 'Qt/resources/**'])

# --- HIDDEN IMPORTS ---
hiddenimports = []
hiddenimports += collect_submodules('fit_configurations.view.tabs')
hiddenimports += collect_submodules('fit_acquisition.tasks')

# PySide6 moduli caricati dinamicamente
hiddenimports += collect_submodules('PySide6')

# --- LIBRARIE DINAMICHE (Qt) ---
binaries = []
binaries += collect_dynamic_libs('PySide6')

a = Analysis(
    ['../../main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=["./pyinstaller/hooks"],  # se hai hook custom
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='fit-mail',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['./icon.png'],
)