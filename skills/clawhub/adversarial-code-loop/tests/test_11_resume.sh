#!/bin/bash
# test_11 — resume from a partial run.
# Run 1 uses a slow DEV so we can kill the loop right after git_setup writes
# state.json (mid-BUILD). Run 2 re-invokes with --resume and a fast DEV; it must
# pick up the SAME loop branch (no loop/<feature>/2) and reach 'done'.
source "$(dirname "$0")/test_helpers.sh"

make_test_repo
make_test_spec

# --- run 1: interrupt mid-build once state.json exists ----------------------
ACL_MOCK_SLEEP=20 setsid "$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" \
    --max-loops 2 --no-merge \
    --dev-cmd "$MOCKS/mock_dev_slow.sh" --review-cmd "$MOCKS/mock_review.sh" \
    >/tmp/acl_t11a.log 2>&1 &
LPID=$!; register_pid "$LPID"

STATE=""
for _ in $(seq 1 100); do
    STATE="$(echo "$WORKDIR"/.adversarial-loop/*/state.json)"
    [ -f "$STATE" ] && break
    sleep 0.1
done
if [ ! -f "$STATE" ]; then
    kill -9 "$LPID" 2>/dev/null
    die "state.json was never written (git_setup did not complete)"
fi
BR1="$("$PY" -c 'import json,sys;print(json.load(open(sys.argv[1])).get("branch",""))' "$STATE" 2>/dev/null)"
kill -9 "-$LPID" 2>/dev/null; kill -9 "$LPID" 2>/dev/null; wait "$LPID" 2>/dev/null
[ -n "$BR1" ] || die "interrupted state.json has no 'branch' field"

# --- run 2: resume with a fast DEV ------------------------------------------
"$PY" "$LOOP" --spec "$SPEC" --workdir "$WORKDIR" \
    --max-loops 2 --no-merge --resume \
    --dev-cmd "$MOCKS/mock_dev.sh" --review-cmd "$MOCKS/mock_review.sh" \
    >/tmp/acl_t11b.log 2>&1
code=$?
[ "$code" -eq 0 ] || die "resume run exited $code (see /tmp/acl_t11b.log)"

# Resume must reuse the existing branch rather than mint loop/<feature>/2.
BR2="$(git -C "$WORKDIR" for-each-ref --format='%(refname:short)' refs/heads/loop/ | head -n1)"
[ "$BR1" = "$BR2" ] \
    || die "resume minted a new branch ($BR1 -> $BR2) instead of continuing"

DONE="$("$PY" -c 'import json,sys;d=json.load(open(sys.argv[1]));print("done" in d.get("completed",[]))' "$STATE" 2>/dev/null)"
[ "$DONE" = "True" ] || die "resume did not reach 'done'"

note "resume continued on $BR1 and completed"
exit 0
