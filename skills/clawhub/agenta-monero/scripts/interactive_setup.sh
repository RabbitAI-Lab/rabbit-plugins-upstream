#!/usr/bin/env bash
# interactive_setup.sh — full first-time setup for Agenta-Monero.
# Generates RPC credentials, writes .env, starts monero-wallet-rpc, runs setup.sh.
# Works in two modes:
#   Non-interactive: all values passed as flags (for agent / tests)
#   Interactive: prompts for any missing values (for manual users)
# Emits JSON on stdout (success) or structured error JSON on stderr.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../lib/format.sh"
source "$SCRIPT_DIR/../lib/config.sh"

usage() {
  cat <<'EOF'
USAGE: interactive_setup.sh [OPTIONS]

Automates first-time setup: generates RPC credentials, writes .env,
starts monero-wallet-rpc, and runs setup.sh.

OPTIONS:
  --wallet-path PATH        Path to wallet file (without .keys extension)
  --wallet-password PASS    Wallet file password
  --network mainnet|stagenet  Monero network (default: mainnet)
  --daemon-type local|remote  Daemon type (default: local)
  --daemon-address HOST:PORT  Remote daemon address (required if --daemon-type remote)
  --daemon-port PORT        Local daemon port (default: 18081 mainnet, 38081 stagenet)
  --force                   Overwrite existing .env without prompting
  --help                    Show this help message

If any required option is missing, the script prompts for it interactively.
EOF
}

# --- Flag parsing ---
WALLET_PATH=""
WALLET_PASSWORD=""
NETWORK="mainnet"
DAEMON_TYPE="local"
DAEMON_ADDRESS=""
DAEMON_PORT=""
FORCE=false

while [[ $# -gt 0 ]]; do case "$1" in
  --wallet-path)      WALLET_PATH="$2";      shift 2;;
  --wallet-password)  WALLET_PASSWORD="$2";  shift 2;;
  --network)          NETWORK="$2";          shift 2;;
  --daemon-type)      DAEMON_TYPE="$2";      shift 2;;
  --daemon-address)   DAEMON_ADDRESS="$2";   shift 2;;
  --daemon-port)      DAEMON_PORT="$2";      shift 2;;
  --force)            FORCE=true;            shift;;
  --help)             usage; exit 0;;
  *) shift;;
esac; done

# --- Validate network ---
case "$NETWORK" in
  mainnet|stagenet) ;;
  *) json_error "CONFIG_INVALID" "MONERO_NETWORK must be mainnet|stagenet (got '$NETWORK')";;
esac

# --- Determine RPC and daemon ports ---
if [[ "$NETWORK" == "mainnet" ]]; then
  RPC_PORT=18088
  : "${DAEMON_PORT:=18081}"
else
  RPC_PORT=38088
  : "${DAEMON_PORT:=38081}"
fi

# --- Dependency checks ---
for t in curl jq flock; do
  command -v "$t" >/dev/null 2>&1 || json_error "CONFIG_MISSING" "missing dependency: $t"
done
if [[ "${BASH_VERSINFO[0]:-0}" -lt 4 ]]; then
  json_error "CONFIG_MISSING" "bash < 4 (${BASH_VERSINFO[0]:-unknown})"
fi
command -v monero-wallet-rpc >/dev/null 2>&1 \
  || json_error "CONFIG_MISSING" "monero-wallet-rpc not found — install from https://getmonero.org/downloads/"

# --- Prompt for missing values (interactive mode) ---
prompt_if_empty() {
  local var_name="$1" prompt="$2" secret="${3:-false}"
  local current="${!var_name:-}"
  if [[ -z "$current" ]]; then
    if [[ "$secret" == "true" ]]; then
      printf '%s' "$prompt" >&2
      read -rs "$var_name"
      echo "" >&2
    else
      printf '%s' "$prompt" >&2
      read -r "$var_name"
    fi
  fi
}

prompt_if_empty WALLET_PATH "Enter wallet file path: "
prompt_if_empty WALLET_PASSWORD "Enter wallet password: " true

if [[ "$WALLET_PASSWORD" == *'"'* || "$WALLET_PASSWORD" == *'\\'* ]]; then
  json_error "INVALID_INPUT" "--wallet-password must not contain double-quotes or backslashes"
