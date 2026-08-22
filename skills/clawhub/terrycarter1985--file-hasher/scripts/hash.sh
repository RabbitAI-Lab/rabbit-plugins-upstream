#!/usr/bin/env bash
set -euo pipefail

FILE="${1:?Usage: hash.sh <file> [algorithm]}"
ALGO="${2:-sha256}"

if [[ ! -f "$FILE" ]]; then
  echo "Error: file not found: $FILE" >&2
  exit 2
fi

case "$ALGO" in
  sha256) sha256sum "$FILE" | awk '{print $1}' ;;
  sha1)   sha1sum   "$FILE" | awk '{print $1}' ;;
  md5)    md5sum    "$FILE" | awk '{print $1}' ;;
  *) echo "Error: unsupported algorithm: $ALGO (use sha256|sha1|md5)" >&2; exit 2 ;;
esac
