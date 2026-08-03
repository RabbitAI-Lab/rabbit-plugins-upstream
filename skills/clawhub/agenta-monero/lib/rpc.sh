#!/usr/bin/env bash
NETRC_FILE=""

ensure_netrc() {
  local dir="${MONERO_LOCK_DIR:-/tmp/agenta-monero}"
  mkdir -p "$dir"; chmod 700 "$dir" 2>/dev/null || true
  NETRC_FILE="$dir/.netrc"
  local host; host=$(printf '%s' "${MONERO_RPC_URL:-}" | sed -E 's#^[a-z]+://##; s#[:/].*$##')
  : "${host:=127.0.0.1}"
  local user="${MONERO_RPC_USER:-}" pass="${MONERO_RPC_PASSWORD:-}"
  {
    printf 'machine %s\n' "$host"
    [[ -n "$user" ]] && printf 'login %s\n' "$user"
    [[ -n "$pass" ]] && printf 'password %s\n' "$pass"
  } > "$NETRC_FILE"
  chmod 600 "$NETRC_FILE"
  trap 'rm -f "$NETRC_FILE"' EXIT
}

_rpc_curl() {
  local body="$1"
  local args=(-s -X POST "${MONERO_RPC_URL}/json_rpc" -H 'Content-Type: application/json'
              --netrc-file "$NETRC_FILE" --digest --max-time "${MONERO_RPC_TIMEOUT:-30}")
  [[ "${MONERO_RPC_URL}" =~ ^https:// ]] && {
    [[ -n "${MONERO_RPC_SSL_CACERT:-}" ]] && args+=(--cacert "$MONERO_RPC_SSL_CACERT")
    [[ -n "${MONERO_RPC_SSL_CAPATH:-}" ]] && args+=(--capath "$MONERO_RPC_SSL_CAPATH")
  }
  curl "${args[@]}" -d "$body"
}

rpc_call() {
  local method="${1:?method}" params="${2:-"{}"}"
  local body; body=$(jq -nc --arg m "$method" --argjson p "$params" '{jsonrpc:"2.0",id:"0",method:$m,params:$p}')
  local resp rc
  resp=$(_rpc_curl "$body"); rc=$?
  [[ $rc -ne 0 ]] && json_error "RPC_UNREACHABLE" "curl exit $rc contacting ${MONERO_RPC_URL}"
  local has_err; has_err=$(echo "$resp" | jq -r '.error.code // empty' 2>/dev/null)
  if [[ -n "$has_err" ]]; then
    local msg; msg=$(echo "$resp" | jq -r '.error.message // "unknown"')
    json_error "RPC_ERROR" "$msg"
  fi
  echo "$resp" | jq -c '.result // {}'
}

rpc_check_connection() {
  rpc_call get_height '{}' >/dev/null || json_error "RPC_UNREACHABLE" "Cannot reach monero-wallet-rpc at ${MONERO_RPC_URL}"
}

rpc_refresh() {
  local timeout="${MONERO_REFRESH_TIMEOUT:-120}"
  [[ "${MONERO_AUTO_REFRESH:-true}" != "true" ]] && return 0
  local stamp="${MONERO_LOCK_DIR:-/tmp/agenta-monero}/.last_refresh"
  local now; now="$(date +%s)"
  if [[ -f "$stamp" ]]; then
    local last; last=$(cat "$stamp")
    [[ $(( now - last )) -lt ${MONERO_REFRESH_MIN_INTERVAL:-30} ]] && return 0
  fi
  MONERO_RPC_TIMEOUT="$timeout" rpc_call refresh '{}' >/dev/null 2>/dev/null || json_error "REFRESH_FAILED" "wallet refresh failed"
  echo "$now" > "$stamp"
}
