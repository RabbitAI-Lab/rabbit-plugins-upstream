#!/bin/bash
# test_03 — no git repo present.
# The workdir has no .git. git_setup must auto-init, run the loop, and exit 0,
# leaving a .git directory behind.
source "$(dirname "$0")/test_helpers.sh"

WORKDIR="$(mktemp -d)"; register_temp "$WORKDIR"   # deliberately NOT git init'd
make_test_spec

"$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" --no-merge \
    --dev-cmd "$MOCKS/mock_dev.sh" --review-cmd "$MOCKS/mock_review.sh" \
    >/tmp/acl_t03.log 2>&1
code=$?
[ "$code" -eq 0 ] || die "expected exit 0 (auto-init), got $code (see /tmp/acl_t03.log)"

[ -d "$WORKDIR/.git" ] || die "auto-init did not create $WORKDIR/.git"
note "no-git repo auto-initialised; loop completed"
exit 0
