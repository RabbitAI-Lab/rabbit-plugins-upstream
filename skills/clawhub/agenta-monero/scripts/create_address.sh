#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init

label=""
account=0
while [[ $# -gt 0 ]]; do case "$1" in
  --label)  label="$2";  shift 2;;
  --account) account="$2"; shift 2;;
  *) shift;; esac; done

validate_label "$label" 2>/dev/null || json_error "INVALID_INPUT" "label invalid: $label"

params=$(jq -nc --argjson account_index "$account" --arg label "$label" '{account_index:$account_index, label:$label}')
res=$(rpc_call create_address "$params")
echo "$res" | jq -c --argjson account "$account" '{address, address_index, account:$account}'
