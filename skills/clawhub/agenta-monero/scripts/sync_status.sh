#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init

# daemon_connected is a real reachability proxy: true iff BOTH wallet-RPC probes
# succeed. The wallet RPC (get_height/get_version) cannot honestly report the
# daemon's sync target_height, so synced/target_height are intentionally NOT
# emitted (the prior always-true `synced` and tautological daemon check gave
# false confidence).
height_rc=0; version_rc=0
h=$(rpc_call get_height '{}') || height_rc=$?
v=$(rpc_call get_version '{}') || version_rc=$?

if [[ $height_rc -ne 0 || $version_rc -ne 0 ]]; then
  json_error "RPC_UNREACHABLE" "could not reach monero-wallet-rpc for get_height/get_version"
fi

height=$(echo "$h" | jq -r '.height')
wallet_version=$(echo "$v" | jq -r '.version // 0')
jq -nc --argjson height "$height" --argjson daemon_connected true --argjson wallet_version "$wallet_version" \
  '{height:$height, daemon_connected:$daemon_connected, wallet_version:$wallet_version}'
