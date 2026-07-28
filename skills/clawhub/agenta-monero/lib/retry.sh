#!/usr/bin/env bash
RETRYABLE="RPC_UNREACHABLE SYNC_FAILED REFRESH_FAILED DAEMON_DISCONNECTED RATE_LIMITED"

is_retryable() { local c="$1"; [[ " $RETRYABLE " == *" $c "* ]]; }

retry_with_backoff() {
  local max="${MONERO_RETRY_MAX:-2}" backoff="${MONERO_RETRY_BACKOFF:-1}" attempt=0 code result exit_code
  while [[ $attempt -le $max ]]; do
    exit_code=0
    result=$("$@" 2>&1) || exit_code=$?
    [[ $exit_code -eq 0 ]] && { printf '%s\n' "$result"; return 0; }
    code=$(echo "$result" | jq -r '.code // empty' 2>/dev/null)
    if is_retryable "$code" && [[ $attempt -lt $max ]]; then
      sleep "$backoff"; backoff=$((backoff*2)); attempt=$((attempt+1)); continue
    fi
    printf '%s\n' "$result" >&2; return "$exit_code"
  done
}
