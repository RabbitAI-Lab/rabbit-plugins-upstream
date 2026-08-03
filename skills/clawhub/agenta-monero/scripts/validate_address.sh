#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init
addr=""
while [[ $# -gt 0 ]]; do case "$1" in --address) addr="$2"; shift 2;; *) shift;; esac; done
[[ -z "$addr" ]] && json_error "CONFIG_MISSING" "--address required"
res=$(rpc_call validate_address "$(jq -nc --arg a "$addr" '{address:$a, any_net_type:true, allow_openalias:false}')")
valid=$(echo "$res" | jq -r '.valid')
net=$(echo "$res" | jq -r '.nettype')
match=$([[ "$net" == "${MONERO_NETWORK}" ]] && echo true || echo false)
[[ "$valid" == "true" ]] || json_error "INVALID_ADDRESS" "address failed validation (format/checksum)"
[[ "$match" == "true" ]] || json_error "NETWORK_MISMATCH" "address nettype '$net' != configured '${MONERO_NETWORK}'"
echo "$res" | jq -c --arg net "$net" --argjson match "$match" \
  '{valid, network:$net, network_match:$match, subaddress, integrated}'
