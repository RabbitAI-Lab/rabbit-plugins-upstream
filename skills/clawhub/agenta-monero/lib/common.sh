#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[1]:-${BASH_SOURCE[0]}}")" && pwd)"
export LIB="$SCRIPT_DIR/../lib"
for f in format.sh config.sh validate.sh rpc.sh retry.sh; do source "$SCRIPT_DIR/../lib/$f"; done

NO_REFRESH=0
for __a in "$@"; do [[ "$__a" == "--no-refresh" ]] && NO_REFRESH=1; done

script_init() {
  if [[ -z "${MONERO_RPC_URL:-}" ]]; then
    parse_env "$SCRIPT_DIR/../.env"
    local k
    for k in MONERO_RPC_URL MONERO_RPC_USER MONERO_RPC_PASSWORD MONERO_WALLET_NAME \
             MONERO_WALLET_PASSWORD MONERO_NETWORK MONERO_CONFIRMATIONS MONERO_LOCK_DIR MONERO_LOCK_TIMEOUT \
             MONERO_AUTO_REFRESH MONERO_REFRESH_MIN_INTERVAL MONERO_RPC_TIMEOUT; do
      [[ -n "${CONFIG[$k]:-}" ]] && export "$k=${CONFIG[$k]}"
    done
  fi
  validate_network || true
  : "${MONERO_LOCK_DIR:=/tmp/agenta-monero}"; export MONERO_LOCK_DIR
  mkdir -p "$MONERO_LOCK_DIR"; chmod 700 "$MONERO_LOCK_DIR" 2>/dev/null || true
  ensure_netrc
  exec 200>"$MONERO_LOCK_DIR/agenta-monero.lock"
  flock -w "${MONERO_LOCK_TIMEOUT:-60}" 200 || json_error "RATE_LIMITED" "could not acquire lock"
  if [[ "$NO_REFRESH" == 1 ]]; then
    export MONERO_AUTO_REFRESH=false
  fi
}
