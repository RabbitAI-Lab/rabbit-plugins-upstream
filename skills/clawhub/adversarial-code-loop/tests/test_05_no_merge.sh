#!/bin/bash
# test_05 — --no-merge keeps the loop branch.
# On approval the pipeline normally squash-merges and deletes the loop branch.
# With --no-merge the branch must survive the run and the process exits 0.
source "$(dirname "$0")/test_helpers.sh"

make_test_repo
make_test_spec

"$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" --no-merge \
    --dev-cmd "$MOCKS/mock_dev.sh" --review-cmd "$MOCKS/mock_review.sh" \
    >/tmp/acl_t05.log 2>&1
code=$?
[ "$code" -eq 0 ] || die "expected exit 0, got $code (see /tmp/acl_t05.log)"

BR="$(current_loop_branch)"
[ -n "$BR" ] || die "--no-merge should have left the loop/* branch in place"

note "--no-merge preserved branch $BR"
exit 0
