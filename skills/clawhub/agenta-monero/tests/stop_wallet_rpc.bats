load "test_helper"
chmod +x "$SCRIPTS/stop_wallet_rpc.sh" 2>/dev/null || true

teardown() { stop_mock_rpc; }

@test "stop_wallet_rpc stops a running process and cleans up PID file" {
  export MONERO_LOCK_DIR="$(mktemp -d)"
  bash -c 'exec -a monero-wallet-rpc sleep 300' &
  local pid=$!
  echo "$pid" > "$MONERO_LOCK_DIR/wallet-rpc.pid"
  echo "18088" > "$MONERO_LOCK_DIR/wallet-rpc.port"
  run bash "$SCRIPTS/stop_wallet_rpc.sh"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e --argjson p "$pid" '.stopped==true and .pid==$p' >/dev/null
  [[ ! -f "$MONERO_LOCK_DIR/wallet-rpc.pid" ]]
  [[ ! -f "$MONERO_LOCK_DIR/wallet-rpc.port" ]]
  ! kill -0 "$pid" 2>/dev/null
}

@test "stop_wallet_rpc reports stopped:false when no PID file exists" {
  export MONERO_LOCK_DIR="$(mktemp -d)"
  run bash "$SCRIPTS/stop_wallet_rpc.sh"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.stopped==false and .pid==null' >/dev/null
}

@test "stop_wallet_rpc reports stopped:false when process already dead" {
  export MONERO_LOCK_DIR="$(mktemp -d)"
  echo "999999" > "$MONERO_LOCK_DIR/wallet-rpc.pid"
  run bash "$SCRIPTS/stop_wallet_rpc.sh"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.stopped==false and .pid==999999' >/dev/null
  [[ ! -f "$MONERO_LOCK_DIR/wallet-rpc.pid" ]]
}
