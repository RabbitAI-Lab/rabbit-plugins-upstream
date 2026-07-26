@echo off
REM Install dependencies for desktop-control skill
echo Installing dependencies...
python -m pip install -r "%~dp0..\requirements.txt"
if %ERRORLEVEL% NEQ 0 (
    echo pip install failed. Trying python3...
    python3 -m pip install -r "%~dp0..\requirements.txt"
)
if %ERRORLEVEL% NEQ 0 (
    echo Still failed. Try: py -m pip install -r "%CD%\requirements.txt"
)
echo Done.
