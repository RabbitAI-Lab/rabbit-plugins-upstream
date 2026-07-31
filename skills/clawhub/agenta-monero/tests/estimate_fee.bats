load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

_setup_ok_fixtures() {
  local dir="$1"
  mkdir -p "$dir"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":true,"nettype":"mainnet","subaddress":false,"integrated":false}}' > "$dir/validate_address.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{"tx_hash":"abcd1234","tx_key":"","amount":1500000000000,"fee":12500000000}}' > "$dir/transfer.json"
}

@test "estimate_fee single dest: exit 0; output {fee,amount,priority:0,num_destinations:1} as XMR strings; body do_not_relay true, get_tx_key false, priority 0, integer piconeros; refresh NOT called" {
  _setup_ok_fixtures "$FIXTURES/ef"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ef"
  run bash "$SCRIPTS/estimate_fee.sh" --address "55Addr" --amount "1.5"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.fee=="0.0125" and .amount=="1.5" and .priority==0 and .num_destinations==1' >/dev/null
  body="$(mock_last_body transfer)"
  echo "$body" | jq -e '.method=="transfer"' >/dev/null
  echo "$body" | jq -e '.params.destinations[0].address=="55Addr"' >/dev/null
  echo "$body" | jq -e '.params.destinations[0].amount==1500000000000' >/dev/null
  echo "$body" | jq -e '.params.priority==0' >/dev/null
  echo "$body" | jq -e '.params.get_tx_key==false' >/dev/null
  echo "$body" | jq -e '.params.do_not_relay==true' >/dev/null
  [ "$(mock_call_count refresh)" -eq 0 ]
}

@test "estimate_fee multi-dest via --dest '[...]': num_destinations==2 and integer piconero amounts" {
  _setup_ok_fixtures "$FIXTURES/ef_multi"
  printf '{"jsonrpc":"2.0","id":"0","result":{"tx_hash":"multi1","tx_key":"","amount":3000000000000,"fee":15000000000}}' > "$FIXTURES/ef_multi/transfer.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ef_multi"
  run bash "$SCRIPTS/estimate_fee.sh" --dest '[{"address":"AAA","amount":"1.0"},{"address":"BBB","amount":"2.0"}]'
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.amount=="3" and .fee=="0.015" and .num_destinations==2' >/dev/null
  body="$(mock_last_body transfer)"
  echo "$body" | jq -e '.params.destinations|length==2' >/dev/null
  echo "$body" | jq -e '.params.destinations[0].address=="AAA" and .params.destinations[0].amount==1000000000000' >/dev/null
  echo "$body" | jq -e '.params.destinations[1].address=="BBB" and .params.destinations[1].amount==2000000000000' >/dev/null
  echo "$body" | jq -e '.params.do_not_relay==true' >/dev/null
  [ "$(mock_call_count refresh)" -eq 0 ]
}

@test "estimate_fee invalid address (valid:false) -> INVALID_ADDRESS" {
  _setup_ok_fixtures "$FIXTURES/ef_bad"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":false}}' > "$FIXTURES/ef_bad/validate_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ef_bad"
  run bash "$SCRIPTS/estimate_fee.sh" --address "55Addr" --amount "1.5"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="INVALID_ADDRESS"' >/dev/null
}

@test "estimate_fee empty --dest '[]' -> AMOUNT_INVALID" {
  export MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/estimate_fee.sh" --dest '[]'
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="AMOUNT_INVALID"' >/dev/null
}
