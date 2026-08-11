#!/bin/bash
# Shared helpers for the adversarial-code-loop integration tests.
# Sourced by every test_*.sh (and run_all.sh); never executed directly.
#
# Design notes:
#  * The spec file lives OUTSIDE the workdir (see make_test_spec). The pipeline
#    runs `git stash -u` during git_setup, which would stash (and thus hide) an
#    untracked spec sitting inside the repo. An external absolute path is immune.
#  * DEV/REVIEW/VERIFY roles are exercised through tiny mock commands under
#    mocks/, so the suite needs no network and no real model CLI.

# --- paths -------------------------------------------------------------------
TESTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$TESTS_DIR")"
LOOP="$SKILL_DIR/scripts/adversarial_loop.py"
MOCKS="$TESTS_DIR/mocks"
PY="${PYTHON:-python3}"

# --- colours (only when stdout is a tty) ------------------------------------
if [ -t 1 ]; then
    GREEN='\033[0;32m'; RED='\033[0;31m'; YELLOW='\033[0;33m'; NC='\033[0m'
else
    GREEN=''; RED=''; YELLOW=''; NC=''
fi

# --- cleanup on exit: kill stray background loops, drop temp paths -----------
_ACL_TEST_TEMPS=()
_ACL_TEST_PIDS=()
register_temp() { _ACL_TEST_TEMPS+=("$1"); }
register_pid()  { _ACL_TEST_PIDS+=("$1"); }
_acl_test_cleanup() {
    if [ "${#_ACL_TEST_PIDS[@]}"  -gt 0 ]; then
        # Kill each PID AND its process group: tests background the loop via
        # `setsid ... &`, which puts the Python interpreter and its spawned
        # subprocesses in a new session. Killing only the setsid PID would
        # orphan those grandchildren (F7); `kill -- -PID` reaps the group.
        for p in "${_ACL_TEST_PIDS[@]}"; do
            kill -9 "-$p" 2>/dev/null
            kill -9 "$p"  2>/dev/null
        done
    fi
    if [ "${#_ACL_TEST_TEMPS[@]}" -gt 0 ]; then rm -rf "${_ACL_TEST_TEMPS[@]}" 2>/dev/null; fi
}
trap _acl_test_cleanup EXIT

# --- tiny assert helpers -----------------------------------------------------
die()  { echo -e "${RED}FAIL${NC}: $*" >&2; exit 1; }
note() { echo -e "${GREEN}ok${NC}: $*"; }

# Set WORKDIR to a fresh empty git repo (temp dir, registered for cleanup).
# Identity is pinned so commits never block on missing user.name/email.
# Call WITHOUT $(): these helpers set globals in the caller's shell so the
# cleanup trap actually sees the temp paths (a $() subshell would discard them).
make_test_repo() {
    WORKDIR="$(mktemp -d)"; register_temp "$WORKDIR"
    git -C "$WORKDIR" init -q
    git -C "$WORKDIR" config user.email "acl@test.local"
    git -C "$WORKDIR" config user.name  "acl-test"
    git -C "$WORKDIR" commit -q --allow-empty -m "init"
}

# Set SPEC to an external (workdir-independent) spec file.
# $1 (optional) is the spec body; defaults to a trivial hello-world task.
make_test_spec() {
    local body="${1:-# add a function that returns 42}"
    SPEC="$(mktemp /tmp/acl_spec_XXXX.md)"; register_temp "$SPEC"
    printf '%s\n' "$body" > "$SPEC"
}

# Every git helper targets $WORKDIR explicitly (via `git -C`) rather than
# relying on the process cwd, so callers need not (and must not) `cd` first:
# these helpers set globals in the caller's shell, so wrapping them in $()
# would discard WORKDIR/SPEC and the cleanup registration.

# Echo the first loop/* branch in $WORKDIR, or "" if there is none.
current_loop_branch() {
    git -C "${WORKDIR:-.}" for-each-ref --format='%(refname:short)' refs/heads/loop/ | head -n1
}

# Echo the number of commits on $1 since its merge-base with the current HEAD.
commits_on_branch() {
    local branch="$1" mb
    mb="$(git -C "${WORKDIR:-.}" merge-base HEAD "$branch")" || return 1
    git -C "${WORKDIR:-.}" rev-list --count "$mb".."$branch"
}
