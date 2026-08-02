#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init
since_block=0; since_ts=0; limit=100; account=0
while [[ $# -gt 0 ]]; do case "$1" in
  --since-block) since_block="$2"; shift 2;; --since-timestamp) since_ts="$2"; shift 2;;
  --limit) limit="$2"; shift 2;; --account) account="$2"; shift 2;; *) shift;; esac; done
rpc_refresh
params=$(jq -nc --argjson a "$account" --argjson min "$since_block" \
  '{out:true, in:false, account_index:$a, filter_by_height:($min>0), min_height:$min}')
res=$(rpc_call get_transfers "$params")
filtered=$(echo "$res" | jq -c \
  --argjson sints "$since_ts" --argjson limit "$limit" '
  (.out // []) as $r
  | $r | map(if $sints>0 then select(.timestamp >= $sints) else . end)
  | .[0:$limit] | to_entries')
ACC=""
while IFS= read -r row; do
  [[ -z "$row" ]] && continue
  amt=$(echo "$row" | jq -r '.value.amount'); xmr=$(piconero_to_xmr "$amt")
  fee=$(echo "$row" | jq -r '.value.fee // 0'); feexmr=$(piconero_to_xmr "$fee")
  obj=$(echo "$row" | jq -c --arg xmr "$xmr" --arg feexmr "$feexmr" \
    '.value | {tx_hash:.txid, amount:$xmr, fee:$feexmr, timestamp, address, address_index, unlock_time}')
  ACC+="${obj}"$'\n'
done < <(echo "$filtered" | jq -c '.[]')
printf '%s' "$ACC" | jq -cs '.'
