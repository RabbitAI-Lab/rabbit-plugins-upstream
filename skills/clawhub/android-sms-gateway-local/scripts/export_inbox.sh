#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${SMS_GATE_BASE_URL:-}"
USER="${SMS_GATE_USER:-}"
PASS="${SMS_GATE_PASS:-}"
DEVICE_ID="${DEVICE_ID:-}"
INBOX_SINCE="${INBOX_SINCE:-}"
INBOX_UNTIL="${INBOX_UNTIL:-}"

if [[ -z "$BASE_URL" ]]; then echo "SMS_GATE_BASE_URL is required"; exit 1; fi
if [[ -z "$USER" ]]; then echo "SMS_GATE_USER is required"; exit 1; fi
if [[ -z "$PASS" ]]; then echo "SMS_GATE_PASS is required"; exit 1; fi
if [[ -z "$DEVICE_ID" ]]; then echo "DEVICE_ID is required"; exit 1; fi
if [[ -z "$INBOX_SINCE" ]]; then echo "INBOX_SINCE is required"; exit 1; fi
if [[ -z "$INBOX_UNTIL" ]]; then echo "INBOX_UNTIL is required"; exit 1; fi

BASE_URL="${BASE_URL%/}"

body="{\"deviceId\":\"$DEVICE_ID\",\"since\":\"$INBOX_SINCE\",\"until\":\"$INBOX_UNTIL\"}"

curl -sS -u "$USER:$PASS" -H "Content-Type: application/json" -d "$body" "$BASE_URL/messages/inbox/export"
