#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init
account=0
while [[ $# -gt 0 ]]; do case "$1" in --account) account="$2"; shift 2;; *) shift;; esac; done
rpc_refresh
res=$(rpc_call get_balance "$(jq -nc --argjson a "$account" '{account_index:$a}')")
bal=$(piconero_to_xmr "$(echo "$res" | jq -r '.balance')")
unl=$(piconero_to_xmr "$(echo "$res" | jq -r '.unlocked_balance')")
echo "$res" | jq -c --arg bal "$bal" --arg unl "$unl" --argjson a "$account" \
  '{balance:$bal, unlocked_balance:$unl, blocks_to_unlock, time_to_unlock, account:$a}'
