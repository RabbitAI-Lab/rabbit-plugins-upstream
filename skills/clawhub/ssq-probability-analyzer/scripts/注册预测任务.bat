@echo off
setlocal
cd /d "%~dp0"

set WD=%~dp0
set TASK=SSQ_V1_Smart
set LAUNCHER=%WD%ssq_run_v8.bat
set LOG=%WD%ssq_predict_register.log

REM Auto-elevate: if not admin, relaunch self as admin via UAC (once, no loop)
powershell -NoProfile -Command "$id=[System.Security.Principal.WindowsIdentity]::GetCurrent(); $p=New-Object System.Security.Principal.WindowsPrincipal($id); if(-not $p.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)){ try { Start-Process -FilePath '%~f0' -Verb RunAs; exit 2 } catch { Write-Host 'UAC denied, please run as administrator'; exit 3 } }"
if "%ERRORLEVEL%"=="2" exit /b
if "%ERRORLEVEL%"=="3" goto :fail

echo ============================================================
echo Register Windows scheduled task: %TASK%
echo   Mode  : SYSTEM account (runs in background, no popup)
echo   Every : weekly TUE,THU,SUN 20:10
echo   Action: %LAUNCHER%
echo ============================================================
echo.

schtasks /create /tn "%TASK%" /tr "%LAUNCHER%" /sc weekly /d TUE,THU,SUN /st 20:10 /ru SYSTEM /f
if errorlevel 1 goto :fail

echo.
echo [OK] Predict task registered. Self-check:
powershell -NoProfile -Command "$t=Get-ScheduledTask -TaskName '%TASK%' -ErrorAction Stop; $i=Get-ScheduledTaskInfo -TaskName '%TASK%'; Write-Host ('  UserId  : '+$t.Principal.UserId); Write-Host ('  Trigger : '+$t.Triggers[0].StartBoundary); Write-Host ('  State   : '+$t.State); Write-Host ('  NextRun : '+$i.NextRunTime); Write-Host ('  Command : '+$t.Actions[0].Execute)"
echo.
echo View   : schtasks /query /tn %TASK%
echo Run now: schtasks /run /tn %TASK%
echo Delete : schtasks /delete /tn %TASK% /f
echo.
echo %date% %time% [OK] SSQ_V1_Smart registered, SYSTEM weekly TUE,THU,SUN 20:10 >> "%LOG%"
goto :done

:fail
echo.
echo [FAILED] Registration failed. Please run this .bat as Administrator:
echo   Right-click  -> Run as administrator, and accept the UAC prompt.
echo.
echo %date% %time% [FAIL] SSQ_V1_Smart registration failed >> "%LOG%"

:done
pause
