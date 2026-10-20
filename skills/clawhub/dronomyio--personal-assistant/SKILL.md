---
name: personal-assistant
description: >-
  Build a personal market-and-research assistant: watchlist-driven price/mover
  briefs from keyless data, a video-transcript ideas fetcher, a reading inbox
  that files summaries with spoken audio, site link-health monitoring, and a
  private dashboard. Use when the user wants a daily market brief, a personal
  news digest, "brief me on my stocks", a reading list with summaries, website
  uptime/link monitoring, or a personal command-center dashboard. Trigger
  phrases (kept specific to avoid accidental invocation): "set up my market
  briefs", "track my watchlist", "daily market digest",
  "monitor my sites", "personal market assistant", "morning market briefing".
user-invocable: true
---

# Personal Assistant

A portable pattern for a personal intelligence system: small scheduled jobs
collect keyless data into flat files; a private dashboard (and/or daily
digest) surfaces it; everything stays quiet unless something is genuinely
significant. Zero personal content ships with this skill — the user supplies
their watchlist, sites, and inbox on setup.

## Purpose

Give one person (or family/friends, each with their own copy) a calm,
always-current briefing layer over *their* interests: their stocks, their
sites, their reading, their media diet. It replaces doomscrolling with a
short, trustworthy morning read plus alerts only when thresholds break.

## Workflow — setup

1. **Lay out directories.** The skill assumes a workspace with:
   `briefs/`, `content-repo/{inbox,notes,audio}`, `site-health/`,
   `news-assistant/`. Any paths work — the scripts take `--out-dir`-style
   args or documented defaults; update them on install.
2. **Create the watchlist.** Copy `templates/watchlist.md` to
   `news-assistant/watchlist.md` and fill in real tickers. Sections:
   `## US stocks`, `## Indian stocks` (or rename for your markets —
   `brief_engine.py --market` takes any label, but the Yahoo fallback
   logic in the script is US/India-specific; adapt as needed).
   Share quantities in parentheses are optional and weight significance.
3. **Configure sites.** Copy `templates/sites.json`, put real
   `{"slug": "https://..."}` entries, point `check_links.py --sites-file`
   at it.
4. **Run the engines once manually** to verify output, then schedule
   (see `references/scheduling-patterns.md` and `templates/brief-cron.md`):
   - `brief_engine.py --market <m>` — pre-market / hourly / close
   - `market_brief.py <m> <slot>` — macro + sector digest
   - `surveillance_fetch.py` — daily transcript fetch (personal use only)
   - `check_links.py --sites-file sites.json` — daily ping / weekly crawl
   - inbox processor every 30 min: summarize → file note (`templates/note.md`)
     + spoken audio → mark done
5. **Build the dashboard** (optional but recommended) following
   `references/dashboard-pattern.md`. Until then, the `latest.json`
   files and notes *are* the product — readable as-is.
6. **Set notification thresholds** per job (the `>5%` mover / site-down
   defaults are in the cron template). Fewer, louder alerts beat many
   quiet ones.

## Output Contract

Every script writes the same shape:

- `<out-dir>/<STAMP>.json` — timestamped run output (UTC `YYYY-MM-DDTHHMMZ`)
- `<out-dir>/latest.json` — pointer to the newest run; downstream readers
  only ever read `latest.*`
- Console: one-line human verdict (`67/67 resolved, 5 movers`), never a dump
- A shared `status.json` gets `{last_run, result, summary}` per job id

## Operating Rules

1. **Keyless sources first.** Yahoo Finance chart API + Google News RSS
   need no keys. Keyed sources go behind explicit per-source flags.
2. **Quiet unless significant.** Jobs message the user only on real
   thresholds; otherwise a one-line verdict in the log. (This rule is
   what makes 20+ daily jobs livable.)
3. **Never fabricate.** A failed collection records `failed` — it never
   writes plausible-looking fake data. No source, no brief.
4. **Licensed content stays local.** Transcripts and full-text extractions
   are personal-consumption only: no public sync, no long quotes.
5. **Staleness is visible.** Every surface shows "last updated" from
   `status.json`. Silent old data is a bug.
6. **Secrets live in the environment**, never in the repo, the skill, or
   chat. This skill needs none by default.

## Content-health agent (Temporal)

One long-running Temporal workflow keeps every content feed fresh — no
scheduler involved. It checks the Surveillance digest, the US brief, and
the India brief; heals what is deterministic (transcript backfills, brief
re-runs); and adapts its own cadence: hourly when healthy, 15-minute
retries while stale, quiet-hour backoff overnight, one recorded alert
instead of a hot loop when something needs a human. Query it any time for
live status. Full install and environment reference:
`references/temporal-setup.md`. Entry point:
`scripts/content_health_workflow.py` (`worker` | `start` | `status` |
`alerts` | `stop`).

## Permissions & tool scope

What this skill needs from its host environment — declared explicitly so a
reviewer never has to guess:

