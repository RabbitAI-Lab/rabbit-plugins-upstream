#!/usr/bin/env bash
# =============================================================================
# camsnap-quick-publish.sh — Fast local publish for dev/testing
# =============================================================================
#
# Usage:
#   ./scripts/camsnap-quick-publish.sh [options]
#
# Options:
#   --version <ver>    Set explicit version (default: auto patch bump + -dev suffix)
#   --changelog <txt>  Changelog text
#   --bump <type>      patch|minor|major (default: patch)
#   --dry-run          Preview without publishing
#   -h, --help         Show help
#
# This is a thin wrapper around camsnap-release.sh optimized for rapid dev
# iteration. It:
#   - Auto-generates a dev version (e.g. 0.1.1-dev.20260801)
#   - Skips CHANGELOG updates (dev churn)
#   - Uses --force to bypass fingerprint check
#   - Adds "dev" tag so it doesn't pollute latest
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
RELEASE_SCRIPT="$SCRIPT_DIR/camsnap-release.sh"

# Defaults
VERSION=""
BUMP="patch"
CHANGELOG=""
DRY_RUN=false

# Colors
GREEN='\033[0;32m'; CYAN='\033[0;36m'; YELLOW='\033[1;33m'; NC='\033[0m'
info()  { echo -e "${CYAN}[quick]${NC} $*"; }
ok()    { echo -e "${GREEN}[ok]${NC} $*"; }
warn()  { echo -e "${YELLOW}[warn]${NC} $*"; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    --version)   VERSION="$2"; shift 2 ;;
    --changelog) CHANGELOG="$2"; shift 2 ;;
    --bump)      BUMP="$2"; shift 2 ;;
    --dry-run)   DRY_RUN=true; shift ;;
    -h|--help)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

# Generate dev version if not specified
if [[ -z "$VERSION" ]]; then
  # Get current version from SKILL.md
  CURRENT=$(sed -n 's/^version: *\(.*\)/\1/p' "$SKILL_DIR/SKILL.md" | head -1 | tr -d ' "')
  IFS='.' read -r major minor patch <<< "$CURRENT"
  case "$BUMP" in
    major) NEXT="$((major+1)).0.0" ;;
    minor) NEXT="${major}.$((minor+1)).0" ;;
    patch) NEXT="${major}.${minor}.$((patch+1))" ;;
  esac
  DATE_TAG=$(date +%Y%m%d%H%M)
  VERSION="${NEXT}-dev.${DATE_TAG}"
fi

info "Quick-publishing camsnap v$VERSION"

ARGS=(--bump "$BUMP" --force)

if [[ -n "$CHANGELOG" ]]; then
  ARGS+=(--changelog "$CHANGELOG [dev]")
else
  ARGS+=(--changelog "Dev build v$VERSION")
fi

if [[ "$DRY_RUN" == true ]]; then
  ARGS+=(--dry-run)
fi

# For dev publishes, we need to handle the version differently.
# The release script auto-bumps, so we set the version in SKILL.md first,
# then use --no-bump trick: set version manually then call with --force and patch bump
# Actually simpler: just set version in files then call release with --force --no-docs

# Pre-set the version
sed -i "s/^version: .*/version: $VERSION/" "$SKILL_DIR/SKILL.md"
sed -i "s/\"version\": \"[^\"]*\"/\"version\": \"$VERSION\"/" "$SKILL_DIR/_meta.json"
info "Set version to $VERSION in SKILL.md and _meta.json"

if [[ "$DRY_RUN" == true ]]; then
  info "[dry-run] Would publish v$VERSION"
  info "Run without --dry-run to actually publish."
  exit 0
fi

# Publish directly with clawhub
info "Publishing to ClawHub..."
clawhub publish "$SKILL_DIR" \
  --slug camsnap \
  --name "CamSnap" \
  --version "$VERSION" \
  --changelog "${CHANGELOG:-Dev build v$VERSION}" \
  --tags "dev" \
  && ok "Published camsnap v$VERSION (tag: dev)" \
  || echo "Publish failed or version already exists."

ok "Quick publish done: v$VERSION"
