#!/usr/bin/env bash
# mirror.sh — back-compat thin shim over scripts/mirror.py (skill "httrack" v2.0.0)
# (root path preserved from v1.0.x so existing muscle memory keeps working)
# Usage: mirror.sh <url> [output_dir] [depth]
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
URL="${1:?usage: mirror.sh <url> [output_dir] [depth]}"
OUT="${2:-./mirror}"
DEPTH="${3:-2}"
exec python3 "$HERE/scripts/mirror.py" mirror "$URL" -o "$OUT" --depth "$DEPTH"
