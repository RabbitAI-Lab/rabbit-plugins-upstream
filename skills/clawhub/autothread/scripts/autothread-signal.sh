#!/bin/bash
# autothread-signal.sh — Signal adapter for /topic (pseudo-topic mode).
#
# IMPORTANT LIMITATION: Signal has no native forum topics or threads.
# There is no bot API object equivalent to a Telegram forum topic or a
# Discord thread. This adapter therefore runs in "pseudo-topic" mode:
#
#   1. It posts a titled, quoted digest of the original message to the
#      same group, using a distinctive header so digest messages are
#      recognisable and searchable ("📌 <title>").
#   2. It returns the *sent timestamp* as the topic_id (Signal's only
#      stable message identifier) and link=null.
#
# Usage:
#   ./autothread-signal.sh <group_id> <timestamp> <sender> [title] [text]
#
# Args:
#   group_id  (required) — Signal group ID (starts with "group." or is
#                          a base64 group id)
#   timestamp (required) — timestamp of the original message (digits);
#                          used for reference only, messages cannot be
#                          quoted programmatically without signal-cli
#                          JSON-RPC receive state.
#   sender    (required) — display name of the original sender
#   title     (optional) — pseudo-topic title (fallback auto-generated)
#   text      (optional) — message body (everything after "/topic")
#
# Prerequisites:
#   - signal-cli installed and a registered account configured in the
#     OpenClaw config (.channels.signal.account).
#
# Output: JSON — {"topic_id": "<timestamp>", "title": "<title>", "link": null}
# Exit codes: 0 = success, 1 = error (details on stderr)

set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/common.sh
source "$SCRIPT_DIR/lib/common.sh"

autothread_require signal-cli jq
autothread_config_path >/dev/null

# ── config ──────────────────────────────────────────────────────────
SIGNAL_ACCOUNT=$(autothread_config_get '.channels.signal.account // empty')

# ── arguments ───────────────────────────────────────────────────────
GROUP_ID="${1:-}"
TIMESTAMP="${2:-}"
SENDER="${3:-}"
TITLE_ARG="${4:-}"
RAW_TEXT="${5:-}"

if [ -z "$GROUP_ID" ] || [ -z "$TIMESTAMP" ] || [ -z "$SENDER" ]; then
  echo "Usage: $0 <group_id> <timestamp> <sender> [title] [text]" >&2
  exit 1
fi

if ! printf '%s' "$TIMESTAMP" | grep -qE '^[0-9]+$'; then
  echo "ERROR: timestamp must be a positive integer (Signal epoch ms), got: '$TIMESTAMP'" >&2
  exit 1
fi

MSG=$(autothread_trim "$RAW_TEXT")

# ── determine title ─────────────────────────────────────────────────
if [ -n "$TITLE_ARG" ]; then
  TITLE="$TITLE_ARG"
else
  TITLE=$(autothread_fallback_title "$MSG")
fi
# Signal caps outgoing messages well above 128 chars, but keep titles
# short and consistent with the other adapters.
TITLE=$(printf '%s' "$TITLE" | cut -c1-128)

# ── compose the pseudo-topic digest ─────────────────────────────────
# Multi-line message body sent via signal-cli. There is no quote API,
# so the digest restates the content with attribution.
BODY="📌 ${TITLE}
────────────────
${MSG}
────────────────
— ${SENDER} (via /topic)"

# ── send to the group ───────────────────────────────────────────────
SEND_OUTPUT=$(signal-cli -u "$SIGNAL_ACCOUNT" send -g "$GROUP_ID" -m "$BODY" 2>&1)
SEND_STATUS=$?

if [ "$SEND_STATUS" -ne 0 ]; then
  echo "ERROR: signal-cli send failed: ${SEND_OUTPUT}" >&2
  exit 1
fi

# signal-cli prints the sent timestamp(s) on stdout. If we got one, use
# it as the topic id; otherwise fall back to the original timestamp.
SENT_TS=$(printf '%s' "$SEND_OUTPUT" | grep -oE '^[0-9]{13,}$' | tail -1)
TOPIC_ID="${SENT_TS:-$TIMESTAMP}"

# No shareable link concept in Signal
autothread_emit_result "$TOPIC_ID" "$TITLE" ""
