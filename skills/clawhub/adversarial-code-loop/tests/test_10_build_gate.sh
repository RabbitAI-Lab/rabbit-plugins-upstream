#!/bin/bash
# test_10 — failing build gate.
# After a successful BUILD, the --build-cmd "false" gate fails (exit 1). A
# genuine gate failure (not an infra/timeout) routes the loop through FIX
# rounds, then exits 3 (REJECT) when max-loops is exhausted.
source "$(dirname "$0")/test_helpers.sh"

make_test_repo
make_test_spec

"$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" --build-cmd "false" \
    --dev-cmd "$MOCKS/mock_dev.sh" --review-cmd "$MOCKS/mock_review.sh" \
    --no-arbiter \
    >/tmp/acl_t10.log 2>&1
code=$?
[ "$code" -eq 3 ] \
    || die "expected exit 3 (REJECT / BUILD_FAILED), got $code (see /tmp/acl_t10.log)"

note "failing build gate rejected the loop (exit 3)"
exit 0
