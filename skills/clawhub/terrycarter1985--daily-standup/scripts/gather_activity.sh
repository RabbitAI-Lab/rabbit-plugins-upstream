#!/usr/bin/env bash
# gather_activity.sh — collect git activity from the last 24 hours
set -euo pipefail

REPO="${1:-.}"
cd "$REPO"

echo "=== Commits (last 24h) ==="
git log --since="24 hours ago" --oneline --no-merges 2>/dev/null || echo "(not a git repo or no commits)"

echo ""
echo "=== Changed files (last 24h) ==="
git log --since="24 hours ago" --name-only --pretty=format:"" --no-merges 2>/dev/null | sort -u | sed '/^$/d' || echo "(none)"
