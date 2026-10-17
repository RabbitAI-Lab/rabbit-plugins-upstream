---
name: personal-assistant
description: >-
  Build a personal market-and-research assistant: watchlist-driven price/mover
  briefs from keyless data, a video-transcript ideas fetcher, a reading inbox
  that files summaries with spoken audio, site link-health monitoring, and a
  private dashboard. Use when the user wants a daily market brief, a personal
  news digest, "brief me on my stocks", a reading list with summaries, website
  uptime/link monitoring, or a personal command-center dashboard. Trigger
  phrases: "set up my market briefs", "track my watchlist", "daily digest",
  "monitor my sites", "personal assistant", "morning briefing".
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

## Changelog

### v1.1.1
- Listing metadata fix: shortened the ClawHub summary to fit the
  300-character limit. No code changes since v1.1.0.

### v1.1.0
- New: `scripts/content_health_workflow.py` — long-running Temporal
  watchdog for content freshness with adaptive scheduling (no scheduler).
- New: `references/temporal-setup.md` — install, systemd units,
  environment variables, operating commands.
- The watchdog also reads the jobs' `status.json`: flags failed runs and
  jobs gone silent, and reconciles jobs whose output recovered since their
  last failed run (no false alarms).
