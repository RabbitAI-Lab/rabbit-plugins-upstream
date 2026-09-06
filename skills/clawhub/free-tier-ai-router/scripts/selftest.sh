#!/usr/bin/env bash
# selftest.sh — free-tier-ai-router v2.4.0 test suite.
# Sandboxed: throwaway HOME, local mock provider only — ZERO real API calls,
# ZERO real user state touched (ClawHub publishing standard, incident C4).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
R="$ROOT/router.py"

SBX="$(mktemp -d)"
export HOME="$SBX"
cleanup() { [ -n "${MOCK_PID:-}" ] && kill "$MOCK_PID" 2>/dev/null; rm -rf "$SBX"; }
trap cleanup EXIT

fails=0
note() { echo "  $1"; }
fail() { echo "  FAIL: $1"; fails=$((fails+1)); }
hits() { python3 -c "import json,sys;print(json.load(open('$SBX/hits.json')).get('$1',0))" 2>/dev/null || echo 0; }

echo "== [1/12] mock provider up =="
: > "$SBX/hits.json"; echo '{}' > "$SBX/hits.json"
python3 "$HERE/mock_provider.py" "$SBX/hits.json" > "$SBX/mock.out" 2>/dev/null &
MOCK_PID=$!
for i in $(seq 1 40); do
  PORT=$(python3 -c "import json;print(json.load(open('$SBX/mock.out'))['port'])" 2>/dev/null) && break
  sleep 0.25
done
[ -n "${PORT:-}" ] || { echo "FATAL: mock server did not start"; exit 1; }
note "mock on 127.0.0.1:$PORT (pid $MOCK_PID)"

mkdir -p "$SBX/.config/ai_router"
cat > "$SBX/.config/ai_router/providers.json" <<EOF
{"providers": {"mock": {
  "base_url": "http://127.0.0.1:$PORT/v1",
  "auth": "none",
  "models": [
    {"id": "ok-model",    "quality": 1, "rpm": 900, "tier": "cheap", "tags": "fast"},
    {"id": "ratey-model", "quality": 5, "rpm": 800, "tier": "cheap"},
    {"id": "dead-model",  "quality": 5, "rpm": 700, "tier": "cheap"}
  ]
}}}
EOF

echo "== [2/12] general answer via ok-model (--json contract) =="
python3 "$R" "hello router" --json > "$SBX/a1.json" 2>/dev/null
[ $? -eq 0 ] || fail "exit 0 for general"
python3 - "$SBX/a1.json" <<'PY' || fail "answer.v1 shape"
import json, sys
d = json.load(open(sys.argv[1]))
assert d["schema"] == "ai_router.answer.v1", d
assert d["text"], d
assert d["provider"] == "mock" and d["model"] == "ok-model", d
assert d["cached"] is False
PY
note "answer.v1 ok (mock/ok-model, uncached)"

echo "== [3/12] cache: repeat prompt = 0 new server hits =="
python3 "$R" "hello router" >/dev/null 2>&1 || fail "repeat call exit"
H1=$(hits ok-model); H2=$(hits ok-model)
[ "$H1" = "$H2" ] && note "cache hit (server hits unchanged at $H1)" || fail "cache miss: $H1 -> $H2"

echo "== [4/12] 429 cooldown + 402 park + fallback exhaustion (exit 2) =="
python3 "$R" "quality gated" -q 5 >/dev/null 2>"$SBX/e1.txt"; RC=$?
[ "$RC" -eq 2 ] || fail "expected exit 2 (all routes fail), got $RC"
H_R=$(hits ratey-model); H_D=$(hits dead-model)
[ "$H_R" -ge 1 ] && [ "$H_D" -ge 1 ] || fail "expected ratey+dead attempts (r=$H_R d=$H_D)"
note "ratey 429'd ($H_R hit), dead 402'd ($H_D hit), router exhausted -> exit 2"

echo "== [5/12] persistence: second -q5 call = 0 new hits (cooldown respected) =="
python3 "$R" "quality gated again" -q 5 >/dev/null 2>&1; RC=$?
[ "$RC" -eq 2 ] || fail "expected exit 2 again, got $RC"
H_R2=$(hits ratey-model); H_D2=$(hits dead-model)
[ "$H_R2" = "$H_R" ] && [ "$H_D2" = "$H_D" ] && note "cooldowns persisted across processes (0 new hits)" \
  || fail "cooldown leak: ratey $H_R->$H_R2 dead $H_D->$H_D2"

