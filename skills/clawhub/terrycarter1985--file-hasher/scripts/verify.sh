#!/usr/bin/env bash
set -euo pipefail

FILE="${1:?Usage: verify.sh <file> <expected-hash> [algorithm]}"
EXPECTED="${2:?Expected hash required}"
ALGO="${3:-sha256}"

if [[ ! -f "$FILE" ]]; then
  echo "Error: file not found: $FILE" >&2
  exit 2
fi

ACTUAL=""
case "$ALGO" in
  sha256) ACTUAL=$(sha256sum "$FILE" | awk '{print $1}') ;;
  sha1)   ACTUAL=$(sha1sum   "$FILE" | awk '{print $1}') ;;
  md5)    ACTUAL=$(md5sum    "$FILE" | awk '{print $1}') ;;
  *) echo "Error: unsupported algorithm: $ALGO" >&2; exit 2 ;;
esac

if [[ "$ACTUAL" == "$EXPECTED" ]]; then
  echo "OK: $ALGO hash matches"
  exit 0
else
  echo "MISMATCH: expected $EXPECTED, got $ACTUAL"
  exit 1
fi
