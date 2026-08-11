#!/bin/bash
# Mock BUILDER/FIXER (dev_cmd). Reads the spec/prompt on stdin (ignored),
# writes a deterministic source file into the worktree (cwd), exits 0.
# Used for happy-path / no-merge / no-git / dirty-tree / resume-complete runs.
cat >/dev/null 2>&1   # drain stdin
cat > answer.py <<'PY'
def answer():
    return 42
PY
exit 0
