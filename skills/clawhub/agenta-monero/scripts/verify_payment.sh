#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init

tx_hash=""
address=""
expected_amount=""
while [[ $# -gt 0 ]]; do case "$1" in
  --tx-hash) tx_hash="$2"; shift 2;;
  --address) address="$2"; shift 2;;
  --expected-amount) expected_amount="$2"; shift 2;;
  *) shift;; esac; done

if [[ -n "$tx_hash" && ( -n "$address" || -n "$expected_amount" ) ]]; then
  json_error "CONFIG_MISSING" "Provide --tx-hash OR (--address + --expected-amount), not both"
fi
if [[ -z "$tx_hash" && -z "$address" && -z "$expected_amount" ]]; then
  json_error "CONFIG_MISSING" "Either --tx-hash OR --address + --expected-amount is required"
fi
if [[ -z "$tx_hash" && ( -z "$address" || -z "$expected_amount" ) ]]; then
  json_error "CONFIG_MISSING" "--address and --expected-amount are both required for address mode"
fi

if [[ -n "$tx_hash" ]]; then
  validate_tx_hash "$tx_hash" 2>/dev/null || json_error "INVALID_INPUT" "tx-hash must be 64 lowercase hex chars"
fi

rpc_refresh

threshold="${MONERO_CONFIRMATIONS:-10}"

if [[ -n "$tx_hash" ]]; then
  params=$(jq -nc --arg t "$tx_hash" '{txid:$t}')
  res=$(rpc_call get_transfer_by_txid "$params")
  out=$(echo "$res" | jq -c --argjson thr "$threshold" --arg txh "$tx_hash" '
    .transfer as $t
    | if ($t | type) != "object" then
        {verified:false, confirmations:0, amount_pico:null, tx_hash:$txh, address:null, address_index:null, confirmed:false}
      else
        ($t.confirmations // 0) as $c
        | ($t.type // "") as $ty
        | ({in:1, pool:1, pending:1} | has($ty)) as $incoming
        | { verified:($incoming and ($c >= $thr)),
            confirmations:$c,
            amount_pico:($t.amount // null),
            tx_hash:($t.txid // $txh),
            address:($t.address // null),
            address_index:($t.address_index // null),
            confirmed:($c >= $thr) }
      end')
else
  expected_pico=$(xmr_to_piconero "$expected_amount")
  params=$(jq -nc '{in:true, out:false, pool:true, pending:true}')
  res=$(rpc_call get_transfers "$params")
  out=$(echo "$res" | jq -c --argjson thr "$threshold" --arg addr "$address" --argjson pico "$expected_pico" '
    ([.in // [], .pool // [], .pending // []] | add) as $all
    | ($all | map(select((.address // "") == $addr and (.amount // -1) == $pico)) | .[0] // null) as $t
    | if $t == null then
        {verified:false, confirmations:0, amount_pico:null, tx_hash:null, address:$addr, address_index:null, confirmed:false}
      else
        ($t.confirmations // 0) as $c
        | { verified:($c >= $thr),
            confirmations:$c,
            amount_pico:$t.amount,
            tx_hash:$t.txid,
            address:$t.address,
            address_index:($t.address_index // null),
            confirmed:($c >= $thr) }
      end')
fi

amt=$(echo "$out" | jq -r '.amount_pico // empty')
if [[ -n "$amt" ]]; then
  xmr=$(piconero_to_xmr "$amt")
  out=$(echo "$out" | jq -c --arg x "$xmr" '.amount=$x')
else
  out=$(echo "$out" | jq -c '.amount=null')
fi
out=$(echo "$out" | jq -c 'del(.amount_pico)')
printf '%s\n' "$out"
