#!/bin/bash
# selftest.sh — prove the kaggle-openmm-md-runbook skill is intact (v1.1.0).
# Writes nothing outside temp dirs; safe to run anywhere.
set -euo pipefail
D="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# 1. all scripts compile + their own selftests pass
python3 -m py_compile "$D/scripts/md_preflight.py" "$D/scripts/skill_query.py" "$D/scripts/learn.py"
python3 "$D/scripts/md_preflight.py" --selftest
python3 "$D/scripts/learn.py" --selftest

# 2. registry validity + integrity vs SKILL.md
python3 - "$D" <<'PY'
import json, re, sys, pathlib
D = pathlib.Path(sys.argv[1])
reg = D / "registry"
traps = json.load(open(reg / "traps.json"))
rules = json.load(open(reg / "rules.json"))
errors = json.load(open(reg / "errors.json"))
params = json.load(open(reg / "params.json"))
schema = json.load(open(reg / "lessons.schema.json"))
assert (len(traps), len(rules), len(errors)) == (21, 16, 20), "registry counts changed"
assert {t["id"] for t in traps} == {f"TRAP-{i:02d}" for i in range(1, 22)}, "trap IDs broken"
assert {r["id"] for r in rules} == {f"R{i:02d}" for i in range(1, 17)}, "rule IDs broken"
# trap cross-links in rules must exist
for r in rules:
    if r.get("trap"):
        assert any(t["id"] == r["trap"] or r["trap"].startswith(t["id"]) for t in traps), \
            f"{r['id']} -> {r['trap']} dangling"
# error causes must reference real traps
for e in errors:
    for c in re.findall(r"TRAP-\d+", e["cause"]):
        assert any(t["id"] == c for t in traps), f"{e['id']} cause {c} dangling"
# params spot-checks (anti-tamper)
assert params["production"]["total_steps"] == 25000000
assert params["forcefields"]["protein"] == "amber19/protein.ff19SB.xml"
assert params["system"]["ligand"].startswith("mebendazole C16H13N3O3")
# SKILL.md must reference all 16 rule IDs and mention the new tooling
sk = (D / "SKILL.md").read_text()
for i in range(1, 17):
    assert f"[R{i:02d}]" in sk, f"SKILL.md missing [R{i:02d}]"
for needle in ("skill_query.py", "learn.py", "Grounding contract", "Self-improvement",
               "--explain", "essence"):
    assert needle in sk, f"SKILL.md missing '{needle}'"
print("REGISTRY OK (21 traps / 16 rules / 20 errors / params+schema; cross-refs + SKILL.md in sync)")
PY

# 3. query CLI smoke (text + json + not-found exit code)
python3 "$D/scripts/skill_query.py" essence >/dev/null
python3 "$D/scripts/skill_query.py" trap TRAP-03 >/dev/null
python3 - "$D" <<'PYQ'
import json, subprocess, sys
r = subprocess.run([sys.executable, sys.argv[1] + "/scripts/skill_query.py", "rule", "R08", "--json"],
                   capture_output=True, text=True)
assert r.returncode == 0, r.stderr
d = json.loads(r.stdout)          # --json must emit valid JSON
assert d["id"] == "R08" and "Re-cent" in d["rule"], d
PYQ
python3 "$D/scripts/skill_query.py" error nvrtc | grep -q ERR-001
if python3 "$D/scripts/skill_query.py" rule R99 >/dev/null 2>&1; then
  echo "SELFTEST FAIL: unknown rule lookup must exit non-zero"; exit 1
fi
echo "QUERY CLI OK (essence/lookup/error-search/json/exit-codes)"

# 4. required files present
for f in SKILL.md README.md RUNBOOK.md \
         references/traps-and-api-matrix.md references/operations.md \
         registry/traps.json registry/rules.json registry/errors.json registry/params.json \
         registry/lessons.jsonl registry/lessons.schema.json; do
  [ -f "$D/$f" ] || { echo "SELFTEST FAIL: missing $f"; exit 1; }
done

python3 -c "open('$D/SKILL.md', encoding='utf-8').read()" || { echo "SELFTEST FAIL: SKILL.md not UTF-8"; exit 1; }
echo "sha256(SKILL.md) = $(sha256sum "$D/SKILL.md" | cut -d' ' -f1)"
echo "SELFTEST.SH OK — skill files intact"
