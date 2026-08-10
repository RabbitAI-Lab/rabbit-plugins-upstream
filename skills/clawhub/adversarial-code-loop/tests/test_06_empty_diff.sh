#!/bin/bash
# test_06 — build that produces no source changes.
# DEV is `true` (writes nothing). The pipeline still completes gracefully:
# setup auto-appends .adversarial-loop/ to .gitignore (a real, committable
# change) so the diff is non-empty, review/fix/verify run, and the loop exits 0.
# This is the documented graceful outcome for a no-op build.
source "$(dirname "$0")/test_helpers.sh"

make_test_repo
make_test_spec "# spec that produces no source changes"

"$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" --no-merge \
    --dev-cmd "true" --review-cmd "$MOCKS/mock_review.sh" \
    >/tmp/acl_t06.log 2>&1
code=$?
[ "$code" -eq 0 ] \
    || die "expected graceful exit 0 for no-op build, got $code (see /tmp/acl_t06.log)"

note "no-op build handled gracefully (exit 0)"
exit 0
