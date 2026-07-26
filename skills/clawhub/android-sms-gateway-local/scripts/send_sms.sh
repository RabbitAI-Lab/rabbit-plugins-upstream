#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${SMS_GATE_BASE_URL:-}"
USER="${SMS_GATE_USER:-}"
PASS="${SMS_GATE_PASS:-}"
PHONE_NUMBERS="${PHONE_NUMBERS:-}"
MESSAGE_TEXT="${MESSAGE_TEXT:-}"
DEVICE_ID="${DEVICE_ID:-}"
SIM_NUMBER="${SIM_NUMBER:-}"
WITH_DELIVERY_REPORT="${WITH_DELIVERY_REPORT:-true}"

if [[ -z "$BASE_URL" ]]; then echo "SMS_GATE_BASE_URL is required"; exit 1; fi
if [[ -z "$USER" ]]; then echo "SMS_GATE_USER is required"; exit 1; fi
if [[ -z "$PASS" ]]; then echo "SMS_GATE_PASS is required"; exit 1; fi
if [[ -z "$PHONE_NUMBERS" ]]; then echo "PHONE_NUMBERS is required (comma-separated)"; exit 1; fi
if [[ -z "$MESSAGE_TEXT" ]]; then echo "MESSAGE_TEXT is required"; exit 1; fi

BASE_URL="${BASE_URL%/}"

IFS=',' read -ra nums <<< "$PHONE_NUMBERS"
json_numbers=""
for n in "${nums[@]}"; do
  n_trim="$(echo "$n" | xargs)"
  if [[ -n "$n_trim" ]]; then
    if [[ -n "$json_numbers" ]]; then json_numbers+=","; fi
    json_numbers+="\"$n_trim\""
  fi
done
if [[ -z "$json_numbers" ]]; then echo "PHONE_NUMBERS must contain at least one number"; exit 1; fi
json_numbers="[$json_numbers]"

msg_esc="$MESSAGE_TEXT"
msg_esc="${msg_esc//\\/\\\\}"
msg_esc="${msg_esc//\"/\\\"}"
msg_esc="${msg_esc//$'\n'/\\n}"

case "$WITH_DELIVERY_REPORT" in
  1|true|TRUE|yes|YES) with_delivery_report=true ;;
  0|false|FALSE|no|NO) with_delivery_report=false ;;
  *) with_delivery_report=true ;;
esac

body="{\"phoneNumbers\":$json_numbers,\"textMessage\":{\"text\":\"$msg_esc\"},\"withDeliveryReport\":$with_delivery_report"
if [[ -n "$DEVICE_ID" ]]; then body+=",\"deviceId\":\"$DEVICE_ID\""; fi
if [[ -n "$SIM_NUMBER" ]]; then body+=",\"simNumber\":$SIM_NUMBER"; fi
body+="}"

curl -sS -u "$USER:$PASS" -H "Content-Type: application/json" -d "$body" "$BASE_URL/messages"
