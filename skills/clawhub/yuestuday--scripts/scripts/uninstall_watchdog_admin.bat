@echo off
setlocal
title OpenClaw Watchdog - Uninstall (needs admin)

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [X] Please right-click this file and "Run as administrator".
    pause
    exit /b 1
)

echo This will:
echo   1. Disable and delete the "OpenClaw Watchdog" scheduled task
echo   2. Stop only watchdog processes (matched by command line)
echo   3. Restore "OpenClaw Gateway" to a plain launch
echo.
set /p CONFIRM=Type Y to continue: 
if /i not "%CONFIRM%"=="Y" ( echo Aborted. & pause & exit /b 1 )
echo.

set "OCX=%USERPROFILE%\.openclaw"

echo [1/3] Removing watchdog task...
schtasks /End /TN "OpenClaw Watchdog" >nul 2>&1
schtasks /Delete /TN "OpenClaw Watchdog" /F >nul 2>&1
if %errorlevel% equ 0 (echo     [OK] Task removed.) else (echo     [!] Task not found or could not be removed.)
echo.

echo [2/3] Stopping watchdog processes...
for /f "delims=" %%P in ('powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'watchdog\.ps1' } | ForEach-Object { $_.ProcessId }"') do (
    taskkill /f /pid %%P >nul 2>&1
    echo     [OK] killed %%P
)
echo.

echo [3/3] Restoring Gateway task to direct launch...
schtasks /Change /TN "OpenClaw Gateway" /TR "\"%OCX%\gateway.cmd\"" >nul 2>&1
if %errorlevel% equ 0 (echo     [OK] Gateway task restored.) else (echo     [!] Could not restore Gateway task.)
echo.
echo Done. Optional cleanup:
echo   del "%OCX%\watchdog.log" "%OCX%\watchdog-status.json"
echo   del "%OCX%\workspace\watchdog.ps1"
echo.
pause
