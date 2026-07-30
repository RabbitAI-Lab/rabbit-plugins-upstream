load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "list_incoming returns array with confirmed flag" {
  mkdir -p "$FIXTURES/li"
  printf '{"jsonrpc":"2.0","id":"0","result":{"in":[{"txid":"c362","amount":1500000000000,"confirmations":15,"address":"A","address_index":3,"timestamp":1535918400,"unlock_time":0}],"pool":[],"pending":[]}}' > "$FIXTURES/li/get_transfers.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/li/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/li"
  run bash "$SCRIPTS/list_incoming.sh"
  stop_mock_rpc
  [ "$status" -eq 0 ]
  echo "$output" | jq -e 'length==1 and .[0].amount=="1.5" and .[0].confirmations==15 and .[0].confirmed==true' >/dev/null
}
@test "--confirmed-only filters below threshold" {
  mkdir -p "$FIXTURES/li2"
  printf '{"jsonrpc":"2.0","id":"0","result":{"in":[{"txid":"x","amount":1000000000000,"confirmations":3,"address":"A","address_index":0,"timestamp":1,"unlock_time":0}]}}' > "$FIXTURES/li2/get_transfers.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/li2/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/li2"
  run bash "$SCRIPTS/list_incoming.sh" --confirmed-only
  stop_mock_rpc
  [ "$status" -eq 0 ]
  echo "$output" | jq -e 'length==0' >/dev/null
}
