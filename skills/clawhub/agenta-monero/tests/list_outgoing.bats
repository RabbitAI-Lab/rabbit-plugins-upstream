load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "list_outgoing returns array with amount and fee as XMR strings" {
  mkdir -p "$FIXTURES/lo"
  printf '{"jsonrpc":"2.0","id":"0","result":{"out":[{"txid":"a1b2c3","amount":500000000000,"fee":43500000000,"address":"77Vx","address_index":3,"timestamp":1535918500,"unlock_time":0}]}}' > "$FIXTURES/lo/get_transfers.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/lo/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/lo"
  run bash "$SCRIPTS/list_outgoing.sh"
  stop_mock_rpc
  [ "$status" -eq 0 ]
  echo "$output" | jq -e 'length==1 and .[0].tx_hash=="a1b2c3" and .[0].amount=="0.5" and (.[0].fee|type)=="string"' >/dev/null
}

@test "list_outgoing returns empty array when no outgoing transfers" {
  mkdir -p "$FIXTURES/lo2"
  printf '{"jsonrpc":"2.0","id":"0","result":{"out":[]}}' > "$FIXTURES/lo2/get_transfers.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/lo2/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/lo2"
  run bash "$SCRIPTS/list_outgoing.sh"
  stop_mock_rpc
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '. == []' >/dev/null
}
