---
name: "gateway-watchdog"
version: "1.0.0"
description: "Windows background watchdog for the OpenClaw Gateway: 5s health checks, auto-restart on crash, hidden no-window operation, tray status icon, and a maintenance lock that keeps repairs (doctor --fix) from racing the watchdog."
author: "yuestuday"
license: "MIT-0"
tags: [openclaw, gateway, watchdog, windows, service, health, powershell, maintenance]
category: "operations"
---

# Gateway Watchdog

A Windows background watchdog for the OpenClaw Gateway. It health-checks the
Gateway every 5 seconds, automatically restarts it when it goes down, and runs
hidden in the background — no CMD window — with a system-tray status icon.

Its key feature is a **maintenance lock**: while a repair such as `doctor --fix`
is running, the watchdog suspends all health checks and restart attempts, so the
two never fight each other. Version-agnostic path resolution, HTTP-first health
probing, log rotation, and deadlock-safe lock expiry are all included.

## When to Use

- Gateway keeps crashing / restarting in a loop
- Watchdog log spams `!! Gateway OFFLINE` even though the port is listening
- A `doctor --fix` run keeps getting interrupted by the watchdog trying to restart
- You want the Gateway + watchdog to run hidden (no CMD window)
- Installing or repairing the watchdog service on Windows

## Architecture

| Piece | File | Role |
|-------|------|------|
| Watchdog | `scripts/watchdog.ps1` | Main loop, health check, restart, tray icon |
| Maintenance wrapper | `scripts/watchdog-maintenance.ps1` | Run a repair while holding the lock |
| Hidden launcher | `scripts/run_gateway_silent.vbs` | Start Gateway with no window |
| Gateway script | `scripts/gateway.cmd` | Dynamic path resolution, no version pin |
| Installer | `scripts/install_watchdog_admin.bat` | One-shot admin setup for scheduled tasks |

## How the Maintenance Lock Works

The lock file is `~/.openclaw/watchdog-maintenance.lock` (JSON: owner, pid, createdAt).

1. Any repair routine creates the lock before it starts.
2. While a **fresh** lock exists, the watchdog pauses all health judgement and
   restart attempts, and switches the tray icon to "maintenance".
3. A lock older than `LOCK_STALE_SEC` (default 300s) is treated as abandoned and
   removed automatically (dead-lock protection).
4. The lock is re-checked immediately before any restart, so maintenance that
   begins mid-wait still wins.
5. The lock is released in a `finally` block, always.

## Usage

### Check status
```powershell
Get-Content "$env:USERPROFILE\.openclaw\watchdog-status.json" -Raw
Get-Content "$env:USERPROFILE\.openclaw\watchdog.log" -Tail 20
```

The status file holds: `state` (starting/ok/down/restarting/maintenance), `cycle`,
`failCount`, `updatedAt`, `uptimeMin`.

### Run a repair safely (coordinated with the watchdog)
```powershell
powershell -NoProfile -File "$env:USERPROFILE\.openclaw\workspace\watchdog-maintenance.ps1" doctor --fix --non-interactive
```

The wrapper takes the lock, runs the command, releases the lock. Never run a
repair bare while the watchdog is live — it will fight you.

### Install / repair (needs Administrator)
```
Right-click -> Run as administrator:
  install_watchdog_admin.bat
```
This switches the Gateway task to the hidden VBS launcher, updates the Watchdog
task to run hidden PowerShell, restarts the Gateway silently, and verifies the port.

## Tray States

- Shield — healthy
- Warning — restarting
- Info — maintenance in progress
- Error — offline

`$SHOW_TRAY = $false` in `watchdog.ps1` disables the tray (headless mode). Without
an interactive session the tray is skipped automatically — the status file is
still written.

## Tuning (`watchdog.ps1` top block)

| Var | Default | Meaning |
|-----|---------|---------|
| `$CHECK_INTERVAL` | 5 | seconds between checks |
| `$GATEWAY_PORT` | 18789 | Gateway port |
| `$RESTART_THRESHOLD` | 2 | consecutive failures before restart |
| `$LOCK_STALE_SEC` | 300 | abandoned-lock timeout |
| `$DOCTOR_TIMEOUT_SEC` | 90 | max doctor --fix runtime |
| `$DOCTOR_COOLDOWN_MIN` | 10 | min gap between doctor runs |
| `$SELF_REFRESH_HOURS` | 24 | relaunch self before shell limits |

## Troubleshooting

- **`!! Gateway OFFLINE` while port is listening** — usually a restart-timing race;
  HTTP probe first. If persistent, check the maintenance lock is not stuck.
- **Watchdog cannot enter maintenance mode / `schtasks` Access denied** — the
  scheduled task needs Administrator. Run the installer as admin.
- **Two watchdogs running** — end the old instance with PowerShell `Stop-Process`.
- **Gateway starts but window pops** — the task still points at `gateway.cmd`;
  re-run the installer to switch it to `run_gateway_silent.vbs`.

## License

MIT-0 — see [LICENSE](LICENSE).
