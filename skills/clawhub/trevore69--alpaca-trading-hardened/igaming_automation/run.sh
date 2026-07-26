#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

LOCKFILE="/tmp/igaming_automation.lock"
if [ -e "$LOCKFILE" ] && kill -0 "$(cat "$LOCKFILE")" 2>/dev/null; then
    echo "Another run is already in progress (PID $(cat "$LOCKFILE")). Skipping."
    exit 0
fi
echo $$ > "$LOCKFILE"
trap 'rm -f "$LOCKFILE"' EXIT

export BRIDGE_API_KEY="${BRIDGE_API_KEY:-341f4f924e0dd07b0fb5817779f55b29be0fd144801999a0c5f792a151caa872}"
export BRIDGE_URL="${BRIDGE_URL:-http://127.0.0.1:5555/v1}"
export SEO_PASSES="${SEO_PASSES:-1}"
export PIPELINE_MODE="${PIPELINE_MODE:-auto}"

LOGFILE="run.log"
exec >> "$LOGFILE" 2>&1

echo "============================================"
echo "Run started: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "Mode: $PIPELINE_MODE"
echo "SEO passes: $SEO_PASSES"
echo "Dry run: ${DRY_RUN:-false}"
echo "============================================"

python3 pipeline.py --mode "$PIPELINE_MODE" --status publish

echo "Run finished: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
