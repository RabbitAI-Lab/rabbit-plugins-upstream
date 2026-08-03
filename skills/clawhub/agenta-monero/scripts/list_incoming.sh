#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init
conf_only=0; since_block=0; since_ts=0; limit=100; account=0
while [[ $# -gt 0 ]]; do case "$1" in
  --all) shift;; --confirmed-only) conf_only=1; shift;;
  --since-block) since_block="$2"; shift 2;; --since-timestamp) since_ts="$2"; shift 2;;
  --limit) limit="$2"; shift 2;; --account) account="$2"; shift 2;; *) shift;; esac; done
rpc_refresh
threshold="${MONERO_CONFIRMATIONS:-10}"
params=$(jq -nc --argjson a "$account" --argjson min "$since_block" \
  '{in:true, out:false, pool:true, pending:true, account_index:$a, filter_by_height:($min>0), min_height:$min}')
res=$(rpc_call get_transfers "$params")
filtered=$(echo "$res" | jq -c \
  --argjson thr "$threshold" --argjson conf "$conf_only" --argjson sints "$since_ts" --argjson limit "$limit" '
  ([.in // [], .pool // [], .pending // []] | add) as $r
  | $r | map(. + {confirmed:(.confirmations >= $thr)})
  | map(if $conf==1 then select(.confirmed==true) else . end)
  | map(if $sints>0 then select(.timestamp >= $sints) else . end)
  | .[0:$limit] | to_entries')
ACC=""
while IFS= read -r row; do
  [[ -z "$row" ]] && continue
  amt=$(echo "$row" | jq -r '.value.amount'); xmr=$(piconero_to_xmr "$amt")
  obj=$(echo "$row" | jq -c --arg xmr "$xmr" '.value | {tx_hash:.txid, amount:$xmr, confirmations, address, address_index, timestamp, confirmed, unlock_time}')
  ACC+="${obj}"$'\n'
done < <(echo "$filtered" | jq -c '.[]')
printf '%s' "$ACC" | jq -cs '.'
