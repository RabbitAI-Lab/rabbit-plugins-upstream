#!/usr/bin/env bash
# commit-helper.sh — Generate a conventional commit message from staged changes

set -euo pipefail

echo "=== Staged changes ==="
git diff --cached --stat
echo ""
echo "=== Full staged diff ==="
git diff --cached
