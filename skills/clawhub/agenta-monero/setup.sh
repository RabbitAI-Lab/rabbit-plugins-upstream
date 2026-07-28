#!/usr/bin/env bash
# setup.sh — check deps, parse .env, build netrc, test RPC connection, report status.
# Always emits a single JSON status object on stdout; failures set *_ok=false, never abort.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/format.sh
source "$SCRIPT_DIR/lib/format.sh"
# shellcheck source=lib/config.sh
source "$SCRIPT_DIR/lib/config.sh"
# shellcheck source=lib/rpc.sh
source "$SCRIPT_DIR/lib/rpc.sh"

ENV_FILE="${1:-$SCRIPT_DIR/.env}"
WARNINGS=()
warn() { WARNINGS+=("$1"); }

# --- Dependency checks ---
deps_ok=true
for t in curl jq flock; do
  command -v "$t" >/dev/null 2>&1 || { deps_ok=false; warn "missing dependency: $t"; }
done
if [[ "${BASH_VERSINFO[0]:-0}" -lt 4 ]]; then
  deps_ok=false; warn "bash < 4 (${BASH_VERSINFO[0]:-unknown})"
fi

# --- Config parse ---
config_ok=false; connection_ok=false; wallet_loaded=false; version="unknown"
if [[ -f "$ENV_FILE" ]]; then
  if parse_env "$ENV_FILE"; then
    config_ok=true
  else
    warn "config parse failed for $ENV_FILE"
  fi
  # Environment takes precedence over .env (12-factor: env > file).
  MONERO_RPC_URL="${MONERO_RPC_URL:-${CONFIG[MONERO_RPC_URL]:-}}";     export MONERO_RPC_URL
  MONERO_RPC_USER="${MONERO_RPC_USER:-${CONFIG[MONERO_RPC_USER]:-}}"; export MONERO_RPC_USER
  MONERO_RPC_PASSWORD="${MONERO_RPC_PASSWORD:-${CONFIG[MONERO_RPC_PASSWORD]:-}}"; export MONERO_RPC_PASSWORD
  MONERO_LOCK_DIR="${MONERO_LOCK_DIR:-${CONFIG[MONERO_LOCK_DIR]:-/tmp/agenta-monero}}"; export MONERO_LOCK_DIR
else
  warn ".env not found at $ENV_FILE (copy .env.example and fill it in)"
fi

# Warn if using cleartext HTTP credentials for a non-localhost endpoint.
if [[ "${MONERO_RPC_URL:-}" =~ ^http:// ]] && [[ ! "${MONERO_RPC_URL}" =~ 127\.0\.0\.1|localhost ]]; then
  warn "MONERO_RPC_URL is HTTP for non-localhost: credentials sent in cleartext"
fi

# --- Connection + wallet checks (rpc_call exits 1 on failure via json_error,
#      so each is wrapped in a subshell to contain the exit and keep status emission) ---
if [[ "$config_ok" == true ]]; then
  ensure_netrc
  if ( rpc_call get_height '{}' >/dev/null 2>&1 ); then
    connection_ok=true
    # monero-wallet-rpc get_version returns an INTEGER (e.g. 196613), not a
    # dotted string, so a lexicographic "< 0.18.0.0" compare is meaningless.
    # Report the version as-is and advise the user to confirm >= 0.18.0.
    ver="$( rpc_call get_version '{}' 2>/dev/null | jq -r '.version // empty' 2>/dev/null )" || ver=""
    if [[ -n "$ver" ]]; then
      version="$ver"
      if [[ "$version" =~ ^[0-9]+$ ]]; then
        warn "verify monero-wallet-rpc >= 0.18.0 (version reported as $version)"
      fi
    fi
    if ( rpc_call get_address '{}' >/dev/null 2>&1 ); then
      wallet_loaded=true
    else
      warn "wallet not loaded (get_address failed)"
    fi
  else
    warn "RPC unreachable at ${MONERO_RPC_URL:-<unset>}"
  fi
fi

# --- Build + emit status JSON (deterministic; booleans as JSON booleans) ---
if [[ ${#WARNINGS[@]} -eq 0 ]]; then
  warnings_json='[]'
else
  warnings_json="$( printf '%s\n' "${WARNINGS[@]}" | jq -R . | jq -s . )"
fi

status_json="$(jq -nc \
  --argjson deps_ok "$deps_ok" \
  --argjson config_ok "$config_ok" \
  --argjson connection_ok "$connection_ok" \
  --argjson wallet_loaded "$wallet_loaded" \
  --arg version "$version" \
  --argjson warnings "$warnings_json" \
  '{deps_ok:$deps_ok, config_ok:$config_ok, connection_ok:$connection_ok,
    wallet_loaded:$wallet_loaded, version:$version, warnings:$warnings}')"

# ready is derived: true iff all *_ok booleans are true.
printf '%s\n' "$status_json" | jq -c '. + {ready:(.deps_ok and .config_ok and .connection_ok and .wallet_loaded)}'
