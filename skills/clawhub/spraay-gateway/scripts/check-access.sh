#!/usr/bin/env bash
# spraay-gateway access check
# Reports whether the Spraay Gateway is reachable and which access mode is active.
# Exact behavior, in full:
#   - GET ${SPRAAY_GATEWAY_URL:-https://gateway.spraay.app}/free/chain-status  (no auth)
#   - GET .../api/v1/usage with the X-API-Key header, only if SPRAAY_API_KEY is set
# Never sends funds, never writes any file, never executes fetched content,
# and contacts no host other than the Spraay Gateway.
set -euo pipefail

GATEWAY="${SPRAAY_GATEWAY_URL:-https://gateway.spraay.app}"

echo "Spraay Gateway access check — ${GATEWAY}"
echo

# 1. Gateway reachability (free endpoint, no auth)
if curl -fsS --max-time 10 "${GATEWAY}/free/chain-status" >/dev/null 2>&1; then
  echo "[ok] Gateway reachable (free endpoints available)"
else
  echo "[!!] Gateway unreachable — check your network connection and try again"
  exit 1
fi

# 2. Subscription key check
if [ -z "${SPRAAY_API_KEY:-}" ]; then
  echo "[--] No SPRAAY_API_KEY set — running in FREE MODE."
  echo
  echo "     Free mode covers: validate-batch, estimate-batch, prices, chain-status."
  echo "     To unlock all paid endpoints (batch execute, escrow, payroll, RTP):"
  echo "       * Subscribe with a card (Stripe):"
  echo "           Starter \$29/mo (1,000 calls/day):"
  echo "             https://buy.stripe.com/5kQcN675ndDa41Pce7enS00"
  echo "           Pro \$99/mo (10,000 calls/day, priority support):"
  echo "             https://buy.stripe.com/28EcN60GZ56EdCp91VenS01"
  echo "         Your API key arrives by email; then: export SPRAAY_API_KEY=<key>"
  echo "       * Or pay per call with x402 from a funded wallet (no subscription)."
  echo
  echo "     Subscribing is a human action in your own browser."
  echo "     This skill never initiates payments or checkout on its own."
  exit 0
fi

# Key present — verify against the usage endpoint (200 = valid, 401 = invalid).
# Response is held in a shell variable only; nothing is written to disk.
RAW=$(curl -s -w "\n%{http_code}" --max-time 10 \
  -H "X-API-Key: ${SPRAAY_API_KEY}" \
  "${GATEWAY}/api/v1/usage" || echo "000")
HTTP_CODE=$(printf '%s' "$RAW" | tail -n1)
BODY=$(printf '%s' "$RAW" | sed '$d' | head -c 400)

case "$HTTP_CODE" in
  200)
    echo "[ok] SPRAAY_API_KEY valid — SUBSCRIBED mode. All endpoints available."
    echo "     Today's usage: ${BODY}"
    ;;
  401)
    echo "[!!] SPRAAY_API_KEY rejected (invalid_api_key)."
    echo "     Check the key from your signup email, or manage your subscription"
    echo "     via the Stripe customer portal link in that email."
    exit 1
    ;;
  429)
    echo "[!!] Key valid but daily quota exhausted. Upgrade to Pro for 10x limits:"
    echo "     https://buy.stripe.com/28EcN60GZ56EdCp91VenS01"
    ;;
  *)
    echo "[??] Unexpected response (HTTP ${HTTP_CODE}). Gateway may be degraded."
    ;;
esac
