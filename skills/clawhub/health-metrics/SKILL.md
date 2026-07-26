---
name: health-metrics
description: >-
  Ingest Apple Health Auto Export JSON (HealthMetrics + Workouts) into a local DuckDB
  database and render offline HTML dashboards plus a Markdown daily summary (activity
  rings, training load, sleep, vitals, per-workout maps). Use when the user wants to
  process Apple Health exports, refresh their health dashboards, or get a training-load /
  rings / sleep / vitals report from their exported data.
version: 1.1.0
metadata:
  openclaw:
    emoji: "🏃"
    requires:
      bins: ["python3", "duckdb"]
    env: ["HEALTH_METRICS_DIR", "HEALTH_WORKOUTS_DIR", "HEALTH_DB_PATH"]
    os: ["macos", "linux"]
---

# Health Metrics

A self-contained pipeline that ingests **Apple Health Auto Export** JSON feeds into a local
DuckDB database and renders static, offline-first HTML dashboards plus an AI-oriented Markdown
digest. No web server, no scheduler, no pip packages — just Python stdlib and the `duckdb` CLI.
You run it on demand whenever new export files land.

## Prerequisites

- `python3` and the `duckdb` CLI binary on `PATH` (no Python `duckdb` package needed).
- Apple Health Auto Export daily JSON files available on disk (see **Configuration**).
- Internet is needed only to *view* workout route maps (Leaflet + satellite tiles from a CDN).
  Everything else renders fully offline.

## Normal workflow

Regenerate everything after new exports arrive:

```bash
python3 {baseDir}/scripts/ingest.py && python3 {baseDir}/scripts/report.py -o <OUT_DIR>
```

- `ingest.py` reads the source JSON and upserts into the DuckDB file (idempotent — safe to
  re-run; unchanged files are skipped).
- `report.py -o <OUT_DIR>` writes all dashboards into a directory **you choose**. Pick a working
  or output directory the user controls; do not write inside the skill folder.

## One-command runner (`scripts/run.sh`) — recommended

`scripts/run.sh` wraps the pipeline and handles two things the raw scripts do not:

1. **Materializes iCloud placeholder files** before ingest (see the gotcha below).
2. **Always ingests before rendering**, so reports never show stale data.

```bash
bash {baseDir}/scripts/run.sh daily-md [YYYY-MM-DD] [OUT_DIR]   # ingest -> flat <OUT_DIR>/YYYY-MM-DD.md (default date = today)
bash {baseDir}/scripts/run.sh html [OUT_DIR]                    # ingest -> full HTML dashboard set in OUT_DIR
bash {baseDir}/scripts/run.sh ingest                           # materialize + ingest only
```

Output dirs: `daily-md` defaults to `$HEALTH_MD_DIR` (else `reports/summary`); `html` defaults
to `$HEALTH_HTML_DIR` (else a timestamped `reports/html-*`). `html` prints `HTML_OUT_DIR=<dir>`
on the last lines. Exits non-zero on failure so schedulers surface it.

**Use `daily-md` from a scheduler** to keep a per-day Markdown log current (e.g. a nightly cron
that writes into a knowledge/notes folder), and **`html` on demand** for shareable dashboards.

### ⚠️ iCloud "dataless placeholder" gotcha (macOS)

Apple Health Auto Export writes into an **iCloud Drive** folder. With **"Optimize Mac Storage"**
enabled, macOS evicts file *contents* to placeholders — the files still appear in `ls` (with a
size!) but their bytes are not on disk until something opens them. DuckDB and Python then fail
to read them with:

```
IO Error: Could not read from file "…HealthMetrics-YYYY-MM-DD.json": Resource deadlock avoided
```

(`EDEADLK`). `run.sh` handles this by running `brctl download` on each source file and waiting
until the bytes are present before ingesting (no-op on Linux / non-iCloud dirs).

**Permanent fix (do once):** in Finder, right-click each source folder
(`iCloud Drive HealthMetrics` and `iCloud Drive Workouts`) → **"Keep Downloaded"**. This pins the
folders so iCloud never evicts them; there is no CLI equivalent. After pinning, the `brctl`
step in `run.sh` becomes a harmless safety net.

## Configuration (all optional — sensible defaults)

| Env var | Purpose | Default |
|---|---|---|
| `HEALTH_METRICS_DIR` | Folder of `HealthMetrics-YYYY-MM-DD.json` files | Apple Health Auto Export iCloud `…/iCloud Drive HealthMetrics` under `$HOME` |
| `HEALTH_WORKOUTS_DIR` | Folder of `Workouts-YYYY-MM-DD.json` files | Apple Health Auto Export iCloud `…/iCloud Drive Workouts` under `$HOME` |
| `HEALTH_DB_PATH` | Where the DuckDB file lives | `~/.local/state/health-metrics/health.duckdb` |

`--db PATH` on `ingest.py` / `report.py` overrides `HEALTH_DB_PATH` for that run.

> ⚠️ **The DuckDB database is personal, sensitive health data.** It is created on first ingest,
> lives **outside** this skill, and must **never** be committed, published, or shared. It is not
> part of the skill bundle.

## Choosing where reports go

`report.py -o <DIR>` mirrors this layout beneath `<DIR>`:

- HTML dashboards → `<DIR>/` (`daily-*.html`, `weekly-*.html`, `monthly-*.html`, `rings.html`,
  `training-load.html`)
- Per-workout pages + index → `<DIR>/workouts/`
- Markdown daily summaries → `<DIR>/summary/`

## Individual stages (targeted re-runs)

Each script is independently runnable and honors `HEALTH_DB_PATH`. A single script's `--out-dir`
is the *literal, flat* directory it writes into (no subfolder appended).

| Script | What it produces | Key flags |
|---|---|---|
| `scripts/ingest_health_metrics.py` | `samples_qty` / `samples_hr` / `sleep_sessions` | — |
| `scripts/ingest_workouts.py` | `workouts` + `workout_route/hr/hr_recovery` | — |
| `scripts/report_health_metrics.py` | activity / sleep / vitals summaries | `--period daily\|weekly\|monthly\|all` `--date YYYY-MM-DD` `-o DIR` |
| `scripts/report_workouts.py` | one page per workout + index | `--force` (re-render all) `-o DIR` |
| `scripts/report_rings.py` | Apple-style activity rings | `-o DIR` |
| `scripts/report_training_load.py` | TRIMP training load trend | `-o DIR` |
| `scripts/report_daily_summary.py` | Markdown digest for AI readers | `--date YYYY-MM-DD` `-o DIR` |

## Ad-hoc analysis

Query the database directly — the tables in `references/schema.md` are the full analysis surface:

```bash
duckdb "$HEALTH_DB_PATH" -json -c "SELECT * FROM workouts ORDER BY date DESC LIMIT 5"
```

Or from Python via `scripts/lib/query.py`'s `query(sql)` helper (shells out to the `duckdb` CLI,
returns parsed JSON rows).

## Internals

See `{baseDir}/references/architecture.md` (data flow, ingestion pattern, report conventions,
`lib/` helpers) and `{baseDir}/references/schema.md` (DuckDB table reference) before modifying
the scripts or adding a new report/metric.
