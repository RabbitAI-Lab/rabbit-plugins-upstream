#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
. "$SCRIPT_DIR/lib/resolve-agent-auth.sh"
export LOBSTERMATCH_AUTH_ROOT="$(lm_auth_root)"
exec python3 "$SCRIPT_DIR/connect.py" "$@"
