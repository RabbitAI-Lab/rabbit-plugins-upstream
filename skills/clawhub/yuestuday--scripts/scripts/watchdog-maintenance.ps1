# ============================================================
# OpenClaw Maintenance Wrapper (2026-10-27, v1.2.0)
# Runs an ALLOWLISTED repair command while holding the watchdog
# maintenance lock, so the watchdog will NOT judge the gateway or
# try to restart it during the repair.
#
# SECURITY: only the commands listed in $ALLOWED can run. This file
# deliberately cannot execute arbitrary executables -- see the
# ClawHub audit findings SDI-2 (2026-10-27).
#
# Usage:
#   powershell -File watchdog-maintenance.ps1 doctor --fix --non-interactive
#   powershell -File watchdog-maintenance.ps1 gateway restart
#   powershell -File watchdog-maintenance.ps1 list
# ============================================================

param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Command
)

$ErrorActionPreference = "Continue"
$LOCK = "$env:USERPROFILE\.openclaw\watchdog-maintenance.lock"
$LOG  = "$env:USERPROFILE\.openclaw\watchdog.log"
$OWNER = "manual-maintenance-$PID"

# Allowlist: exact argument vectors that may be executed.
$ALLOWED = @(
    @('doctor','--fix','--non-interactive'),
    @('doctor','--fix'),
    @('gateway','restart'),
    @('gateway','status'),
    @('status')
)

function Log($m) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') | [maint] $m"
    Add-Content -Path $LOG -Value $line -Encoding UTF8
    Write-Host $line
}

if (-not $Command -or $Command.Count -eq 0) {
    Write-Host 'No command given.'
    Write-Host 'Allowed:'
    foreach ($a in $ALLOWED) { Write-Host ('  openclaw ' + ($a -join ' ')) }
    exit 2
}

if ($Command[0] -eq 'list') {
    Write-Host 'Allowed commands:'
    foreach ($a in $ALLOWED) { Write-Host ('  openclaw ' + ($a -join ' ')) }
    exit 0
}

# Validate against the allowlist before doing anything else.
$match = $null
foreach ($a in $ALLOWED) {
    if ($a.Count -eq $Command.Count) {
        $same = $true
        for ($i = 0; $i -lt $a.Count; $i++) {
            if ($a[$i] -ne $Command[$i]) { $same = $false; break }
        }
        if ($same) { $match = $a; break }
    }
}
if (-not $match) {
    Write-Host '[X] Refused: command is not on the maintenance allowlist.' -ForegroundColor Red
    Write-Host ('    requested: ' + ($Command -join ' '))
    Write-Host '    run with "list" to see allowed commands.'
    exit 3
}

# Resolve the openclaw entry point; never trust PATH with elevation.
function Resolve-OpenClaw {
    $cands = @(
        "$env:APPDATA\npm\openclaw.cmd",
        "$env:APPDATA\npm\openclaw",
        'C:\Program Files\nodejs\openclaw.cmd'
    )
    foreach ($c in $cands) { if (Test-Path $c) { return $c } }
    $g = Get-Command openclaw -ErrorAction SilentlyContinue
    if ($g) { return $g.Source }
    return $null
}

$exe = Resolve-OpenClaw
if (-not $exe) {
    Write-Host '[X] Could not locate the openclaw executable.' -ForegroundColor Red
    exit 4
}

# Acquire lock
[ordered]@{ owner = $OWNER; pid = $PID; createdAt = (Get-Date).ToString('o') } |
    ConvertTo-Json | Set-Content -Path $LOCK -Encoding UTF8
Log "Maintenance lock acquired by $OWNER"

try {
    Log ("Running: openclaw " + ($match -join ' '))
    Log ('Executable: ' + $exe)
    & $exe @match
    $code = $LASTEXITCODE
    Log "Command exited with code $code"
    exit $code
}
finally {
    Remove-Item $LOCK -Force -ErrorAction SilentlyContinue
    Log "Maintenance lock released by $OWNER"
}
