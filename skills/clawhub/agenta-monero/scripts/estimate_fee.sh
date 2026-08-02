#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init

address=""; amount=""; dest_raw=""
priority=0
while [[ $# -gt 0 ]]; do case "$1" in
  --address)    address="$2"; shift 2;;
  --amount)     amount="$2";  shift 2;;
  --dest)       dest_raw="$2"; shift 2;;
  --priority)   priority="$2"; shift 2;;
  *) shift;;
esac; done

[[ "$priority" =~ ^[0-4]$ ]] || json_error "INVALID_INPUT" "priority must be 0-4 (got $priority)"

if [[ -n "$dest_raw" ]]; then
  validate_dest_json "$dest_raw" 2>/dev/null || json_error "DEST_JSON_INVALID" "--dest must be a JSON array of {address, amount}"
  [[ "$(echo "$dest_raw" | jq 'length')" -gt 0 ]] || json_error "AMOUNT_INVALID" "destinations array is empty"
  dests_json="$dest_raw"
elif [[ -n "$address" && -n "$amount" ]]; then
  dests_json=$(jq -nc --arg a "$address" --arg amt "$amount" '[{address:$a, amount:$amt}]')
else
  json_error "CONFIG_MISSING" "either (--address + --amount) or --dest is required"
fi

piconero_dests="[]"
total_piconero=0
n=$(echo "$dests_json" | jq 'length')
for (( i=0; i<n; i++ )); do
  addr=$(echo "$dests_json" | jq -r ".[$i].address")
  amt=$(echo "$dests_json" | jq -r ".[$i].amount")
  va=$(rpc_call validate_address "$(jq -nc --arg a "$addr" '{address:$a, any_net_type:true, allow_openalias:false}')")
  [[ "$(echo "$va" | jq -r '.valid')" == "true" ]] || json_error "INVALID_ADDRESS" "address failed validation: $addr"
  [[ "$(echo "$va" | jq -r '.nettype')" == "${MONERO_NETWORK}" ]] || json_error "NETWORK_MISMATCH" "address nettype mismatch for $addr"
  validate_amount "$amt"
  pico=$(xmr_to_piconero "$amt")
  [[ "$pico" -gt 0 ]] || json_error "AMOUNT_INVALID" "amount must be positive: $amt"
  piconero_dests=$(echo "$piconero_dests" | jq -c --arg a "$addr" --argjson p "$pico" '. + [{address:$a, amount:$p}]')
  total_piconero=$(( total_piconero + pico ))
done

params=$(jq -nc \
  --argjson destinations "$piconero_dests" \
  --argjson priority "$priority" \
  '{destinations:$destinations, priority:$priority, get_tx_key:false, do_not_relay:true}')

res=$(rpc_call transfer "$params")

fee_xmr=$(piconero_to_xmr "$(echo "$res" | jq -r '.fee // 0')")
amt_xmr=$(piconero_to_xmr "$total_piconero")
echo "$res" | jq -c --arg fee "$fee_xmr" --arg amt "$amt_xmr" --argjson priority "$priority" --argjson n "$n" \
  '{fee:$fee, amount:$amt, priority:$priority, num_destinations:$n}'
