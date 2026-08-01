#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init

address=""; account=0; subaddress=""; priority=0; do_not_relay=false; confirmed=false
while [[ $# -gt 0 ]]; do case "$1" in
  --address)    address="$2"; shift 2;;
  --account)    account="$2"; shift 2;;
  --subaddress) subaddress="$2"; shift 2;;
  --priority)   priority="$2"; shift 2;;
  --dry-run)    do_not_relay=true; shift;;
  --confirm)    confirmed=true; shift;;
  *) shift;;
esac; done

[[ "$priority" =~ ^[0-4]$ ]] || json_error "INVALID_INPUT" "priority must be 0-4 (got $priority)"

[[ -n "$address" ]] || json_error "CONFIG_MISSING" "--address is required"

va=$(rpc_call validate_address "$(jq -nc --arg a "$address" '{address:$a, any_net_type:true, allow_openalias:false}')")
[[ "$(echo "$va" | jq -r '.valid')" == "true" ]] || json_error "INVALID_ADDRESS" "address failed validation: $address"
[[ "$(echo "$va" | jq -r '.nettype')" == "${MONERO_NETWORK}" ]] || json_error "NETWORK_MISMATCH" "address nettype mismatch for $address"

[[ "$do_not_relay" == "true" || "$confirmed" == "true" ]] || json_error "CONFIRM_REQUIRED" "use --dry-run to preview or --confirm to broadcast"

rpc_refresh

if [[ -n "$subaddress" ]]; then
  params=$(jq -nc \
    --arg address "$address" \
    --argjson account_index "$account" \
    --argjson priority "$priority" \
    --argjson do_not_relay "$do_not_relay" \
    --argjson subaddr_indices "[$subaddress]" \
    '{address:$address, account_index:$account_index, priority:$priority, do_not_relay:$do_not_relay, subaddr_indices:$subaddr_indices}')
else
  params=$(jq -nc \
    --arg address "$address" \
    --argjson account_index "$account" \
    --argjson priority "$priority" \
    --argjson do_not_relay "$do_not_relay" \
    '{address:$address, account_index:$account_index, priority:$priority, do_not_relay:$do_not_relay}')
fi

res=$(rpc_call sweep_all "$params")

# Aggregate amount_list/fee_list with bash INTEGER math (not jq float `add`):
# IEEE-double `add` loses precision on large piconero sums and may emit
# sci-notation that piconero_to_xmr rejects AFTER the sweep already broadcast.
mapfile -t amt_list < <(echo "$res" | jq -r '.amount_list // [] | .[]')
mapfile -t fee_list < <(echo "$res" | jq -r '.fee_list // [] | .[]')
mapfile -t hash_list < <(echo "$res" | jq -r '.tx_hash_list // [] | .[]')
amount_pico=0; for a in "${amt_list[@]}"; do amount_pico=$(( amount_pico + a )); done
fee_pico=0;   for f in "${fee_list[@]}"; do fee_pico=$(( fee_pico + f )); done
if   (( ${#hash_list[@]} == 1 )); then tx_hash="${hash_list[0]}";
elif (( ${#hash_list[@]} > 1 ));  then tx_hash=$(IFS=,; echo "${hash_list[*]}");
else tx_hash=""; fi
fee_xmr=$(piconero_to_xmr "$fee_pico")
amt_xmr=$(piconero_to_xmr "$amount_pico")
echo "$res" | jq -c --arg tx_hash "$tx_hash" --arg fee "$fee_xmr" --arg amt "$amt_xmr" \
  '{tx_hash:$tx_hash, fee:$fee, amount:$amt}'
