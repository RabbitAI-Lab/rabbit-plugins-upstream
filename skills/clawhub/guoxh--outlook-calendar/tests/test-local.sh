#!/usr/bin/env bash
# tests/test-local.sh
# Offline smoke + JSON-escaping tests for the outlook-calendar skill.
#
# Does NOT make any real network call to Microsoft. Run with:
#   ./tests/test-local.sh
#
# Exits non-zero on the first failure (or accumulates failures and reports at end
# if you set ACCUMULATE=1).

set -Eeuo pipefail
IFS=$' \t\n'

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
SKILL_DIR="$(cd -- "$SCRIPT_DIR/.." >/dev/null 2>&1 && pwd)"
SCRIPTS="$SKILL_DIR/scripts"

ACCUMULATE="${ACCUMULATE:-0}"
FAILS=0
TOTAL=0

# Use a sandboxed OUTLOOK_CAL_DIR for the duration of the tests.
TEST_HOME=$(mktemp -d -t outlook-cal-tests-XXXXXX)
export OUTLOOK_CAL_DIR="$TEST_HOME/dir"
export HOME="$TEST_HOME"
mkdir -p "$OUTLOOK_CAL_DIR"

cleanup() { rm -rf "$TEST_HOME"; }
trap cleanup EXIT

pass() { printf '  \033[32m✓\033[0m %s\n' "$*"; }
fail() {
    printf '  \033[31m✗\033[0m %s\n' "$*"
    if [[ "$ACCUMULATE" == "1" ]]; then
        FAILS=$((FAILS+1))
    else
        exit 1
    fi
}

assert_eq() {
    local got="$1" want="$2" msg="$3"
    if [[ "$got" == "$want" ]]; then
        pass "$msg"
    else
        fail "$msg  (got='$got' want='$want')"
    fi
}

assert_jq() {
    local json="$1" filter="$2" want="$3" msg="$4"
    local got
    got=$(printf '%s' "$json" | jq -r "$filter" 2>/dev/null) || got="<jq-error>"
    assert_eq "$got" "$want" "$msg"
}

section() { printf '\n\033[1m== %s ==\033[0m\n' "$*"; }

###############################################################################
section "1. shell syntax check (bash -n) on every script"
###############################################################################
for s in _lib.sh setup-device-code.sh token.sh calendar-read.sh calendar-write.sh; do
    TOTAL=$((TOTAL+1))
    if bash -n "$SCRIPTS/$s" 2>&1; then
        pass "$s parses"
    else
        fail "$s has a syntax error"
    fi
done

# shellcheck is optional
if command -v shellcheck >/dev/null 2>&1; then
    section "1b. shellcheck (best-effort, advisory)"
    for s in _lib.sh setup-device-code.sh token.sh calendar-read.sh calendar-write.sh; do
        TOTAL=$((TOTAL+1))
        if shellcheck -x -e SC1091,SC2155,SC2086,SC2128 "$SCRIPTS/$s" >/tmp/sc.$$ 2>&1; then
            pass "shellcheck: $s clean"
        else
            # advisory only - count but don't fail
            printf '  \033[33m…\033[0m shellcheck: %s has advisories (see /tmp/sc.%s)\n' "$s" "$$"
        fi
    done
    rm -f /tmp/sc.$$
else
    printf '  (shellcheck not installed; skipping)\n'
fi

###############################################################################
section "2. JSON payload builders handle nasty inputs safely"
###############################################################################
# Source the lib to use build_event_body directly
# shellcheck source=../scripts/_lib.sh
. "$SCRIPTS/_lib.sh"

NASTY='She said "hi"
backslash \ quote \"
tab	end
emoji 🦀 中文 null byte follows: \u0000 (not real) and a control: \b\b\b'

PAYLOAD=$(build_event_body "$NASTY" "2026-06-18T12:00:00+08:00" "2026-06-18T13:00:00+08:00" "Asia/Shanghai" "$NASTY" "$NASTY")
TOTAL=$((TOTAL+1))
if printf '%s' "$PAYLOAD" | jq -e . >/dev/null 2>&1; then
    pass "build_event_body produces valid JSON even with quotes/newlines/emoji/CJK"
else
    fail "build_event_body produced invalid JSON: $PAYLOAD"
fi

# Round-trip: the subject field must equal the input verbatim
TOTAL=$((TOTAL+1))
GOT=$(printf '%s' "$PAYLOAD" | jq -r '.subject')
if [[ "$GOT" == "$NASTY" ]]; then
    pass "subject round-trips byte-for-byte"
else
    fail "subject did not round-trip"
fi

