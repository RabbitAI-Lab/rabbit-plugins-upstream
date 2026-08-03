load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "validate_address: valid + network match" {
  mkdir -p "$FIXTURES/va"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":true,"nettype":"mainnet","subaddress":false,"integrated":false}}' > "$FIXTURES/va/validate_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/va"
  run bash "$SCRIPTS/validate_address.sh" --address "ADDR"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.valid==true and .network=="mainnet" and .network_match==true and .subaddress==false' >/dev/null
}
@test "validate_address: network mismatch -> NETWORK_MISMATCH" {
  mkdir -p "$FIXTURES/va2"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":true,"nettype":"stagenet","subaddress":false,"integrated":false}}' > "$FIXTURES/va2/validate_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/va2"
  run bash "$SCRIPTS/validate_address.sh" --address "ADDR"
  [ "$status" -ne 0 ]
  [[ "$output" == *"NETWORK_MISMATCH"* ]]
}
@test "validate_address: invalid (valid=false) -> INVALID_ADDRESS (checked before network)" {
  mkdir -p "$FIXTURES/va3"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":false}}' > "$FIXTURES/va3/validate_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/va3"
  run bash "$SCRIPTS/validate_address.sh" --address "ADDR"
  [ "$status" -ne 0 ]
  [[ "$output" == *"INVALID_ADDRESS"* ]]
}
