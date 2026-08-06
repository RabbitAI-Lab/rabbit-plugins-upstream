#!/bin/bash
# test_02 — dirty working tree.
# An untracked file present at start must not break the loop: git_setup stashes
# it (-u) and _restore pops it back on every exit path. After the run the file
# must still be there and the loop must exit 0.
source "$(dirname "$0")/test_helpers.sh"

make_test_repo
make_test_spec

# Dirty tree: an untracked file the loop must stash then restore.
echo "uncommitted dirty content" > "$WORKDIR/dirty_uncommitted.txt"

"$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" --no-merge \
    --dev-cmd "$MOCKS/mock_dev.sh" --review-cmd "$MOCKS/mock_review.sh" \
    >/tmp/acl_t02.log 2>&1
code=$?
[ "$code" -eq 0 ] || die "expected exit 0 despite dirty tree, got $code (see /tmp/acl_t02.log)"

[ -f "$WORKDIR/dirty_uncommitted.txt" ] \
    || die "dirty file was not restored after stash/unstash"
note "dirty tree tolerated; untracked file restored"
exit 0
