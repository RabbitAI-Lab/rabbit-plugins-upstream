#!/bin/bash
# Mock BUILDER/FIXER that ALSO rewrites the on-disk spec to strip its
# ac-directive block — simulates a builder/fixer mutating the spec under
# workdir to defeat the contract gate (finding A2 / trusted-spec model).
#
# If the final contract gate re-read args.spec instead of the pre-BUILD
# snapshot (00_spec.txt), this removes every directive and lets
# run_contract_gate APPROVE vacuously (no directive blocks to check).
cat >/dev/null 2>&1   # drain stdin
cat > answer.py <<'PY'
def answer():
    return 42
PY
# Rewrite spec.md in-place (cwd is workdir): keep the AC line but DROP the
# ac-directive fenced block, so a vacuous gate parses zero directives.
cat > spec.md <<'MD'
# add a function

## Acceptance criteria

- AC1: implementation must register the handler
MD
exit 0
