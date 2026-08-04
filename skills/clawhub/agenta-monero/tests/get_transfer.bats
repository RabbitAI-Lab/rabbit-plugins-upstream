load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "get_transfer found incoming tx -> direction in, amount XMR string, confirmed flag" {
  local hash=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
  mkdir -p "$FIXTURES/gt"
  printf '{"jsonrpc":"2.0","id":"0","result":{"transfer":{"txid":"%s","amount":1500000000000,"fee":80000000000,"confirmations":15,"address":"55ABC","address_index":3,"type":"in","timestamp":1535918400,"unlock_time":0}}}' "$hash" > "$FIXTURES/gt/get_transfer_by_txid.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/gt/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/gt"
  run bash "$SCRIPTS/get_transfer.sh" --tx-hash "$hash"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e --arg h "$hash" \
    '.direction=="in" and .amount=="1.5" and .fee=="0.08" and .confirmations==15 and .confirmed==true and .tx_hash==$h and .address=="55ABC" and .address_index==3 and .unlock_time==0' >/dev/null
}

@test "get_transfer wallet-side not found (RPC error -38) -> TX_NOT_FOUND, exit non-zero" {
  local hash=ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
  mkdir -p "$FIXTURES/gt_nf"
  printf '{"jsonrpc":"2.0","id":"0","error":{"code":-38,"message":"no transfer found"}}' > "$FIXTURES/gt_nf/get_transfer_by_txid.ERR.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/gt_nf/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/gt_nf"
  run bash "$SCRIPTS/get_transfer.sh" --tx-hash "$hash"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="TX_NOT_FOUND"' >/dev/null
}

@test "get_transfer success but empty result -> TX_NOT_FOUND, exit non-zero" {
  local hash=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  mkdir -p "$FIXTURES/gt_empty"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/gt_empty/get_transfer_by_txid.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/gt_empty/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/gt_empty"
  run bash "$SCRIPTS/get_transfer.sh" --tx-hash "$hash"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="TX_NOT_FOUND"' >/dev/null
}

@test "get_transfer transport failure (daemon down) -> RPC_UNREACHABLE, NOT TX_NOT_FOUND" {
  # Double-send safety: if the daemon is unreachable we must NOT claim the tx is
  # absent. Point at a port with no server so curl fails (RPC_UNREACHABLE) and
  # assert the script propagates that code instead of relabelling it TX_NOT_FOUND.
  local hash=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
  export MONERO_RPC_URL="http://127.0.0.1:18097" MONERO_LOCK_DIR="$(mktemp -d)" \
         MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false MONERO_RPC_TIMEOUT=3
  run bash "$SCRIPTS/get_transfer.sh" --tx-hash "$hash"
  [ "$status" -ne 0 ]
  [[ "$output" == *"RPC_UNREACHABLE"* ]]
  [[ "$output" != *"TX_NOT_FOUND"* ]]
}

@test "get_transfer invalid hash -> INVALID_INPUT, exit non-zero" {
  export MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/get_transfer.sh" --tx-hash deadbeef
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="INVALID_INPUT"' >/dev/null
}
