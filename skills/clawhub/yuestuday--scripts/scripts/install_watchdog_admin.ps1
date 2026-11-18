# OpenClaw Watchdog installer v3 (admin required)
$ErrorActionPreference = "Stop"
$ocx = "$env:USERPROFILE\.openclaw"
$wid = [System.Security.Principal.WindowsIdentity]::GetCurrent()
$pr = New-Object System.Security.Principal.WindowsPrincipal($wid)
if (-not $pr.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)) { Write-Host "[X] Run as Administrator."; exit 1 }
Write-Host "[OK] Admin confirmed."
$sid = $wid.User.Value
$wdPath = "$ocx\workspace\watchdog.ps1"

$wdXml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.3" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo><URI>\OpenClaw Watchdog</URI></RegistrationInfo>
  <Principals><Principal id="Author"><UserId>__SID__</UserId><LogonType>InteractiveToken</LogonType></Principal></Principals>
  <Settings>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <RestartOnFailure><Count>999</Count><Interval>PT1M</Interval></RestartOnFailure>
    <StartWhenAvailable>true</StartWhenAvailable>
    <IdleSettings><StopOnIdleEnd>false</StopOnIdleEnd><RestartOnIdle>false</RestartOnIdle></IdleSettings>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
  </Settings>
  <Triggers><LogonTrigger /></Triggers>
  <Actions Context="Author"><Exec><Command>powershell</Command>
    <Arguments>-NoProfile -WindowStyle Hidden -File __WD__</Arguments></Exec></Actions>
</Task>
"@

$guardArgs = @'
-NoProfile -WindowStyle Hidden -Command "$p = Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like ''*watchdog.ps1*'' }; if (-not $p) { Start-Process powershell -ArgumentList ''-NoProfile'',''-WindowStyle'',''Hidden'',''-File'',''__WD__'' -WindowStyle Hidden }"
'@
$guardArgs = $guardArgs.Trim()
$gXml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.3" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo><URI>\OpenClaw Watchdog Guard</URI></RegistrationInfo>
  <Principals><Principal id="Author"><UserId>__SID__</UserId><LogonType>InteractiveToken</LogonType></Principal></Principals>
  <Settings>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <StartWhenAvailable>true</StartWhenAvailable>
    <ExecutionTimeLimit>PT5M</ExecutionTimeLimit>
    <IdleSettings><StopOnIdleEnd>false</StopOnIdleEnd><RestartOnIdle>false</RestartOnIdle></IdleSettings>
  </Settings>
  <Triggers>
    <LogonTrigger />
    <TimeTrigger><StartBoundary>2026-10-10T00:00:00</StartBoundary><Repetition><Interval>PT5M</Interval><Duration>P1D</Duration></Repetition></TimeTrigger>
  </Triggers>
  <Actions Context="Author"><Exec><Command>powershell</Command><Arguments>__GUARD__</Arguments></Exec></Actions>
</Task>
"@

$wdXml = $wdXml.Replace("__SID__", $sid).Replace("__WD__", $wdPath)
$guardArgs = $guardArgs.Replace("__WD__", $wdPath)
$gXml  = $gXml.Replace("__SID__", $sid).Replace("__GUARD__", $guardArgs)
if ($wdXml -match "__" -or $gXml -match "__") { Write-Host "[X] Placeholder left"; exit 2 }

$wdFile = "$env:TEMP\oc-watchdog-task.xml"
$gFile  = "$env:TEMP\oc-guard-task.xml"
[System.IO.File]::WriteAllText($wdFile, $wdXml, (New-Object System.Text.UnicodeEncoding($false,$true)))
[System.IO.File]::WriteAllText($gFile,  $gXml,  (New-Object System.Text.UnicodeEncoding($false,$true)))

Write-Host "[1/4] Replacing Watchdog task..."
schtasks /Create /TN "OpenClaw Watchdog" /XML $wdFile /F | Out-Null
Write-Host "[2/4] Creating Guard task..."
schtasks /Create /TN "OpenClaw Watchdog Guard" /XML $gFile /F | Out-Null

$wdNow = (schtasks /query /tn "OpenClaw Watchdog" /xml | Out-String)
if ($wdNow -match "<StopOnIdleEnd>false</StopOnIdleEnd>") { Write-Host "    [OK] Watchdog StopOnIdleEnd=false" } else { Write-Host "    [!] StopOnIdleEnd NOT false" }
$gNow = (schtasks /query /tn "OpenClaw Watchdog Guard" /xml | Out-String)
if ($gNow -match "watchdog.ps1") { Write-Host "    [OK] Guard args replaced" } else { Write-Host "    [!] Guard args wrong" }

Write-Host "[3/4] Starting watchdog now..."
$exist = Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like "*watchdog.ps1*" }
if (-not $exist) { Start-Process powershell -ArgumentList "-NoProfile","-WindowStyle","Hidden","-File",$wdPath -WindowStyle Hidden }
Start-Sleep -Seconds 3
Write-Host "[4/4] Verifying..."
$run = Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like "*watchdog.ps1*" }
if ($run) { Write-Host ("    [OK] Watchdog running: " + (($run | ForEach-Object { $_.ProcessId }) -join ",")) } else { Write-Host "    [!] Not detected" }
$st = "$ocx\watchdog-status.json"
if (Test-Path $st) { Write-Host ("    status: " + (Get-Content $st -Raw).Trim()) }
Write-Host "Done."
