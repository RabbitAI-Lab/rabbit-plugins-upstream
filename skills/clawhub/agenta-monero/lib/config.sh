#!/usr/bin/env bash
# Safe .env parser. NEVER sources the file.
declare -gA CONFIG 2>/dev/null || declare -A CONFIG

_parse_env_fail() { echo "CONFIG_INVALID: $1" >&2; return 1; }

parse_env() {
  local env_file="${1:-.env}"
  [[ -f "$env_file" ]] || { echo "CONFIG_MISSING: $env_file not found" >&2; return 1; }
  local line key value
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" || "$line" =~ ^[[:space:]]*# ]] && continue
    [[ ! "$line" =~ ^[A-Z_]+=.+$ ]] && { _parse_env_fail "Malformed line: $line"; return 1; }
    [[ "$line" =~ [\$\`\(\)\{\}\;\|\&\<\>] ]] && { _parse_env_fail "Shell metacharacters not allowed: $line"; return 1; }
    key="${line%%=*}"; value="${line#*=}"
    value="${value#\"}"; value="${value%\"}"
    value="${value#\'}"; value="${value%\'}"
    CONFIG["$key"]="$value"
  done < "$env_file"
}

require_config() {
  local k
  for k in "$@"; do
    if [[ -z "${CONFIG[$k]+x}" || -z "${CONFIG[$k]}" ]]; then
      echo "CONFIG_MISSING: required env var '$k' not set" >&2; return 1
    fi
  done
}

validate_network() {
  local n="${MONERO_NETWORK:-${CONFIG[MONERO_NETWORK]:-}}"
  case "$n" in mainnet|stagenet) return 0;; *) echo "CONFIG_INVALID: MONERO_NETWORK must be mainnet|stagenet (got '$n')" >&2; return 1;; esac
}

get_config() { printf '%s' "${CONFIG[$1]:-}"; }
