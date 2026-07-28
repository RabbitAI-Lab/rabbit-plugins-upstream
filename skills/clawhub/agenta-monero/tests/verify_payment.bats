load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "verify_payment --tx-hash found + confirmed -> verified:true, amount XMR string" {
  local txh="abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789"
  mkdir -p "$FIXTURES/vp_tx"
  printf '{"jsonrpc":"2.0","id":"0","result":{"transfer":{"txid":"%s","amount":1500000000000,"confirmations":15,"address":"55ABC","address_index":3,"type":"in","timestamp":1535918400,"unlock_time":0}}}' "$txh" > "$FIXTURES/vp_tx/get_transfer_by_txid.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/vp_tx/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/vp_tx"
  run bash "$SCRIPTS/verify_payment.sh" --tx-hash "$txh"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e --arg t "$txh" '.verified==true and .confirmed==true and .confirmations==15 and .amount=="1.5" and .tx_hash==$t and .address=="55ABC" and .address_index==3' >/dev/null
}

@test "verify_payment --tx-hash with type=out (non-incoming) -> verified:false, exit 0" {
  local txh="1122334455667788112233445566778811223344556677881122334455667788"
  mkdir -p "$FIXTURES/vp_out"
  printf '{"jsonrpc":"2.0","id":"0","result":{"transfer":{"txid":"%s","amount":5000000000000,"confirmations":50,"address":"X","address_index":0,"type":"out","timestamp":1535918400,"unlock_time":0}}}' "$txh" > "$FIXTURES/vp_out/get_transfer_by_txid.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/vp_out/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/vp_out"
  run bash "$SCRIPTS/verify_payment.sh" --tx-hash "$txh"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.verified==false and .confirmations==50 and .amount=="5"' >/dev/null
}

@test "verify_payment --address + --expected-amount found + confirmed -> verified:true" {
  mkdir -p "$FIXTURES/vp_addr"
  printf '{"jsonrpc":"2.0","id":"0","result":{"in":[{"txid":"txA","amount":1500000000000,"confirmations":20,"address":"55ABC","address_index":3,"type":"in","timestamp":1535918400,"unlock_time":0}],"pool":[],"pending":[]}}' > "$FIXTURES/vp_addr/get_transfers.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/vp_addr/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/vp_addr"
  run bash "$SCRIPTS/verify_payment.sh" --address 55ABC --expected-amount 1.5
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.verified==true and .confirmed==true and .amount=="1.5" and .tx_hash=="txA" and .address=="55ABC" and .address_index==3' >/dev/null
}

@test "verify_payment insufficient confirmations -> verified:false, exit 0" {
  local txh="9988776655443322998877665544332299887766554433229988776655443322"
  mkdir -p "$FIXTURES/vp_low"
  printf '{"jsonrpc":"2.0","id":"0","result":{"transfer":{"txid":"%s","amount":2000000000000,"confirmations":2,"address":"X","address_index":0,"type":"in","timestamp":1535918400,"unlock_time":0}}}' "$txh" > "$FIXTURES/vp_low/get_transfer_by_txid.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/vp_low/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/vp_low"
  run bash "$SCRIPTS/verify_payment.sh" --tx-hash "$txh"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.verified==false and .confirmed==false and .confirmations==2 and .amount=="2"' >/dev/null
}

@test "verify_payment address mode no match -> verified:false, exit 0" {
  mkdir -p "$FIXTURES/vp_nomatch"
  printf '{"jsonrpc":"2.0","id":"0","result":{"in":[{"txid":"z","amount":1000000000000,"confirmations":15,"address":"OTHER","address_index":0,"type":"in","timestamp":1535918400,"unlock_time":0}],"pool":[],"pending":[]}}' > "$FIXTURES/vp_nomatch/get_transfers.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/vp_nomatch/refresh.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/vp_nomatch"
  run bash "$SCRIPTS/verify_payment.sh" --address NOPE --expected-amount 1.0
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.verified==false and .address=="NOPE" and .amount==null and .tx_hash==null' >/dev/null
}

@test "verify_payment missing args -> CONFIG_MISSING" {
  export MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/verify_payment.sh"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING"' >/dev/null
}

@test "verify_payment address mode missing --expected-amount -> CONFIG_MISSING" {
  export MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/verify_payment.sh" --address FOO
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING"' >/dev/null
}

@test "verify_payment malformed --tx-hash -> INVALID_INPUT (validated before RPC)" {
  export MONERO_LOCK_DIR="$(mktemp -d)" MONERO_CONFIRMATIONS=10 MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/verify_payment.sh" --tx-hash "not-a-real-hash"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="INVALID_INPUT"' >/dev/null
}
