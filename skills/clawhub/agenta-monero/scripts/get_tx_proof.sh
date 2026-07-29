#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init

tx_hash=""
address=""
while [[ $# -gt 0 ]]; do case "$1" in
  --tx-hash) tx_hash="$2"; shift 2;;
  --address) address="$2"; shift 2;;
  *) shift;; esac; done

[[ -n "$tx_hash" ]] || json_error "CONFIG_MISSING" "--tx-hash is required"
[[ -n "$address" ]] || json_error "CONFIG_MISSING" "--address is required"
validate_tx_hash "$tx_hash" 2>/dev/null || json_error "INVALID_INPUT" "tx-hash must be 64 lowercase hex chars"

params=$(jq -nc --arg t "$tx_hash" --arg a "$address" '{txid:$t, address:$a}')
res=$(rpc_call get_tx_proof "$params")

proof=$(printf '%s' "$res" | jq -r '.signature // empty')
[[ -n "$proof" ]] || json_error "RPC_ERROR" "no proof returned for txid $tx_hash"

jq -nc --arg txh "$tx_hash" --arg addr "$address" --arg p "$proof" \
  '{tx_hash:$txh, address:$addr, proof:$p}'
