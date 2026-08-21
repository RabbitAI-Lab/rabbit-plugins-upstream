#!/usr/bin/env bash
set -euo pipefail

FILE="${1:?Usage: hash-all.sh <file>}"

if [[ ! -f "$FILE" ]]; then
  echo "Error: file not found: $FILE" >&2
  exit 2
fi

echo "MD5:    $(md5sum    "$FILE" | awk '{print $1}')"
echo "SHA-1:  $(sha1sum   "$FILE" | awk '{print $1}')"
echo "SHA-256: $(sha256sum "$FILE" | awk '{print $1}')"
