#!/usr/bin/env bash
# pipeline.sh - Full pipeline: fetch -> qualify -> report
# Usage: bash pipeline.sh [--fresh] [--platform <name>] [--quote] [--date YYYY-MM-DD]

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CACHE_DIR="${SCRIPT_DIR}/bid_cache"
REPORT_DIR="${SCRIPT_DIR}/bid_reports"
QUOTE_DIR="${SCRIPT_DIR}/bid_quotes"
RULES_FILE="${SCRIPT_DIR}/qual_rules.json"

mkdir -p "$CACHE_DIR" "$REPORT_DIR" "$QUOTE_DIR"

FRESH=0
PLATFORM=""
GEN_QUOTE=0
TARGET_DATE=""

while [[ $# -gt 0 ]]; do
  case $1 in
    --fresh) FRESH=1; shift;;
    --platform) PLATFORM="$2"; shift 2;;
    --quote) GEN_QUOTE=1; shift;;
    --date) TARGET_DATE="$2"; shift 2;;
    *) echo "Unknown option: $1" >&2; exit 1;;
  esac
done

[[ -z "$TARGET_DATE" ]] && TARGET_DATE="$(date +%Y-%m-%d)"
CACHE_FILE="${CACHE_DIR}/bid_${TARGET_DATE}.jsonl"
QUAL_FILE="${CACHE_DIR}/qual_${TARGET_DATE}.jsonl"
TEXT_REPORT="${REPORT_DIR}/report_${TARGET_DATE}.txt"
HTML_REPORT="${REPORT_DIR}/report_${TARGET_DATE}.html"

PYTHON="${PYTHON:-python3}"

echo "=== BidHunter Pipeline ==="
echo "Date: ${TARGET_DATE}"
echo ""

# Step 1: Fetch
echo "[1/4] Fetching announcements..."
FETCH_ARGS=""
[[ $FRESH -eq 1 ]] && FETCH_ARGS="--fresh"
[[ -n "$PLATFORM" ]] && FETCH_ARGS="$FETCH_ARGS --platform $PLATFORM"
[[ -n "$TARGET_DATE" ]] && FETCH_ARGS="$FETCH_ARGS --date $TARGET_DATE"

bash "${SCRIPT_DIR}/bid_monitor.sh" $FETCH_ARGS > "$CACHE_FILE" 2>/dev/null || {
  echo "ERROR: fetch failed" >&2
  exit 1
}

ITEM_COUNT=$(wc -l < "$CACHE_FILE" | tr -d ' ')
echo "    Fetched: ${ITEM_COUNT} items"

if [[ "$ITEM_COUNT" -eq 0 ]]; then
  echo "    No items found. Done."
  echo "今日无新公告。" > "$TEXT_REPORT"
  exit 0
fi

# Step 2: Qualify
echo "[2/4] Running qualification check..."
$PYTHON "${SCRIPT_DIR}/qual_check.py" "$CACHE_FILE" "$RULES_FILE" > "$QUAL_FILE" 2>/dev/null || {
  echo "ERROR: qualification check failed" >&2
  exit 1
}

QUAL_COUNT=$(wc -l < "$QUAL_FILE" | tr -d ' ')
echo "    Qualified: ${QUAL_COUNT} items"

# Step 3: Generate reports
echo "[3/4] Generating reports..."
$PYTHON "${SCRIPT_DIR}/report_text.py" "$QUAL_FILE" "$TARGET_DATE" > "$TEXT_REPORT" 2>/dev/null || {
  echo "WARN: text report generation had issues" >&2
}
$PYTHON "${SCRIPT_DIR}/report_html.py" "$QUAL_FILE" "$TARGET_DATE" "$HTML_REPORT" 2>/dev/null || {
  echo "WARN: html report generation had issues" >&2
}

echo "    Text:  ${TEXT_REPORT}"
echo "    HTML:  ${HTML_REPORT}"

# Step 4: Quote generation (optional)
if [[ $GEN_QUOTE -eq 1 ]]; then
  echo "[4/4] Generating quote draft..."
  $PYTHON "${SCRIPT_DIR}/quote_gen.py" "$QUAL_FILE" "$TARGET_DATE" "${QUOTE_DIR}" 2>/dev/null || {
    echo "WARN: quote generation had issues" >&2
  }
  echo "    Quotes: ${QUOTE_DIR}"
else
  echo "[4/4] Quote generation skipped (use --quote to enable)"
fi

echo ""
echo "=== Pipeline complete ==="
echo "Reports saved to: ${REPORT_DIR}/"
