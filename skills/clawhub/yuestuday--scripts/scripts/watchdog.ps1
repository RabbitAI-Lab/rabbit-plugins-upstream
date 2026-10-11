# ============================================================
# OpenClaw Gateway Watchdog (v3, 2026-10-10)
# - Runs hidden in the background (no cmd window)
# - Live status via system-tray icon + watchdog-status.json
# - Auto-restarts the Gateway when it goes down
# - Version-agnostic path resolution
# - MAINTENANCE LOCK: suspends health checks while doctor --fix
#   (or any repair) is running, so it never races the repair.
# ============================================================

$ErrorActionPreference = "SilentlyContinue"

# ---------- Configuration ----------
$CHECK_INTERVAL      = 5
$LOG_FILE            = "$env:USERPROFILE\.openclaw\watchdog.log"
$STATUS_FILE         = "$env:USERPROFILE\.openclaw\watchdog-status.json"
# Maintenance lock file: while present+fresh, watchdog pauses its checks.
$MAINTENANCE_LOCK    = "$env:USERPROFILE\.openclaw\watchdog-maintenance.lock"
$LOCK_STALE_SEC      = 300   # a lock older than this is considered abandoned
$MAX_LOG_LINES       = 500
$GATEWAY_PORT        = 18789
$GATEWAY_URL         = "http://127.0.0.1:$GATEWAY_PORT/"
$SELF_REFRESH_HOURS  = 24
$RESTART_THRESHOLD   = 2
$DOCTOR_TIMEOUT_SEC  = 90
$DOCTOR_COOLDOWN_MIN = 10
$SHOW_TRAY           = $true

$START_TIME   = Get-Date
$lastDoctorAt = $null
$failCount    = 0
$consecutiveFails = 0
$cycle        = 0
$lastStatus   = "starting"

# ---------- Dynamic path resolution ----------
function Get-NodePath {
    $candidates = @(
        "$env:APPDATA\npm\node.exe",
        "C:\Program Files\nodejs\node.exe",
        "C:\Program Files (x86)\nodejs\node.exe"
    )
    foreach ($c in $candidates) { if (Test-Path $c) { return $c } }
    $cmd = Get-Command node -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    return "node"
}

function Get-OpenClawEntry {
    $mjs  = "$env:APPDATA\npm\node_modules\openclaw\openclaw.mjs"
    $dist = "$env:APPDATA\npm\node_modules\openclaw\dist\index.js"
    if (Test-Path $mjs)  { return @{ path = $mjs;  kind = "mjs" } }
    if (Test-Path $dist) { return @{ path = $dist; kind = "dist" } }
    return $null
}

# ---------- Maintenance lock helpers ----------
# The lock is a small JSON file. Any repair routine (this watchdog's own
# doctor --fix, or a manual maintenance run) can create it to tell the
# watchdog "hands off, I am working on the gateway".
function New-MaintenanceLock {
    param([string]$Owner)
    try {
        $obj = [ordered]@{
            owner     = $Owner
            pid       = $PID
            createdAt = (Get-Date).ToString("o")
        }
        $obj | ConvertTo-Json | Set-Content -Path $MAINTENANCE_LOCK -Encoding UTF8
        Write-Log ">> Maintenance lock acquired by $Owner"
    } catch { Write-Log ">> Failed to create maintenance lock: $_" }
}

function Remove-MaintenanceLock {
    param([string]$Owner = "")
    try {
        # Only remove the lock if we own it (or owner unknown).
        if (Test-Path $MAINTENANCE_LOCK) {
            $cur = (Get-Content $MAINTENANCE_LOCK -Raw | ConvertFrom-Json).owner
            if ($Owner -eq "" -or $cur -eq $Owner) {
                Remove-Item $MAINTENANCE_LOCK -Force -ErrorAction SilentlyContinue
                Write-Log ">> Maintenance lock released by $Owner"
            }
        }
    } catch {}
}

function Test-MaintenanceLock {
    # Returns $true if a FRESH lock is held by someone else.
    if (-not (Test-Path $MAINTENANCE_LOCK)) { return $false }
    try {
        $age = ((Get-Date) - (Get-Item $MAINTENANCE_LOCK).LastWriteTime).TotalSeconds
        if ($age -gt $LOCK_STALE_SEC) {
            Write-Log ">> Stale maintenance lock (age ${age}s) removed"
            Remove-Item $MAINTENANCE_LOCK -Force -ErrorAction SilentlyContinue
            return $false
        }
        return $true
    } catch { return $false }
}

# ---------- Logging ----------
function Write-Log {
    param([string]$Msg)
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') | $Msg"
    Add-Content -Path $LOG_FILE -Value $line -Encoding UTF8
    Write-Host $line
}

