#!/bin/bash
# Run every test_*.sh in this directory and print a summary.
# Exits 0 iff all tests pass. No `set -e`: a failing test must be counted, not
# abort the runner, and we use $(( )) (not (( )) ) so a zero count never trips.
cd "$(dirname "$0")" || exit 1

PASS=0; FAIL=0; FAILED=()
for t in test_*.sh; do
    [ "$t" = "test_helpers.sh" ] && continue   # helper, not a test
    [ "$t" = "run_all.sh" ]       && continue   # this script
    if bash "$t"; then
        PASS=$((PASS + 1))
    else
        FAIL=$((FAIL + 1)); FAILED+=("$t")
    fi
done

echo "-----------------------------"
echo "Results: $PASS passed, $FAIL failed"
if [ "$FAIL" -gt 0 ]; then
    echo "Failed: ${FAILED[*]}" >&2
    exit 1
fi
exit 0
