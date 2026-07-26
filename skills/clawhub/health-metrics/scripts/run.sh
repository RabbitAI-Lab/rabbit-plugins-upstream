#!/usr/bin/env bash
# health-metrics runner — one-command wrapper around the pipeline.
#
# Does the two things the raw scripts do NOT do on their own:
#   1. Materializes iCloud "dataless" placeholder files before ingest. Apple Health
#      Auto Export writes into an iCloud Drive folder; with "Optimize Mac Storage"
#      on, macOS evicts file *contents* to placeholders until something opens them.
#      DuckDB/Python then fail to read with: "Resource deadlock avoided" (EDEADLK).
#      This runs `brctl download` per file and waits until the bytes are on disk.
#      (Permanent fix: in Finder, right-click each source folder -> "Keep Downloaded".
#       This step then becomes a harmless safety net.) No-op on Linux / non-iCloud dirs.
#   2. Always ingests before generating any report, so reports never render stale data.
#
# Modes:
#   run.sh daily-md [YYYY-MM-DD] [OUT_DIR]
#       Ingest, then write the Markdown daily summary (flat <OUT_DIR>/YYYY-MM-DD.md).
#       Default date = today. Default OUT_DIR = $HEALTH_MD_DIR or ./reports/summary.
#   run.sh html [OUT_DIR]
#       Ingest, then render the full HTML dashboard set into OUT_DIR.
#       Default OUT_DIR = $HEALTH_HTML_DIR or ./reports/html-<timestamp>.
#       Prints "HTML_OUT_DIR=<dir>" and lists the top-level .html files.
#   run.sh ingest
#       Materialize + ingest only.
#
# Config (env, all optional — see SKILL.md for defaults):
#   HEALTH_METRICS_DIR, HEALTH_WORKOUTS_DIR, HEALTH_DB_PATH  (consumed by the Python scripts)
#   HEALTH_MD_DIR    default output dir for daily-md
#   HEALTH_HTML_DIR  default output dir for html (a timestamp is NOT appended when set)
#
# Exits non-zero on failure so schedulers surface it.
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd -P)"

log() { echo "[health-metrics $(date '+%H:%M:%S')] $*"; }

# Resolve the source dirs the Python scripts will read, mirroring their defaults,
# so we can materialize the right folders here. Keep in sync with scripts/lib.
default_export_base() {
  # Apple Health Auto Export's iCloud container on macOS.
  echo "$HOME/Library/Mobile Documents/iCloud~com~ifunography~HealthExport/Documents"
}
metrics_dir()  { echo "${HEALTH_METRICS_DIR:-$(default_export_base)/iCloud Drive HealthMetrics}"; }
workouts_dir() { echo "${HEALTH_WORKOUTS_DIR:-$(default_export_base)/iCloud Drive Workouts}"; }

# Force-download iCloud placeholders in a dir, then wait until every JSON is readable.
# No-op if brctl is missing (Linux) or the dir doesn't exist.
materialize() {
  local dir="$1" label="$2"
  [ -d "$dir" ] || { log "skip materialize ($label): no dir $dir"; return 0; }
  command -v brctl >/dev/null 2>&1 || { log "skip materialize ($label): no brctl (non-iCloud host)"; return 0; }
  log "materializing $label ..."
  find "$dir" -maxdepth 1 -name '*.json' -print0 | while IFS= read -r -d '' f; do
    brctl download "$f" 2>/dev/null || true
  done
  local i fail total
  for i in $(seq 1 60); do
    fail=0; total=0
    while IFS= read -r -d '' f; do
      total=$((total+1))
      python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$f" 2>/dev/null || fail=$((fail+1))
    done < <(find "$dir" -maxdepth 1 -name '*.json' -print0)
    if [ "$fail" -eq 0 ]; then log "$label ready ($total files)"; return 0; fi
    sleep 5
  done
  log "WARN: $label still has $fail unreadable file(s); ingest will skip locked files"
  return 0
}

ingest() {
  materialize "$(metrics_dir)"  "HealthMetrics"
  materialize "$(workouts_dir)" "Workouts"
  log "ingesting ..."
  python3 "$SCRIPT_DIR/ingest.py"
}

daily_md() {
  local date="${1:-$(date '+%Y-%m-%d')}"
  local out="${2:-${HEALTH_MD_DIR:-$SCRIPT_DIR/../reports/summary}}"
  ingest
  mkdir -p "$out"
  log "writing daily markdown for $date -> $out"
  python3 "$SCRIPT_DIR/report_daily_summary.py" --date "$date" -o "$out"
  log "done: $out/$date.md"
}

html() {
  local out="${1:-${HEALTH_HTML_DIR:-$SCRIPT_DIR/../reports/html-$(date '+%Y-%m-%d_%H%M%S')}}"
  ingest
  mkdir -p "$out"
  log "rendering HTML dashboards -> $out"
  python3 "$SCRIPT_DIR/report.py" -o "$out"
  log "HTML_OUT_DIR=$out"
  ls "$out"/*.html 2>/dev/null || true
}

case "${1:-}" in
  daily-md) shift; daily_md "${1:-}" "${2:-}";;
  html)     shift; html "${1:-}";;
  ingest)   ingest;;
  *) echo "usage: run.sh {daily-md [YYYY-MM-DD] [OUT_DIR]|html [OUT_DIR]|ingest}" >&2; exit 2;;
esac