function Write-Status {
    param([string]$State, [string]$Detail = "")
    $obj = [ordered]@{
        state     = $State
        detail    = $Detail
        pid       = $PID
        port      = $GATEWAY_PORT
        cycle     = $cycle
        failCount = $failCount
        updatedAt = (Get-Date).ToString("o")
        uptimeMin = [int]((Get-Date) - $START_TIME).TotalMinutes
    }
    try { $obj | ConvertTo-Json | Set-Content -Path $STATUS_FILE -Encoding UTF8 } catch {}
}

function Rotate-Log {
    if (Test-Path $LOG_FILE) {
        $lines = Get-Content $LOG_FILE -Encoding UTF8
        if ($lines.Count -gt $MAX_LOG_LINES) {
            ($lines | Select-Object -Last $MAX_LOG_LINES) | Set-Content $LOG_FILE -Encoding UTF8
        }
    }
}

# ---------- Health check (HTTP first, port fallback) ----------
function Test-GatewayAlive {
    try {
        $resp = Invoke-WebRequest -Uri $GATEWAY_URL -UseBasicParsing -TimeoutSec 5
        if ($resp.StatusCode -ge 200 -and $resp.StatusCode -lt 500) { return $true }
    } catch {}
    $tcp = netstat -ano 2>$null | Select-String ":$GATEWAY_PORT\s.*LISTENING"
    if ($tcp) { return $true }
    return $false
}

# ---------- Restart ----------
function Start-Gateway {
    Write-Log ">> Gateway down, restarting..."
    Write-Status "restarting" "dispatching gateway start"
    $node  = Get-NodePath
    $entry = Get-OpenClawEntry
    try {
        if ($entry) {
            Start-Process -FilePath $node -ArgumentList (""" + $entry.path + """),"gateway","start" -WindowStyle Hidden | Out-Null
        } else {
            Start-Process -FilePath "openclaw" -ArgumentList "gateway","start" -WindowStyle Hidden | Out-Null
        }
        Write-Log ">> Restart dispatched"
    } catch {
        Write-Log ">> Start failed: $_"
    }
    for ($i = 0; $i -lt 8; $i++) {
        Start-Sleep -Seconds 3
        if (Test-GatewayAlive) {
            Write-Log ">> Restart OK"
            Write-Status "ok" "recovered after restart"
            return $true
        }
    }
    Write-Log ">> Restart failed"
    return $false
}

# ---------- Doctor (guarded + locked) ----------
function Invoke-DoctorFix {
    if ($lastDoctorAt -and (((Get-Date) - $lastDoctorAt).TotalMinutes -lt $DOCTOR_COOLDOWN_MIN)) {
        $waited = [int]((Get-Date) - $lastDoctorAt).TotalMinutes
        Write-Log ">> doctor --fix skipped (cooldown ${DOCTOR_COOLDOWN_MIN}m, last ran ${waited}m ago)"
        return $false
    }
    Write-Log ">> Restart failed; running 'openclaw doctor --fix'..."
    $script:lastDoctorAt = Get-Date
    # Take the maintenance lock so no other watchdog/repair runs concurrently.
    New-MaintenanceLock "watchdog-doctor"
    Write-Status "maintenance" "doctor --fix running"
    Update-Tray "maintenance" "doctor --fix"
    try {
        $node  = Get-NodePath
        $entry = Get-OpenClawEntry
        $outFile = [System.IO.Path]::GetTempFileName()
        $errFile = [System.IO.Path]::GetTempFileName()
        if ($entry -and $entry.kind -eq "mjs") {
            $proc = Start-Process -FilePath $node -ArgumentList (""" + $entry.path + """),"doctor","--fix","--non-interactive" -NoNewWindow -PassThru -RedirectStandardOutput $outFile -RedirectStandardError $errFile
        } else {
            $proc = Start-Process -FilePath "openclaw" -ArgumentList "doctor","--fix","--non-interactive" -NoNewWindow -PassThru -RedirectStandardOutput $outFile -RedirectStandardError $errFile
        }
        $waited = 0
        while (-not $proc.HasExited -and $waited -lt $DOCTOR_TIMEOUT_SEC) {
            Start-Sleep -Seconds 2; $waited += 2
        }
        if (-not $proc.HasExited) {
            Write-Log ">> doctor --fix timed out, killing"
            Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue
        }
        $tail = ((Get-Content $outFile -Raw -ErrorAction SilentlyContinue) + (Get-Content $errFile -Raw -ErrorAction SilentlyContinue)).Trim()
        Remove-Item $outFile, $errFile -Force -ErrorAction SilentlyContinue
        if ($tail.Length -gt 600) { $tail = $tail.Substring($tail.Length - 600) }
        Write-Log ">> doctor --fix done (exit=$($proc.ExitCode)): $tail"
        return $true
    } catch {
        Write-Log ">> doctor --fix error: $_"
        return $false
    } finally {
        Remove-MaintenanceLock "watchdog-doctor"
    }
}

