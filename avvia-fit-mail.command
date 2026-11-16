#!/bin/bash
cd "$(dirname "$0")"
if command -v poetry >/dev/null; then poetry run python main.py; else python3.12 -m poetry run python main.py; fi
