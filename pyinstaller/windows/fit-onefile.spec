import platform, zipfile
from pathlib import Path
from shutil import move, make_archive, rmtree

from fit_common.core import get_version
from PyInstaller.utils.hooks import collect_data_files, collect_submodules


datas = [('../../fit_mail/lang', './fit_mail/lang'), ('../../icon.ico', '.')]
datas += collect_data_files('fit_assets', includes=['icons/', 'images/', 'templates/'])
datas += collect_data_files('fit_common', includes=['lang/*.json'])
datas += collect_data_files('fit_cases', includes=['lang/*.json'])
datas += collect_data_files('fit_configurations', includes=['lang/*.json'])
datas += collect_data_files('fit_acquisition', includes=['lang/*.json'])
datas += collect_data_files('fit_scraper', includes=['lang/*.json'])

hiddenimports = []
hiddenimports += collect_submodules('fit_configurations.view.tabs')
hiddenimports += collect_submodules('fit_acquisition.tasks')


a = Analysis(
    ["..\\..\\main.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=["./pyinstaller/hooks"],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="fit-mail",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=["..\\..\\icon.ico"],
)


dist_dir = Path("dist")
exe_path = dist_dir / "fit-mail.exe"
arch = (platform.machine() or "x86_64").replace("AMD64", "x86_64")
zip_path = dist_dir / f"fit-mail-portable-{get_version()}-windows-{arch}.zip"

with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(exe_path, arcname="fit-mail.exe")

print(f"ZIP created: {zip_path}")