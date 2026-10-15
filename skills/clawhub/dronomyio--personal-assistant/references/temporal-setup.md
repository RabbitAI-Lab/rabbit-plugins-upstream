# Content-health agent on Temporal (v1.1.0)

A long-running Temporal workflow that watches the assistant's content feeds
for freshness and heals what it can — with **no external scheduler**. The
workflow itself decides when to check next (adaptive scheduling).

## What it watches

| Feed | Check | Stale means |
|---|---|---|
| `surveillance` | Digest `surveillance-YYYY-MM-DD.md` exists for the most recent expected weekday episode | No digest (or transcript) past the posting cutoff |
| `us_brief` | `us/latest.json` modified within `BRIEF_STALE_HOURS` | Brief engine hasn't produced output |
| `india_brief` | `india/latest.json` modified within `BRIEF_STALE_HOURS` | Same |
| `job_status` | Per-job `ok`/`failed`/`last_run` from the jobs' `status.json` | A job failed recently, or went silent past its expected interval; reconciles jobs whose output has since recovered |

## Adaptive scheduling

The workflow owns its timing; nothing else wakes it up:

* **healthy** → sleep `HEALTHY_INTERVAL_SEC` (default 3600)
* **quiet hours** (01:00–05:00 local) and healthy → `QUIET_INTERVAL_SEC` (default 10800)
* **today's episode not yet posted** (before `POSTING_CUTOFF_HOUR`, default 18:00 local) → `pending`, re-check hourly, no alert
* **stale** → run backfill activities, re-check every `STALE_RETRY_SEC` (default 900), up to `MAX_STALE_RETRIES` (default 8)
* **stale past retries / needs an agent** (e.g. transcript fetched but digest needs LLM distillation) → one recorded alert, back off to the healthy interval — never a hot loop

Deterministic backfills run as activities: the Surveillance transcript fetcher
(idempotent) and, optionally, the brief engine re-run (`BRIEF_BACKFILL_ENABLED=1`).
Anything needing judgment is surfaced via the `alerts` query and the status file —
never silently dropped.

Every iteration writes a JSON snapshot to `HEALTH_STATUS_FILE`
(default `<BRIEFS_DIR>/content-health-status.json`) with per-feed state,
the chosen cadence, actions taken, and alerts. Query the live workflow any time:

```
python scripts/content_health_workflow.py status   # full health snapshot
python scripts/content_health_workflow.py alerts   # active alerts
python scripts/content_health_workflow.py stop     # graceful shutdown (signal)
```

History hygiene: the workflow calls `continue_as_new` every
`ITERATIONS_BEFORE_CONTINUE` iterations (default 500), carrying alerts forward,
so one workflow runs effectively forever without unbounded history growth.

## Install

Requires Python 3.10+ and the Temporal CLI (single binary, includes a dev
server with SQLite persistence — fine for one always-on watchdog; it is not a
production Temporal cluster).

```bash
# 1. Temporal CLI (linux/amd64 example; pick your asset from
#    https://github.com/temporalio/cli/releases)
curl -sL -o temporal.tar.gz <release-asset-url>
tar xzf temporal.tar.gz --no-same-owner && rm temporal.tar.gz

# 2. Python SDK (use a venv, never system pip)
python3 -m venv ~/venvs/temporal
~/venvs/temporal/bin/pip install temporalio

# 3. Configure (see Environment below), then start the server + worker
```

## Run it always-on (systemd user services)

`~/.config/systemd/user/temporal-dev-server.service`:

```ini
[Unit]
Description=Temporal dev server (content-health watchdog)
After=network.target

[Service]
ExecStart=%h/temporal/bin/temporal server start-dev --db-filename %h/temporal/data/dev.db --port 7233
Restart=always
RestartSec=10

[Install]
WantedBy=default.target
```

`~/.config/systemd/user/temporal-content-worker.service`:

