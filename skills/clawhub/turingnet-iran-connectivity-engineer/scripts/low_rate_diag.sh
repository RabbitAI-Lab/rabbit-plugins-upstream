#!/usr/bin/env bash
# low_rate_diag.sh — LOW-RATE path evidence, owned/authorized scope ONLY.
# Requires explicit --owned attestation; clamps count 1-5 and interval >=2s;
# one ping at a time (never parallel, never flood); output piped through
# redact_pii.py before writing. Refuses non-http-checkable targets? No —
# ownership cannot be verified by software; the attestation is logged.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
OWNED=0; TARGET=""; COUNT=3; INTERVAL=5; OUT="evidence_path.txt"

while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="${2:?}"; shift 2 ;;
    --count) COUNT="${2:?}"; shift 2 ;;
    --interval) INTERVAL="${2:?}"; shift 2 ;;
    --output) OUT="${2:?}"; shift 2 ;;
    --owned) OWNED=1; shift ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

[ -n "$TARGET" ] || { echo "usage: low_rate_diag.sh --target HOST --owned [--count 3] [--interval 5] [--output F]" >&2; exit 2; }
[ "$OWNED" = "1" ] || { echo "refusing: --owned attestation required (you assert the target is yours or in written scope)" >&2; exit 2; }
command -v ping >/dev/null 2>&1 || { echo "ping not available" >&2; exit 3; }

# clamps
[ "$COUNT" -lt 1 ] && COUNT=1
[ "$COUNT" -gt 5 ] && COUNT=5
INTERVAL_NUM="${INTERVAL%s}"
[ "$INTERVAL_NUM" -ge 2 ] 2>/dev/null || INTERVAL_NUM=2

RAW="$(mktemp)"
{
  echo "# low-rate path evidence (owned-scope attested, $(date -u +%FT%TZ))"
  echo "# target: $TARGET  count: $COUNT  interval: ${INTERVAL_NUM}s — single stream, no flood"
  i=1
  while [ "$i" -le "$COUNT" ]; do
    ping -c 1 -W 5 "$TARGET" 2>&1 || echo "(no reply #$i)"
    [ "$i" -lt "$COUNT" ] && sleep "$INTERVAL_NUM"
    i=$((i + 1))
  done
} > "$RAW"

# FAIL CLOSED: a redaction failure must never leak raw diagnostics.
if python3 "$HERE/redact_pii.py" --input "$RAW" --output "$OUT" --mode standard 2>/dev/null; then
  rm -f "$RAW"
  echo "wrote $OUT (redacted)"
  exit 0
else
  rm -f "$RAW"
  echo "REFUSED: redaction failed — raw diagnostics withheld, nothing written" >&2
  exit 4
fi