# ---------- Tray icon ----------
$script:tray = $null
function Initialize-Tray {
    if (-not $SHOW_TRAY) { return }
    try {
        Add-Type -AssemblyName System.Windows.Forms
        Add-Type -AssemblyName System.Drawing
        $script:tray = New-Object System.Windows.Forms.NotifyIcon
        $script:tray.Icon = [System.Drawing.SystemIcons]::Shield
        $script:tray.Text = "OpenClaw Gateway Watchdog"
        $script:tray.Visible = $true
    } catch {
        Write-Log ">> Tray init skipped: $_"
        $script:tray = $null
    }
}

function Update-Tray {
    param([string]$State, [string]$Text)
    if (-not $script:tray) { return }
    try {
        switch ($State) {
            "ok"          { $script:tray.Icon = [System.Drawing.SystemIcons]::Shield }
            "restarting"  { $script:tray.Icon = [System.Drawing.SystemIcons]::Warning }
            "maintenance" { $script:tray.Icon = [System.Drawing.SystemIcons]::Information }
            "down"        { $script:tray.Icon = [System.Drawing.SystemIcons]::Error }
            default       { $script:tray.Icon = [System.Drawing.SystemIcons]::Application }
        }
        $msg = "OpenClaw Watchdog: $Text"
        if ($msg.Length -gt 63) { $msg = $msg.Substring(0, 63) }
        $script:tray.Text = $msg
    } catch {}
}

# ---------- Main ----------
Initialize-Tray
Write-Log "=== Watchdog v3 started (pid $PID) ==="
Write-Log "Interval: ${CHECK_INTERVAL}s | Port: $GATEWAY_PORT | Tray: $SHOW_TRAY"
Write-Status "starting" "watchdog booted"
Update-Tray "starting" "starting"

while ($true) {
    try {
        Rotate-Log
        $cycle++

        # --- MAINTENANCE GATE ---
        # If a repair (ours or external) holds a fresh lock, do NOT judge
        # the gateway health or attempt a restart. Just wait.
        if (Test-MaintenanceLock) {
            if ($lastStatus -ne "maintenance") {
                Write-Log ">> Maintenance in progress - pausing health checks"
                Write-Status "maintenance" "waiting for repair to finish"
                Update-Tray "maintenance" "maintenance"
                $lastStatus = "maintenance"
            }
            Start-Sleep -Seconds $CHECK_INTERVAL
            continue
        }
        if ($lastStatus -eq "maintenance") {
            Write-Log ">> Maintenance finished - resuming health checks"
            $consecutiveFails = 0
            $lastStatus = ""
        }

        if (((Get-Date) - $START_TIME).TotalHours -ge $SELF_REFRESH_HOURS) {
            Write-Log ">> Self-refresh: relaunching watchdog before 72h limit"
            $self = $MyInvocation.MyCommand.Path
            if (-not $self) { $self = "$env:USERPROFILE\.openclaw\workspace\watchdog.ps1" }
            Start-Process -FilePath "powershell" -ArgumentList ("-NoProfile -WindowStyle Hidden -File "" + $self + """) -WindowStyle Hidden | Out-Null
            Write-Log ">> New watchdog dispatched, exiting old (pid $PID)"
            if ($script:tray) { $script:tray.Visible = $false; $script:tray.Dispose() }
            exit 0
        }

        if (Test-GatewayAlive) {
            if ($lastStatus -ne "ok") {
                Write-Log "Gateway healthy"
                Write-Status "ok" "gateway listening"
                Update-Tray "ok" "healthy"
                $lastStatus = "ok"
            }
            if ($cycle % 60 -eq 0) { Write-Log "Watchdog OK (cycle $cycle)" }
            if ($consecutiveFails -gt 0) {
                Write-Log "Gateway recovered ($consecutiveFails consecutive failures)"
                $consecutiveFails = 0
            }
        }
        else {
            $consecutiveFails++
            $failCount++
            if ($consecutiveFails -eq 1) {
                Write-Log "!! Gateway OFFLINE (total $failCount)"
                Write-Status "down" "gateway offline"
                Update-Tray "down" "OFFLINE"
                $lastStatus = "down"
            }
            if ($consecutiveFails -ge $RESTART_THRESHOLD) {
                # Re-check the lock right before acting, in case maintenance
                # started during our wait.
                if (Test-MaintenanceLock) {
                    Write-Log ">> Maintenance started; skipping restart"
                    $consecutiveFails = 0
                } else {
                    $ok = Start-Gateway
                    if (-not $ok) {
                        if (Invoke-DoctorFix) {
                            Write-Log ">> Retrying restart after doctor --fix..."
                            Start-Gateway | Out-Null
                        }
                    }
                    $consecutiveFails = 0
                }
            }
        }
    }
    catch {
        Write-Log "!! Error: $_"
    }
    Start-Sleep -Seconds $CHECK_INTERVAL
}
