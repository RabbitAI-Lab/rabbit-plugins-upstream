load "test_helper"
chmod +x "$ROOT/setup.sh" 2>/dev/null || true

teardown() { stop_mock_rpc; }

@test "setup reports deps_ok missing jq (manual, path-dependent)" {
  # Simulate missing jq by shadowing PATH; kept skipped per plan.
  run env PATH="/usr/bin:/bin" bash -c 'command -v jq >/dev/null || echo skip'
  skip "path-dependent; run setup manually on a clean box"
}

@test "setup emits valid JSON status with all fields (live)" {
  mkdir -p "$FIXTURES/setup"
  printf '{"jsonrpc":"2.0","id":"0","result":{"height":1}}'   > "$FIXTURES/setup/get_height.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{"version":196613}}' > "$FIXTURES/setup/get_version.json"
  printf '{"jsonrpc":"2.0","id":"0","result":{"address":"A"}}' > "$FIXTURES/setup/get_address.json"
  export MONERO_RPC_URL="http://127.0.0.1:18099"
  start_mock_rpc 18099 "$FIXTURES/setup"
  d="$(mktemp -d)"; cp "$ROOT/.env.example" "$d/.env"
  export MONERO_LOCK_DIR="$(mktemp -d)"
  run bash "$ROOT/setup.sh" "$d/.env"
  [ "$status" -eq 0 ]
  echo "$output" | jq -e \
    '.ready==true and .deps_ok==true and .config_ok==true and .connection_ok==true and .wallet_loaded==true and (.version|type=="string" and .!="unknown") and (.warnings|type=="array")' >/dev/null
}
