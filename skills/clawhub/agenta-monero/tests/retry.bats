load "test_helper"
source "$LIB/format.sh"
source "$LIB/retry.sh"

FLAKY_COUNTER="$(mktemp)"

flaky() {
  local n="$(cat "$FLAKY_COUNTER" 2>/dev/null || echo 0)"
  n=$((n+1)); echo "$n" >"$FLAKY_COUNTER"
  [[ $n -ge 2 ]] && echo "ok" || json_error "RPC_UNREACHABLE" "boom"
}

@test "is_retryable classifies codes" {
  is_retryable RPC_UNREACHABLE; [ $? -eq 0 ]
  ! is_retryable CONFIG_MISSING
}

@test "retry_with_backoff retries transient then succeeds" {
  export MONERO_RETRY_MAX=2 MONERO_RETRY_BACKOFF=0
  rm -f "$FLAKY_COUNTER"
  run retry_with_backoff flaky
  [ "$status" -eq 0 ]
  [[ "$output" == "ok" ]]
}

@test "retry_with_backoff does not retry non-retryable" {
  export MONERO_RETRY_MAX=3 MONERO_RETRY_BACKOFF=0
  local calls; calls="$(mktemp)"; echo 0 > "$calls"
  boom() { local n; n="$(cat "$calls" 2>/dev/null || echo 0)"; n=$((n+1)); echo "$n" > "$calls"; json_error "INVALID_ADDRESS" "no"; }
  run retry_with_backoff boom
  local n; n="$(cat "$calls" 2>/dev/null || echo 0)"; rm -f "$calls"
  [ "$status" -ne 0 ]
  [[ "$output" == *"INVALID_ADDRESS"* ]]
  [ "$n" -eq 1 ]   # ran exactly once — no retry
}

@test "retry_with_backoff retries under set -e (regression)" {
  # Genuine set -e subshell: the output capture MUST NOT abort the shell; the wrapper
  # retries the transient failure to success rather than exiting at the capture line.
  local counter; counter="$(mktemp)"; echo 0 > "$counter"
  local flaky; flaky="$(mktemp).sh"
  cat > "$flaky" <<'SH'
#!/usr/bin/env bash
c="$(cat "$1")"; c=$((c+1)); echo "$c" > "$1"
[[ $c -ge 2 ]] && { echo "ok"; exit 0; } || { printf '{"code":"RPC_UNREACHABLE"}\n' >&2; exit 1; }
SH
  chmod +x "$flaky"
  run bash -c "set -e; source '$LIB/format.sh'; source '$LIB/retry.sh'; MONERO_RETRY_MAX=2 MONERO_RETRY_BACKOFF=0 retry_with_backoff '$flaky' '$counter'"
  local calls; calls="$(cat "$counter" 2>/dev/null || echo 0)"; rm -f "$counter" "$flaky"
  [ "$status" -eq 0 ]
  [[ "$output" == *"ok"* ]]
  [ "$calls" -eq 2 ]   # failed once (retryable) then succeeded ⇒ it retried
}
