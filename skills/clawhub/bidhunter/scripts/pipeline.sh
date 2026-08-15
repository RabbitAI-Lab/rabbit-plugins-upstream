#!/usr/bin/env bash
# pipeline.sh - Full pipeline: fetch -> qualify -> report
# Usage:
#   bash pipeline.sh [--fresh] [--platform <name>] [--quote] [--date YYYY-MM-DD]
#   bash pipeline.sh --dry-run [--summary]
#   bash pipeline.sh --help

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
DRY_RUN=0
SUMMARY_MODE=0

print_help() {
  cat << 'EOF'
BidHunter Pipeline v1.1

Usage:
  bash pipeline.sh [options]

Options:
  --dry-run           干跑模式：执行全流程但不推送，输出报告预览
  --platform <name>   指定单平台运行（默认采集所有已配置平台）
                       支持: cnooc, sinopec, petrochina, cnpc 等
  --summary           精华版报告（Top 5，适合 IM 推送）
  --fresh             强制重新采集当天数据（跳过缓存）
  --quote             生成报价表底稿（CSV）
  --date YYYY-MM-DD   指定运行日期（默认今天）
  --help              显示本帮助信息

Examples:
  # 每日定时运行（全流程）
  bash pipeline.sh

  # 预览今天数据（不推送）
  bash pipeline.sh --dry-run

  # 只看精华版
  bash pipeline.sh --dry-run --summary

  # 指定平台 + 强制重新采集
  bash pipeline.sh --platform cnooc --fresh

Environment:
  PYTHON              Python interpreter (default: python3)
EOF
}

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --help)
      print_help
      exit 0
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --platform)
      PLATFORM="$2"
      shift 2
      ;;
    --summary)
      SUMMARY_MODE=1
      shift
      ;;
    --fresh)
      FRESH=1
      shift
      ;;
    --quote)
      GEN_QUOTE=1
      shift
      ;;
    --date)
      TARGET_DATE="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1" >&2
      echo "Run with --help for usage." >&2
      exit 1
      ;;
  esac
done

[[ -z "$TARGET_DATE" ]] && TARGET_DATE="$(date +%Y-%m-%d)"
CACHE_FILE="${CACHE_DIR}/bid_${TARGET_DATE}.jsonl"
QUAL_FILE="${CACHE_DIR}/qual_${TARGET_DATE}.jsonl"
TEXT_REPORT="${REPORT_DIR}/report_${TARGET_DATE}.txt"
HTML_REPORT="${REPORT_DIR}/report_${TARGET_DATE}.html"

PYTHON="${PYTHON:-python3}"

# DRY RUN: validate rules first, then show preview
if [[ $DRY_RUN -eq 1 ]]; then
  echo "=== BidHunter Pipeline [DRY RUN] ==="
  echo "Date: ${TARGET_DATE}"
  echo ""

  # Validate rules
  echo "[Validate] Checking rule library..."
  if $PYTHON "${SCRIPT_DIR}/qual_check.py" --validate-rules "$RULES_FILE"; then
    echo "  Rules: OK"
  else
    echo "  Rules: Issues found (see above)" >&2
  fi
  echo ""

  # Check if cache exists
  if [[ ! -f "$CACHE_FILE" ]]; then
    echo "No cached data for ${TARGET_DATE}. Run without --dry-run to fetch data."
    exit 0
  fi

  ITEM_COUNT=$(wc -l < "$CACHE_FILE" | tr -d ' ')
  echo "Cache: ${ITEM_COUNT} items found"
  echo ""

  # Run qualification check
  echo "[Qualify] Running qualification check..."
  $PYTHON "${SCRIPT_DIR}/qual_check.py" "$CACHE_FILE" "$RULES_FILE" > "$QUAL_FILE" 2>&1 || true

  # Generate text report
  echo "[Report] Generating text report..."
  if [[ $SUMMARY_MODE -eq 1 ]]; then
    REPORT_CONTENT=$($PYTHON "${SCRIPT_DIR}/report_text.py" "$QUAL_FILE" "$TARGET_DATE" --summary 2>/dev/null)
  else
    REPORT_CONTENT=$($PYTHON "${SCRIPT_DIR}/report_text.py" "$QUAL_FILE" "$TARGET_DATE" 2>/dev/null)
  fi

  # Show preview (first 30 lines)
  echo "========== Report Preview (first 30 lines) =========="
  echo "$REPORT_CONTENT" | head -n 30
  echo "..."
  echo "========== End Preview =========="
  echo ""

  # List output files
  echo "Output files:"
  echo "  Text:  ${TEXT_REPORT}"
  echo "  Qual:  ${QUAL_FILE}"
  echo "  HTML:  ${HTML_REPORT}"
  echo ""
  echo "✅ Dry run complete. Remove --dry-run to run for real."
  echo "   Example: bash pipeline.sh --summary"
  exit 0
fi

# Normal full run
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
REPORT_ARGS=()
[[ $SUMMARY_MODE -eq 1 ]] && REPORT_ARGS+=("--summary")

$PYTHON "${SCRIPT_DIR}/report_text.py" "$QUAL_FILE" "$TARGET_DATE" "${REPORT_ARGS[@]}" > "$TEXT_REPORT" 2>/dev/null || {
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