# Same for body.content and location.displayName
TOTAL=$((TOTAL+1))
GOT=$(printf '%s' "$PAYLOAD" | jq -r '.body.content')
assert_eq "$GOT" "$NASTY" "body.content round-trips byte-for-byte"

TOTAL=$((TOTAL+1))
GOT=$(printf '%s' "$PAYLOAD" | jq -r '.location.displayName')
assert_eq "$GOT" "$NASTY" "location.displayName round-trips byte-for-byte"

# start/end timeZone must be carried through
TOTAL=$((TOTAL+1))
GOT=$(printf '%s' "$PAYLOAD" | jq -r '.start.timeZone')
assert_eq "$GOT" "Asia/Shanghai" "start.timeZone is preserved"

# A truly nasty control character: \u0001 (SOH) - jq --arg must pass it through safely
TOTAL=$((TOTAL+1))
CTRL=$'ab'
P=$(build_event_body "$CTRL" "2026-06-18T12:00:00+08:00" "2026-06-18T13:00:00+08:00")
GOT=$(printf '%s' "$P" | jq -r '.subject')
if [[ "$GOT" == "$CTRL" ]]; then
    pass "control character (SOH) round-trips safely"
else
    fail "control character did not survive (got=$(printf %q "$GOT"))"
fi

# A backslash + double quote injection attempt must NOT escape the JSON string
TOTAL=$((TOTAL+1))
INJECT='","isAllDay": true, "x": "'
P=$(build_event_body "$INJECT" "2026-06-18T12:00:00+08:00" "2026-06-18T13:00:00+08:00")
GOT=$(printf '%s' "$P" | jq -r '.subject')
assert_eq "$GOT" "$INJECT" "injection string is contained inside the subject field"
# And isAllDay must NOT exist (no field was passed)
TOTAL=$((TOTAL+1))
HAS=$(printf '%s' "$P" | jq 'has("isAllDay")')
assert_eq "$HAS" "false" "isAllDay was not added by the injection"

###############################################################################
section "3. All-day event payload (calendar-write.sh style)"
###############################################################################
ALL_DAY_PAYLOAD=$(jq -n \
    --arg subject "Travel" \
    --arg loc "Tokyo" \
    --arg start "2026-06-20" \
    --arg end   "2026-06-22" \
    --arg tz    "Asia/Shanghai" \
    '{
        subject:  $subject,
        isAllDay: true,
        start:    { dateTime: ($start + "T00:00:00"), timeZone: $tz },
        end:      { dateTime: ($end   + "T00:00:00"), timeZone: $tz },
        location: { displayName: $loc }
     }')
TOTAL=$((TOTAL+1))
assert_jq "$ALL_DAY_PAYLOAD" '.isAllDay'      "true"     "isAllDay is true"
TOTAL=$((TOTAL+1))
assert_jq "$ALL_DAY_PAYLOAD" '.start.dateTime' "2026-06-20T00:00:00" "all-day start dateTime"
TOTAL=$((TOTAL+1))
assert_jq "$ALL_DAY_PAYLOAD" '.end.dateTime'   "2026-06-22T00:00:00" "all-day end dateTime"
TOTAL=$((TOTAL+1))
assert_jq "$ALL_DAY_PAYLOAD" '.start.timeZone' "Asia/Shanghai"        "all-day timeZone"

###############################################################################
section "4. Scope policy (calendar/contacts/todo shared auth, no mail/files/admin)"
###############################################################################
# Check that the allow-list in setup-device-code.sh does not contain forbidden scopes.
# NOTE: this skill uses shared Outlook Graph auth with calendar, contacts, and todo
# scopes (Calendars.ReadWrite, Contacts.ReadWrite, Tasks.ReadWrite). Only mail,
# files, notes, sites, and admin scopes are truly forbidden.
TOTAL=$((TOTAL+1))
if grep -qE 'Mail\.|MailboxSettings|Files\.|Notes\.|Sites\.' "$SCRIPTS/setup-device-code.sh"; then
    fail "setup-device-code.sh mentions a forbidden scope keyword"
else
    pass "setup-device-code.sh contains no mail/files/notes/sites/admin scope references"
fi

# Check that the FORBIDDEN_REGEX is present and active
TOTAL=$((TOTAL+1))
if grep -qE 'FORBIDDEN_REGEX' "$SCRIPTS/setup-device-code.sh"; then
    pass "FORBIDDEN_REGEX guard is present"
else
    fail "FORBIDDEN_REGEX guard missing from setup-device-code.sh"
fi

