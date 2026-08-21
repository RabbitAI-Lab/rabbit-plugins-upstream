#!/usr/bin/env bash
# git-standup: Generate a daily standup report from git commit history
set -euo pipefail

# --- Defaults ---
HOURS=24
AUTHOR=""
FORMAT="text"
REPO="."

# --- Parse args ---
while [[ $# -gt 0 ]]; do
  case "$1" in
    --hours)   HOURS="$2"; shift 2 ;;
    --author)  AUTHOR="$2"; shift 2 ;;
    --format)  FORMAT="$2"; shift 2 ;;
    --repo)    REPO="$2"; shift 2 ;;
    -h|--help)
      echo "Usage: standup.sh [--repo PATH] [--hours N] [--author NAME] [--format text|json]"
      exit 0 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

cd "$REPO" 2>/dev/null || { echo "Error: cannot access repo at $REPO"; exit 1; }
git rev-parse --is-inside-work-tree &>/dev/null || { echo "Error: not a git repository"; exit 1; }

SINCE="${HOURS} hours ago"

# --- Collect commits ---
if [[ -n "$AUTHOR" ]]; then
  COMMITS=$(git log --since="$SINCE" --author="$AUTHOR" --pretty=format:"%s" 2>/dev/null || true)
else
  COMMITS=$(git log --since="$SINCE" --pretty=format:"%s" 2>/dev/null || true)
fi

DATE=$(date +"%Y-%m-%d")

if [[ "$FORMAT" == "json" ]]; then
  COUNT=0
  JSON_ITEMS=""
  while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    COUNT=$((COUNT + 1))
    JSON_ITEMS+="{\"subject\":\"$line\"},"
  done <<< "$COMMITS"
  JSON_ITEMS="${JSON_ITEMS%,}"
  echo "{\"date\":\"$DATE\",\"lookbackHours\":$HOURS,\"author\":\"${AUTHOR:-all}\",\"commitCount\":$COUNT,\"commits\":[${JSON_ITEMS}]}"
  exit 0
fi

# --- Text output ---
echo "📋 Standup Report — ${DATE}"
echo ""

if [[ -z "$COMMITS" ]]; then
  echo "  No commits found in the last ${HOURS} hours."
  exit 0
fi

echo "Yesterday:"
while IFS= read -r line; do
  [[ -z "$line" ]] && continue
  echo "  ✅ $line"
done <<< "$COMMITS"

echo ""
echo "Today:"
echo "  ⬜ (add planned tasks here)"
echo ""
echo "Blockers:"
echo "  ⚠️ (none reported)"