```ini
[Unit]
Description=Temporal worker: content-health watchdog
After=network.target temporal-dev-server.service

[Service]
ExecStart=%h/venvs/temporal/bin/python %h/workspace/skills/personal-assistant/scripts/content_health_workflow.py worker
Environment=BRIEFS_DIR=%h/workspace/briefs
Environment=SURVEILLANCE_FETCH_SCRIPT=%h/workspace/briefs/surveillance_fetch.py
Environment=BRIEF_ENGINE_SCRIPT=%h/workspace/briefs/brief_engine.py
Environment=TIMEZONE=America/Los_Angeles
Restart=always
RestartSec=10

[Install]
WantedBy=default.target
```

Then:

```bash
systemctl --user daemon-reload
systemctl --user enable --now temporal-dev-server.service temporal-content-worker.service
# start the watchdog workflow once (idempotent; survives worker restarts via event history)
~/venvs/temporal/bin/python scripts/content_health_workflow.py start
```

### Sandbox note (Muse VM)

The Muse sandbox runs as root in a container without a user systemd bus,
so `systemctl --user` does not work there. The units above are still the
reference, but on the sandbox supervision is a small shell script plus one
15-minute cron that restarts dead processes (process supervision only — it
does no content checking; all checking cadence stays inside the workflow):

* `~/workspace/temporal/supervise.sh` — idempotent: starts the dev server
  (waits for port 7233), then the worker, if either is missing.
* Cron `temporal-supervisor` (every 15 min) runs it. Because the runtime's
  scheduler survives VM replacement, this also recovers the stack after a
  reboot: at most ~15 minutes of downtime.

The SQLite file (`~/workspace/temporal/data/dev.db`) keeps workflow history
across restarts; the supervisor restarts the processes. Adjust `%h`-rooted
paths to your layout.

## Environment

| Variable | Default | Meaning |
|---|---|---|
| `TEMPORAL_ADDRESS` | `localhost:7233` | Dev server address |
| `CONTENT_TASK_QUEUE` | `content-health` | Task queue |
| `CONTENT_WORKFLOW_ID` | `content-health-watchdog` | Fixed workflow id (one watchdog) |
| `BRIEFS_DIR` | `~/briefs` | Content root (`us/`, `india/` underneath) |
| `SURVEILLANCE_DIR` | `<BRIEFS_DIR>/us` | Where surveillance digests live |
| `SURVEILLANCE_FETCH_SCRIPT` | `<script-dir>/surveillance_fetch.py` | Transcript backfill |
| `BRIEF_ENGINE_SCRIPT` | `<script-dir>/brief_engine.py` | Brief backfill |
| `HEALTH_STATUS_FILE` | `<BRIEFS_DIR>/content-health-status.json` | Snapshot output |
| `JOB_STATUS_FILE` | `<BRIEFS_DIR>/../news-assistant/status.json` | Per-job ok/failed/last_run records |
| `TIMEZONE` | `America/Los_Angeles` | Local-time rules |
| `HEALTHY_INTERVAL_SEC` | `3600` | Sleep when healthy |
| `QUIET_INTERVAL_SEC` | `10800` | Sleep 01:00–05:00 when healthy |
| `STALE_RETRY_SEC` | `900` | Retry cadence while stale |
| `MAX_STALE_RETRIES` | `8` | Backfills before `needs_attention` |
| `POSTING_CUTOFF_HOUR` | `18` | Episode expected by this local hour |
| `BRIEF_STALE_HOURS` | `8` | Brief freshness threshold |
| `BRIEF_BACKFILL_ENABLED` | `1` | Re-run brief engine when stale |
| `ITERATIONS_BEFORE_CONTINUE` | `500` | History hygiene |

## Notes and limits

* The dev server is a single Go binary with SQLite — good for one watchdog,
  not a substitute for a production Temporal cluster (no multi-node, no
  advanced visibility). For this skill's purpose it is the right weight.
* The workflow never messages you on its own; it heals what is deterministic
  and records the rest. Read `content-health-status.json` (or query the
  workflow) when you want the live picture.
* Memory: the dev server plus worker fit in ~200–300 MB. If your box is
  smaller, raise the intervals.