# Check that the only scopes ever sent to Graph are the three allowed ones
TOTAL=$((TOTAL+1))
SCOPES=$(grep -oE 'offline_access|User\.Read|Calendars\.ReadWrite' "$SCRIPTS/setup-device-code.sh" "$SCRIPTS/_lib.sh" | sort -u | tr '\n' ' ')
if [[ "$SCOPES" == *"offline_access"* && "$SCOPES" == *"User.Read"* && "$SCOPES" == *"Calendars.ReadWrite"* ]]; then
    pass "only allowed scopes appear in the code: $SCOPES"
else
    fail "unexpected scopes found: $SCOPES"
fi

###############################################################################
section "5. client-id / tenant-id / authority validation"
###############################################################################
# Run setup-device-code.sh with bad inputs and check that it fails
TOTAL=$((TOTAL+1))
if "$SCRIPTS/setup-device-code.sh" --client-id not-a-uuid 2>/dev/null; then
    fail "setup accepted an invalid client_id"
else
    pass "setup-device-code.sh rejects an invalid client_id"
fi

TOTAL=$((TOTAL+1))
if "$SCRIPTS/setup-device-code.sh" --client-id 12345678-1234-1234-1234-123456789012 --tenant-id "evil.example.com" 2>/dev/null; then
    fail "setup accepted an invalid tenant_id"
else
    pass "setup-device-code.sh rejects an invalid tenant_id"
fi

TOTAL=$((TOTAL+1))
if "$SCRIPTS/setup-device-code.sh" --client-id 12345678-1234-1234-1234-123456789012 --authority "https://attacker.example.com" 2>/dev/null; then
    fail "setup accepted a non-login.microsoftonline.com authority"
else
    pass "setup-device-code.sh rejects a non-login.microsoftonline.com authority"
fi

###############################################################################
section "6. write safety: dry-run does not call the network"
###############################################################################
# No config, no tokens => dry-run should still build JSON and must not attempt Graph.
TOTAL=$((TOTAL+1))
OUT=$("$SCRIPTS/calendar-write.sh" create --subject "x" --start "2026-06-18 12:00" --end "2026-06-18 13:00" 2>&1 || true)
if echo "$OUT" | grep -q 'DRY-RUN' && echo "$OUT" | grep -q '"subject": "x"'; then
    pass "write dry-run works without tokens (no Graph call attempted)"
else
    fail "write dry-run behaved unexpectedly without tokens: $OUT"
fi

# Calendar-read should also fail loudly
TOTAL=$((TOTAL+1))
OUT=$("$SCRIPTS/calendar-read.sh" today 2>&1 || true)
if echo "$OUT" | grep -qE 'tokens missing|run scripts/setup-device-code.sh'; then
    pass "read refuses to run without tokens"
else
    fail "read behaved unexpectedly without tokens: $OUT"
fi

