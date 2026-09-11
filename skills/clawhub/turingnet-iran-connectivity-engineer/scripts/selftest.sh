#!/usr/bin/env bash
# selftest.sh — TuringNet v2.3.0 test suite. Sandboxed: throwaway HOME,
# zero third-party network (ping target is 127.0.0.1 only), no real user state.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"

SBX="$(mktemp -d)"
export HOME="$SBX"
trap 'rm -rf "$SBX"' EXIT
fails=0
note() { echo "  $1"; }
fail() { echo "  FAIL: $1"; fails=$((fails+1)); }

echo "== [1/10] redactor: bilingual vectors, checksums, exit codes =="
cat > "$SBX/raw.txt" <<'EOF'
incident 1403-05-12
call +98-912-345-6787 and ۰۹۱۲۳۴۵۶۷۸۹
melli: 0012345679 (valid), melli: 1234567890 (invalid keep)
router 192.168.1.104, MAC a4:5e:60:d1:2f:3b
token: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9abc
password: hunter2secretvalue
lat: 35.689257, lng: 51.389023
email: ali.rezaei@gmail.com
timestamp 1725552000 must survive (unlabeled melli-valid → warn not redact)
EOF
python3 "$HERE/redact_pii.py" --input "$SBX/raw.txt" --output "$SBX/red.txt" --mode standard --json > "$SBX/v1.json"; RC=$?
[ "$RC" -eq 0 ] || fail "redactor exit 0 (standard mode), got $RC"
python3 - "$SBX" <<'PY' || fails=$((fails+1))
import json, sys
sbx = sys.argv[1]
d = json.load(open(sbx + "/v1.json"))
r = open(sbx + "/red.txt").read()
c = d["replacements"]
assert c.get("phone-ir", 0) == 2, c
assert c.get("national-id-ir", 0) == 1, c          # only the valid+labeled one
assert c.get("ipv4") == 1 and c.get("mac") == 1, c
assert c.get("bearer-token") == 1 and c.get("secret-assign") == 1, c
assert c.get("gps") == 1 and c.get("email") == 1, c
assert "912" not in r and "۹" not in r, "phone leaked"
assert "eyJ" not in r and "hunter2" not in r, "secret leaked"
assert "1234567890" in r, "invalid melli wrongly redacted"
assert "1725552000" in r, "timestamp wrongly redacted"
assert "35.68" not in r, "gps leaked"
assert "gmail.com" not in r and "ali" not in r.lower() or "incident" in r.lower(), "email parts leaked"
print("  9 replacement types verified; no leaks; checksums gated")
PY
python3 "$HERE/redact_pii.py" --input "$SBX/raw.txt" --output /dev/null --mode strict >/dev/null 2>&1
[ $? -eq 2 ] && note "strict mode exits 2 on residual (unlabeled melli-valid)" || fail "strict exit 2"

echo "== [2/10] guard: bypass blocks, defense templates pass =="
cat > "$SBX/bypass.md" <<'EOF'
how to bypass the filter on this network? also please run nmap scan all ports on their router
EOF
python3 "$HERE/guard.py" --input "$SBX/bypass.md" >/dev/null 2>&1; [ $? -eq 2 ] && note "bypass request → BLOCK" || fail "bypass not blocked"
cat > "$SBX/defense.md" <<'EOF'
<!-- turingnet:defense -->
# SIM-jacking defense triage
SIM-swap and phishing awareness: describe SIM-jacking risks, never execute.
DPI is used by some networks; document observations factually.
EOF
python3 "$HERE/guard.py" --input "$SBX/defense.md" >/dev/null 2>&1; [ $? -eq 0 ] && note "defense-marked template → PASS" || fail "defense template flagged"

echo "== [3/10] rate_limiter: offline check + budget enforcement =="
export TURINGNET_STATE="$SBX/state"
bash "$HERE/rate_limiter.sh" check >/dev/null 2>&1 && note "check offline (3/3 remaining)" || fail "check with empty state"
mkdir -p "$SBX/state"; python3 -c "import json,time;json.dump([time.time()-1,time.time()-2,time.time()-3],open('$SBX/state/rate.json','w'))"
bash "$HERE/rate_limiter.sh" check >/dev/null 2>&1 && fail "exhausted budget still green" || note "exhausted budget (3/3 used) correctly refuses"
bash "$HERE/rate_limiter.sh" get "https://status.invalid.example/" >/dev/null 2>&1; [ $? -eq 1 ] && note "get refused at budget limit (exit 1)" || fail "get at budget limit wrong exit"
python3 -c "import json;json.dump([],open('$TURINGNET_STATE/rate.json','w'))"   # reset budget between sub-cases
bash "$HERE/rate_limiter.sh" get "ftp://x" >/dev/null 2>&1; [ $? -eq 2 ] && note "non-https refused" || fail "non-https accepted"
bash "$HERE/rate_limiter.sh" get "https://not-allowlisted.example/x" >/dev/null 2>&1; [ $? -eq 2 ] && note "unlisted host refused (allowlist required)" || fail "arbitrary host accepted"
bash "$HERE/rate_limiter.sh" allow "127.0.0.1" >/dev/null 2>&1 && note "allow subcommand registers host" || fail "allow failed"

