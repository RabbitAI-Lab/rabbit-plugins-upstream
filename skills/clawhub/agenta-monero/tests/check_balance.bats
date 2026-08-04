load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "check_balance reads native blocks_to_unlock + time_to_unlock" {
  mkdir -p "$FIXTURES/check_balance"
  printf '{"jsonrpc":"2.0","id":"0","result":{"balance":10500000000000,"unlocked_balance":8200000000000,"blocks_to_unlock":42,"time_to_unlock":30240}}' > "$FIXTURES/check_balance/get_balance.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/check_balance/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/check_balance"
  run bash "$SCRIPTS/check_balance.sh"
  stop_mock_rpc
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.balance=="10.5" and .unlocked_balance=="8.2" and .blocks_to_unlock==42 and .time_to_unlock==30240' >/dev/null
}
