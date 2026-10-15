# ============================================================
# OpenClaw Maintenance Wrapper (2026-10-10)
# Runs a repair command (e.g. doctor --fix) while holding the
# watchdog maintenance lock, so the watchdog will NOT judge the
# gateway or try to restart it during the repair.
#
# Usage:
#   powershell -File watchdog-maintenance.ps1 doctor --fix --non-interactive
#   powershell -File watchdog-maintenance.ps1 gateway restart
# ============================================================

param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Command
)

$ErrorActionPreference = "Continue"
$LOCK = "$env:USERPROFILE\.openclaw\watchdog-maintenance.lock"
$LOG  = "$env:USERPROFILE\.openclaw\watchdog.log"
$OWNER = "manual-maintenance-$PID"

function Log($m) {
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') | [maint] $m"
    Add-Content -Path $LOG -Value $line -Encoding UTF8
    Write-Host $line
}

if (-not $Command -or $Command.Count -eq 0) {
    Write-Host "No command given. Example: watchdog-maintenance.ps1 doctor --fix --non-interactive"
    exit 2
}

# Acquire lock
[ordered]@{ owner = $OWNER; pid = $PID; createdAt = (Get-Date).ToString("o") } |
    ConvertTo-Json | Set-Content -Path $LOCK -Encoding UTF8
Log "Maintenance lock acquired by $OWNER"

try {
    $exe  = $Command[0]
    $args = @()
    if ($Command.Count -gt 1) { $args = $Command[1..($Command.Count - 1)] }
    Log ("Running: " + ($Command -join " "))
    & $exe @args
    $code = $LASTEXITCODE
    Log "Command exited with code $code"
}
finally {
    Remove-Item $LOCK -Force -ErrorAction SilentlyContinue
    Log "Maintenance lock released by $OWNER"
}
