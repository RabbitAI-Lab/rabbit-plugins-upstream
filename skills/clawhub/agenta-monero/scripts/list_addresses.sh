#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init
account=0
while [[ $# -gt 0 ]]; do case "$1" in --account) account="$2"; shift 2;; *) shift;; esac; done
res=$(rpc_call get_address "$(jq -nc --argjson a "$account" '{account_index:$a}')")
echo "$res" | jq -c '
  ([.addresses // [.address]] | add) as $a
  | ([.labels // []] | add) as $l
  | [range(0; ($a|length)) as $i | {index:$i, address:$a[$i], label:($l[$i] // "")}]'
