load "test_helper"

@test "script_init acquires flock and exposes parsed config (.env mode)" {
  d="$(mktemp -d)"; printf 'MONERO_NETWORK="mainnet"\nMONERO_RPC_URL="http://127.0.0.1:18099"\nMONERO_LOCK_DIR="%s"\n' "$(mktemp -d)" > "$d/.env"
  mkdir -p "$d/lib" "$d/scripts"
  cp "$LIB"/*.sh "$d/lib/"
  printf 'MONERO_LOCK_DIR=""\n' >> "$d/.env"
  cat > "$d/scripts/x.sh" <<'SH'
#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init
echo "net=${CONFIG[MONERO_NETWORK]}"
SH
  chmod +x "$d/scripts/x.sh"
  run env -u MONERO_RPC_URL -u MONERO_NETWORK -u MONERO_LOCK_DIR -u MONERO_CONFIRMATIONS \
    bash "$d/scripts/x.sh"
  [ "$status" -eq 0 ]
  [[ "$output" == *"net=mainnet"* ]]
}

@test "script_init works with pre-exported env vars (test mode)" {
  d="$(mktemp -d)"; mkdir -p "$d/lib" "$d/scripts"
  cp "$LIB"/*.sh "$d/lib/"
  lockdir="$(mktemp -d)"
  cat > "$d/scripts/x.sh" <<SH
#!/usr/bin/env bash
set -euo pipefail
source "\$(dirname "\${BASH_SOURCE[0]}")/../lib/common.sh"
script_init
echo "url=\${MONERO_RPC_URL}"
echo "lock=\${MONERO_LOCK_DIR}"
SH
  chmod +x "$d/scripts/x.sh"
  run env MONERO_RPC_URL="http://127.0.0.1:18099" \
          MONERO_NETWORK="mainnet" \
          MONERO_LOCK_DIR="$lockdir" \
    bash "$d/scripts/x.sh"
  [ "$status" -eq 0 ]
  [[ "$output" == *"url=http://127.0.0.1:18099"* ]]
  [[ "$output" == *"lock=$lockdir"* ]]
}

@test "script_init --no-refresh exports MONERO_AUTO_REFRESH=false" {
  d="$(mktemp -d)"; printf 'MONERO_NETWORK="mainnet"\nMONERO_RPC_URL="http://127.0.0.1:18099"\nMONERO_LOCK_DIR="%s"\n' "$(mktemp -d)" > "$d/.env"
  mkdir -p "$d/lib" "$d/scripts"
  cp "$LIB"/*.sh "$d/lib/"
  cat > "$d/scripts/x.sh" <<'SH'
#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init
echo "auto=${MONERO_AUTO_REFRESH}"
SH
  chmod +x "$d/scripts/x.sh"
  run env -u MONERO_RPC_URL -u MONERO_NETWORK -u MONERO_LOCK_DIR -u MONERO_CONFIRMATIONS \
    bash "$d/scripts/x.sh" --no-refresh
  [ "$status" -eq 0 ]
  [[ "$output" == *"auto=false"* ]]
}

@test "script_init --no-refresh honored in non-first arg position (regression)" {
  d="$(mktemp -d)"; printf 'MONERO_NETWORK="mainnet"\nMONERO_RPC_URL="http://127.0.0.1:18099"\nMONERO_LOCK_DIR="%s"\n' "$(mktemp -d)" > "$d/.env"
  mkdir -p "$d/lib" "$d/scripts"
  cp "$LIB"/*.sh "$d/lib/"
  cat > "$d/scripts/x.sh" <<'SH'
#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init
echo "auto=${MONERO_AUTO_REFRESH}"
SH
  chmod +x "$d/scripts/x.sh"
  run env -u MONERO_RPC_URL -u MONERO_NETWORK -u MONERO_LOCK_DIR -u MONERO_CONFIRMATIONS \
    bash "$d/scripts/x.sh" --confirmed-only --no-refresh
  [ "$status" -eq 0 ]
  [[ "$output" == *"auto=false"* ]]
}

@test "script_init exports MONERO_WALLET_PASSWORD from .env" {
  d="$(mktemp -d)"; printf 'MONERO_NETWORK="mainnet"\nMONERO_RPC_URL="http://127.0.0.1:18099"\nMONERO_LOCK_DIR="%s"\nMONERO_WALLET_PASSWORD="secret123"\n' "$(mktemp -d)" > "$d/.env"
  mkdir -p "$d/lib" "$d/scripts"
  cp "$LIB"/*.sh "$d/lib/"
  cat > "$d/scripts/x.sh" <<'SH'
#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"
script_init
[[ -n "${MONERO_WALLET_PASSWORD}" ]] && echo "wp_set=true" || echo "wp_set=false"
SH
  chmod +x "$d/scripts/x.sh"
  run env -u MONERO_RPC_URL -u MONERO_NETWORK -u MONERO_LOCK_DIR -u MONERO_CONFIRMATIONS -u MONERO_WALLET_PASSWORD \
    bash "$d/scripts/x.sh"
  [ "$status" -eq 0 ]
  [[ "$output" == *"wp_set=true"* ]]
}

teardown() { stop_mock_rpc; }
