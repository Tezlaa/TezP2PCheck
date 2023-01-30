# Create a venv for the bot
```
python -m venv venv
```
```
cd: .\venv\Scripts\activate
```
```
pip install -r requirements.txt
```
# Creating a file to run via .bat
Create file ``` run_bot.bat ```
### Write to a file:
```
@echo off
call %~dp0venv\Scripts\activate
::token with bot
set TOKEN= token with @botfather

python run.py
pause
```
* * *
**Start run_bot.bat file**
