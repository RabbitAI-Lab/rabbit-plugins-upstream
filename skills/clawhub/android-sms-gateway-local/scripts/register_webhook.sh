#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${SMS_GATE_BASE_URL:-}"
USER="${SMS_GATE_USER:-}"
PASS="${SMS_GATE_PASS:-}"
WEBHOOK_URL="${WEBHOOK_URL:-}"
WEBHOOK_EVENT="${WEBHOOK_EVENT:-sms:received}"
DEVICE_ID="${DEVICE_ID:-}"

if [[ -z "$BASE_URL" ]]; then echo "SMS_GATE_BASE_URL is required"; exit 1; fi
if [[ -z "$USER" ]]; then echo "SMS_GATE_USER is required"; exit 1; fi
if [[ -z "$PASS" ]]; then echo "SMS_GATE_PASS is required"; exit 1; fi
if [[ -z "$WEBHOOK_URL" ]]; then echo "WEBHOOK_URL is required"; exit 1; fi

BASE_URL="${BASE_URL%/}"

url_esc="$WEBHOOK_URL"
url_esc="${url_esc//\\/\\\\}"
url_esc="${url_esc//\"/\\\"}"

body="{\"url\":\"$url_esc\",\"event\":\"$WEBHOOK_EVENT\""
if [[ -n "$DEVICE_ID" ]]; then body+=",\"deviceId\":\"$DEVICE_ID\""; fi
body+="}"

curl -sS -u "$USER:$PASS" -H "Content-Type: application/json" -d "$body" "$BASE_URL/webhooks"