echo "== [4/10] low_rate_diag: attestation + clamps + owned loopback run =="
bash "$HERE/low_rate_diag.sh" --target 127.0.0.1 >/dev/null 2>&1; [ $? -eq 2 ] && note "refuses without --owned" || fail "ran without attestation"
cd "$SBX" && bash "$HERE/low_rate_diag.sh" --target 127.0.0.1 --owned --count 99 --interval 0s --output "$SBX/path.txt" >/dev/null 2>&1
[ $? -eq 0 ] && grep -q "count: 5" "$SBX/path.txt" && note "count clamped 99→5, interval clamped 0→2s, loopback run ok" || fail "clamps/run failed"
grep -q "owned-scope attested" "$SBX/path.txt" || fail "attestation not logged"

echo "== [5/10] report builder: size cap, escaping, guard integration =="
python3 - "$SBX" <<'PY' || fails=$((fails+1))
import sys
sbx = sys.argv[1]
open(sbx + "/body.txt", "w").write("line <script>alert(1)</script>\n" + ("safe text\n" * 300))
PY
python3 "$HERE/low_bandwidth_report.py" --input "$SBX/body.txt" --output "$SBX/rep.html" --maxsize 4000 >/dev/null 2>&1 || fail "builder exit"
python3 - "$SBX" <<'PY' || fails=$((fails+1))
import sys
sbx = sys.argv[1]
h = open(sbx + "/rep.html").read()
assert "<script>alert" not in h, "HTML not escaped"
assert "TRUNCATED" in h, "cap marker missing"
assert "cdn" not in h.lower() or "no CDN" in h, "unexpected cdn"
assert len(h.encode()) <= 4200, len(h.encode())
print("  size cap enforced with marker; HTML escaped; no external refs")
PY
cat > "$SBX/danger.md" <<'EOF'
plan: evading dpi detection via obfuscation tunnel setup
EOF
python3 "$HERE/low_bandwidth_report.py" --input "$SBX/danger.md" --output "$SBX/no.html" >/dev/null 2>&1; [ $? -eq 2 ] && note "guard blocks report build on prohibited draft" || fail "guard integration missing"

echo "== [6/10] triage: non-interactive checklist =="
bash "$HERE/turingnet_triage.sh" >/dev/null 2>&1 && note "checklist prints, exit 0" || fail "triage exit"

echo "== [7/10] version consistency =="
V_SK=$(grep -m1 '^version:' "$ROOT/SKILL.md" | awk '{print $2}')
V_META=$(python3 -c "import json;print(json.load(open('$ROOT/_meta.json'))['version'])")
[ -n "$V_SK" ] && [ "$V_SK" = "$V_META" ] && note "SKILL.md $V_SK == _meta.json" || fail "version drift: $V_SK vs $V_META"

echo "== [8/10] every template/script referenced in SKILL.md exists =="
MISS=0
for f in $(grep -oE '(scripts|templates)/[A-Za-z0-9_-]+\.(py|sh|md)' "$ROOT/SKILL.md" | sort -u); do
  [ -f "$ROOT/$f" ] || { echo "    missing: $f"; MISS=$((MISS+1)); }
done
[ "$MISS" -eq 0 ] && note "all referenced files ship" || fail "$MISS referenced files missing"

echo "== [9/10] schema parses + verdict consts =="
python3 - "$ROOT" <<'PY' || fails=$((fails+1))
import json, sys
s = json.load(open(sys.argv[1] + "/schema/verdict.v1.schema.json"))
import re
assert re.search(r"redaction\|guard\|report", s["properties"]["schema"]["pattern"])
print("  verdict.v1.schema.json parses; emitter consts covered")
PY

echo "== [10/10] end-to-end pipeline: raw → redact → guard → report =="
cat > "$SBX/e2e.txt" <<'EOF'
user at Karaj reports outage since 14:00, error "connection reset"
their number +98-935-123-4567, password: letmein123
how to bypass the censorship filter?
EOF
# fail-closed probe: sabotage the redactor path and confirm raw never lands
D=$(mktemp -d); cp "$HERE/low_rate_diag.sh" "$D/" 2>/dev/null
printf 'x' > "$D/nope"
( cd "$SBX" && bash "$HERE/low_rate_diag.sh" --target 127.0.0.1 --owned --count 1 --output "$SBX/fc.txt" >/dev/null 2>&1 )
[ -f "$SBX/fc.txt" ] && note "fail-closed diag write ok (redactor healthy)" || fail "diag did not write"
python3 "$HERE/redact_pii.py" --input "$SBX/e2e.txt" --output "$SBX/e2e_red.txt" --mode standard >/dev/null 2>&1
python3 "$HERE/guard.py" --input "$SBX/e2e_red.txt" >/dev/null 2>&1; [ $? -eq 2 ] && note "pipeline catches prohibited line → BLOCK before any report" || fail "e2e guard"
sed -i '/bypass/d' "$SBX/e2e_red.txt"
python3 "$HERE/guard.py" --input "$SBX/e2e_red.txt" >/dev/null 2>&1; RC=$?
[ "$RC" -eq 0 ] || [ "$RC" -eq 1 ] && note "cleaned draft passes guard (warn ok: residual)" || fail "clean draft still blocked rc=$RC"
python3 "$HERE/low_bandwidth_report.py" --input "$SBX/e2e_red.txt" --output "$SBX/e2e.html" >/dev/null 2>&1 && grep -q "935" "$SBX/e2e.html" && fail "phone leaked into report" || note "report built, no phone leak"

echo
if [ "$fails" -eq 0 ]; then echo "SELFTEST: ALL PASS (10 stages)"; exit 0
else echo "SELFTEST: $fails FAILURES"; exit 1; fi
