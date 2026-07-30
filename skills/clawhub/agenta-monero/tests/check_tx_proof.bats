load "test_helper"
bats_require_minimum_version 1.5.0

teardown() { stop_mock_rpc; }

@test "check_tx_proof valid proof -> exit 0, output {verified:true, confirmations, amount XMR string, tx_hash, address}; refresh + single /json_rpc" {
  mkdir -p "$FIXTURES/ctp_ok"
  printf '{"jsonrpc":"2.0","id":"0","result":{"good":true,"received_amount":1500000000000,"confirmations":15}}' > "$FIXTURES/ctp_ok/check_tx_proof.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/ctp_ok/refresh.json"
  local HASH="a1b2c3d4e5f60718293a4b5c6d7e8f901234567890abcdef1234567890abcdef"
  local ADDR="55ABCdef"
  local PROOF="ProofV1.abcdef.0123456789=="
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)"
  start_mock_rpc 18099 "$FIXTURES/ctp_ok"
  run bash "$SCRIPTS/check_tx_proof.sh" --tx-hash "$HASH" --address "$ADDR" --proof "$PROOF"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e --arg h "$HASH" --arg a "$ADDR" \
    '.verified==true and .confirmations==15 and .amount=="1.5" and .tx_hash==$h and .address==$a' >/dev/null
  [[ "$(mock_call_count check_tx_proof)" == "1" ]]
  [[ "$(mock_call_count refresh)" == "1" ]]
  # signature must be passed as a jq --arg (string), not interpolated
  mock_last_body check_tx_proof | jq -e --arg p "$PROOF" --arg t "$HASH" --arg a "$ADDR" \
    '.method=="check_tx_proof" and .params.txid==$t and .params.address==$a and .params.signature==$p' >/dev/null
}

@test "check_tx_proof invalid proof (good:false) -> PROOF_INVALID, exit non-zero" {
  mkdir -p "$FIXTURES/ctp_bad"
  printf '{"jsonrpc":"2.0","id":"0","result":{"good":false,"received_amount":0,"confirmations":0}}' > "$FIXTURES/ctp_bad/check_tx_proof.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/ctp_bad/refresh.json"
  local HASH="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ctp_bad"
  run bash "$SCRIPTS/check_tx_proof.sh" --tx-hash "$HASH" --address "55ABC" --proof "ProofV1.wrong=="
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="PROOF_INVALID"' >/dev/null
}

@test "check_tx_proof wallet RPC error -> PROOF_INVALID (wallet rejected proof)" {
  mkdir -p "$FIXTURES/ctp_err"
  printf '{"jsonrpc":"2.0","id":"0","error":{"code":-1,"message":"signature invalid"}}' > "$FIXTURES/ctp_err/check_tx_proof.ERR.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{}}' > "$FIXTURES/ctp_err/refresh.json"
  local HASH="cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  start_mock_rpc 18099 "$FIXTURES/ctp_err"
  run bash "$SCRIPTS/check_tx_proof.sh" --tx-hash "$HASH" --address "55ABC" --proof "ProofV1.bad=="
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="PROOF_INVALID"' >/dev/null
}

@test "check_tx_proof transport failure (daemon down) -> RPC_UNREACHABLE, NOT PROOF_INVALID" {
  # Double-send safety: a daemon-down MUST NOT be reported as PROOF_INVALID.
  local HASH="dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
  export MONERO_RPC_URL="http://127.0.0.1:18097" MONERO_LOCK_DIR="$(mktemp -d)" \
         MONERO_AUTO_REFRESH=false MONERO_RPC_TIMEOUT=3
  run bash "$SCRIPTS/check_tx_proof.sh" --tx-hash "$HASH" --address "55ABC" --proof "ProofV1.x=="
  [ "$status" -ne 0 ]
  [[ "$output" == *"RPC_UNREACHABLE"* ]]
  [[ "$output" != *"PROOF_INVALID"* ]]
}

@test "check_tx_proof invalid hash -> INVALID_INPUT" {
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/check_tx_proof.sh" --tx-hash deadbeef --address "55ABC" --proof "ProofV1.x=="
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="INVALID_INPUT"' >/dev/null
}

@test "check_tx_proof missing --proof -> CONFIG_MISSING" {
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/check_tx_proof.sh" --tx-hash a1b2c3d4e5f60718293a4b5c6d7e8f901234567890abcdef1234567890abcdef --address "55ABC"
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING"' >/dev/null
}

@test "check_tx_proof missing --address -> CONFIG_MISSING" {
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)" MONERO_AUTO_REFRESH=false
  run bash "$SCRIPTS/check_tx_proof.sh" --tx-hash a1b2c3d4e5f60718293a4b5c6d7e8f901234567890abcdef1234567890abcdef --proof "ProofV1.x=="
  [ "$status" -ne 0 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING"' >/dev/null
}

@test "check_tx_proof --no-refresh skips refresh even with auto-refresh default" {
  mkdir -p "$FIXTURES/ctp_nr"
  printf '{"jsonrpc":"2.0","id":"0","result":{"good":true,"received_amount":2500000000000,"confirmations":3}}' > "$FIXTURES/ctp_nr/check_tx_proof.json"
  local HASH="e1b2c3d4e5f60718293a4b5c6d7e8f901234567890abcdef1234567890abcdef"
  export MONERO_RPC_URL="http://127.0.0.1:18099" MONERO_LOCK_DIR="$(mktemp -d)"
  start_mock_rpc 18099 "$FIXTURES/ctp_nr"
  run bash "$SCRIPTS/check_tx_proof.sh" --no-refresh --tx-hash "$HASH" --address "55ABC" --proof "ProofV1.x=="
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.verified==true and .amount=="2.5" and .confirmations==3' >/dev/null
  [[ "$(mock_call_count check_tx_proof)" == "1" ]]
  [[ "$(mock_call_count refresh)" == "0" ]]
}
