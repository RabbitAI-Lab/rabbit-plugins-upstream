load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

# "ok" fixture set: valid mainnet address, successful sweep_all.
_setup_ok_fixtures() {
  local dir="$1"
  mkdir -p "$dir"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":true,"nettype":"mainnet","subaddress":false,"integrated":false}}' > "$dir/validate_address.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{"tx_hash_list":["abcd1234"],"amount_list":[1500000000000],"fee_list":[12500000000],"weight_list":[6414],"multisig_txset":"","unsigned_txset":""}}' > "$dir/sweep_all.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$dir/refresh.json"
}

@test "sweep_all happy path: output XMR strings + body has address (jq --arg), account_index 0, priority 0, do_not_relay false, NO subaddr_indices key" {
  _setup_ok_fixtures "$FIXTURES/sw"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sw"
  run bash "$SCRIPTS/sweep_all.sh" --address "55Addr" --confirm
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.tx_hash=="abcd1234" and .amount=="1.5" and .fee=="0.0125"' >/dev/null
  body="$(mock_last_body sweep_all)"
  echo "$body" | jq -e '.method=="sweep_all"' >/dev/null
  echo "$body" | jq -e '.params.address=="55Addr"' >/dev/null
  echo "$body" | jq -e '.params.account_index==0' >/dev/null
  echo "$body" | jq -e '.params.priority==0' >/dev/null
  echo "$body" | jq -e '.params.do_not_relay==false' >/dev/null
  echo "$body" | jq -e '(.params | has("subaddr_indices")) | not' >/dev/null
}

@test "sweep_all multi-tx: aggregates amount_list/fee_list (integer sum) and joins tx_hash_list with comma" {
  local dir="$FIXTURES/sw_multi"
  mkdir -p "$dir"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":true,"nettype":"mainnet","subaddress":false,"integrated":false}}' > "$dir/validate_address.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{"tx_hash_list":["h1","h2"],"amount_list":[1000000000000,2000000000000],"fee_list":[50000000000,60000000000],"weight_list":[6414,6414],"multisig_txset":"","unsigned_txset":""}}' > "$dir/sweep_all.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$dir/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$dir"
  run bash "$SCRIPTS/sweep_all.sh" --address "55Addr" --confirm
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.tx_hash=="h1,h2"' >/dev/null
  echo "$output" | jq -e '.amount=="3"' >/dev/null
  echo "$output" | jq -e '.fee=="0.11"' >/dev/null
}

@test "sweep_all aggregation is INTEGER math (no IEEE-double precision loss)" {
  # amount_list sums to 9007199254740993 pico = 2^53+1 (odd, > 2^53). jq float
  # `add` would round to 9007199254740992; bash integer arithmetic keeps it exact.
  local dir="$FIXTURES/sw_int"
  mkdir -p "$dir"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":true,"nettype":"mainnet","subaddress":false,"integrated":false}}' > "$dir/validate_address.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{"tx_hash_list":["h1","h2"],"amount_list":[4503599627370496,4503599627370497],"fee_list":[0,0],"weight_list":[0,0],"multisig_txset":"","unsigned_txset":""}}' > "$dir/sweep_all.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$dir/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$dir"
  run bash "$SCRIPTS/sweep_all.sh" --address "55Addr" --confirm
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.amount=="9007.199254740993"' >/dev/null
}

@test "sweep_all --dry-run: body do_not_relay true" {
  _setup_ok_fixtures "$FIXTURES/sw_dry"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sw_dry"
  run bash "$SCRIPTS/sweep_all.sh" --address "55Addr" --dry-run
  [ "$status" -eq 0 ]
  body="$(mock_last_body sweep_all)"
  echo "$body" | jq -e '.params.do_not_relay==true' >/dev/null
  echo "$body" | jq -e '(.params | has("subaddr_indices")) | not' >/dev/null
}

@test "sweep_all --subaddress 2: body subaddr_indices==[2]" {
  _setup_ok_fixtures "$FIXTURES/sw_sub"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sw_sub"
  run bash "$SCRIPTS/sweep_all.sh" --address "55Addr" --subaddress 2 --confirm
  [ "$status" -eq 0 ]
  body="$(mock_last_body sweep_all)"
  echo "$body" | jq -e '.params.subaddr_indices==[2]' >/dev/null
  echo "$body" | jq -e '.params.account_index==0' >/dev/null
}

@test "sweep_all --account 3: body account_index==3" {
  _setup_ok_fixtures "$FIXTURES/sw_acc"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sw_acc"
  run bash "$SCRIPTS/sweep_all.sh" --address "55Addr" --account 3 --confirm
  [ "$status" -eq 0 ]
  body="$(mock_last_body sweep_all)"
  echo "$body" | jq -e '.params.account_index==3' >/dev/null
}

@test "sweep_all missing --address -> CONFIG_MISSING" {
  export MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/sweep_all.sh"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING"' >/dev/null
}

@test "sweep_all invalid address (valid:false) -> INVALID_ADDRESS" {
  _setup_ok_fixtures "$FIXTURES/sw_bad"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":false}}' > "$FIXTURES/sw_bad/validate_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sw_bad"
  run bash "$SCRIPTS/sweep_all.sh" --address "BadAddr"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="INVALID_ADDRESS"' >/dev/null
}

@test "sweep_all network mismatch (valid but stagenet) -> NETWORK_MISMATCH" {
  _setup_ok_fixtures "$FIXTURES/sw_net"
  printf '{"jsonrpc":"2.0","id":"0","result":{"valid":true,"nettype":"stagenet","subaddress":false,"integrated":false}}' > "$FIXTURES/sw_net/validate_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_NETWORK=mainnet MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/sw_net"
  run bash "$SCRIPTS/sweep_all.sh" --address "55Addr"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="NETWORK_MISMATCH"' >/dev/null
}
