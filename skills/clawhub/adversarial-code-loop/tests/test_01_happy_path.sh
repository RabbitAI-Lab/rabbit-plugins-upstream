#!/bin/bash
# test_01 — happy path.
# git repo + trivial spec + --no-merge --max-loops 1 must:
#   * create a loop/* branch
#   * leave >=2 commits on it (build + fix)
#   * exit 0
source "$(dirname "$0")/test_helpers.sh"

make_test_repo
make_test_spec "# add a hello world function"

"$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" \
    --no-merge --max-loops 1 \
    --dev-cmd "$MOCKS/mock_dev.sh" --review-cmd "$MOCKS/mock_review.sh" \
    >/tmp/acl_t01.log 2>&1
code=$?
[ "$code" -eq 0 ] || die "expected exit 0, got $code (see /tmp/acl_t01.log)"

BR="$(current_loop_branch)"
[ -n "$BR" ] || die "no loop/* branch was created"

N="$(commits_on_branch "$BR")" || die "could not count commits on $BR"
[ "$N" -ge 2 ] || die "expected >=2 commits on $BR (build + fix), got $N"

note "happy path: $BR carries $N commits"
exit 0
