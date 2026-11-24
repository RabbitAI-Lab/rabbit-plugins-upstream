# Gateway Watchdog — Deploy Guide

Deploy the watchdog on a Windows host running an OpenClaw Gateway.

> **v1.2.0 (2026-10-27)** — hardened after a ClawHub security audit.
> Changes: scoped process termination, maintenance allowlist, auto-repair
> now **off by default**. See CHANGELOG.md.

---

## What this does to your machine

Read this before installing. The watchdog is a **persistent background process**.

| Action | Detail |
|---|---|
| Modifies scheduled tasks | `OpenClaw Gateway` and `OpenClaw Watchdog` get new actions (hidden launchers) |
| Requires Administrator | Only for the task changes; the watchdog itself runs as your user |
| Runs hidden | No console window. Deliberate — otherwise a black box flashes every cycle |
| Persists across reboot | Via the Logon trigger on both tasks |
| Restarts the Gateway | When health checks fail twice in a row |
| Writes state | `%USERPROFILE%\.openclaw\watchdog.log` and `watchdog-status.json` |
| **Does NOT** kill other programs | v1.2.0 removed the old `taskkill /im node.exe` behaviour entirely |
| **Does NOT** auto-repair by default | `$AUTO_DOCTOR = $false`; flip it yourself if you want it |

## What ships here

- `scripts/watchdog.ps1` — the watchdog loop, health check, tray icon, restart
- `scripts/watchdog-maintenance.ps1` — allowlisted maintenance wrapper (lock-aware)
- `scripts/run_gateway_silent.vbs` — hidden Gateway launcher
- `scripts/gateway.cmd` — Gateway start script (dynamic paths)
- `scripts/gateway.vbs` — hidden, non-waiting launcher
- `scripts/install_watchdog_admin.bat` — admin installer (asks for confirmation)
- `scripts/install_watchdog_admin.ps1` — PowerShell variant of the installer
- `scripts/uninstall_watchdog_admin.bat` — restores original task actions

## Deploy steps

1. Copy `scripts/watchdog.ps1` → `%USERPROFILE%\.openclaw\workspace\watchdog.ps1`
2. Copy `scripts/watchdog-maintenance.ps1` → `%USERPROFILE%\.openclaw\workspace\`
3. Copy `scripts/gateway.cmd`, `gateway.vbs`, `run_gateway_silent.vbs` → `%USERPROFILE%\.openclaw\`
4. Review `install_watchdog_admin.bat` — it lists every change it will make.
5. Right-click `install_watchdog_admin.bat` → **Run as administrator**, type `Y`.

## Verify

```powershell
Get-Content "$env:USERPROFILE\.openclaw\watchdog-status.json" -Raw
netstat -ano | findstr ":18789" | findstr LISTENING
# exactly one watchdog process, not zero and not two:
@(Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'watchdog\.ps1' }).Count
```

## Disable / uninstall

**Temporarily pause (watchdog stops acting, task stays):**

```powershell
Disable-ScheduledTask -TaskName 'OpenClaw Watchdog'
```

**Restore original behaviour:**

```bat
scripts\uninstall_watchdog_admin.bat   (run as administrator)
```

**Remove completely:**

```powershell
Stop-ScheduledTask   -TaskName 'OpenClaw Watchdog' -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName 'OpenClaw Watchdog' -Confirm:$false
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'watchdog\.ps1' } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
Remove-Item "$env:USERPROFILE\.openclaw\workspace\watchdog.ps1"
Remove-Item "$env:USERPROFILE\.openclaw\watchdog.log",
            "$env:USERPROFILE\.openclaw\watchdog-status.json" -ErrorAction SilentlyContinue
```

## Auto-repair (opt-in)

By default the watchdog **only** restarts the Gateway. It will never run
`openclaw doctor --fix`.

To opt in, edit the top of `watchdog.ps1`:

```powershell
$AUTO_DOCTOR = $true
```

With it enabled, after a restart fails the watchdog takes the maintenance lock
and runs `openclaw doctor --fix --non-interactive`, rate-limited by
`$DOCTOR_COOLDOWN_MIN` and capped by `$DOCTOR_TIMEOUT_SEC`. Understand that this
lets a hidden background process modify local OpenClaw state.

## Maintenance wrapper

Only allowlisted commands run; anything else is refused with exit code 3.

```powershell
powershell -File watchdog-maintenance.ps1 list                  # show allowlist
powershell -File watchdog-maintenance.ps1 doctor --fix --non-interactive
powershell -File watchdog-maintenance.ps1 gateway restart
```

## Known limitations

- Windows only (scheduled tasks, WSH, tray icon via `System.Windows.Forms`)
- Restart detection is HTTP + TCP port probe; a Gateway listening but wedged is not detected
- The tray icon requires an interactive desktop session
- Review the scripts yourself before running them with elevation