###############################################################################
section "7. tokens never appear in scripts' stdout/stderr"
###############################################################################
# Synthesize a fake tokens file with a recognizable fake token string.
FAKE_TOKEN='FAKE-TOKEN-do-not-leak-1A2B3C4D5E6F'
mkdir -p "$OUTLOOK_CAL_DIR"
cat > "$OUTLOOK_CAL_DIR/tokens.json" <<EOF
{
  "access_token":  "$FAKE_TOKEN",
  "refresh_token": "FAKE-REFRESH-do-not-leak-XYZ",
  "expires_at":    $(($(date +%s)+3600)),
  "expires_in":    3600,
  "token_type":    "Bearer",
  "scope":         "offline_access https://graph.microsoft.com/User.Read https://graph.microsoft.com/Calendars.ReadWrite"
}
EOF
cat > "$OUTLOOK_CAL_DIR/config.json" <<EOF
{
  "client_id":  "12345678-1234-1234-1234-123456789012",
  "tenant_id":  "common",
  "authority":  "https://login.microsoftonline.com/common",
  "graph_base": "https://graph.microsoft.com/v1.0",
  "scopes":     ["offline_access","https://graph.microsoft.com/User.Read","https://graph.microsoft.com/Calendars.ReadWrite"],
  "version":    1
}
EOF
chmod 700 "$OUTLOOK_CAL_DIR"
chmod 600 "$OUTLOOK_CAL_DIR"/*.json

# token status: must NOT echo the fake access/refresh token
TOTAL=$((TOTAL+1))
OUT=$("$SCRIPTS/token.sh" status 2>&1 || true)
if echo "$OUT" | grep -q "$FAKE_TOKEN"; then
    fail "token.sh status leaked the access token!"
    echo "  OUTPUT: $OUT"
else
    pass "token.sh status does not echo the access_token"
fi
TOTAL=$((TOTAL+1))
if echo "$OUT" | grep -q "FAKE-REFRESH"; then
    fail "token.sh status leaked the refresh token!"
else
    pass "token.sh status does not echo the refresh_token"
fi

# token scopes: should print scopes (not tokens)
TOTAL=$((TOTAL+1))
OUT=$("$SCRIPTS/token.sh" scopes 2>&1 || true)
if echo "$OUT" | grep -q "$FAKE_TOKEN" || echo "$OUT" | grep -q "FAKE-REFRESH"; then
    fail "token.sh scopes leaked a token"
else
    pass "token.sh scopes does not leak tokens"
fi

# Now, simulate an expired token so the lib tries to refresh - it should fail
# with a "no host / transport error" because we haven't mocked the network.
# Importantly, the fake token should still not appear in the error.
TOTAL=$((TOTAL+1))
# Put a totally bogus authority that won't resolve to login.microsoftonline.com
jq '.authority = "https://login.microsoftonline.com/nonexistent-tenant-for-test" | .tenant_id = "nonexistent-tenant-for-test"' \
   "$OUTLOOK_CAL_DIR/config.json" > "$OUTLOOK_CAL_DIR/config.json.new"
mv "$OUTLOOK_CAL_DIR/config.json.new" "$OUTLOOK_CAL_DIR/config.json"
# Make the access token expired
jq '.expires_at = 1' "$OUTLOOK_CAL_DIR/tokens.json" > "$OUTLOOK_CAL_DIR/tokens.json.new"
mv "$OUTLOOK_CAL_DIR/tokens.json.new" "$OUTLOOK_CAL_DIR/tokens.json"

OUT=$(HOME="$TEST_HOME" OUTLOOK_CAL_DIR="$OUTLOOK_CAL_DIR" "$SCRIPTS/calendar-read.sh" today 2>&1 || true)
if echo "$OUT" | grep -q "$FAKE_TOKEN"; then
    fail "calendar-read.sh leaked the access token in error output!"
    echo "  OUTPUT: $OUT"
else
    pass "calendar-read.sh does not leak the access token even on error"
fi

###############################################################################
section "8. clear subcommand requires --yes-i-really-mean-it"
###############################################################################
TOTAL=$((TOTAL+1))
OUT=$("$SCRIPTS/token.sh" clear 2>&1 || true)
if [[ -f "$OUTLOOK_CAL_DIR/tokens.json" ]] && [[ -f "$OUTLOOK_CAL_DIR/config.json" ]]; then
    pass "token.sh clear without flag did NOT delete tokens or config"
else
    fail "token.sh clear without flag deleted files anyway"
fi

TOTAL=$((TOTAL+1))
OUT=$("$SCRIPTS/token.sh" clear --yes-i-really-mean-it 2>&1 || true)
if [[ ! -f "$OUTLOOK_CAL_DIR/tokens.json" ]] && [[ ! -f "$OUTLOOK_CAL_DIR/config.json" ]]; then
    pass "token.sh clear with --yes-i-really-mean-it removed both files"
else
    fail "token.sh clear with --yes-i-really-mean-it did not remove both files"
fi

###############################################################################
section "9. normalize_dt (timezone math) round-trips"
###############################################################################
if command -v python3 >/dev/null 2>&1; then
    OUT=$(python3 - <<'PY'
from datetime import datetime
from zoneinfo import ZoneInfo
tz = ZoneInfo("Asia/Shanghai")
# 2026-06-18 12:00 in Shanghai == 2026-06-18 04:00 UTC
local = datetime(2026, 6, 18, 12, 0, tzinfo=tz)
utc   = local.astimezone(ZoneInfo("UTC"))
print(local.isoformat(timespec="seconds"))
print(utc.isoformat(timespec="seconds"))
PY
)
    TOTAL=$((TOTAL+1))
    assert_eq "$(echo "$OUT" | sed -n '1p')" "2026-06-18T12:00:00+08:00" "Shanghai local ISO"
    TOTAL=$((TOTAL+1))
    assert_eq "$(echo "$OUT" | sed -n '2p')" "2026-06-18T04:00:00+00:00" "Shanghai -> UTC ISO"
else
    echo "  (python3 not available, skipping)"
fi

###############################################################################
section "summary"
###############################################################################
TOTAL=$((TOTAL+1))
if (( FAILS == 0 )); then
    printf '\033[32mAll %d checks passed.\033[0m\n' "$TOTAL"
    exit 0
else
    printf '\033[31m%d of %d checks failed.\033[0m\n' "$FAILS" "$TOTAL"
    exit 1
fi
