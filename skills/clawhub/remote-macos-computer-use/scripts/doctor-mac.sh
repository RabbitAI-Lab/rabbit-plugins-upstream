#!/usr/bin/env bash
# Health checks for the remote-macos-computer-use bridge, run ON THE MAC.
# Env: REMOTE_HOST (required), REVERSE_PORT (default 2299), REMOTE_USER (default ubuntu)
set -uo pipefail
REVERSE_PORT="${REVERSE_PORT:-2299}"
REMOTE_USER="${REMOTE_USER:-ubuntu}"
REMOTE_HOST="${REMOTE_HOST:-}"
if [ -z "$REMOTE_HOST" ]; then echo "ERROR: set REMOTE_HOST to your server address"; exit 1; fi

echo "== [1/5] cua-driver install =="
cua-driver --version 2>&1 | head -1

echo; echo "== [2/5] cua-driver daemon =="
cua-driver status 2>&1 | head -4

echo; echo "== [3/5] cua-driver permissions =="
cua-driver permissions status --json 2>&1 | python3 -c 'import sys,json
try:
  d=json.load(sys.stdin); print("  accessibility:", d.get("accessibility"), "| screen_recording:", d.get("screen_recording"), "| attribution:", d.get("source",{}).get("attribution"))
except Exception as e: print("  could not parse:", e)' 2>&1 | head -3

echo; echo "== [4/5] LaunchAgents (persistence) =="
launchctl list 2>/dev/null | grep -E "trycua|remote-macos|keep-awake" | sed 's/^/   /' || echo "   (none loaded)"

echo; echo "== [5/5] tunnel process + server listener =="
pgrep -fal "ssh -N.*-R $REVERSE_PORT" | grep -v 'grep\|/bin/zsh' | head -1 | sed 's/^/   /' || echo "   tunnel NOT running"
ssh -o BatchMode=yes -o ConnectTimeout=6 "$REMOTE_USER@$REMOTE_HOST" \
  "ss -ltn 2>/dev/null | grep ':$REVERSE_PORT ' || echo 'server not listening'" 2>/dev/null | sed 's/^/   server: /' || echo "   server check failed"

echo; echo "== done =="