fi

# --- Validate wallet file ---
# Strip .keys extension if present (monero-wallet-rpc adds it automatically)
WALLET_PATH="${WALLET_PATH%.keys}"
WALLET_KEYS_FILE="${WALLET_PATH}.keys"
if [[ ! -f "$WALLET_KEYS_FILE" ]]; then
  if [[ ! -f "$WALLET_PATH" ]]; then
    json_error "CONFIG_MISSING" "wallet file not found: $WALLET_PATH or $WALLET_KEYS_FILE"
  fi
fi

# --- Validate daemon type and address ---
case "$DAEMON_TYPE" in
  local|remote) ;;
  *) json_error "CONFIG_INVALID" "--daemon-type must be local|remote (got '$DAEMON_TYPE')";;
esac
if [[ "$DAEMON_TYPE" == "remote" ]]; then
  prompt_if_empty DAEMON_ADDRESS "Enter remote daemon address (host:port): "
  [[ -z "$DAEMON_ADDRESS" ]] && json_error "CONFIG_MISSING" "--daemon-address required when --daemon-type remote"
  DAEMON_PORT=""  # remote: address includes port
fi

# --- Generate random RPC credentials ---
gen_random() {
  local len="${1:?length}" chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
  LC_ALL=C tr -dc "$chars" </dev/urandom 2>/dev/null | head -c "$len" || true
}
RPC_USER=$(gen_random 12)
RPC_PASSWORD=$(gen_random 24)

# --- Resolve .env path ---
ENV_FILE="$SCRIPT_DIR/../.env"

if [[ -f "$ENV_FILE" && "$FORCE" != true ]]; then
  printf '%s' ".env already exists at $ENV_FILE — overwrite? [y/N] " >&2
  answer=""
  read -r answer
  [[ "$answer" =~ ^[yY] ]] || json_error "CONFIG_INVALID" "setup cancelled by user"
fi

# --- Write .env ---
cat > "$ENV_FILE" <<EOF
# === Monero Wallet RPC Connection ===
MONERO_RPC_URL="http://127.0.0.1:$RPC_PORT"
MONERO_RPC_USER="$RPC_USER"
MONERO_RPC_PASSWORD="$RPC_PASSWORD"
MONERO_WALLET_NAME="$WALLET_PATH"
MONERO_WALLET_PASSWORD="$WALLET_PASSWORD"

# === Network ===
MONERO_NETWORK="$NETWORK"

# === Lifecycle Management ===
MONERO_LIFECYCLE="managed"

# === Remote Node (optional) ===
MONERO_REMOTE_NODE=""
MONERO_REMOTE_PORT=""

# === Display ===
MONERO_CONFIRMATIONS="10"
MONERO_AMOUNT_FORMAT="xmr"

# === Refresh ===
MONERO_AUTO_REFRESH="true"
MONERO_REFRESH_MIN_INTERVAL="30"
MONERO_REFRESH_TIMEOUT="120"

# === Retry ===
MONERO_RETRY_MAX="2"
MONERO_RETRY_BACKOFF="1"

# === Concurrency ===
MONERO_LOCK_DIR="/tmp/agenta-monero"
MONERO_LOCK_TIMEOUT="60"

# === Advanced ===
MONERO_RPC_TIMEOUT="30"
MONERO_RPC_SSL_CACERT=""
MONERO_RPC_SSL_CAPATH=""
EOF
chmod 600 "$ENV_FILE"

# --- Resolve lock dir for PID file ---
: "${MONERO_LOCK_DIR:=/tmp/agenta-monero}"
export MONERO_LOCK_DIR
mkdir -p "$MONERO_LOCK_DIR"; chmod 700 "$MONERO_LOCK_DIR" 2>/dev/null || true

PID_FILE="$MONERO_LOCK_DIR/wallet-rpc.pid"
PORT_FILE="$MONERO_LOCK_DIR/wallet-rpc.port"
LOG_FILE="$MONERO_LOCK_DIR/wallet-rpc.log"

