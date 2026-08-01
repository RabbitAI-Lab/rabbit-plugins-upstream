load "test_helper"
source "$LIB/format.sh"
source "$LIB/rpc.sh"

teardown() { stop_mock_rpc; }

@test "rpc_call returns result object for get_height fixture" {
  mkdir -p "$FIXTURES/rpc"
  printf '{"jsonrpc":"2.0","id":"0","result":{"height":999}}' > "$FIXTURES/rpc/get_height.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099"
  start_mock_rpc 18099 "$FIXTURES/rpc"
  ensure_netrc
  run rpc_call get_height '{}'
  stop_mock_rpc
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.height==999' >/dev/null
}

@test "rpc_call surfaces RPC error as json_error" {
  mkdir -p "$FIXTURES/rpc"
  printf '{"jsonrpc":"2.0","id":"0","error":{"code":-1,"message":"nope"}}' > "$FIXTURES/rpc/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099"
  start_mock_rpc 18099 "$FIXTURES/rpc"
  ensure_netrc
  run rpc_call refresh '{}'
  stop_mock_rpc
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.code=="RPC_ERROR" and .message=="nope"' >/dev/null
}

@test "rpc_check_connection fails with RPC_UNREACHABLE when no server" {
  export MONERO_RPC_URL="http://127.0.0.1:18097"
  ensure_netrc
  run rpc_check_connection
  [ "$status" -ne 0 ]
  [[ "$output" == *"RPC_UNREACHABLE"* ]]
}

@test "rpc_refresh writes a locale-independent integer timestamp and calls refresh" {
  mkdir -p "$FIXTURES/rpcr"
  printf '{"jsonrpc":"2.0","id":"0","result":{"blocks_fetched":0}}' > "$FIXTURES/rpcr/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18097"
  export MONERO_AUTO_REFRESH=true MONERO_REFRESH_MIN_INTERVAL=30 MONERO_REFRESH_TIMEOUT=5
  start_mock_rpc 18097 "$FIXTURES/rpcr"
  ensure_netrc
  rpc_refresh
  count="$(mock_call_count refresh)"
  stop_mock_rpc
  [ "$count" = "1" ]
  [[ -f "$MONERO_LOCK_DIR/.last_refresh" ]]
  # must be a pure base-10 integer (regression guard for the comma-locale bug)
  [[ "$(cat "$MONERO_LOCK_DIR/.last_refresh")" =~ ^[0-9]+$ ]]
}
