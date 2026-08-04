#!/bin/bash
# test_04 — impossible spec rejected after max-loops.
# The mock verifier keeps the finding disputed, so after --max-loops 1 (no
# arbiter) the loop terminates REJECTED: exit code 3 and a [REJECTED] commit.
source "$(dirname "$0")/test_helpers.sh"

make_test_repo
make_test_spec "# impossible spec that no model can satisfy"

"$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" \
    --max-loops 1 --no-arbiter \
    --dev-cmd "$MOCKS/mock_dev.sh" --review-cmd "$MOCKS/mock_review_reject.sh" \
    >/tmp/acl_t04.log 2>&1
code=$?
[ "$code" -eq 3 ] || die "expected exit 3 (REJECT), got $code (see /tmp/acl_t04.log)"

BR="$(current_loop_branch)"
[ -n "$BR" ] || die "no loop/* branch to inspect for the [REJECTED] marker"
git -C "$WORKDIR" log --oneline "$(git -C "$WORKDIR" merge-base HEAD "$BR")".."$BR" \
    | grep -q '\[REJECTED\]' \
    || die "no [REJECTED] commit on $BR"

note "impossible spec rejected (exit 3) with [REJECTED] commit"
exit 0