# --- Check if wallet-rpc already running ---
WALLET_PID=""
if [[ -f "$PID_FILE" ]]; then
  existing_pid=$(cat "$PID_FILE" 2>/dev/null || echo "")
  if [[ -n "$existing_pid" ]] && kill -0 "$existing_pid" 2>/dev/null; then
    if [[ "$FORCE" == true ]]; then
      kill "$existing_pid" 2>/dev/null || true
      sleep 1
      kill -9 "$existing_pid" 2>/dev/null || true
      rm -f "$PID_FILE" "$PORT_FILE"
    else
      pid_args=$(ps -p "$existing_pid" -o args= 2>/dev/null || echo "")
      if [[ "$pid_args" == *"wallet-rpc"* ]]; then
        WALLET_PID="$existing_pid"
      else
        rm -f "$PID_FILE" "$PORT_FILE"
      fi
    fi
  fi
fi

# --- Start monero-wallet-rpc if not already running ---
if [[ -z "$WALLET_PID" ]]; then
  if curl -s -o /dev/null --connect-timeout 1 --max-time 2 "http://127.0.0.1:$RPC_PORT/" 2>/dev/null; then
    json_error "RPC_UNREACHABLE" "port $RPC_PORT already in use — stop the existing process or use a different port"
  fi

  daemon_addr=""
  if [[ "$DAEMON_TYPE" == "remote" ]]; then
    daemon_addr="$DAEMON_ADDRESS"
    daemon_trust="--untrusted-daemon"
  else
    daemon_addr="127.0.0.1:$DAEMON_PORT"
    daemon_trust="--trusted-daemon"
  fi

  stagenet_flag=""
  [[ "$NETWORK" == "stagenet" ]] && stagenet_flag="--stagenet"

  monero-wallet-rpc \
    $stagenet_flag \
    --wallet-file "$WALLET_PATH" --password "$WALLET_PASSWORD" \
    --rpc-bind-ip 127.0.0.1 \
    --rpc-bind-port "$RPC_PORT" \
    --rpc-login "$RPC_USER:$RPC_PASSWORD" \
    --daemon-address "$daemon_addr" $daemon_trust \
    >"$LOG_FILE" 2>&1 &
  WALLET_PID=$!
  echo "$WALLET_PID" > "$PID_FILE"
  echo "$RPC_PORT" > "$PORT_FILE"

  # Wait for process to stabilize (poll port up to 15s)
  for _ in $(seq 1 "${MONERO_STARTUP_POLL:-30}"); do
    kill -0 "$WALLET_PID" 2>/dev/null || break
    curl -s -o /dev/null --connect-timeout 1 "http://127.0.0.1:$RPC_PORT/json_rpc" 2>/dev/null && break
    sleep 0.5
  done
  if ! kill -0 "$WALLET_PID" 2>/dev/null; then
    rm -f "$PID_FILE" "$PORT_FILE"
    json_error "RPC_UNREACHABLE" "monero-wallet-rpc failed to start (process died — see $LOG_FILE)"
  fi
fi

# --- Run setup.sh to verify ---
WARNINGS=()
setup_result=$(bash "$SCRIPT_DIR/../setup.sh" "$ENV_FILE" 2>/dev/null || echo "")
ready=$(echo "$setup_result" | jq -r '.ready // false' 2>/dev/null || echo "false")

if [[ "$ready" != "true" ]]; then
  WARNINGS+=("setup.sh did not report ready — check $LOG_FILE and daemon connectivity")
fi

# --- Build warnings JSON ---
if [[ ${#WARNINGS[@]} -eq 0 ]]; then
  warnings_json='[]'
else
  warnings_json=$(printf '%s\n' "${WARNINGS[@]}" | jq -R . | jq -s .)
fi

# --- Emit final JSON ---
# Credentials are NOT emitted in stdout — they are in .env (chmod 600).
# Exposing them in stdout risks leakage through agent transcripts and logs.
jq -nc \
  --argjson ready "$ready" \
  --argjson credentials_written true \
  --argjson rpc_port "$RPC_PORT" \
  --argjson wallet_pid "${WALLET_PID:-null}" \
  --arg wallet_rpc_log "$LOG_FILE" \
  --argjson warnings "$warnings_json" \
  '{ready:$ready, credentials_written:$credentials_written, rpc_port:$rpc_port, wallet_pid:$wallet_pid, wallet_rpc_log:$wallet_rpc_log, warnings:$warnings}'
