#!/usr/bin/env bash
# Pre-merge safety checklist for finishing-a-development-branch.
# Read-only / informational. Does NOT merge, push, or delete anything.
#
# Usage (run inside the repo, on the branch to be merged):
#   bash scripts/pre_merge_check.sh [base-branch]
set -euo pipefail

BASE="${1:-main}"
echo "=== Pre-merge check (base: $BASE) ==="

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not inside a git repository." >&2
  exit 1
fi

BRANCH="$(git rev-parse --abbrev-ref HEAD)"
echo "Current branch: $BRANCH"
echo

echo "1) Tests / checks (informational — runs a detected runner if present):"
if [ -f package.json ] && grep -q '"test"' package.json; then
  npm test --silent || echo "  [warn] npm test failed or unavailable"
elif command -v pytest >/dev/null 2>&1 && ls tests >/dev/null 2>&1; then
  pytest -q || echo "  [warn] pytest failed"
elif command -v python3 >/dev/null 2>&1 && ls test_*.py >/dev/null 2>&1; then
  python3 -m unittest discover -s . -p 'test_*.py' || echo "  [warn] unittest failed"
else
  echo "  - no test runner detected — run your project's checks manually"
fi
echo

echo "2) Diff vs $BASE (look for stray files / scope creep):"
git diff --stat "$BASE"...HEAD
echo

echo "3) Secret scan of the diff (sk-..., ghp_..., gho_..., github_pat...):"
if git diff "$BASE"...HEAD | grep -nE 'sk-[A-Za-z0-9]{10,}|ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}'; then
  echo "  [FAIL] POTENTIAL SECRET FOUND — remove before push/PR."
  exit 3
else
  echo "  [ok] no obvious secrets in diff"
fi
echo

echo "4) Worktrees (clean up stale ones only AFTER merge):"
git worktree list
echo

echo "=== Done. If all clear, integrate per your chosen strategy, verify on"
echo "    $BASE after merge, and delete the branch ONLY once merge is confirmed. ==="
