load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

# Write the "ok" fixture set: valid mainnet address, ample balance, successful transfer.
_setup_ok_fixtures() {
  local dir="$1"
  mkdir -p "$dir"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":true,"nettype":"mainnet","subaddress":false,"integrated":false}}' > "$dir/validate_address.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{"balance":100000000000000,"unlocked_balance":100000000000000}}' > "$dir/get_balance.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{"tx_hash":"abcd1234","tx_key":"secretkey","amount":1500000000000,"fee":12500000000}}' > "$dir/transfer.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$dir/refresh.json"
}

@test "send_xmr single dest happy path: output XMR strings + body has integer piconeros, priority 0, get_tx_key false, do_not_relay false" {
  _setup_ok_fixtures "$FIXTURES/sx"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sx"
  run bash "$SCRIPTS/send_xmr.sh" --address "55Addr" --amount "1.5" --confirm
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.tx_hash=="abcd1234" and .amount=="1.5" and .fee=="0.0125" and (.tx_key|not)' >/dev/null
  body="$(mock_last_body transfer)"
  echo "$body" | jq -e '.method=="transfer"' >/dev/null
  echo "$body" | jq -e '.params.destinations[0].address=="55Addr"' >/dev/null
  echo "$body" | jq -e '.params.destinations[0].amount==1500000000000' >/dev/null
  echo "$body" | jq -e '.params.priority==0' >/dev/null
  echo "$body" | jq -e '.params.get_tx_key==false' >/dev/null
  echo "$body" | jq -e '.params.do_not_relay==false' >/dev/null
}

@test "send_xmr --get-tx-key: body get_tx_key true AND output includes tx_key" {
  _setup_ok_fixtures "$FIXTURES/sx"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sx"
  run bash "$SCRIPTS/send_xmr.sh" --address "55Addr" --amount "1.5" --get-tx-key --confirm
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.tx_key=="secretkey"' >/dev/null
  body="$(mock_last_body transfer)"
  echo "$body" | jq -e '.params.get_tx_key==true' >/dev/null
  echo "$body" | jq -e '.params.do_not_relay==false' >/dev/null
}

@test "send_xmr --dry-run: body do_not_relay true" {
  _setup_ok_fixtures "$FIXTURES/sx"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sx"
  run bash "$SCRIPTS/send_xmr.sh" --address "55Addr" --amount "1.5" --dry-run
  [ "$status" -eq 0 ]
  body="$(mock_last_body transfer)"
  echo "$body" | jq -e '.params.do_not_relay==true' >/dev/null
  echo "$body" | jq -e '.params.get_tx_key==false' >/dev/null
}

@test "send_xmr multi-dest via --dest '[...]': body destinations length 2 with integer piconero amounts" {
  _setup_ok_fixtures "$FIXTURES/sx_multi"
  printf '{"jsonrpc":"2.0","id":"0","result":{"tx_hash":"multi1","tx_key":"","amount":3000000000000,"fee":15000000000}}' > "$FIXTURES/sx_multi/transfer.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sx_multi"
  run bash "$SCRIPTS/send_xmr.sh" --dest '[{"address":"AAA","amount":"1.0"},{"address":"BBB","amount":"2.0"}]' --confirm
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.amount=="3" and .fee=="0.015"' >/dev/null
  body="$(mock_last_body transfer)"
  echo "$body" | jq -e '.params.destinations|length==2' >/dev/null
  echo "$body" | jq -e '.params.destinations[0].address=="AAA" and .params.destinations[0].amount==1000000000000' >/dev/null
  echo "$body" | jq -e '.params.destinations[1].address=="BBB" and .params.destinations[1].amount==2000000000000' >/dev/null
}

@test "send_xmr insufficient unlocked balance -> INSUFFICIENT_BALANCE" {
  _setup_ok_fixtures "$FIXTURES/sx_low"
  printf '{"jsonrpc":"2.0","id":"0","result":{"balance":200000000000,"unlocked_balance":100000000000}}' > "$FIXTURES/sx_low/get_balance.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sx_low"
  run bash "$SCRIPTS/send_xmr.sh" --address "55Addr" --amount "1.5"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="INSUFFICIENT_BALANCE"' >/dev/null
}

@test "send_xmr invalid address (valid:false) -> INVALID_ADDRESS" {
  _setup_ok_fixtures "$FIXTURES/sx_bad"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":false}}' > "$FIXTURES/sx_bad/validate_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sx_bad"
  run bash "$SCRIPTS/send_xmr.sh" --address "55Addr" --amount "1.5"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="INVALID_ADDRESS"' >/dev/null
}

@test "send_xmr network mismatch (valid but stagenet) -> NETWORK_MISMATCH" {
  _setup_ok_fixtures "$FIXTURES/sx_net"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":true,"nettype":"stagenet","subaddress":false,"integrated":false}}' > "$FIXTURES/sx_net/validate_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sx_net"
  run bash "$SCRIPTS/send_xmr.sh" --address "55Addr" --amount "1.5"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="NETWORK_MISMATCH"' >/dev/null
}

@test "send_xmr empty --dest '[]' -> AMOUNT_INVALID" {
  export MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/send_xmr.sh" --dest '[]'
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="AMOUNT_INVALID"' >/dev/null
}

@test "send_xmr non-array --dest '{...}' -> DEST_JSON_INVALID" {
  export MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/send_xmr.sh" --dest '{"address":"X","amount":"1.0"}'
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="DEST_JSON_INVALID"' >/dev/null
}

@test "send_xmr missing args -> CONFIG_MISSING" {
  export MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/send_xmr.sh"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING"' >/dev/null
}

@test "send_xmr --address without --amount -> CONFIG_MISSING" {
  export MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/send_xmr.sh" --address "55Addr"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING"' >/dev/null
}
