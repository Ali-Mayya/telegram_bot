@echo off 

set path=cd
call   %~$PATH:1 venv\scripts\activate


cd %~dp0telegram_bot


python bot_telegram.py

pause