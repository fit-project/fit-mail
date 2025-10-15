import json
import locale
from pathlib import Path

LANG_DIR = Path(__file__).parent
DEFAULT_LANG = "en"


def get_system_lang():
    try:
        locale.setlocale(locale.LC_ALL, "")
        lang = locale.getlocale()[0]
        return (lang or DEFAULT_LANG).split("_")[0]
    except Exception:
        return DEFAULT_LANG


def load_translations(lang=None):
    lang = lang or get_system_lang()
    filename = f"{lang}.json"
    path = LANG_DIR / filename

    if not path.exists():
        path = LANG_DIR / f"{DEFAULT_LANG}.json"

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
