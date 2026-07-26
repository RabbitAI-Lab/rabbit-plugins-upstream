#!/bin/bash
# dealwork.ai API helper with HMAC-SHA256 signing
# Usage: bash ~/.openwork/ow-api.sh GET /api/v1/jobs
#        bash ~/.openwork/ow-api.sh POST /api/v1/contracts/abc/events '{"type":"START_WORK"}'

CREDS_FILE="$HOME/.openwork/credentials.json"
METHOD="$1"; ENDPOINT="$2"; BODY="${3:-}"

AGENT_ID=$(jq -r .agentAccountId "$CREDS_FILE")
HMAC_SECRET=$(jq -r .hmacSecret "$CREDS_FILE")
BASE_URL=$(jq -r .baseUrl "$CREDS_FILE")
TS=$(date +%s)
SIG=$(printf '%s' "${AGENT_ID}${TS}${BODY}" | openssl dgst -sha256 -hmac "${HMAC_SECRET}" | sed 's/.* //')

if [ "$METHOD" = "GET" ]; then
  curl -s "${BASE_URL}${ENDPOINT}" \
    -H "X-Agent-ID: ${AGENT_ID}" -H "X-Timestamp: ${TS}" -H "X-Signature: ${SIG}"
else
  curl -s -X "$METHOD" "${BASE_URL}${ENDPOINT}" \
    -H "Content-Type: application/json" \
    -H "X-Agent-ID: ${AGENT_ID}" -H "X-Timestamp: ${TS}" -H "X-Signature: ${SIG}" \
    -d "$BODY"
fi