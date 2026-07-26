#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${SMS_GATE_BASE_URL:-}"
USER="${SMS_GATE_USER:-}"
PASS="${SMS_GATE_PASS:-}"
MESSAGE_ID="${MESSAGE_ID:-}"

if [[ -z "$BASE_URL" ]]; then echo "SMS_GATE_BASE_URL is required"; exit 1; fi
if [[ -z "$USER" ]]; then echo "SMS_GATE_USER is required"; exit 1; fi
if [[ -z "$PASS" ]]; then echo "SMS_GATE_PASS is required"; exit 1; fi
if [[ -z "$MESSAGE_ID" ]]; then echo "MESSAGE_ID is required"; exit 1; fi

BASE_URL="${BASE_URL%/}"

curl -sS -u "$USER:$PASS" "$BASE_URL/messages/$MESSAGE_ID"
