#!/usr/bin/env bash
# mirror.sh — safe HTTrack wrapper (part of the "httrack" ClawHub skill)
# Usage: mirror.sh <url> [output_dir] [depth]
set -euo pipefail

URL="${1:?usage: mirror.sh <url> [output_dir] [depth]}"
OUT="${2:-./mirror}"
DEPTH="${3:-2}"

if ! command -v httrack >/dev/null 2>&1; then
  echo "error: httrack not found — install with: sudo apt install httrack" >&2
  exit 1
fi

echo "Mirroring: $URL"
echo "Output:    $OUT"
echo "Depth:     $DEPTH"
echo "Reminder:  respect robots.txt, site terms of service, and copyright law."

exec httrack "$URL" -O "$OUT" -r"$DEPTH" -c2 --robots=1
