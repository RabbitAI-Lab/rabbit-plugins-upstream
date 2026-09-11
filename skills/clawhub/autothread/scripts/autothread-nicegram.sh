#!/bin/bash
# autothread-nicegram.sh — Nicegram adapter.
#
# Nicegram is a third-party client for the Telegram platform: Nicegram
# groups/chats ARE Telegram chats on the same Bot API. This adapter
# therefore delegates to autothread-telegram.sh, optionally using a
# dedicated Nicegram bot token if one is configured.
#
# Usage:
#   ./autothread-nicegram.sh <chat_id> <message_id> <sender> [title] [text]
#
# Args: identical to autothread-telegram.sh
#
# Config: token is read from .channels.nicegram.botToken when present,
# falling back to .channels.telegram.botToken.
#
# Output: JSON — {"topic_id": <id>, "title": "<title>", "link": "<url>"}
# Exit codes: 0 = success, 1 = error (details on stderr)

set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/common.sh
source "$SCRIPT_DIR/lib/common.sh"

autothread_require jq
autothread_config_path >/dev/null

# Resolve the token source: a Nicegram-specific token when present,
# otherwise leave the Telegram adapter to use the shared token.
if [ -f "$AUTOTHREAD_CONFIG_FILE" ]; then
  NICEGRAM_TOKEN=$(jq -r '.channels.nicegram.botToken // empty' "$AUTOTHREAD_CONFIG_FILE" 2>/dev/null)
  if [ -n "$NICEGRAM_TOKEN" ]; then
    export AUTOTHREAD_OVERRIDE_TOKEN="$NICEGRAM_TOKEN"
  fi
fi

# Delegate to the Telegram adapter (same API, same semantics).
exec "$SCRIPT_DIR/autothread-telegram.sh" "$@"
