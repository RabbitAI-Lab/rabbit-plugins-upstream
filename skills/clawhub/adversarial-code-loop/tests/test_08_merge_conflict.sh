#!/bin/bash
# test_08 — parent branch advances during the loop (merge conflict).
# While the loop runs on its branch, the parent branch is advanced with a
# conflicting change to the same file. The squash-merge then conflicts; the
# pipeline must report an infrastructure failure (exit 1), describe the failed
# squash in final.json, and leave the repository usable.
source "$(dirname "$0")/test_helpers.sh"

make_test_repo
printf 'base\n' > "$WORKDIR/shared.txt"
git -C "$WORKDIR" add -A
git -C "$WORKDIR" commit -q -m "shared file"
PARENT="$(git -C "$WORKDIR" symbolic-ref --short HEAD)"
make_test_spec

# Loop in its own session: DEV rewrites shared.txt then sleeps to open a window.
ACL_MOCK_SLEEP=4 setsid "$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" \
    --feature merge-conflict \
    --dev-cmd "$MOCKS/mock_dev_conflict.sh" --review-cmd "$MOCKS/mock_review.sh" \
    >/tmp/acl_t08.log 2>&1 &
LPID=$!; register_pid "$LPID"

# Wait for git_setup to create the loop branch.
for _ in $(seq 1 60); do
    git -C "$WORKDIR" for-each-ref --format='%(refname:short)' refs/heads/loop/ \
        | grep -q . && break
    sleep 0.1
done

# Advance the parent from a throwaway worktree (can't checkout a branch held by
# the running loop in the main worktree), then release it.
WT="$(mktemp -d)"; register_temp "$WT"
git -C "$WORKDIR" worktree add -q "$WT" "$PARENT"
( cd "$WT" && printf 'parent-wins\n' > shared.txt && git add -A && git commit -q -m "parent advance" )
git -C "$WORKDIR" worktree remove --force "$WT"

# Let the loop reach finalize and collect its real exit status.
for _ in $(seq 1 120); do kill -0 "$LPID" 2>/dev/null || break; sleep 0.25; done
kill -0 "$LPID" 2>/dev/null && die "pipeline timed out before merge conflict"
wait "$LPID"
RC=$?

[ "$RC" -eq 1 ] || die "merge conflict returned $RC (expected infrastructure exit 1)"
FINAL="$WORKDIR/.adversarial-loop/merge-conflict/final.json"
[ -f "$FINAL" ] || die "final.json missing after merge conflict"
grep -q '"merged": false' "$FINAL" \
    || die "final.json did not record merged=false"
grep -q '"error": "git finalize failed: squash merge' "$FINAL" \
    || die "final.json missing descriptive squash-merge error"

# Graceful-handling checks: no stuck index lock, git still responsive, HEAD sane.
[ ! -e "$WORKDIR/.git/index.lock" ] || die "index.lock left behind after conflict"
git -C "$WORKDIR" status --porcelain >/dev/null 2>&1 \
    || die "git status is broken after the conflict"
git -C "$WORKDIR" rev-parse --verify HEAD >/dev/null 2>&1 \
    || die "HEAD is invalid after the conflict"

note "merge conflict returns infrastructure failure with final.json error"
exit 0