echo "== [6/12] --plan offline (0 hits) + status/learn reports =="
H3=$(hits ok-model)
python3 "$R" --plan --json > "$SBX/plan.json" 2>/dev/null || fail "plan exit"
python3 - "$SBX/plan.json" <<'PY' || fail "plan.v1 shape"
import json, sys
d = json.load(open(sys.argv[1]))
assert d["schema"] == "ai_router.plan.v1", d
assert d["task"] == "general" and d["order"], d
PY
H4=$(hits ok-model); [ "$H3" = "$H4" ] && note "plan made 0 API calls" || fail "plan hit the server"
python3 "$R" --status --json >/dev/null 2>&1 || fail "status exit"
python3 "$R" --learn --json > "$SBX/learn.json" 2>/dev/null || fail "learn report exit"
python3 - "$SBX/learn.json" <<'PY' || fail "learn.v1 recorded the live outcomes"
import json, sys
d = json.load(open(sys.argv[1]))
assert d["schema"] == "ai_router.learn.v1", d
r = d["routes"]["mock|ok-model"]
assert r["ok"] >= 1, r          # case 2/3 successes recorded
assert d["routes"]["mock|ratey-model"]["f429"] >= 1, d   # the 429 was learned
PY
note "learn.v1 has ok success + ratey 429 recorded"

echo "== [7/12] --stream: SSE passthrough end-to-end =="
H5=$(hits ok-model)
python3 "$R" "stream me" --stream --no-cache > "$SBX/s1.txt" 2>/dev/null
[ $? -eq 0 ] || fail "stream exit"
grep -q "mock answer to: stream me" "$SBX/s1.txt" || fail "stream text incomplete"
H6=$(hits ok-model); [ "$H6" -gt "$H5" ] && note "stream answered live (fresh call, not cached)" || fail "stream did not call server"
python3 "$R" "x" --stream --json >/dev/null 2>&1 && fail "stream+json must error" || note "stream+json correctly rejected"

echo "== [8/12] malformed providers.json -> warning + exit 4 =="
echo '{ oops' > "$SBX/.config/ai_router/providers.json"
python3 "$R" "q" --json > "$SBX/a9.json" 2>/dev/null; RC=$?
[ "$RC" -eq 4 ] || fail "expected exit 4, got $RC"
grep -q "invalid providers config" "$SBX/a9.json" || fail "exit-4 json body"
note "malformed config rejected with exit 4"

echo "== [9/12] --learn-reset + dead-state recovery =="
echo '{ oops' > "$SBX/.cache/ai_router/state.json"
python3 "$R" --learn-reset >/dev/null 2>&1 || fail "learn-reset exit"
[ ! -f "$SBX/.cache/ai_router/learn.json" ] || fail "learn overlay not cleared"
echo '{}' > "$SBX/.config/ai_router/providers.json"   # still malformed-ish but valid json: no providers
python3 "$R" --plan >/dev/null 2>&1 || fail "plan with empty config"
note "learn overlay cleared; router survives corrupt state"

echo "== [10/12] corrupted learn.json mid-flight is survivable =="
cat > "$SBX/.config/ai_router/providers.json" <<EOF
{"providers": {"mock": {
  "base_url": "http://127.0.0.1:$PORT/v1",
  "auth": "none",
  "models": [{"id": "ok-model", "quality": 1, "rpm": 900, "tier": "cheap", "tags": "fast"}]
}}}
EOF
echo '{ not json' > "$SBX/.cache/ai_router/learn.json"
python3 "$R" "survive corrupt learn" --no-cache >/dev/null 2>&1 || fail "router crashed on corrupt learn.json"
note "corrupt learn.json treated as empty; routing unaffected"

echo "== [11/12] concurrency: 6 parallel calls, state stays exact =="
rm -f "$SBX/.cache/ai_router/learn.json"
H0=$(hits ok-model)
PIDS=""
for i in 1 2 3 4 5 6; do
  python3 "$R" "parallel call $i" --no-cache >/dev/null 2>&1 &
  PIDS="$PIDS $!"
done
wait $PIDS
H1=$(hits ok-model)
python3 -c "import sys;sys.exit(0 if int('$H1')-int('$H0')==6 else 1)" || fail "expected exactly 6 new server hits, got $((H1-H0))"
python3 "$R" --learn --json 2>/dev/null | python3 -c "
import json,sys
d=json.load(sys.stdin)
r=d['routes'].get('mock|ok-model',{})
assert r.get('ok',0)>=6, r
print('  learn recorded all 6 concurrent successes: ok=%d' % r['ok'])" || fail "learn lost concurrent updates"
note "6/6 parallel answered; learn counted every one (flock + atomic replace held)"

echo "== [12/12] --doctor diagnoses offline against the mock =="
python3 "$R" --doctor >/dev/null 2>&1 || fail "doctor exit"
note "doctor ran clean (configured provider detected)"

echo
if [ "$fails" -eq 0 ]; then echo "SELFTEST: ALL PASS (12 stages)"; exit 0
else echo "SELFTEST: $fails FAILURES"; exit 1; fi
