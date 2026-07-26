# Architecture

Internals of the `health-metrics` skill — read this before modifying the scripts or adding a new
report/metric. Operational usage lives in `../SKILL.md`; the table reference in `./schema.md`.

## Data flow

```
Apple Health Auto Export folders (source JSON, outside this skill)
  -> scripts/ingest_*.py   (parse + normalize, idempotent upsert into the DuckDB file)
  -> scripts/report_*.py   (query DuckDB, render self-contained HTML/Markdown into an out-dir)
```

Source JSON lives outside the skill, in the Apple Health Auto Export folders. The folders are
configurable via `HEALTH_METRICS_DIR` / `HEALTH_WORKOUTS_DIR` (see `../SKILL.md`); the defaults
point at the standard iCloud locations:

- `…/iCloud~com~ifunography~HealthExport/Documents/iCloud Drive HealthMetrics/HealthMetrics-YYYY-MM-DD.json`
- `…/iCloud Drive Workouts/Workouts-YYYY-MM-DD.json`

Each ingester only reads **daily** files (`HealthMetrics-YYYY-MM-DD.json` /
`Workouts-YYYY-MM-DD.json`). Weekly/monthly/yearly rollup files in those same folders are ignored.

The DuckDB file location comes from `HEALTH_DB_PATH` (default
`~/.local/state/health-metrics/health.duckdb`), resolved centrally by `scripts/lib/query.py`'s
`db_path()`. It is per-person sensitive state — created on first ingest, never versioned or
bundled.

## Ingestion pattern (`scripts/ingest_health_metrics.py`, `scripts/ingest_workouts.py`)

Both follow the same idempotent shape, invoking the `duckdb` CLI via `subprocess` (never the
`duckdb` Python package):

1. `CREATE TABLE IF NOT EXISTS` schema block, run every time.
2. Glob candidate files matching the strict daily-file regex.
3. Skip a file if its `mtime` matches what's recorded in `ingested_files` / `ingested_workout_files`.
4. Otherwise DELETE-then-INSERT the affected rows in one transaction, then upsert the tracking row.
   - `ingest_health_metrics.py` dedupes by `date` (one file = one day = full delete/replace of that
     day's rows across all three tables).
   - `ingest_workouts.py` dedupes by workout `id`, not by file/day — a workout can appear in
     multiple period files with the same `id`, and re-ingesting replaces that workout's rows
     wherever it lands.
5. `scripts/lib/metrics.py` is a whitelist: only metrics listed there are kept from HealthMetrics
   exports. Anything else (nutrition, weight, mindful minutes, swimming, …) is silently dropped at
   ingest time — check that file before assuming a metric name is queryable.
6. `ingest_workouts.py` additionally defends against Apple omitting fields per-workout-type (e.g.
   `flightsClimbed` absent for a swim) rather than nulling them — `available_fields()` probes the
   file's inferred schema via `DESCRIBE` before building the INSERT, since an all-null/all-absent
   JSON field can't be `.qty`-accessed or UNNESTed. Read `WORKOUT_FIELD_EXPRS` in that file before
   adding a new workout column.

## Report scripts

All build a full HTML/Markdown string in Python and `write_text()` it into the out-dir.

- `report_health_metrics.py` — daily/weekly/rolling-28-day summary dashboards (activity, sleep,
  vitals, "other tracked" metrics, auto-generated text insights vs. a 28-day baseline). Static SVG
  via `lib/svg.py`.
- `report_workouts.py` — one detail page per workout (`workouts/<date>-<slug>.html`) plus
  `index.html`. Route map uses Leaflet + Esri World Imagery satellite tiles from public CDNs at
  view time — the **only** part that needs internet to render; everything else is fully offline.
- `report_rings.py` — Apple-style Activity Rings (Move/Exercise/Stand against fixed goals), hero
  ring + 7-day mini rings + 28-day interactive trend charts via `lib/ichart.py`.
- `report_training_load.py` — TRIMP-based training load (Banister formula) as a 7-day rolling sum
  ("weekly load") vs. a tau=28-day EWMA scaled to weekly-equivalent units ("monthly trend"). Both
  series kept in the same units so they're visually comparable on one chart (see `ewma_series()`).
- `report_daily_summary.py` — the **only Markdown report**, written for AI/LLM readers. One
  self-contained file per day at `summary/YYYY-MM-DD.md` (YAML frontmatter + prose), deep-diving the
  target day plus 7d/28d/90d trend context, in three insight tiers (progress, readiness,
  trajectory). It **imports and reuses** the engines from `report_training_load.py` (TRIMP/EWMA),
  `report_rings.py` (ring goals + `daily_activity`), and `report_health_metrics.py` (`DISPLAY_NAME`)
  rather than re-deriving them, so the Markdown numbers can't drift from the HTML dashboards.

### CSS building convention

All report `HTML_HEAD` strings build CSS via plain single-brace strings +
`.replace("__PLACEHOLDER__", …)` substitution, **not** `str.format()` — a past bug came from CSS
braces needing `{{ }}` escaping for a `.format()` that was never actually called, silently breaking
the `<style>` block. Keep new report scripts consistent with this pattern. (The only legitimate
`__…__` token that survives into rendered output is `window.__ICHART_DATA`, the ichart runtime.)

## `scripts/lib/` (shared, imported by ingest and report scripts)

- `query.py` — `db_path()` (resolves `HEALTH_DB_PATH`) and the `query(sql)` helper.
- `metrics.py` — metric whitelist/category maps (`QTY_METRICS`, `HR_METRICS`, `ALL_QTY`,
  `CUMULATIVE_METRICS`, `CATEGORY_OF`). Whether a metric is summed vs. averaged over a period is
  decided by `CUMULATIVE_METRICS` — check it before aggregating a new metric.
- `geo.py` — `haversine_m`, `douglas_peucker` (route simplification), `km_splits` (per-km pace).
  Pure stdlib.
- `svg.py` — static precomputed SVG chart primitives (rings, gauges, calendar heatmap, stacked
  bars, sparklines, `line_chart`). Used where no interactivity is needed.
- `ichart.py` — the interactive chart component (client-side hover/touch tooltips). Use this (not
  `svg.line_chart`) for any new interactive trend chart.

Every script does `sys.path.insert(0, str(Path(__file__).parent))` then imports siblings and
`lib.*`, so the whole `scripts/` tree relocates as a unit without import edits.

## Adding a stage

Both `scripts/ingest.py` and `scripts/report.py` are thin orchestrators — import any new stage
module and call its `main()` / `render()` in sequence there. Follow the
`report_rings.py`/`report_training_load.py` pattern (interactive `lib/ichart.py` charts,
`.replace()`-based HTML head) for new reports unless a chart genuinely doesn't need interactivity.

## Historical note: backfill

History older than when daily exports began was originally bootstrapped once with two one-off
scripts (`split_healthmetrics_history.py`, `split_workout_history.py`) that split multi-day
weekly/monthly/yearly rollup files into synthetic per-day files the daily-only ingesters could pick
up. Those scripts were non-idempotent-by-design, have already been run, and are **not shipped** with
this skill. HealthMetrics *yearly* files were intentionally never split (their metrics are bucketed
per-week, not per-day, so splitting would misattribute a week's total to a single day).
