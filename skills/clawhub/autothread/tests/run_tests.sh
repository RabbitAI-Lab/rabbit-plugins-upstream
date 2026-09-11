#!/bin/bash
# run_tests.sh — offline end-to-end tests for the autothread adapters.
#
# Spins up a local mock API server, points the adapters at it via
# AUTOTHREAD_API_BASE, and asserts on their JSON output and the exact
# requests they made. No network access and no real credentials needed.

set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$HERE")"
PORT="${TEST_PORT:-8977}"
BASE="http://127.0.0.1:${PORT}"
MOCK_LOG="/tmp/autothread_mock_requests.log"
FAKE_CONFIG="/tmp/autothread_fake_openclaw.json"

PASS=0
FAIL=0

# ── fake OpenClaw config ─────────────────────────────────────────────
cat > "$FAKE_CONFIG" <<'EOF'
{
  "channels": {
    "telegram": { "botToken": "TEST_TELEGRAM_TOKEN" },
    "nicegram": { "botToken": "TEST_NICEGRAM_TOKEN" },
    "discord":  { "token": "TEST_DISCORD_TOKEN" },
    "signal":   { "account": "+15550001111" }
  }
}
EOF
export OPENCLAW_CONFIG="$FAKE_CONFIG"

# ── helpers ──────────────────────────────────────────────────────────
check() { # check <name> <expected> <actual>
  if [ "$2" = "$3" ]; then
    PASS=$((PASS + 1))
    echo "PASS: $1"
  else
    FAIL=$((FAIL + 1))
    echo "FAIL: $1"
    echo "  expected: $2"
    echo "  actual:   $3"
  fi
}

start_mock() {
  rm -f "$MOCK_LOG"
  python3 "$HERE/mock_server.py" "$PORT" "$MOCK_LOG" &
  MOCK_PID=$!
  for _ in $(seq 1 30); do
    curl -s "$BASE/ping" >/dev/null 2>&1 && return 0
    sleep 0.2
  done
  echo "ERROR: mock server did not start" >&2
  exit 1
}

stop_mock() { kill "$MOCK_PID" 2>/dev/null; wait "$MOCK_PID" 2>/dev/null; }

# ── tests ────────────────────────────────────────────────────────────
start_mock

# 1. Telegram: text mode
OUT=$(AUTOTHREAD_API_BASE="$BASE" "$ROOT/scripts/autothread-telegram.sh" \
  -1001234 42 "Alice" "Passport Renewal Before March" \
  "I need to look into renewing my passport before March")
check "telegram text: topic_id"      "777" "$(echo "$OUT" | jq -r .topic_id)"
check "telegram text: title"         "Passport Renewal Before March" "$(echo "$OUT" | jq -r .title)"
check "telegram text: link"          "https://t.me/c/1234/777" "$(echo "$OUT" | jq -r .link)"
CREATE=$(grep createForumTopic "$MOCK_LOG" | tail -1)
check "telegram text: create name"   "Passport Renewal Before March" \
  "$(echo "$CREATE" | jq -r '.body.name')"
SENDMSG=$(grep sendMessage "$MOCK_LOG" | tail -1)
check "telegram text: thread id"     "777" "$(echo "$SENDMSG" | jq -r '.body.message_thread_id')"
check "telegram text: quote sender"  "true" "$(echo "$SENDMSG" | jq -r '.body | .text | contains("Alice")')"

# 2. Telegram: media mode (empty text -> forwardMessage)
> "$MOCK_LOG"
OUT=$(AUTOTHREAD_API_BASE="$BASE" "$ROOT/scripts/autothread-telegram.sh" \
  -1001234 42 "Bob" "" "")
check "telegram media: fallback title" "New Topic" "$(echo "$OUT" | jq -r .title)"
FWD=$(grep forwardMessage "$MOCK_LOG" | tail -1)
check "telegram media: forwarded"    "42" "$(echo "$FWD" | jq -r '.body.message_id')"

# 3. Nicegram: delegates with its own token
> "$MOCK_LOG"
OUT=$(AUTOTHREAD_API_BASE="$BASE" "$ROOT/scripts/autothread-nicegram.sh" \
  -1001234 42 "Alice" "Nicegram Topic" "hello from nicegram")
check "nicegram: topic_id"           "777" "$(echo "$OUT" | jq -r .topic_id)"
AUTH=$(grep createForumTopic "$MOCK_LOG" | tail -1)
check "nicegram: uses nicegram token" "true" "$(echo "$AUTH" | jq '.path | contains("TEST_NICEGRAM_TOKEN")')"

# 4. Discord: thread from message
> "$MOCK_LOG"
OUT=$(AUTOTHREAD_API_BASE="$BASE" "$ROOT/scripts/autothread-discord.sh" \
  111 42 "Carol" "Deploy Checklist" "list of things to deploy tomorrow")
check "discord: thread id"           "555" "$(echo "$OUT" | jq -r .topic_id)"
check "discord: title"               "Deploy Checklist" "$(echo "$OUT" | jq -r .title)"
check "discord: link"                "https://discord.com/channels/999/555" "$(echo "$OUT" | jq -r .link)"
THREAD_CALL=$(grep "threads" "$MOCK_LOG" | tail -1)
check "discord: thread name"         "Deploy Checklist" "$(echo "$THREAD_CALL" | jq -r '.body.name')"
DMSG=$(grep "/channels/555/messages" "$MOCK_LOG" | tail -1)
check "discord: quote sender"        "true" "$(echo "$DMSG" | jq '.body.content | contains("Carol")')"
# guild_id appears only in the response, not the request log — the link
# assertion above already proves the resolve+thread-creation flow works.
# Assert the channel-resolve GET happened:
check "discord: channel resolved"    "0" "$(grep -cE '"/channels/111"' "$MOCK_LOG" | grep -v '^0$' >/dev/null; echo $?)"

# 5. Title fallback edge cases via common.sh
# shellcheck source=../scripts/lib/common.sh
source "$ROOT/scripts/lib/common.sh"
check "fallback: 50-char cut"  "I need to look into renewing my passport before…" \
  "$(autothread_fallback_title 'I need to look into renewing my passport before March and book an appointment')"
check "fallback: empty"        "New Topic" "$(autothread_fallback_title '')"
check "fallback: custom max"   "Short and snappy.…" "$(autothread_fallback_title 'Short and snappy. Extra detail' 20)"

stop_mock

echo "────────────────────"
echo "PASSED: $PASS  FAILED: $FAIL"
[ "$FAIL" -eq 0 ]
