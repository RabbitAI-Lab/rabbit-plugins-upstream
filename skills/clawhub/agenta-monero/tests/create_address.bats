load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "create_address --label happy path -> {address, address_index, account} and label reaches RPC" {
  mkdir -p "$FIXTURES/ca"
  printf '{"jsonrpc":"2.0","id":"0","result":{"address":"SubAddr1","address_index":3}}' > "$FIXTURES/ca/create_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ca"
  run bash "$SCRIPTS/create_address.sh" --label "Payment from Alice"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.address=="SubAddr1" and .address_index==3 and .account==0' >/dev/null
  [ "$(mock_call_count create_address)" = "1" ]
  mock_last_body create_address | jq -e '.method=="create_address" and .params.label=="Payment from Alice" and .params.account_index==0' >/dev/null
}

@test "create_address label with double-quote round-trips intact to RPC" {
  mkdir -p "$FIXTURES/ca_q"
  printf '{"jsonrpc":"2.0","id":"0","result":{"address":"Q","address_index":2}}' > "$FIXTURES/ca_q/create_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ca_q"
  run bash "$SCRIPTS/create_address.sh" --label 'Alice "bob"'
  [ "$status" -eq 0 ]
  mock_last_body create_address | jq -e '.params.label=="Alice \"bob\""' >/dev/null
}

@test "create_address --account N propagates to RPC params.account_index and output account" {
  mkdir -p "$FIXTURES/ca_acc"
  printf '{"jsonrpc":"2.0","id":"0","result":{"address":"SubAddr5","address_index":7}}' > "$FIXTURES/ca_acc/create_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ca_acc"
  run bash "$SCRIPTS/create_address.sh" --account 5 --label "lbl"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.account==5 and .address=="SubAddr5" and .address_index==7' >/dev/null
  mock_last_body create_address | jq -e '.params.account_index==5 and .params.label=="lbl"' >/dev/null
}

@test "create_address no --label -> default empty label, exit 0" {
  mkdir -p "$FIXTURES/ca_nolabel"
  printf '{"jsonrpc":"2.0","id":"0","result":{"address":"Sub9","address_index":9}}' > "$FIXTURES/ca_nolabel/create_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ca_nolabel"
  run bash "$SCRIPTS/create_address.sh"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.address=="Sub9" and .address_index==9 and .account==0' >/dev/null
  mock_last_body create_address | jq -e '.params.account_index==0 and .params.label==""' >/dev/null
}

@test "create_address label >255 chars -> INVALID_INPUT, no RPC call" {
  mkdir -p "$FIXTURES/ca_long"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ca_long"
  local long; long="$(printf 'a%.0s' $(seq 1 256))"
  run bash "$SCRIPTS/create_address.sh" --label "$long"
  [ "$status" -ne 0 ]
  [[ "$output" == *"INVALID_INPUT"* ]]
  [ "$(mock_call_count create_address)" = "0" ]
}

@test "create_address label with control char -> INVALID_INPUT, no RPC call" {
  mkdir -p "$FIXTURES/ca_ctrl"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ca_ctrl"
  run bash "$SCRIPTS/create_address.sh" --label $'bad\tlabel'
  [ "$status" -ne 0 ]
  [[ "$output" == *"INVALID_INPUT"* ]]
  [ "$(mock_call_count create_address)" = "0" ]
}
