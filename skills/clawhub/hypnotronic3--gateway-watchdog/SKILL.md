---
name: gateway-watchdog
description: "Monitor an OpenClaw gateway, auto-restart on failure, and alert when recovery fails."
---

# Gateway Watchdog

Monitor an OpenClaw gateway process. Auto-restart on failure (with configurable attempts and cooldown). Write status/alert JSON files for remote monitoring. Integrate with nginx for HTTP status endpoints and with a separate OpenClaw cron job for notifications.

## When to use

Deploy on any Linux server running an OpenClaw gateway that should stay up automatically. Pair with a remote OpenClaw instance that checks the status endpoints and alerts you when recovery fails.

## Quick start

1. Copy `scripts/watchdog.py` and `scripts/watchdog.conf` to your server (e.g. `/opt/openclaw-watchdog/`).
2. Edit `watchdog.conf` with your settings.
3. Copy `scripts/openclaw-gateway-watchdog.service` to `/etc/systemd/system/`.
4. Edit the service file paths if needed.
5. Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable openclaw-gateway-watchdog
sudo systemctl start openclaw-gateway-watchdog
```

6. (Optional) Add the nginx location block from `references/nginx-snippet.conf` to expose status endpoints.
7. (Optional) Set up a cron job on your PC/local OpenClaw to check the status endpoints and notify you.

## Configuration

All settings are in `scripts/watchdog.conf`. Key options:

| Setting | Default | Description |
|---------|---------|-------------|
| `HEALTH_URL` | `http://127.0.0.1:18789/health` | Gateway health endpoint |
| `CHECK_INTERVAL` | `60` | Seconds between checks |
| `RESTART_COOLDOWN` | `30` | Seconds to wait after restart before re-checking |
| `MAX_RESTART_ATTEMPTS` | `3` | Restart attempts per failure cycle |
| `STATE_FILE` | `/opt/openclaw-watchdog/watchdog-state.json` | Persistent state file path |
| `ALERT_FILE` | `/opt/openclaw-watchdog/watchdog-alert.json` | Alert file path (written on critical failure) |
| `LOG_FILE` | `/var/log/openclaw-gateway-watchdog.log` | Log file path |
| `GATEWAY_SERVICE` | `openclaw-gateway` | systemd user service name to restart |

## How it works

1. Every `CHECK_INTERVAL` seconds, curls the health endpoint.
2. On failure: increments consecutive failure count, attempts restart (up to `MAX_RESTART_ATTEMPTS`).
3. After each restart, waits `RESTART_COOLDOWN` seconds then re-checks health.
4. If all restart attempts fail: writes alert file, sets status to `critical`.
5. On recovery: clears alert file, sets status to `healthy`, resets counters.

### Status file (`watchdog-state.json`)

```json
{
  "status": "healthy|degraded|critical|starting",
  "consecutive_failures": 0,
  "restart_attempts": 0,
  "total_restarts": 0,
  "last_known_good": "2026-07-12T05:04:39.944168+00:00",
  "last_failure_time": null
}
```

### Alert file (`watchdog-alert.json`)

Only exists when status is `critical`. Deleted on recovery.

```json
{
  "severity": "critical",
  "subject": "Gateway DOWN — Auto-Recovery Failed",
  "message": "OpenClaw gateway down for X checks. Manual intervention required.",
  "timestamp": "2026-07-12T05:10:00+00:00",
  "gateway_url": "http://127.0.0.1:18789/health"
}
```

## Remote monitoring with OpenClaw cron

Set up a cron job on another machine's OpenClaw to check the status endpoint every 5 minutes and notify you on critical failures:

```json
{
  "name": "Server Gateway Health Check",
  "schedule": { "kind": "every", "everyMs": 300000 },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "Check the server gateway watchdog. Run: curl -sf http://YOUR_SERVER/watchdog/state.json and curl -sf http://YOUR_SERVER/watchdog/alert.json — if status is 'critical' or there's an alert, notify the user immediately."
  },
  "delivery": { "mode": "announce" }
}
```

## Troubleshooting

- **Watchdog not starting**: Check `LOG_FILE` and ensure `STATE_FILE` directory is writable by the service user.
- **Restart failing**: Verify the service user can run `systemctl --user restart GATEWAY_SERVICE`. Check `XDG_RUNTIME_DIR` is set.
- **Permission denied on state file**: Ensure the directory and files are readable by the web server user (e.g. `www-data`) if exposing via nginx.
- **Nginx 403 on status endpoints**: Ensure directory traversal permissions (`chmod 755` on parent directories, `chmod 644` on JSON files).