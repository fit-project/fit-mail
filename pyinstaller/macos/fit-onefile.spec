import runpy
import os
import stat
import subprocess
from pathlib import Path
from shutil import copy, move
from fit_common.core import get_version
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

version_value = get_version()
version_file_path = Path("./_version.py")
version_file_path.write_text(f'__version__ = "{version_value}"\n', encoding="utf-8")



datas = [('../../fit_mail/lang', './fit_mail/lang'), ('../../icon.ico', '.')]
datas += collect_data_files('fit_assets', includes=['icons/', 'images/', 'templates/'])
datas += collect_data_files('fit_common', includes=['lang/*.json'])
datas += collect_data_files('fit_cases', includes=['lang/*.json'])
datas += collect_data_files('fit_configurations', includes=['lang/*.json'])
datas += collect_data_files('fit_acquisition', includes=['lang/*.json'])
datas += collect_data_files('fit_scraper', includes=['lang/*.json'])

datas.append(("../../_version.py", "."))

hiddenimports = []
hiddenimports += collect_submodules('fit_configurations.view.tabs')
hiddenimports += collect_submodules('fit_acquisition.tasks')

a = Analysis(
    ['../../main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=["./pyinstaller/hooks"],
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
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['../icon.png'],
)
app = BUNDLE(
    exe,
    name='FitMail.app',
    icon='../icon.icns',
    bundle_identifier="org.fit-project.fit",
    version=version_value,
)

dmg_folder = Path("./dist/fit_dmg")
os.makedirs(dmg_folder, exist_ok=True)
move("./dist/FitMail.app", dmg_folder / "FitMail.app")

dmg_file = dmg_folder / f"fit-mail-portable-{version_value}-macos-{os.uname().machine}.dmg"

print("Building", dmg_file)
try:
    os.symlink("/Applications", dmg_folder / "Applications")

    subprocess.run([
        "hdiutil", "create", 
        "-volname", "FitMailApp", 
        "-srcfolder", str(dmg_folder), 
        "-ov", "-format", "UDZO", 
        str(dmg_file)
    ], check=True)
except FileExistsError:
    print("The symbolic link already exists.")
except subprocess.CalledProcessError as e:
    print(f"Error while creating the DMG: {e}")
except Exception as e:
    print(f"Unexpected error while creating the DMG: {e}")

finally:
    if version_file_path.exists():
        version_file_path.unlink()
        print(f"Rimosso {version_file_path}")