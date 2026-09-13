#!/usr/bin/env bash
# selftest.sh — regression suite for the httrack skill. FULLY OFFLINE:
# it shadows httrack with a local stub (creates representative files, records
# argv), so every recipe + contract is exercised with no network and no sudo.
cd "$(dirname "$0")/.." || exit 1
S=scripts; P=0; F=0

SBX="$(mktemp -d /tmp/httrack-selftest.XXXXXX)" || exit 1
trap 'rm -rf "$SBX"' EXIT

# ── stub httrack ─────────────────────────────────────────────────────────────
mkdir -p "$SBX/bin"
cat > "$SBX/bin/httrack" <<'STUB'
#!/usr/bin/env bash
# Fake httrack: validates wrapper flag composition deterministically, offline.
if [ "$#" -ge 1 ] && [ "$1" = "--version" ]; then echo "HTTrack version 3.49.2 (stub)"; exit 0; fi
printf '%s\n' "$@" > "${STUB_ARGV_FILE:-/dev/null}"
OUT=""; while [ $# -gt 0 ]; do if [ "$1" = "-O" ]; then OUT="$2"; shift; fi; shift; done
[ -z "$OUT" ] && OUT=./out-stub
if [ "${FAKE_FAIL:-0}" = "1" ]; then echo "server error 500" >&2; exit 1; fi
mkdir -p "$OUT/site.example"
printf '<html>page</html>' > "$OUT/site.example/index.html"
printf 'body{}' > "$OUT/site.example/app.css"
printf 'a' > "$OUT/site.example/logo.png"
echo "HTTrack stub done" > "$OUT/hts-log.txt"
exit 0
STUB
chmod +x "$SBX/bin/httrack"
export HTTRACK_BIN="$SBX/bin/httrack"
export STUB_ARGV_FILE="$SBX/argv.log"

chk(){ if eval "$2" >/dev/null 2>&1; then echo "PASS $1"; P=$((P+1)); else echo "FAIL $1"; F=$((F+1)); fi; }

# doctor
chk "doctor JSON ok" "python3 $S/mirror.py doctor | python3 -c 'import sys,json; d=json.load(sys.stdin); assert d[\"schema\"]==\"httrack.doctor.v1\" and d[\"binary\"][\"found\"] is True and d[\"policy\"][\"shell_used\"] is False'"
chk "doctor missing binary rc3+found:false" "HTTRACK_BIN=/nonexistent/httrack python3 $S/mirror.py doctor > \"$SBX/d.json\"; test \$? -eq 3 && python3 -c 'import json,sys; assert json.load(open(sys.argv[1]))[\"binary\"][\"found\"] is False' \"$SBX/d.json\""
# policy
chk "ftp scheme refused rc2+reason" "python3 $S/mirror.py mirror ftp://x/ -o \"$SBX/m1\" 2> \"$SBX/e\"; test \$? -eq 2 && grep -q 'scheme' \"$SBX/e\""
chk "schemaless refused rc2+reason" "python3 $S/mirror.py mirror example.com -o \"$SBX/m1\" 2> \"$SBX/e\"; test \$? -eq 2 && grep -q 'scheme' \"$SBX/e\""
chk "snapshot extra filters refused rc2+reason" "python3 $S/mirror.py snapshot https://x.example/ -o \"$SBX/s1\" --allow '*.pdf' 2> \"$SBX/e\"; test \$? -eq 2 && grep -q 'pins' \"$SBX/e\""
chk "pattern sign normalized single prefix" "python3 $S/mirror.py mirror https://x.example/ -o \"$SBX/m1\" --deny '-*bad*'; rv=\$?; grep -q -- '^-\*bad\*$' \"$STUB_ARGV_FILE\" && grep -c -- '^-\*bad\*$' \"$STUB_ARGV_FILE\" | grep -q '^1$' && test \$rv -eq 0"
chk "pattern with space refused rc2+reason" "python3 $S/mirror.py mirror https://x.example/ -o \"$SBX/m1\" --allow 'a b' 2> \"$SBX/e\"; test \$? -eq 2 && grep -q 'glob' \"$SBX/e\""
# snapshot recipe
chk "snapshot rc0" "python3 $S/mirror.py snapshot https://example.com/art -o \"$SBX/s1\""
chk "snapshot argv has -r1 -%e0 -n -a" "python3 $S/mirror.py snapshot https://example.com/art -o \"$SBX/s1\"; grep -q -- '^-r1$' \"$STUB_ARGV_FILE\" && grep -q -- '^-%e0$' \"$STUB_ARGV_FILE\" && grep -q -- '^-n$' \"$STUB_ARGV_FILE\" && grep -q -- '^-a$' \"$STUB_ARGV_FILE\""
chk "snapshot deny-all + asset rules" "python3 $S/mirror.py snapshot https://example.com/art -o \"$SBX/s1\"; grep -q -- '^-\\*$' \"$STUB_ARGV_FILE\" && grep -q -- '^+\\*.css$' \"$STUB_ARGV_FILE\" && grep -q -- '^+\\*.webp$' \"$STUB_ARGV_FILE\""
chk "snapshot JSON report fields" "python3 $S/mirror.py snapshot https://example.com/art -o \"$SBX/s1\" --json | python3 -c 'import sys,json; d=json.load(sys.stdin); r=d[\"result\"]; assert d[\"schema\"]==\"httrack.report.v1\" and r[\"exit_code\"]==0 and r[\"files\"]>0 and r[\"bytes\"]>0 and r[\"html_pages\"]>=1 and isinstance(r[\"duration_s\"],float)'"
chk "snapshot report files == walk count" "python3 $S/mirror.py snapshot https://example.com/art -o \"$SBX/s1\" --json | python3 -c 'import sys,json,os; d=json.load(sys.stdin); real=sum(len(f) for _,_,f in os.walk(\"$SBX/s1\")); assert d[\"result\"][\"files\"]==real'"
# mirror recipe
chk "mirror argv has -r5 -c2 -s2 -a" "python3 $S/mirror.py mirror https://example.com -o \"$SBX/m1\" --depth 5; grep -q -- '^-r5$' \"$STUB_ARGV_FILE\" && grep -q -- '^-c2$' \"$STUB_ARGV_FILE\" && grep -q -- '^-s2$' \"$STUB_ARGV_FILE\" && grep -q -- '^-a$' \"$STUB_ARGV_FILE\""
chk "mirror resume adds -i" "python3 $S/mirror.py mirror https://example.com -o \"$SBX/m1\" --resume; grep -q -- '^-i$' \"$STUB_ARGV_FILE\""
chk "mirror robots override -s3" "python3 $S/mirror.py mirror https://example.com -o \"$SBX/m1\" --robots 3; grep -q -- '^-s3$' \"$STUB_ARGV_FILE\""
chk "mirror invalid robots rc2+reason" "python3 $S/mirror.py mirror https://example.com -o \"$SBX/m1\" --robots 9 2> \"$SBX/e\"; test \$? -eq 2 && grep -qi 'invalid choice' \"$SBX/e\""
chk "mirror allow/deny become bare +/-" "python3 $S/mirror.py mirror https://example.com -o \"$SBX/m1\" --allow '*.pdf' --deny '*/forums/*'; grep -q -- '^+\\*.pdf$' \"$STUB_ARGV_FILE\" && grep -q -- '^-\\*/forums/\\*$' \"$STUB_ARGV_FILE\""
chk "mirror max-time/max-mb mapped -E/-M" "python3 $S/mirror.py mirror https://example.com -o \"$SBX/m1\" --max-time 600 --max-mb 200; grep -q -- '^-E600$' \"$STUB_ARGV_FILE\" && grep -q -- '^-M200000000$' \"$STUB_ARGV_FILE\""
chk "mirror failure rc4" "FAKE_FAIL=1 python3 $S/mirror.py mirror https://example.com -o \"$SBX/m1\" 2>/dev/null; test \$? -eq 4"
chk "mirror sockets floor rc2+reason" "python3 $S/mirror.py mirror https://example.com -o \"$SBX/m1\" --sockets 0 2> \"$SBX/e\"; test \$? -eq 2 && grep -q 'sockets must' \"$SBX/e\""
# shim
chk "mirror.sh shim runs mirror depth 3" "sh mirror.sh https://example.com \"$SBX/sh\" 3; grep -q -- '^-r3$' \"$STUB_ARGV_FILE\""
# machine index + docs
chk "userinfo url refused rc2+reason" "python3 $S/mirror.py mirror http://victim.com@evil.example/ -o \"$SBX/m1\" 2> \"$SBX/e\"; test \$? -eq 2 && grep -qi 'userinfo' \"$SBX/e\""
chk "loopback refused rc2+reason" "python3 $S/mirror.py mirror http://127.0.0.1:8080/x -o \"$SBX/m1\" 2> \"$SBX/e\"; test \$? -eq 2 && grep -qi 'private' \"$SBX/e\""
chk "localhost refused rc2+reason" "python3 $S/mirror.py mirror http://localhost/x -o \"$SBX/m1\" 2> \"$SBX/e\"; test \$? -eq 2 && grep -qi 'private' \"$SBX/e\""
chk "private allowed with flag" "python3 $S/mirror.py mirror http://127.0.0.1:8080/x -o \"$SBX/m1\" --allow-private"
chk "traversal -o refused rc2+reason" "python3 $S/mirror.py mirror https://example.com -o ../m1 2> \"$SBX/e\"; test \$? -eq 2 && grep -qi 'traversal\|noqa\|output\|relative' \"$SBX/e\""
chk "fragment stripped from request" "python3 $S/mirror.py mirror https://example.com/p#frag -o \"$SBX/m1\" --json | python3 -c 'import sys,json; d=json.load(sys.stdin); assert d[\"request\"][\"url\"] == \"https://example.com/p\"'"

chk "manifest parses + contracts" "python3 -c 'import json; m=json.load(open(\"manifest.json\")); assert { \"httrack.doctor.v1\", \"httrack.report.v1\" } <= set(m[\"contracts\"]) and m[\"version\"]==\"2.0.1\" and m[\"exit_codes\"][\"4\"].startswith(\"httrack\")'"
chk "version sync everywhere" "python3 -c 'import json,os; m=json.load(open(\"manifest.json\")); skill=open(\"SKILL.md\").read().split(\"---\")[1]; card=open(\"skill-card.md\").read() if os.path.exists(\"skill-card.md\") else \"2.0.1\"; assert m[\"version\"]==\"2.0.1\" and \"version: 2.0.1\" in skill and card and \"v2.0.1\" in open(\"README.md\").read() and \"2.0.1\" in card'"
chk "hallucinated rows absent" "python3 -c 't=open(\"SKILL.md\").read()+open(\"docs/recipes.md\").read(); assert \"--robots=1\" not in t and \"-A \\\"*.pdf\" not in t'"
chk "evidence cites mirrorlinks -Y" "grep -q 'mirrorlinks' docs/evidence.md && grep -q -- '-s2' docs/evidence.md"

echo "-------- $P passed, $F failed --------"
[ "$F" -eq 0 ]
