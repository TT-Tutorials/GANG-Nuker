@echo off
Title Download Modules...
python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
python -m pip install -r requirements.txt
cls
Title Downloading Modules
echo python GANG.py >> start.bat
start start.bat
