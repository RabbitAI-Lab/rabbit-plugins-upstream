#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init

tx_hash=""
address=""
proof=""
while [[ $# -gt 0 ]]; do case "$1" in
  --tx-hash) tx_hash="$2"; shift 2;;
  --address) address="$2"; shift 2;;
  --proof)   proof="$2";   shift 2;;
  --no-refresh) shift;;
  *) shift;; esac; done

[[ -n "$tx_hash" ]]  || json_error "CONFIG_MISSING" "--tx-hash is required"
[[ -n "$address" ]]  || json_error "CONFIG_MISSING" "--address is required"
[[ -n "$proof"   ]]  || json_error "CONFIG_MISSING" "--proof is required"
validate_tx_hash "$tx_hash" 2>/dev/null || json_error "INVALID_INPUT" "tx-hash must be 64 lowercase hex chars"

rpc_refresh

params=$(jq -nc --arg t "$tx_hash" --arg a "$address" --arg s "$proof" \
  '{txid:$t, address:$a, signature:$s}')

err_file="$(mktemp)"
rc=0
out=$(rpc_call check_tx_proof "$params" 2>"$err_file") || rc=$?
if [[ $rc -ne 0 ]]; then
  code=$(jq -r '.code // empty' "$err_file" 2>/dev/null || true)
  msg=$(jq -r '.message // "unknown error"' "$err_file" 2>/dev/null || true)
  rm -f "$err_file"
  if [[ "$code" == "RPC_UNREACHABLE" ]]; then
    json_error "RPC_UNREACHABLE" "$msg"
  fi
  json_error "PROOF_INVALID" "$msg"
fi
rm -f "$err_file"

good=$(printf '%s' "$out" | jq -r '.good // false')
if [[ "$good" != "true" ]]; then
  json_error "PROOF_INVALID" "wallet rejected the proof (good=false)"
fi

confirmations=$(printf '%s' "$out" | jq -r '.confirmations // 0')
pico=$(printf '%s' "$out" | jq -r '.received_amount // 0')
amount=$(piconero_to_xmr "$pico")

jq -nc --argjson v true --argjson c "$confirmations" --arg amt "$amount" \
     --arg txh "$tx_hash" --arg addr "$address" \
  '{verified:$v, confirmations:$c, amount:$amt, tx_hash:$txh, address:$addr}'
