---
name: "gateway-watchdog"
version: "1.2.0"
description: "Windows background watchdog for the OpenClaw Gateway: 5s health checks, auto-restart on crash, hidden no-window operation, tray status icon, and a maintenance lock that keeps repairs (doctor --fix) from racing the watchdog. Auto-repair is OFF by default; the watchdog only restarts the Gateway."
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

## Single-instance guard (v1.1.0)

The watchdog holds a named mutex for its whole lifetime:

```powershell
$MUTEX_NAME = "Global\OpenClawWatchdog_SingleInstance"
$script:mutex = New-Object System.Threading.Mutex($false, $MUTEX_NAME)
$gotIt = $script:mutex.WaitOne(0)
if (-not $gotIt) { exit 0 }
```

**Why this exists.** v1.0.0 was launched by a 5-minute repetition trigger while
its own `while ($true)` loop never exited. Eight copies stacked in 25 minutes,
each polling the same status file and drawing its own tray icon. Fix has two
halves and both are required:

1. **Trigger** — a long-running loop gets a *logon* trigger only. Repetition is
   for scripts that exit on their own.
2. **Code** — the mutex above, so an unexpected launch path is harmless.

Verify a second copy really dies:

```powershell
Start-Process wscript.exe -ArgumentList 'run_watchdog_silent.vbs' -WindowStyle Hidden
Start-Sleep -Seconds 6
@(Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'watchdog\.ps1' }).Count
# must be 1
```
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

## The Four Scheduled-Task Flaws (v3 fix)

A default `schtasks` install of this watchdog can die silently. Four compounding causes:

| # | Flaw | Symptom | v3 fix |
|---|------|---------|--------|
| 1 | Trigger is `LogonTrigger` only | Killed once, never comes back | `RestartOnFailure` 999x/1min + a **Guard task** |
| 2 | `StopOnIdleEnd=true` | **Task killed when you return to the PC** (exit `0xC000013A`) | Explicitly set `false` |
| 3 | Self-refresh exits without confirming the replacement | Coverage gap if the new process fails | Wait for the status-file pid to change; stay alive otherwise |
| 4 | No independent supervisor | Nothing restarts a dead watchdog | `\OpenClaw Watchdog Guard` task, every 5 min |

### Hard-won gotchas

- **Do not delete `<IdleSettings>`** - Task Scheduler re-adds it with defaults (`StopOnIdleEnd=true`). Always write the block explicitly with `false`.
- **Never edit `.ps1` through a JSON/JS string tool** - escaping layers collide; corruption is *offset*, so the reported error line is not the real one. Write a small patch `.ps1` and use `[System.IO.File]::WriteAllText/WriteAllLines`.
- **Placeholder order matters**: if `__WD__` lives inside the `__GUARD__` value, replace `__GUARD__` *first*, then `__WD__`.
- **`schtasks /Create /XML` validates syntax, not substitutions.** Re-read via `schtasks /query /tn <name> /xml` and assert no `__` remains.
- **Changing a scheduled task needs Administrator.** Non-admin `schtasks /Change` gives *Access denied*.
- **Do not use a read-tool result as a write basis when a file looks wrong** - a truncation/placeholder notice can be written back as file content. Read raw bytes with `[System.IO.File]::ReadAllText` before rewriting.

### Verify after install

```powershell
schtasks /query /tn "OpenClaw Watchdog" /xml | Select-String StopOnIdleEnd
schtasks /query /tn "OpenClaw Watchdog Guard" /xml | Select-String Arguments
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*watchdog.ps1*' }
Get-Content "$env:USERPROFILE\.openclaw\watchdog.log" -Tail 10
```

### Known minor issue

The Guard task can occasionally start a second watchdog process. Functionally
harmless; tighten the CommandLine filter if you want strict single-instance.
## Security & scope disclosure (v1.2.0)

Added after a ClawHub audit on 2026-10-27. Read before installing.

**What requires elevation:** only the installer, and only to change two scheduled
task actions. The watchdog process itself runs as the logged-in user.

**What runs hidden:** the Gateway launcher (`run_gateway_silent.vbs`) and the
watchdog (`run_watchdog_silent.vbs`). Hidden operation is the point — Task
Scheduler would otherwise flash a console window every cycle — but you should
know it is happening. `watchdog.log` and `watchdog-status.json` record every
action; the tray icon shows current state.

**Persistence:** both tasks carry a Logon trigger, so they survive reboot. See
`README.md` for the exact disable and uninstall steps.

**Process termination is scoped.** v1.1.0 and earlier ran
`taskkill /f /im node.exe` and `taskkill /f /im wscript.exe` from the elevated
installer, which could kill unrelated Node.js and Windows Script Host workloads.
v1.2.0 never kills by image name; it stops and starts the named scheduled task
and nothing else.

**Auto-repair is opt-in.** The watchdog no longer runs `openclaw doctor --fix`
on its own. Restart-only is the default. Set `$AUTO_DOCTOR = $true` at the top of
`watchdog.ps1` if you want a hidden background process to modify local OpenClaw
state automatically.

**The maintenance wrapper is allowlisted.** `watchdog-maintenance.ps1` used to
execute whatever command it was given. It now matches the full argument vector
against a fixed list and exits 3 on anything else. Run it with `list` to see
what is permitted.

## Uninstall

```powershell
Stop-ScheduledTask       -TaskName 'OpenClaw Watchdog' -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName 'OpenClaw Watchdog' -Confirm:$false
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'watchdog\.ps1' } |
    ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
Remove-Item "$env:USERPROFILE\.openclaw\workspace\watchdog.ps1" -ErrorAction SilentlyContinue
```

To pause without uninstalling: `Disable-ScheduledTask -TaskName 'OpenClaw Watchdog'`
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
