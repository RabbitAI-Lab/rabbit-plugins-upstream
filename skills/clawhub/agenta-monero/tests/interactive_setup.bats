load "test_helper"
chmod +x "$SCRIPTS/interactive_setup.sh" 2>/dev/null || true

teardown() { stop_mock_rpc; }

@test "interactive_setup --help prints usage and exits 0" {
  run bash "$SCRIPTS/interactive_setup.sh" --help
  [ "$status" -eq 0 ]
  [[ "$output" == *"USAGE"* ]]
  [[ "$output" == *"--wallet-path"* ]]
  [[ "$output" == *"--network"* ]]
  [[ "$output" == *"--daemon-type"* ]]
}

@test "interactive_setup errors when monero-wallet-rpc not found" {
  local fake_bin
  fake_bin="$(mktemp -d)"
  ln -s "$(command -v bash)" "$fake_bin/bash"
  ln -s "$(command -v dirname)" "$fake_bin/dirname"
  ln -s "$(command -v curl)" "$fake_bin/curl"
  ln -s "$(command -v jq)" "$fake_bin/jq"
  ln -s "$(command -v flock)" "$fake_bin/flock"
  run env PATH="$fake_bin" bash "$SCRIPTS/interactive_setup.sh" \
    --wallet-path /tmp/nonexistent --wallet-password "pass" --network mainnet --daemon-type local
  [ "$status" -eq 1 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING" and (.message|test("monero-wallet-rpc"))' >/dev/null
}

@test "interactive_setup errors when wallet file not found" {
  local fake_bin stub
  fake_bin="$(mktemp -d)"
  stub="$fake_bin/monero-wallet-rpc"
  printf '#!/usr/bin/env bash\nexit 0\n' > "$stub"
  chmod +x "$stub"
  run env PATH="$fake_bin:/usr/bin:/bin" bash "$SCRIPTS/interactive_setup.sh" \
    --wallet-path /tmp/nope_wallet --wallet-password "pass" --network mainnet --daemon-type local
  [ "$status" -eq 1 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_MISSING" and (.message|test("wallet"))' >/dev/null
}

@test "interactive_setup errors on invalid network" {
  run bash "$SCRIPTS/interactive_setup.sh" \
    --wallet-path /tmp/nope --wallet-password "pass" --network testnet --daemon-type local
  [ "$status" -eq 1 ]
  echo "$output" | jq -e '.error==true and .code=="CONFIG_INVALID"' >/dev/null
}

@test "interactive_setup writes .env with correct values (with stub monero-wallet-rpc)" {
  local fake_bin stub wallet_dir env_file
  fake_bin="$(mktemp -d)"
  stub="$fake_bin/monero-wallet-rpc"
  # Stub that just sleeps (simulates running wallet-rpc)
  printf '#!/usr/bin/env bash\nexec -a monero-wallet-rpc sleep 300\n' > "$stub"
  chmod +x "$stub"

  wallet_dir="$(mktemp -d)"
  # Create a fake wallet file
  touch "$wallet_dir/test_wallet.keys"

  # Stub for setup.sh — we test .env writing via --dry-run-style approach:
  # We point the script at a skill dir copy so it writes .env there
  local skill_copy
  skill_copy="$(mktemp -d)"
  cp "$ROOT"/.env.example "$skill_copy/.env.example"
  cp -r "$SCRIPTS" "$skill_copy/scripts"
  cp -r "$LIB" "$skill_copy/lib"
  cp "$ROOT/setup.sh" "$skill_copy/setup.sh"
  chmod +x "$skill_copy/scripts/interactive_setup.sh" 2>/dev/null || true

  # Replace the script's SCRIPT_DIR by running from skill_copy
  local lock_dir
  lock_dir="$(mktemp -d)"
  run env PATH="$fake_bin:/usr/bin:/bin" \
    MONERO_LOCK_DIR="$lock_dir" \
    MONERO_STARTUP_POLL=2 \
    bash "$skill_copy/scripts/interactive_setup.sh" \
      --wallet-path "$wallet_dir/test_wallet" \
      --wallet-password "walletpass" \
      --network stagenet \
      --daemon-type local \
      --daemon-port 38081 \
      --force 2>/dev/null

  [ "$status" -eq 0 ]
  local pid
  pid=$(cat "$lock_dir/wallet-rpc.pid" 2>/dev/null || echo "")
  [[ -n "$pid" ]] && kill "$pid" 2>/dev/null || true

  # Verify .env was written
  [[ -f "$skill_copy/.env" ]]
  local env_contents
  env_contents=$(cat "$skill_copy/.env")
  [[ "$env_contents" == *"MONERO_NETWORK=\"stagenet\""* ]]
  [[ "$env_contents" == *"MONERO_WALLET_PASSWORD=\"walletpass\""* ]]
  [[ "$env_contents" == *"MONERO_WALLET_NAME=\"$wallet_dir/test_wallet\""* ]]
  [[ "$env_contents" == *"MONERO_RPC_URL=\"http://127.0.0.1:38088\""* ]]
  [[ "$env_contents" == *"MONERO_RPC_USER=\""* ]]  # generated username
  [[ "$env_contents" == *"MONERO_RPC_PASSWORD=\""* ]]  # generated password
}

@test "interactive_setup generates random RPC credentials of correct length" {
  local fake_bin stub wallet_dir
  fake_bin="$(mktemp -d)"
  stub="$fake_bin/monero-wallet-rpc"
  printf '#!/usr/bin/env bash\nexec -a monero-wallet-rpc sleep 300\n' > "$stub"
  chmod +x "$stub"

  wallet_dir="$(mktemp -d)"
  touch "$wallet_dir/w.keys"

  local skill_copy
  skill_copy="$(mktemp -d)"
  cp "$ROOT"/.env.example "$skill_copy/.env.example"
  cp -r "$SCRIPTS" "$skill_copy/scripts"
  cp -r "$LIB" "$skill_copy/lib"
  cp "$ROOT/setup.sh" "$skill_copy/setup.sh"
  chmod +x "$skill_copy/scripts/interactive_setup.sh" 2>/dev/null || true

  local lock_dir
  lock_dir="$(mktemp -d)"
  run env PATH="$fake_bin:/usr/bin:/bin" \
    MONERO_LOCK_DIR="$lock_dir" \
    MONERO_STARTUP_POLL=2 \
    bash "$skill_copy/scripts/interactive_setup.sh" \
      --wallet-path "$wallet_dir/w" \
      --wallet-password "p" \
      --network mainnet \
      --daemon-type local \
      --force 2>/dev/null

  [ "$status" -eq 0 ]
  local pid
  pid=$(cat "$lock_dir/wallet-rpc.pid" 2>/dev/null || echo "")
  [[ -n "$pid" ]] && kill "$pid" 2>/dev/null || true

  # Extract generated credentials from .env
  local rpc_user rpc_pass
  rpc_user=$(grep '^MONERO_RPC_USER=' "$skill_copy/.env" | sed 's/^MONERO_RPC_USER="//; s/"$//')
  rpc_pass=$(grep '^MONERO_RPC_PASSWORD=' "$skill_copy/.env" | sed 's/^MONERO_RPC_PASSWORD="//; s/"$//')
  # Username should be 12 chars, password 24 chars
  [[ ${#rpc_user} -eq 12 ]]
  [[ ${#rpc_pass} -eq 24 ]]
  [[ "$rpc_user" =~ ^[a-zA-Z0-9]+$ ]]
  [[ "$rpc_pass" =~ ^[a-zA-Z0-9]+$ ]]
}

@test "interactive_setup starts wallet-rpc, writes PID, outputs ready JSON" {
  local fake_bin stub wallet_dir
  fake_bin="$(mktemp -d)"
  stub="$fake_bin/monero-wallet-rpc"
  # Stub that creates a PID-like file and sleeps (simulates wallet-rpc running)
  printf '#!/usr/bin/env bash\nexec -a monero-wallet-rpc sleep 300\n' > "$stub"
  chmod +x "$stub"

  wallet_dir="$(mktemp -d)"
  touch "$wallet_dir/w.keys"

  local lock_dir
  lock_dir="$(mktemp -d)"

  # Create a skill copy with stubbed setup.sh that reports ready
  local skill_copy
  skill_copy="$(mktemp -d)"
  cp "$ROOT"/.env.example "$skill_copy/.env.example"
  cp -r "$SCRIPTS" "$skill_copy/scripts"
  cp -r "$LIB" "$skill_copy/lib"
  # Stub setup.sh to report ready:true
  printf '#!/usr/bin/env bash\necho '\''{"ready":true,"deps_ok":true,"config_ok":true,"connection_ok":true,"wallet_loaded":true,"version":"196613","warnings":[]}'\''\n' > "$skill_copy/setup.sh"
  chmod +x "$skill_copy/scripts/interactive_setup.sh" 2>/dev/null || true

  run env PATH="$fake_bin:/usr/bin:/bin" \
    MONERO_LOCK_DIR="$lock_dir" \
    MONERO_STARTUP_POLL=2 \
    bash "$skill_copy/scripts/interactive_setup.sh" \
      --wallet-path "$wallet_dir/w" \
      --wallet-password "p" \
      --network mainnet \
      --daemon-type local \
      --force

  [ "$status" -eq 0 ]
  # Credentials must NOT appear in stdout JSON (security: prevent transcript leakage)
  echo "$output" | jq -e '.ready==true and .credentials_written==true and (.rpc_user|not) and (.rpc_password|not) and .rpc_port==18088 and (.wallet_pid|type=="number") and (.warnings|type=="array")' >/dev/null
  # PID file should exist
  [[ -f "$lock_dir/wallet-rpc.pid" ]]
  [[ -f "$lock_dir/wallet-rpc.port" ]]

  # Clean up the stub process
  local pid
  pid=$(cat "$lock_dir/wallet-rpc.pid" 2>/dev/null || echo "")
  [[ -n "$pid" ]] && kill "$pid" 2>/dev/null || true
}

@test "interactive_setup reuses running wallet-rpc when not --force" {
  local fake_bin stub wallet_dir
  fake_bin="$(mktemp -d)"
  stub="$fake_bin/monero-wallet-rpc"
  printf '#!/usr/bin/env bash\nexec -a monero-wallet-rpc sleep 300\n' > "$stub"
  chmod +x "$stub"

  wallet_dir="$(mktemp -d)"
  touch "$wallet_dir/w.keys"

  local lock_dir
  lock_dir="$(mktemp -d)"

  # Simulate wallet-rpc already running: write a PID file
  bash -c 'exec -a monero-wallet-rpc sleep 300' &
  local existing_pid=$!
  echo "$existing_pid" > "$lock_dir/wallet-rpc.pid"
  echo "18088" > "$lock_dir/wallet-rpc.port"

  local skill_copy
  skill_copy="$(mktemp -d)"
  cp "$ROOT"/.env.example "$skill_copy/.env.example"
  cp -r "$SCRIPTS" "$skill_copy/scripts"
  cp -r "$LIB" "$skill_copy/lib"
  printf '#!/usr/bin/env bash\necho '\''{"ready":true,"deps_ok":true,"config_ok":true,"connection_ok":true,"wallet_loaded":true,"version":"196613","warnings":[]}'\''\n' > "$skill_copy/setup.sh"
  chmod +x "$skill_copy/scripts/interactive_setup.sh" 2>/dev/null || true

  run env PATH="$fake_bin:/usr/bin:/bin" \
    MONERO_LOCK_DIR="$lock_dir" \
    MONERO_STARTUP_POLL=2 \
    bash "$skill_copy/scripts/interactive_setup.sh" \
      --wallet-path "$wallet_dir/w" \
      --wallet-password "p" \
      --network mainnet \
      --daemon-type local

  kill "$existing_pid" 2>/dev/null || true
  [ "$status" -eq 0 ]
  # Should reuse existing PID (no --force)
  echo "$output" | jq -e '.wallet_pid=='"$existing_pid" >/dev/null
}

@test "interactive_setup stops and restarts wallet-rpc when --force and already running" {
  local fake_bin stub wallet_dir
  fake_bin="$(mktemp -d)"
  stub="$fake_bin/monero-wallet-rpc"
  printf '#!/usr/bin/env bash\nexec -a monero-wallet-rpc sleep 300\n' > "$stub"
  chmod +x "$stub"

  wallet_dir="$(mktemp -d)"
  touch "$wallet_dir/w.keys"

  local lock_dir
  lock_dir="$(mktemp -d)"

  # Simulate wallet-rpc already running: write a PID file
  bash -c 'exec -a monero-wallet-rpc sleep 300' &
  local existing_pid=$!
  echo "$existing_pid" > "$lock_dir/wallet-rpc.pid"
  echo "18088" > "$lock_dir/wallet-rpc.port"

  local skill_copy
  skill_copy="$(mktemp -d)"
  cp "$ROOT"/.env.example "$skill_copy/.env.example"
  cp -r "$SCRIPTS" "$skill_copy/scripts"
  cp -r "$LIB" "$skill_copy/lib"
  printf '#!/usr/bin/env bash\necho '\''{"ready":true,"deps_ok":true,"config_ok":true,"connection_ok":true,"wallet_loaded":true,"version":"196613","warnings":[]}'\''\n' > "$skill_copy/setup.sh"
  chmod +x "$skill_copy/scripts/interactive_setup.sh" 2>/dev/null || true

  run env PATH="$fake_bin:/usr/bin:/bin" \
    MONERO_LOCK_DIR="$lock_dir" \
    MONERO_STARTUP_POLL=2 \
    bash "$skill_copy/scripts/interactive_setup.sh" \
      --wallet-path "$wallet_dir/w" \
      --wallet-password "p" \
      --network mainnet \
      --daemon-type local \
      --force

  [ "$status" -eq 0 ]
  # Old PID should have been killed
  ! kill -0 "$existing_pid" 2>/dev/null
  # New PID should be different and alive
  local new_pid
  new_pid=$(echo "$output" | jq -r '.wallet_pid')
  [[ "$new_pid" != "$existing_pid" ]]
  kill -0 "$new_pid" 2>/dev/null
  # Clean up new stub process
  kill "$new_pid" 2>/dev/null || true
}
