#!/bin/bash
# Mock BUILDER that sleeps ACL_MOCK_SLEEP seconds (default 30) before writing.
# Used to open a window the test can kill inside (test_11 resume) or to force a
# per-subprocess timeout (test_09, ACL_MOCK_SLEEP > --timeout).
cat >/dev/null 2>&1
sleep "${ACL_MOCK_SLEEP:-30}"
cat > answer.py <<'PY'
def answer():
    return 42
PY
exit 0
