#!/bin/bash
# ============================================================
# WatchItAI Skill - Cross-platform entry point (no Node.js needed)
#
# This script auto-detects the platform/architecture and launches
# the correct self-contained Go binary with all forwarded arguments.
#
# Special behavior:
#   - All commands are executed from SCRIPT_DIR (the skill install dir)
#     so that config.json (including accessKey) lives in one place,
#     regardless of which shell cwd the user runs from.
#   - "authorize" command can also accept a code for one-step linking.
#
# Usage:
#   bash run.sh share              # Start screen sharing
#   bash run.sh link               # Create session & return viewer link
#   bash run.sh start              # Start bridge server only
#   bash run.sh status             # Check bridge server status
#   bash run.sh permissions        # Check system permissions
#   bash run.sh preflight          # Run permission pre-check (macOS)
#   bash run.sh info               # Show system info
#   bash run.sh authorize <CODE>   # Link skill to your watchitai.net
#                                    account via one-time auth code
#                                    (XXXX-XXXX format, 5 min TTL)
#   bash run.sh version            # Show version
#   bash run.sh help               # Show help
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Detect platform
PLATFORM=$(uname -s | tr '[:upper:]' '[:lower:]')

# Detect architecture
ARCH=$(uname -m)
case "$ARCH" in
    x86_64|amd64) ARCH="amd64" ;;
    arm64|aarch64) ARCH="arm64" ;;
    *) echo "❌ Unsupported architecture: $ARCH" >&2; exit 1 ;;
esac

# Resolve binary path
BINARY_NAME="watchitai-${PLATFORM}-${ARCH}"
BINARY_PATH="${SCRIPT_DIR}/bin/${BINARY_NAME}"

if [ ! -f "$BINARY_PATH" ]; then
    # On Apple Silicon, try Rosetta fallback to amd64
    if [ "$PLATFORM" = "darwin" ] && [ "$ARCH" = "arm64" ]; then
        FALLBACK="${SCRIPT_DIR}/bin/watchitai-darwin-amd64"
        if [ -f "$FALLBACK" ]; then
            BINARY_PATH="$FALLBACK"
        else
            echo "❌ Binary not found: ${BINARY_PATH}" >&2
            echo "   Also tried Rosetta fallback: ${FALLBACK}" >&2
            echo "   Please reinstall the skill from https://watchitai.net" >&2
            exit 1
        fi
    else
        echo "❌ Binary not found: ${BINARY_PATH}" >&2
        echo "   Please reinstall the skill from https://watchitai.net" >&2
        exit 1
    fi
fi

chmod +x "$BINARY_PATH" 2>/dev/null || true

# Ensure config.json exists (create minimal skeleton with correct perms if missing)
# so the Go binary can write accessKey without ENOENT.
if [ ! -f "${SCRIPT_DIR}/config.json" ]; then
    cat > "${SCRIPT_DIR}/config.json" <<'EOF'
{
  "domain": "watchitai.net",
  "bridgePort": 8765,
  "mode": "server"
}
EOF
    chmod 600 "${SCRIPT_DIR}/config.json"
fi

# --- Special handling for authorize command with friendly help ---------------
if [ "$1" = "authorize" ]; then
    # If user passes no args OR only --request/-r, delegate to binary;
    # otherwise keep friendly --help output in pure shell.
    shift  # drop "authorize" so remaining args are <CODE> or --request/-r
    AUTH_ARGS=("$@")
    NEED_HELP=1
    for a in "${AUTH_ARGS[@]}"; do
        if [ "$a" = "--request" ] || [ "$a" = "-r" ] || [ -n "$a" ]; then
            NEED_HELP=0
            break
        fi
    done
    if [ "$NEED_HELP" = "1" ]; then
        cat <<'HELP'
Usage:
  bash run.sh authorize <XXXX-XXXX>     Bind using one-time auth code
  bash run.sh authorize --request        Auto Device Flow (recommended)

Bind this skill to your watchitai.net account to unlock:
  • Longer sessions (no 15-min single-session anonymous cap)
  • Higher daily quota (no 30-min/day anonymous cap)
  • Session ownership and audit history

Recommended — one-click Device Flow:
  1. Run:  bash run.sh authorize --request
  2. Browser opens automatically; log in if needed
  3. Click "Confirm authorize" on the web page
  4. Skill auto-receives credentials (no copy/paste required)

Legacy auth code path:
  1. Log in at https://watchitai.net
  2. Go to Profile → 技能授权 (Access Keys)
  3. Click "生成授权码" and copy the 8-character code
  4. Run:  bash run.sh authorize XXXX-XXXX
HELP
        exit 1
    fi
    # Restore args so `exec` below receives: authorize <rest...>
    set -- "authorize" "${AUTH_ARGS[@]}"
fi

# Run from SCRIPT_DIR so config.json (including accessKey) lives next to
# the skill install dir regardless of the user's shell working directory.
# We use "cd + exec $BINARY \"\$@\"" pattern to avoid losing arg quoting.
cd "$SCRIPT_DIR"
exec "$BINARY_PATH" "$@"
