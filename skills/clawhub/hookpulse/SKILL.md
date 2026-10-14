---
name: hookpulse
description: Monitor cron jobs, webhooks, backups and scheduled GitHub Actions workflows with HookPulse (hookpulse.net), a dead man's switch. Create a monitor with an interval or a cron schedule, import a crontab, send start, success and failure signals with the exit code, instrument a fleet with one setup key, and read monitor state, check-ins and the public status page. A missed or failed run alerts by e-mail or webhook. Use when a task mentions a cron job, crontab, scheduled task, heartbeat, dead man's switch, missed run, backup that stopped, or a GitHub Actions schedule.
license: MIT-0
compatibility: Needs HTTPS access to hookpulse.net. Works with the remote MCP server or with plain HTTP calls.
---

# HookPulse

HookPulse watches routines that should run on a schedule. The routine sends a check-in to its link when it runs.
If the check-in is late, or the routine reports a failure, HookPulse sends an alert. The next good check-in sends a
recovery message.

## Connect

- MCP server (preferred): `https://hookpulse.net/mcp?checkout=site`. Transport: Streamable HTTP. With
  `checkout=site`, the person buys on the site and the agent never pays.
- HTTP API: base URL `https://hookpulse.net`. Each MCP tool calls one route of this API.
- Identity: `create_guest` returns a guest token `hp_…`. Send it as `X-Guest-Token` on later calls. Keep it: the
  monitors belong to it until the person signs in on the site.
- Discovery: `GET https://hookpulse.net/api/` lists the routes, prices and limits.
  `https://hookpulse.net/llms-full.txt` has the full reference.

## MCP tools

| Tool | HTTP | Use it to |
|---|---|---|
| `create_guest` | `POST /api/guest` | Get the guest token that owns the monitors. |
| `create_endpoint` | `POST /api/endpoints` | Create a monitor: `interval_sec`, or `cron` + `tz` + `grace_sec`, and the alert destinations. |
| `import_crontab` | `POST /api/import/crontab` | Read a crontab and propose one monitor per line. Nothing is written without `apply=1`. |
| `list_endpoints` | `GET /api/endpoints` | List the monitors and their state. |
| `get_endpoint` | `GET /api/endpoints/{id}` | Read one monitor: state, next expected time, last check-in. |
| `list_events` | `GET /api/endpoints/{id}/events` | Read the latest check-ins of a monitor. |
| `delete_endpoint` | `DELETE /api/endpoints/{id}` | Remove a monitor. |
| `ping_ingest` | `GET /in/{id}` | Send a success check-in, as the routine does. |
| `signal_start` | `GET /in/{id}/start` | Record that a run started, to measure its duration. |
| `signal_fail` | `GET /in/{id}/fail` | Record a failed run; the alert leaves on the next five-minute check. |
| `signal_exit_code` | `GET /in/{id}/{exit_code}` | Record the shell exit code: 0 is success, 1 to 255 a failure. |
| `ingest_key` | `GET /api/ingest-key` | Get the setup key for `/in/{key}/{slug}`: the first check-in of a name creates its monitor. |
| `ping_slug` | `GET /in/{key}/{slug}` | Check in by name with the setup key, creating the monitor the first time. |
| `status_feed_url` | `GET /api/status-feed` | Get the public status page and feed of all monitors of the owner. |
| `list_templates` | `GET /api/templates` | Get ready snippets: curl, crontab line, n8n, GitHub Actions and the alert JSON. |
| `billing` | `GET /api/billing` | Read the free allowances, prices and the account trial. |
| `pricing` | `GET /api/pricing` | Read the current prices. |

## Rules

1. Read `billing` before you create more than ten monitors or add e-mail alerts to more than one monitor. Do not
   use a price from memory.
2. Never pay by yourself. If a call returns HTTP 402, show the price and https://hookpulse.net/pricing to the user.
   The person buys on the site.
3. The monitor ID is a credential: whoever has it can send check-ins and silence the alarm. Do not print it in
   public logs or issues. The status page link is the one to share.
4. A start or failure signal is not proof of life. Only a success check-in resets the expected time.
5. For a schedule, prefer `cron` with `tz` and a `grace_sec` that covers the usual delay and run time.
6. If you get HTTP 429 or 503, wait for the time in `Retry-After` and try once more.

## Examples

```bash
# Guest token, then a monitor for a backup at 03:00 São Paulo time with 15 minutes of allowed delay
HP=$(curl -s -XPOST https://hookpulse.net/api/guest | jq -r .token)
curl -s -XPOST https://hookpulse.net/api/endpoints -H "X-Guest-Token: $HP" -H 'content-type: application/json' \
  -d '{"name":"nightly-backup","cron":"0 3 * * *","tz":"America/Sao_Paulo","grace_sec":900}'

# At the end of the routine: the exit code of the last command
curl -fsS "https://hookpulse.net/in/$ID/$?"
```

## Limits

- The service checks monitors every five minutes, so an alert can arrive up to five minutes after the allowed delay.
- Terms: https://hookpulse.net/terms. Privacy: https://hookpulse.net/privacy. Contact: contato@hookpulse.net.
