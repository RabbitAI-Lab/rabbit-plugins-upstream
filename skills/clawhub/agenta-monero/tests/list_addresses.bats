load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "list_addresses maps subaddresses to JSON array" {
  mkdir -p "$FIXTURES/list_addresses"
  printf '{"jsonrpc":"2.0","id":"0","result":{"address":"A0","addresses":["A0","A1"],"labels":["Primary","x"]}}' > "$FIXTURES/list_addresses/get_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/list_addresses"
  run bash "$SCRIPTS/list_addresses.sh"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e 'length==2 and .[0].address=="A0" and .[1].label=="x"' >/dev/null
}
