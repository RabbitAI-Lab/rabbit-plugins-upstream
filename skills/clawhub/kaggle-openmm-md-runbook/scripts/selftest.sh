#!/bin/bash
# selftest.sh — prove the kaggle-openmm-md-runbook skill is intact.
# Writes nothing outside temp dirs; safe to run anywhere.
set -euo pipefail
D="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 -m py_compile "$D/scripts/md_preflight.py"
python3 "$D/scripts/md_preflight.py" --selftest

for f in SKILL.md README.md RUNBOOK.md \
         references/traps-and-api-matrix.md references/operations.md; do
  [ -f "$D/$f" ] || { echo "SELFTEST FAIL: missing $f"; exit 1; }
done

echo "sha256(SKILL.md) = $(sha256sum "$D/SKILL.md" | cut -d' ' -f1)"
echo "SELFTEST.SH OK — skill files intact"
