#!/usr/bin/env bash
# stop_wallet_rpc.sh — stop the monero-wallet-rpc background process.
# Reads PID from $MONERO_LOCK_DIR/wallet-rpc.pid, sends SIGTERM, waits, SIGKILL.
# Emits JSON on stdout.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../lib/format.sh"
source "$SCRIPT_DIR/../lib/config.sh"

if [[ -z "${MONERO_LOCK_DIR:-}" ]]; then
  parse_env "$SCRIPT_DIR/../.env" 2>/dev/null || true
  : "${MONERO_LOCK_DIR:=${CONFIG[MONERO_LOCK_DIR]:-/tmp/agenta-monero}}"
fi
export MONERO_LOCK_DIR

PID_FILE="$MONERO_LOCK_DIR/wallet-rpc.pid"
PORT_FILE="$MONERO_LOCK_DIR/wallet-rpc.port"

pid=""
stopped=false

if [[ -f "$PID_FILE" ]]; then
  pid=$(cat "$PID_FILE" 2>/dev/null || echo "")
  if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
    pid_args=$(ps -p "$pid" -o args= 2>/dev/null || echo "")
    if [[ "$pid_args" == *"wallet-rpc"* ]]; then
      kill -TERM "$pid" 2>/dev/null || true
      for _ in $(seq 1 50); do
        kill -0 "$pid" 2>/dev/null || break
        sleep 0.1
      done
      if kill -0 "$pid" 2>/dev/null; then
        kill -KILL "$pid" 2>/dev/null || true
        sleep 0.5
      fi
      for _ in $(seq 1 5); do
        kill -0 "$pid" 2>/dev/null || break
        sleep 0.1
      done
      kill -0 "$pid" 2>/dev/null || stopped=true
    fi
  fi
  rm -f "$PID_FILE" "$PORT_FILE" 2>/dev/null || true
fi

jq -nc --argjson stopped "$stopped" --argjson pid "${pid:-null}" \
  '{stopped:$stopped, pid:$pid}'
