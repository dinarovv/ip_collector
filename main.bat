@echo off

set "ORIG_DIR=%CD%"
cd /d "%~dp0"
pip install -r requirements.txt > nul
echo Dependency installation was successful!
echo Repo: https://github.com/dinarovv/ip_collector
pause
cls
python main.py
cd /d "%ORIG_DIR%"
cls
exit /b 0