load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "get_tx_proof happy path -> exit 0, output {tx_hash, address, proof} verbatim" {
  mkdir -p "$FIXTURES/gtp_ok"
  printf '{"jsonrpc":"2.0","id":"0","result":{"signature":"ProofV1.abcdef.0123456789=="}}' > "$FIXTURES/gtp_ok/get_tx_proof.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/gtp_ok"
  local HASH="a1b2c3d4e5f60718293a4b5c6d7e8f901234567890abcdef1234567890abcdef"
  run bash "$SCRIPTS/get_tx_proof.sh" --tx-hash "$HASH" --address 55ABC
  [ "$status" -eq 0 ]
  echo "$output" | jq -e --arg h "$HASH" '.tx_hash==$h and .address=="55ABC" and .proof=="ProofV1.abcdef.0123456789=="' >/dev/null
  [[ "$(mock_call_count get_tx_proof)" == "1" ]]
  [[ "$(mock_call_count refresh)" == "0" ]]
}

@test "get_tx_proof invalid hash -> INVALID_INPUT" {
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/get_tx_proof.sh" --tx-hash not-a-hash --address 55ABC
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="INVALID_INPUT"' >/dev/null
}

@test "get_tx_proof missing --address -> CONFIG_MISSING" {
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/get_tx_proof.sh" --tx-hash a1b2c3d4e5f60718293a4b5c6d7e8f901234567890abcdef1234567890abcdef
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING"' >/dev/null
}

@test "get_tx_proof missing --tx-hash -> CONFIG_MISSING" {
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/get_tx_proof.sh" --address 55ABC
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING"' >/dev/null
}
