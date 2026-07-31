#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init

tx_hash=""
while [[ $# -gt 0 ]]; do case "$1" in
  --tx-hash) tx_hash="$2"; shift 2;;
  *) shift;; esac; done

[[ -n "$tx_hash" ]] || json_error "INVALID_INPUT" "--tx-hash is required"
validate_tx_hash "$tx_hash" 2>/dev/null || json_error "INVALID_INPUT" "tx-hash must be 64 lowercase hex chars"

rpc_refresh

threshold="${MONERO_CONFIRMATIONS:-10}"
params=$(jq -nc --arg txid "$tx_hash" '{txid:$txid}')

# rpc_call prints only .result on success (stdout). On failure it exits non-zero
# after writing a structured error JSON to stderr whose .code is RPC_UNREACHABLE
# (transport/daemon down) or RPC_ERROR (wallet-side error). We capture stdout and
# stderr merged: on success $res is the clean .result object; on failure $res
# holds the error JSON (curl runs with -s, suppressing its own noise).
#
# Distinguish the failure modes for double-send safety:
#   - RPC_UNREACHABLE means "could not check" (NOT "tx absent") -> propagate it
#     verbatim so a retry-safety caller does NOT conclude it is safe to resend.
#   - anything else (wallet RPC_ERROR = not in wallet, or empty result) -> TX_NOT_FOUND.
res=""
rc=0
res=$(rpc_call get_transfer_by_txid "$params" 2>&1) || rc=$?
if [[ $rc -ne 0 ]]; then
  code=""
  if [[ "$res" == *"{"* ]]; then
    code=$(printf '%s' "{${res#*\{}" | jq -r '.code // empty' 2>/dev/null || true)
  fi
  if [[ "$code" == "RPC_UNREACHABLE" ]]; then
    printf '%s\n' "{${res#*\{}" >&2
    exit 1
  fi
  json_error "TX_NOT_FOUND" "no transfer found for txid $tx_hash"
fi

transfer=$(printf '%s' "$res" | jq -c '(.transfer // (.transfers // [])[0]) // empty')
[[ -n "$transfer" && "$transfer" != "null" ]] \
  || json_error "TX_NOT_FOUND" "no transfer found for txid $tx_hash"

amount_pico=$(printf '%s' "$transfer" | jq -r '.amount // empty')
fee_pico=$(printf '%s' "$transfer" | jq -r '.fee // 0')

amount_xmr=$(piconero_to_xmr "$amount_pico")
fee_xmr=$(piconero_to_xmr "$fee_pico")

out=$(printf '%s' "$transfer" | jq -c \
  --argjson thr "$threshold" --arg amt "$amount_xmr" --arg fee "$fee_xmr" '
  . as $t
  | (($t.confirmations // 0)) as $c
  | { tx_hash:   ($t.txid // ""),
      amount:    $amt,
      fee:       $fee,
      direction: ($t.type // "in"),
      confirmations: $c,
      address:       ($t.address // null),
      address_index: ($t.address_index // null),
      timestamp:     ($t.timestamp // null),
      confirmed:     ($c >= $thr),
      unlock_time:   ($t.unlock_time // 0) }')

printf '%s\n' "$out"