- **Network (outbound only).** `surveillance_fetch.py` → YouTube
  (`youtube.com`, `youtu.be`) via yt-dlp; `brief_engine.py` /
  `market_brief.py` → Yahoo Finance chart API and Google News RSS;
  `check_links.py` → only the site URLs the user puts in their own
  `sites.json`. No other hosts. Nothing is uploaded anywhere.
- **Shell.** `yt-dlp` and `ffmpeg` are invoked via `subprocess` in
  list-form (`shell=False`, never `shell=True`); URLs passed to yt-dlp are
  built by `watch_url()` and restricted to YouTube domains with validated
  video ids. No arbitrary command execution, no shell interpolation.
- **Filesystem.** Reads/writes are confined to the data directories the
  user creates (`briefs/`, `content-repo/`, `site-health/`,
  `news-assistant/`) plus the local Memori SQLite file. Scripts never write
  outside them.
- **Memory.** `memori_client.py` uses Memori's open-source SDK in local
  BYODB mode: SQLite storage + local ONNX embeddings. No API key, no
  cloud, no data leaves the machine. Per-agent namespaces
  (`<user>/<agent>`) keep agents' learnings separated.
- **Background execution.** Scheduling is opt-in and user-owned. The
  engines run on cron entries you create from `templates/brief-cron.md`;
  the content-health watchdog runs as a Temporal worker / systemd unit you
  install from `references/temporal-setup.md` — the skill installs no
  background services by itself. Review the schedule and the systemd units
  before enabling anything (see Uninstall for removal).
- **Secrets.** None required by default. Keyed sources sit behind explicit
  per-source flags; keys live in the environment, never in the skill.
- **No hosted backend.** This package is the interface layer (docs +
  engines). There is no server component, no telemetry, no phone-home.

## Uninstall

Removal is the reverse of setup, in this order:

1. **Stop scheduled jobs.** Delete the cron entries you created from
   `templates/brief-cron.md` (`crontab -e`); stop and disable the
   content-health systemd units from `references/temporal-setup.md`
   (`systemctl --user disable --now <unit>`); terminate any Temporal
   schedules for the watchdog. Verify: `crontab -l | grep -i
   personal-assistant` prints nothing and `systemctl --user list-units |
   grep -i content-health` prints nothing.
2. **Delete data directories** created during setup: `briefs/`,
   `content-repo/`, `site-health/`, `news-assistant/` (under your workspace).
3. **Delete local memory** created by `memori_client.py` if you used it.
4. **Remove the skill** from your agent's skills directory.

The skill makes no system-wide changes, so steps 1–4 are complete removal.

## What ships in this package

This is deliberately a thin interface layer, not a hosted product:

- `SKILL.md` — the workflow documentation you are reading
- `scripts/` — the engines; each does one documented job (see Workflow
  §4 and Content-health agent above):
  - `brief_engine.py` / `market_brief.py` — watchlist price/mover briefs
  - `surveillance_fetch.py` — daily Bloomberg Surveillance transcript fetch
  - `check_links.py` — site link-health monitoring
  - `content_health_workflow.py` — Temporal watchdog for feed freshness
  - `memori_client.py` — local memory layer (SQLite + ONNX, no cloud)
- `templates/` — starter watchlist, sites file, cron templates, note format
- `references/` — scheduling, dashboard, Temporal setup, architecture

Heavy compute (scheduled runs, the dashboard, the watchdog worker) executes
in *your* environment on *your* schedule — nothing here runs without you
enabling it. Each script is one component of the documented pipeline, not
the whole system; that per-file scope is intentional, not a mismatch.

## Changelog

### v1.1.2
- Security-review hardening after the ClawHub audit (outcome: Review):
  new **Permissions & tool scope** section (network / shell / filesystem /
  memory / background / secrets declared explicitly); new **Uninstall**
  section (cron, systemd units, Temporal schedules, data dirs, local
  memory); new **What ships in this package** section mapping each script
  to its documented job; trigger phrases narrowed to avoid accidental
  invocation; `surveillance_fetch.py` gains a `watch_url()` guard
  (validated YouTube video ids, YouTube-only domains, list-form
  subprocess).
### v1.1.1
- Listing metadata fix: shortened the ClawHub summary to fit the
  300-character limit.
- Watchdog fix: the `job_status` reconciler now treats a failed
  surveillance run as recovered if a digest exists for any episode date
  on/after the failed run (previously only checked the current expected
  date, which raised a false alert overnight).

### v1.1.0
- New: `scripts/content_health_workflow.py` — long-running Temporal
  watchdog for content freshness with adaptive scheduling (no scheduler).
- New: `references/temporal-setup.md` — install, systemd units,
  environment variables, operating commands.
- The watchdog also reads the jobs' `status.json`: flags failed runs and
  jobs gone silent, and reconciles jobs whose output recovered since their
  last failed run (no false alarms).
