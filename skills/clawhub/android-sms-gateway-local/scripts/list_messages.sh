#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${SMS_GATE_BASE_URL:-}"
USER="${SMS_GATE_USER:-}"
PASS="${SMS_GATE_PASS:-}"
MSG_FROM="${MSG_FROM:-}"
MSG_TO="${MSG_TO:-}"
MSG_STATE="${MSG_STATE:-}"
DEVICE_ID="${DEVICE_ID:-}"
MSG_LIMIT="${MSG_LIMIT:-50}"
MSG_OFFSET="${MSG_OFFSET:-0}"

if [[ -z "$BASE_URL" ]]; then echo "SMS_GATE_BASE_URL is required"; exit 1; fi
if [[ -z "$USER" ]]; then echo "SMS_GATE_USER is required"; exit 1; fi
if [[ -z "$PASS" ]]; then echo "SMS_GATE_PASS is required"; exit 1; fi

BASE_URL="${BASE_URL%/}"

query=""
add_q() {
  local key="$1"; local val="$2"
  if [[ -n "$val" ]]; then
    if [[ -n "$query" ]]; then query+="&"; fi
    query+="$key=$val"
  fi
}

add_q "from" "$MSG_FROM"
add_q "to" "$MSG_TO"
add_q "state" "$MSG_STATE"
add_q "deviceId" "$DEVICE_ID"
add_q "limit" "$MSG_LIMIT"
add_q "offset" "$MSG_OFFSET"

url="$BASE_URL/messages"
if [[ -n "$query" ]]; then url+="?$query"; fi

curl -sS -u "$USER:$PASS" "$url"
