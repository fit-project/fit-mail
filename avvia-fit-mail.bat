@echo off
cd /d "%~dp0"
where poetry >nul 2>nul
if %errorlevel%==0 (poetry run python main.py) else (py -3.12 -m poetry run python main.py)
pause
