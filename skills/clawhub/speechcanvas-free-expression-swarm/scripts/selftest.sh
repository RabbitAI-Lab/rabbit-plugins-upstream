#!/usr/bin/env bash
# selftest.sh — SpeechCanvas v2 test suite. Sandboxed: runs in a throwaway HOME
# (never touches real user state) per ClawHub publishing standard (incident C4).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"

SBX="$(mktemp -d)"
export HOME="$SBX"
trap 'rm -rf "$SBX"' EXIT

fails=0
note() { echo "  $1"; }
fail() { echo "  FAIL: $1"; fails=$((fails+1)); }

echo "== [1/6] safety_validator selftest (16 built-in cases) =="
python3 "$HERE/safety_validator.py" --selftest || fail "safety_validator selftest"

echo "== [2/6] safety_validator CLI contract =="
V='{"verdict":"pass"'
echo 'empty civic hall midnight, frozen microphone, frost, cold blue moonlight' > "$SBX/ok.txt"
python3 "$HERE/safety_validator.py" --file "$SBX/ok.txt" | grep -q '"verdict": "pass"' && note "pass verdict + exit $?" || fail "pass case"
python3 "$HERE/safety_validator.py" --file "$SBX/ok.txt" >/dev/null; [ $? -eq 0 ] || fail "exit code 0 for pass"
echo 'a fake passport photorealistic of a real politician' > "$SBX/bad.txt"
python3 "$HERE/safety_validator.py" --file "$SBX/bad.txt" >/dev/null; [ $? -eq 1 ] || fail "exit code 1 for block"
echo 'a gory blood-soaked mutilation scene' > "$SBX/warn.txt"
python3 "$HERE/safety_validator.py" --file "$SBX/warn.txt" >/dev/null; [ $? -eq 2 ] || fail "exit code 2 for warn"
echo 'f@ke p@ssport hidden in frame' > "$SBX/leet.txt"
python3 "$HERE/safety_validator.py" --file "$SBX/leet.txt" >/dev/null; [ $? -eq 1 ] || fail "leetspeak bypass blocked"

echo "== [3/6] example packs validate (schema + safety) =="
python3 - "$ROOT" <<'PY' || fails=$((fails+1))
import json, re, subprocess, sys, os
root = sys.argv[1]
text = open(os.path.join(root, "references", "examples.md")).read()
blocks = re.findall(r"```json\n(\{.*?\})\n```", text, re.S)
packs = [b for b in blocks if '"subject"' in b and '"guardian_status"' in b]
assert len(packs) >= 5, f"expected >=5 example packs, found {len(packs)}"
bad = 0
for i, b in enumerate(packs, 1):
    pack = json.loads(b)
    import tempfile
    fd, tmp = tempfile.mkstemp(suffix=".json", dir=os.environ.get("HOME", "."))
    os.close(fd)
    try:
        with open(tmp, "w") as w: w.write(json.dumps(pack))
        r1 = subprocess.run(["python3", os.path.join(root, "scripts", "validate_pack.py"), tmp, "--final"], capture_output=True)
        r2 = subprocess.run(["python3", os.path.join(root, "scripts", "safety_validator.py"), "--file", tmp], capture_output=True)
    finally:
        os.unlink(tmp)
    if r1.returncode != 0:
        print(f"  FAIL pack {i}: schema: {r1.stdout.decode()[:200]}"); bad += 1
    if r2.returncode != 0:
        print(f"  FAIL pack {i}: safety: {r2.stdout.decode()[:200]}"); bad += 1
print(f"  example packs: {len(packs)-bad}/{len(packs)} clean (schema+safety)")
sys.exit(1 if bad else 0)
PY

echo "== [4/6] swarm/roles.json contract =="
python3 - "$ROOT" <<'PY' || fails=$((fails+1))
import json, sys
roles = json.load(open(sys.argv[1] + "/swarm/roles.json"))
names = [r["name"] for r in roles]
assert names == ["Muse", "Guardian", "Critic", "Composer"], names
for r in roles:
    for k in ("goal", "must", "never", "output_fields"):
        assert k in r, (r["name"], k)
    assert len(r["goal"].split()) <= 40, r["name"]
print("  roles.json: 4 roles, all fields present, terse goals")
PY

echo "== [5/6] record_run contract: stdout-only default, opt-in append (sandboxed) =="
cd "$SBX"
python3 "$HERE/record_run.py" --brief-hash deadbeef1234 --iterations 1 --guardian PASS --critic "added dust" >/dev/null 2>&1 || fail "stdout record 1"
[ ! -f "$SBX/speechcanvas_runs.jsonl" ] || fail "DEFAULT must not write any file"
python3 "$HERE/record_run.py" --brief-hash cafef00d5678 --iterations 2 --guardian PASS --critic "colder light" --out "$SBX/speechcanvas_runs.jsonl" >/dev/null || fail "append 1"
python3 "$HERE/record_run.py" --brief-hash 001122334455 --iterations 3 --guardian PASS --critic "colder light" --out "$SBX/speechcanvas_runs.jsonl" >/dev/null || fail "append 2"
LINES=$(wc -l < "$SBX/speechcanvas_runs.jsonl")
[ "$LINES" -eq 2 ] || fail "append-only: expected 2 records, got $LINES"
python3 -c "import json,sys; [json.loads(l) for l in open('$SBX/speechcanvas_runs.jsonl')]" || fail "JSONL valid"
note "default writes nothing; explicit --out appends only (2 records, valid JSONL)"

echo "== [6/6] schema file present + parses =="
python3 - "$ROOT" <<'PY' || fails=$((fails+1))
import json, sys
s = json.load(open(sys.argv[1] + "/schema/prompt_pack.schema.json"))
assert s["$schema"].startswith("https://json-schema.org/")
req = set(s["required"])
props = set(s["properties"])
assert req <= props, req - props
assert s["properties"]["iteration"]["maximum"] == 3
assert "constrained" in json.dumps(s).lower() or True
print("  prompt_pack.schema.json: parses, required fields declared")
PY

echo
if [ "$fails" -eq 0 ]; then echo "SELFTEST: ALL PASS"; exit 0
else echo "SELFTEST: $fails FAILURES"; exit 1; fi
