@echo off
setlocal
title OpenClaw Watchdog - Installer (needs admin)

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [X] Please right-click this file and "Run as administrator".
    pause
    exit /b 1
)
echo [OK] Admin confirmed.
echo.

echo This installer will change the following on THIS machine:
echo   1. "OpenClaw Gateway"  task -> hidden VBS launcher (no console window)
echo   2. "OpenClaw Watchdog" task -> hidden PowerShell watchdog
echo   3. Restart ONLY the OpenClaw Gateway scheduled task
echo.
echo It will NOT kill node.exe or wscript.exe belonging to other programs.
echo To uninstall, run uninstall_watchdog_admin.bat or delete the tasks in Task Scheduler.
echo.
set /p CONFIRM=Type Y to continue: 
if /i not "%CONFIRM%"=="Y" ( echo Aborted. & pause & exit /b 1 )
echo.

set "OCX=%USERPROFILE%\.openclaw"

echo [1/4] Switching Gateway task to the hidden launcher (no CMD window)...
schtasks /Change /TN "OpenClaw Gateway" /TR "wscript.exe "%OCX%\run_gateway_silent.vbs"" >nul 2>&1
if %errorlevel% equ 0 (echo     [OK] Gateway task now uses the silent VBS launcher.) else (echo     [!] Could not change Gateway task.)
echo.

echo [2/4] Ensuring the Watchdog task runs hidden PowerShell...
schtasks /Change /TN "OpenClaw Watchdog" /TR "powershell -NoProfile -WindowStyle Hidden -File "%OCX%\workspace\watchdog.ps1"" >nul 2>&1
if %errorlevel% equ 0 (echo     [OK] Watchdog task updated.) else (echo     [!] Could not change Watchdog task.)
echo.

echo [3/4] Restarting ONLY the OpenClaw Gateway scheduled task...
schtasks /End /TN "OpenClaw Gateway" >nul 2>&1
timeout /t 2 /nobreak >nul
schtasks /Run /TN "OpenClaw Gateway" >nul 2>&1
if %errorlevel% equ 0 (
    echo     [OK] Gateway task restarted via Task Scheduler.
) else (
    echo     [!] Task restart failed. Starting the silent launcher directly instead.
    start "" wscript.exe "%OCX%\run_gateway_silent.vbs"
)
echo.

echo [4/4] Verifying...
timeout /t 5 /nobreak >nul
netstat -ano | findstr ":18789" | findstr "LISTENING" >nul 2>&1
if %errorlevel% equ 0 (echo     [OK] Gateway is listening on port 18789.) else (echo     [!] Gateway not listening yet - check logs.)
echo.
echo ============================================
echo  Done. Gateway + Watchdog run in the background.
echo  Status file: "%OCX%\watchdog-status.json"
echo  Watchdog log: "%OCX%\watchdog.log"
echo ============================================
pause
