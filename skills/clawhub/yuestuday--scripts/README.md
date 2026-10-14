# Gateway Watchdog — Deploy Guide

Deploy the watchdog on a Windows host running an OpenClaw Gateway.

License: MIT-0 (see LICENSE).

## What ships here
- `scripts/watchdog.ps1` — the watchdog itself
- `scripts/watchdog-maintenance.ps1` — maintenance wrapper (lock-aware)
- `scripts/run_gateway_silent.vbs` — hidden Gateway launcher
- `scripts/gateway.cmd` — Gateway start script (dynamic paths)
- `scripts/gateway.vbs` — hidden, non-waiting launcher
- `scripts/install_watchdog_admin.bat` — admin one-shot installer

## Deploy steps
1. Copy `scripts/watchdog.ps1` → `%USERPROFILE%\.openclaw\workspace\watchdog.ps1`
2. Copy `scripts/watchdog-maintenance.ps1` → `%USERPROFILE%\.openclaw\workspace\`
3. Copy `scripts/gateway.cmd`, `gateway.vbs`, `run_gateway_silent.vbs` → `%USERPROFILE%\.openclaw\`
4. Edit paths in `install_watchdog_admin.bat` if `%USERPROFILE%\.openclaw` differs.
5. Right-click `install_watchdog_admin.bat` → Run as administrator.

## Verify
```powershell
Get-Content "$env:USERPROFILE\.openclaw\watchdog-status.json" -Raw
netstat -ano | findstr ":18789" | findstr LISTENING
```
