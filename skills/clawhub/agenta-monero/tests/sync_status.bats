load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "sync_status emits honest {height, daemon_connected, wallet_version} shape" {
  mkdir -p "$FIXTURES/sync_status"
  printf '{"jsonrpc":"2.0","id":"0","result":{"height":123}}' > "$FIXTURES/sync_status/get_height.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{"version":196613}}' > "$FIXTURES/sync_status/get_version.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sync_status"
  run --separate-stderr bash "$SCRIPTS/sync_status.sh"
  stop_mock_rpc
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.height==123 and .daemon_connected==true and .wallet_version==196613' >/dev/null
  # honest shape: synced/target_height dropped (not computable from wallet RPC)
  echo "$output" | jq -e '(has("synced")|not) and (has("target_height")|not)' >/dev/null
}
