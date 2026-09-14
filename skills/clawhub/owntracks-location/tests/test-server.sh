#!/usr/bin/env bash
# Focused tests for the OwnTracks receiver: loopback default, auth on every data
# endpoint, retention/cap, and the purge off-switch. Uses a throwaway data dir and
# an env-supplied token, so no keychain entry and no real trail are touched.
set -uo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
SERVER="$SRC/scripts/server.mjs"
D=$(mktemp -d /tmp/ot-test.XXXXXX)
PORT=${OT_TEST_PORT:-18899}
TOKEN="test-token-$RANDOM$RANDOM"
pass=0; fail=0
ok(){ printf '  \033[32mPASS\033[0m %s\n' "$1"; pass=$((pass+1)); }
no(){ printf '  \033[31mFAIL\033[0m %s\n       %s\n' "$1" "$2"; fail=$((fail+1)); }
code(){ curl -s -o /dev/null -w '%{http_code}' "$@"; }

echo "== refuses to start with no token =="
out=$(OWNTRACKS_DATA="$D" OWNTRACKS_SECRET="" node "$SERVER" 2>&1); rc=$?
if [[ $rc -ne 0 && "$out" == *"No token configured"* ]]; then ok "no token => refuses to start"; else no "no token => refuses to start" "rc=$rc $out"; fi

echo "== starts with a token, on loopback by default =="
OWNTRACKS_DATA="$D" OWNTRACKS_SECRET="$TOKEN" OWNTRACKS_PORT=$PORT \
  OWNTRACKS_RETENTION_DAYS=1 OWNTRACKS_MAX_POINTS=3 node "$SERVER" >"$D/log" 2>&1 &
SRV=$!
for _ in $(seq 1 50); do [[ "$(code http://127.0.0.1:$PORT/health)" == 200 ]] && break; sleep 0.1; done
grep -q "listening on http://127.0.0.1:$PORT" "$D/log" && ok "binds 127.0.0.1 by default" || no "binds 127.0.0.1 by default" "$(cat "$D/log")"
grep -q "token required" "$D/log" && ok "startup banner says token required" || no "startup banner" "$(cat "$D/log")"

echo "== auth: /health open, everything with location data closed =="
[[ "$(code http://127.0.0.1:$PORT/health)" == 200 ]] && ok "/health open (no location data)" || no "/health open" "$(code http://127.0.0.1:$PORT/health)"
for ep in latest history; do
  c=$(code "http://127.0.0.1:$PORT/$ep")
  [[ "$c" == 401 ]] && ok "GET /$ep unauthenticated => 401" || no "GET /$ep => 401" "got $c"
done
c=$(code -X POST -H 'content-type: application/json' -d '{"_type":"location","lat":1,"lon":2,"tst":1}' "http://127.0.0.1:$PORT/owntracks")
[[ "$c" == 401 ]] && ok "POST /owntracks unauthenticated => 401 (writes closed too)" || no "POST unauthenticated => 401" "got $c"
c=$(code -H "Authorization: Bearer wrong-token" "http://127.0.0.1:$PORT/latest")
[[ "$c" == 401 ]] && ok "wrong bearer token => 401" || no "wrong token => 401" "got $c"

echo "== authenticated write + read, Bearer and Basic =="
NOW=$(date +%s)
c=$(code -X POST -H "Authorization: Bearer $TOKEN" -H 'content-type: application/json' \
     -d "{\"_type\":\"location\",\"lat\":41.32,\"lon\":1.89,\"acc\":10,\"batt\":80,\"SSID\":\"MyWifi\",\"tst\":$NOW}" \
     "http://127.0.0.1:$PORT/owntracks")
[[ "$c" == 200 ]] && ok "POST with Bearer accepted" || no "POST with Bearer" "got $c"
body=$(curl -s -H "Authorization: Bearer $TOKEN" "http://127.0.0.1:$PORT/latest")
[[ "$body" == *'"lat": 41.32'* ]] && ok "GET /latest with Bearer returns the fix" || no "GET /latest with Bearer" "$body"
# OwnTracks phones send HTTP Basic; the token is the PASSWORD.
b64=$(printf 'anyuser:%s' "$TOKEN" | base64 -w0)
c=$(code -H "Authorization: Basic $b64" "http://127.0.0.1:$PORT/latest")
[[ "$c" == 200 ]] && ok "Basic auth accepted (token as password, as OwnTracks sends)" || no "Basic auth" "got $c"

