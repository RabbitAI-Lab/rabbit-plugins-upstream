@echo off
REM ============================================================
REM DLT independent watchdog launcher
REM Called directly by Windows scheduled task DLT_Watchdog.
REM Avoids the && escaping accident inside /tr.
REM Python path is portable: prefer local WorkBuddy runtime,
REM fall back to py/python from PATH if not found.
REM ============================================================
cd /d "%~dp0"
set PYTHONUTF8=1
set "PYRUN="
if exist "C:\Users\www74\.workbuddy\binaries\python\versions\3.13.12\python.exe" (
    set "PYRUN=C:\Users\www74\.workbuddy\binaries\python\versions\3.13.12\python.exe"
) else (
    where py >nul 2>&1 && set "PYRUN=py -3" || set "PYRUN=python"
)
%PYRUN% lib\dlt_watchdog_win.py
