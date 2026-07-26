#!/usr/bin/env bash
# weather_daily.sh
#
# Implements exactly what SKILL.md declares in metadata.openclaw:
#   requires.bins = [curl]
#   requires.env  = [OPENWEATHER_API_KEY]
# It must not use anything beyond that — that's the whole point of the
# W902 "declaration matches behavior" chapter.
set -euo pipefail

: "${OPENWEATHER_API_KEY:?OPENWEATHER_API_KEY is not set — see SKILL.md.}"

LOCATION="${1:-San Francisco}"
OUTPUT_DIR="${WEATHER_DAILY_OUTPUT_DIR:-$HOME/Obsidian/Daily}"
TODAY="$(date +%Y-%m-%d)"
OUTPUT_FILE="${OUTPUT_DIR}/${TODAY}.md"

mkdir -p "$OUTPUT_DIR"

RESPONSE="$(curl -s -G "https://api.openweathermap.org/data/2.5/weather" \
  --data-urlencode "q=${LOCATION}" \
  --data-urlencode "appid=${OPENWEATHER_API_KEY}" \
  --data-urlencode "units=metric")"

# Never echo $RESPONSE or $OPENWEATHER_API_KEY into logs — logging the
# raw request/response is exactly the mistake behind the v1.2.3 incident
# documented in SECURITY.md.

DESCRIPTION="$(printf '%s' "$RESPONSE" | grep -o '"description":"[^"]*"' | head -1 | cut -d':' -f2 | tr -d '"')"
TEMP="$(printf '%s' "$RESPONSE" | grep -o '"temp":[0-9.-]*' | head -1 | cut -d':' -f2)"

{
  echo "## Weather — ${LOCATION}"
  echo ""
  echo "- Conditions: ${DESCRIPTION:-unknown}"
  echo "- Temperature: ${TEMP:-unknown}°C"
  echo ""
} >> "$OUTPUT_FILE"

echo "Wrote briefing to ${OUTPUT_FILE}"