echo "== privacy defaults =="
[[ "$body" != *"MyWifi"* ]] && ok "SSID dropped unless OWNTRACKS_STORE_SSID=1" || no "SSID dropped by default" "$body"
grep -qE '41\.32' "$D/log" && no "coordinates kept out of logs by default" "log has coords" || ok "coordinates kept out of logs by default"

echo "== file modes =="
for f in latest.json history.json; do
  m=$(stat -c '%a' "$D/$f" 2>/dev/null)
  [[ "$m" == "600" ]] && ok "$f is 0600" || no "$f is 0600" "got $m"
done
m=$(stat -c '%a' "$D"); [[ "$m" == "700" ]] && ok "data dir is 0700" || no "data dir is 0700" "got $m"

echo "== retention: MAX_POINTS caps the trail =="
for i in 1 2 3 4 5; do
  curl -s -o /dev/null -X POST -H "Authorization: Bearer $TOKEN" -H 'content-type: application/json' \
    -d "{\"_type\":\"location\",\"lat\":$i,\"lon\":$i,\"tst\":$((NOW+i))}" "http://127.0.0.1:$PORT/owntracks"
done
# The history endpoint emits ONE line, so count OCCURRENCES, not lines — `grep -c`
# here would return 1 no matter how many points were stored and prove nothing.
n=$(curl -s -H "Authorization: Bearer $TOKEN" "http://127.0.0.1:$PORT/history?limit=99" | grep -o '"lat"' | wc -l)
if [[ "$n" -eq 3 ]]; then ok "6 points posted, history capped at OWNTRACKS_MAX_POINTS=3 (got $n)"
else no "MAX_POINTS cap" "expected exactly 3 points, got $n"; fi

echo "== retention: points older than the window are dropped =="
kill $SRV 2>/dev/null; wait $SRV 2>/dev/null
python3 - "$D/history.json" <<'PYEOF'
import json,sys,time
p=sys.argv[1]; h=json.load(open(p))
h.insert(0, {"lat":9.9,"lon":9.9,"tst":int(time.time())-40*86400})
json.dump(h, open(p,"w"))
PYEOF
OWNTRACKS_DATA="$D" OWNTRACKS_SECRET="$TOKEN" OWNTRACKS_PORT=$PORT \
  OWNTRACKS_RETENTION_DAYS=7 OWNTRACKS_MAX_POINTS=500 node "$SERVER" >"$D/log2" 2>&1 &
SRV=$!
for _ in $(seq 1 50); do [[ "$(code http://127.0.0.1:$PORT/health)" == 200 ]] && break; sleep 0.1; done
h=$(curl -s -H "Authorization: Bearer $TOKEN" "http://127.0.0.1:$PORT/history?limit=99")
[[ "$h" != *"9.9"* ]] && ok "40-day-old point pruned by OWNTRACKS_RETENTION_DAYS=7" || no "retention prune" "$h"
kill $SRV 2>/dev/null; wait $SRV 2>/dev/null

echo "== --purge-data erases the trail =="
out=$(OWNTRACKS_DATA="$D" node "$SERVER" --purge-data 2>&1)
if [[ ! -e "$D/latest.json" && ! -e "$D/history.json" ]]; then ok "--purge-data deletes latest.json and history.json"; else no "--purge-data" "$out"; fi
echo "$out" | grep -qi "places" && ok "--purge-data says named places are untouched" || no "--purge-data mentions places" "$out"

echo "== --revoke clears the token and explains the phone side =="
out=$(OWNTRACKS_DATA="$D" OWNTRACKS_SECRET="$TOKEN" node "$SERVER" --revoke 2>&1)
echo "$out" | grep -q "still set in this environment" && ok "--revoke warns OWNTRACKS_SECRET is still in the env" || no "--revoke env warning" "$out"
echo "$out" | grep -qi "phone" && ok "--revoke tells you to clear the phone too" || no "--revoke phone step" "$out"

find "$D" -mindepth 1 -delete 2>/dev/null; rmdir "$D" 2>/dev/null
echo; echo "owntracks-location: $pass passed, $fail failed"
[[ $fail -eq 0 ]]
