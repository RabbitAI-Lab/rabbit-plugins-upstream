#!/usr/bin/env bash
# =============================================================================
# camsnap-autopublish.sh — Detect changes and auto-publish if needed
# =============================================================================
#
# Designed to be called from:
#   - Git pre-push / post-commit hooks
#   - CI/CD pipelines (GitHub Actions, etc.)
#   - Cron jobs
#
# It checks whether the skill content has changed since the last publish
# and, if so, runs the release pipeline.
#
# Usage:
#   ./scripts/camsnap-autopublish.sh [--bump patch|minor|major] [--dry-run]
#
# Exit codes:
#   0 — No changes (nothing to do) or publish succeeded
#   1 — Publish failed
#   2 — Prerequisites missing
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
RELEASE_SCRIPT="$SCRIPT_DIR/camsnap-release.sh"
ORIGIN_JSON="$SKILL_DIR/.clawhub/origin.json"

BUMP="patch"
DRY_RUN=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --bump) BUMP="$2"; shift 2 ;;
    --dry-run) DRY_RUN=true; shift ;;
  esac
done

# Compute current fingerprint
CURRENT_FP=$(find "$SKILL_DIR" -type f \
  ! -path '*/.clawhub/*' \
  ! -name '_meta.json' \
  ! -name 'CHANGELOG.md' \
  ! -name '.DS_Store' \
  -print0 | sort -z | xargs -0 sha256sum | sha256sum | awk '{print $1}')

# Get last published fingerprint
LAST_FP=""
if [[ -f "$ORIGIN_JSON" ]]; then
  LAST_FP=$(grep '"fingerprint"' "$ORIGIN_JSON" | head -1 | sed 's/.*"fingerprint": *"\([^"]*\)".*/\1/' || true)
  if [[ "$LAST_FP" == "null" ]] || [[ "$LAST_FP" == *"fingerprint"* ]]; then
    LAST_FP=""
  fi
fi

if [[ "$CURRENT_FP" == "$LAST_FP" ]]; then
  echo "[autopublish] No changes detected (fingerprint match). Nothing to do."
  exit 0
fi

echo "[autopublish] Changes detected! Current fp: ${CURRENT_FP:0:12}, last: ${LAST_FP:0:12}"
echo "[autopublish] Running release pipeline (bump: $BUMP)..."

ARGS=("--bump" "$BUMP")
if [[ "$DRY_RUN" == true ]]; then
  ARGS+=("--dry-run")
fi

exec "$RELEASE_SCRIPT" "${ARGS[@]}"
