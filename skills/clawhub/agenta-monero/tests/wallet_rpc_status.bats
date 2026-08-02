load "test_helper"
chmod +x "$SCRIPTS/wallet_rpc_status.sh" 2>/dev/null || true

teardown() { stop_mock_rpc; }

@test "wallet_rpc_status reports running:false when no PID file exists" {
  export MONERO_LOCK_DIR="$(mktemp -d)"
  run bash "$SCRIPTS/wallet_rpc_status.sh"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.running==false and .pid==null and .port==null' >/dev/null
}

@test "wallet_rpc_status reports running:true with pid when process alive" {
  export MONERO_LOCK_DIR="$(mktemp -d)"
  bash -c 'exec -a monero-wallet-rpc sleep 300' &
  local pid=$!
  echo "$pid" > "$MONERO_LOCK_DIR/wallet-rpc.pid"
  echo "18088" > "$MONERO_LOCK_DIR/wallet-rpc.port"
  run bash "$SCRIPTS/wallet_rpc_status.sh"
  kill "$pid" 2>/dev/null || true
  [ "$status" -eq 0 ]
  echo "$output" | jq -e --argjson p "$pid" '.running==true and .pid==$p and .port==18088' >/dev/null
}

@test "wallet_rpc_status reports running:false when PID file exists but process dead" {
  export MONERO_LOCK_DIR="$(mktemp -d)"
  echo "999999" > "$MONERO_LOCK_DIR/wallet-rpc.pid"
  run bash "$SCRIPTS/wallet_rpc_status.sh"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e '.running==false and .pid==999999' >/dev/null
}
