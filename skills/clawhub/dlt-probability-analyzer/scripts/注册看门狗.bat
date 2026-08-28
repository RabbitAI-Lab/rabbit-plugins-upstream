@echo off
setlocal
cd /d "%~dp0"

set WD=%~dp0
set TASK=DLT_Watchdog
set LAUNCHER=%WD%dlt_watchdog_launcher.bat
set LOG=%WD%dlt_watchdog_register.log

REM Auto-elevate: if not admin, relaunch self as admin via UAC (once, no loop)
powershell -NoProfile -Command "$id=[System.Security.Principal.WindowsIdentity]::GetCurrent(); $p=New-Object System.Security.Principal.WindowsPrincipal($id); if(-not $p.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)){ try { Start-Process -FilePath '%~f0' -Verb RunAs; exit 2 } catch { Write-Host 'UAC denied, please run as administrator'; exit 3 } }"
if "%ERRORLEVEL%"=="2" exit /b
if "%ERRORLEVEL%"=="3" goto :fail

echo ============================================================
echo Register Windows scheduled task: %TASK%
echo   Mode  : SYSTEM account (runs in background, no popup)
echo   Every : daily 21:30
echo   Action: %LAUNCHER%
echo ============================================================
echo.

schtasks /create /tn "%TASK%" /tr "%LAUNCHER%" /sc daily /st 21:30 /ru SYSTEM /f
if errorlevel 1 goto :fail

echo.
echo [OK] Watchdog registered. Self-check:
powershell -NoProfile -Command "$t=Get-ScheduledTask -TaskName '%TASK%' -ErrorAction Stop; $i=Get-ScheduledTaskInfo -TaskName '%TASK%'; Write-Host ('  UserId  : '+$t.Principal.UserId); Write-Host ('  Trigger : '+$t.Triggers[0].StartBoundary); Write-Host ('  State   : '+$t.State); Write-Host ('  NextRun : '+$i.NextRunTime); Write-Host ('  Command : '+$t.Actions[0].Execute)"
echo.
echo View   : schtasks /query /tn %TASK%
echo Run now: schtasks /run /tn %TASK%
echo Delete : schtasks /delete /tn %TASK% /f
echo.
echo %date% %time% [OK] DLT_Watchdog registered, SYSTEM daily 21:30 >> "%LOG%"
goto :done

:fail
echo.
echo [FAILED] Registration failed. Please run this .bat as Administrator:
echo   Right-click  -^> Run as administrator, and accept the UAC prompt.
echo.
echo %date% %time% [FAIL] DLT_Watchdog registration failed >> "%LOG%"

:done
pause
