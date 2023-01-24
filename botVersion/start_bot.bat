@echo off
call %~dp0venv\Scripts\activate
::token with bot
set TOKEN="BOT TOKEN"
::run file with bot
python run.py
pause