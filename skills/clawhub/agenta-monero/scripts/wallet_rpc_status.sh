#!/usr/bin/env bash
# wallet_rpc_status.sh — check if monero-wallet-rpc process is alive.
# Reads PID + port from $MONERO_LOCK_DIR. Emits JSON on stdout.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../lib/format.sh"
source "$SCRIPT_DIR/../lib/config.sh"

# Resolve MONERO_LOCK_DIR from .env if not in environment
if [[ -z "${MONERO_LOCK_DIR:-}" ]]; then
  parse_env "$SCRIPT_DIR/../.env" 2>/dev/null || true
  : "${MONERO_LOCK_DIR:=${CONFIG[MONERO_LOCK_DIR]:-/tmp/agenta-monero}}"
fi
export MONERO_LOCK_DIR

PID_FILE="$MONERO_LOCK_DIR/wallet-rpc.pid"
PORT_FILE="$MONERO_LOCK_DIR/wallet-rpc.port"

pid=""
port=""
running=false

if [[ -f "$PID_FILE" ]]; then
  pid=$(cat "$PID_FILE" 2>/dev/null || echo "")
  if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
    pid_args=$(ps -p "$pid" -o args= 2>/dev/null || echo "")
    if [[ "$pid_args" == *"wallet-rpc"* ]]; then
      running=true
      [[ -f "$PORT_FILE" ]] && port=$(cat "$PORT_FILE" 2>/dev/null || echo "")
    fi
  fi
fi

jq -nc --argjson running "$running" \
       --argjson pid "${pid:-null}" \
       --argjson port "${port:-null}" \
  '{running:$running, pid:$pid, port:$port}'
