#!/usr/bin/env bash
# =============================================================================
# camsnap-release.sh — Automated release & publish pipeline for camsnap skill
# =============================================================================
#
# Usage:
#   ./scripts/camsnap-release.sh [options]
#
# Options:
#   --bump <patch|minor|major>   Version bump type (default: patch)
#   --changelog <text>           Changelog entry for this release
#   --dry-run                    Show what would happen without publishing
#   --no-docs                    Skip doc sync step
#   --no-publish                 Skip clawhub publish (version bump + docs only)
#   --force                      Skip version-diff check, publish anyway
#   -h, --help                   Show this help
#
# What it does:
#   1. Detects the current published version from ClawHub
#   2. Computes a local content fingerprint (hash of skill files)
#   3. Compares against last-published fingerprint — skips if unchanged
#   4. Bumps the version in SKILL.md frontmatter and _meta.json
#   5. Syncs version info into skill-card.md
#   6. Generates/updates CHANGELOG.md
#   7. Publishes to ClawHub via `clawhub publish`
#   8. Updates local .clawhub/origin.json with new fingerprint
# =============================================================================

set -euo pipefail

# ── Paths ────────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE_DIR="$(cd "$SKILL_DIR/../.." && pwd)"
SKILL_NAME="camsnap"
SKILL_MD="$SKILL_DIR/SKILL.md"
META_JSON="$SKILL_DIR/_meta.json"
CARD_MD="$SKILL_DIR/skill-card.md"
ORIGIN_JSON="$SKILL_DIR/.clawhub/origin.json"
CHANGELOG_MD="$SKILL_DIR/CHANGELOG.md"
LOCKFILE="$WORKSPACE_DIR/.clawhub/lock.json"

# ── Defaults ─────────────────────────────────────────────────────────────────
BUMP="patch"
CHANGELOG=""
DRY_RUN=false
NO_DOCS=false
NO_PUBLISH=false
FORCE=false

# ── Colors ───────────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'
info()  { echo -e "${CYAN}[release]${NC} $*"; }
ok()    { echo -e "${GREEN}[ok]${NC} $*"; }
warn()  { echo -e "${YELLOW}[warn]${NC} $*"; }
err()   { echo -e "${RED}[error]${NC} $*" >&2; }
die()   { err "$*"; exit 1; }

# ── Args ─────────────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --bump)       BUMP="$2"; shift 2 ;;
    --changelog)  CHANGELOG="$2"; shift 2 ;;
    --dry-run)    DRY_RUN=true; shift ;;
    --no-docs)    NO_DOCS=true; shift ;;
    --no-publish) NO_PUBLISH=true; shift ;;
    --force)      FORCE=true; shift ;;
    -h|--help)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) die "Unknown option: $1" ;;
  esac
done

# ── Validation ───────────────────────────────────────────────────────────────
command -v clawhub >/dev/null 2>&1 || die "clawhub CLI not found. Install: npm i -g clawhub"
[[ -f "$SKILL_MD" ]] || die "SKILL.md not found at $SKILL_MD"
[[ -f "$META_JSON" ]] || die "_meta.json not found at $META_JSON"

# ── Helpers ──────────────────────────────────────────────────────────────────

# Extract version from SKILL.md frontmatter
get_skill_version() {
  sed -n 's/^version: *\(.*\)/\1/p' "$SKILL_MD" | head -1 | tr -d ' "'
}

# Extract version from _meta.json
get_meta_version() {
  grep '"version"' "$META_JSON" | head -1 | sed 's/.*"version": *"\([^"]*\)".*/\1/'
}

# Compute semantic version bump
bump_version() {
  local v="$1" type="$2"
  local major minor patch
  IFS='.' read -r major minor patch <<< "$v"
  case "$type" in
    major) echo "$((major+1)).0.0" ;;
    minor) echo "${major}.$((minor+1)).0" ;;
    patch) echo "${major}.${minor}.$((patch+1))" ;;
    *) die "Invalid bump type: $type (use patch|minor|major)" ;;
  esac
}

# Compute content fingerprint of the skill directory (excluding .clawhub, meta, etc.)
compute_fingerprint() {
  local dir="$1"
  find "$dir" -type f \
    ! -path '*/.clawhub/*' \
    ! -name '_meta.json' \
    ! -name 'CHANGELOG.md' \
    ! -name '.DS_Store' \
    -print0 | sort -z | xargs -0 sha256sum | sha256sum | awk '{print $1}'
}

# Get the last-published fingerprint from origin.json
get_last_fingerprint() {
  if [[ -f "$ORIGIN_JSON" ]]; then
    local fp
    fp=$(grep '"fingerprint"' "$ORIGIN_JSON" | head -1 | sed 's/.*"fingerprint": *"\([^"]*\)".*/\1/')
    # If grep didn't match (null value), return empty
    if [[ "$fp" == "null" ]] || [[ "$fp" == *"fingerprint"* ]]; then
      echo ""
    else
      echo "$fp"
    fi
  else
    echo ""
  fi
}

# Get the last-published version from origin.json
get_last_version() {
  if [[ -f "$ORIGIN_JSON" ]]; then
    grep '"installedVersion"' "$ORIGIN_JSON" | sed 's/.*"installedVersion": *"\([^"]*\)".*/\1/'
  else
    echo "0.0.0"
  fi
}

# ── Main ─────────────────────────────────────────────────────────────────────

info "=== CamSnap Release Pipeline ==="
info "Skill dir: $SKILL_DIR"

# 1. Current versions
CURRENT_VERSION="$(get_skill_version)"
META_VERSION="$(get_meta_version)"
LAST_VERSION="$(get_last_version)"
LAST_FP="$(get_last_fingerprint)"

info "SKILL.md version: $CURRENT_VERSION"
info "_meta.json version: $META_VERSION"
info "Last published: $LAST_VERSION (fp: ${LAST_FP:0:12}...)"

# Keep versions in sync
if [[ "$CURRENT_VERSION" != "$META_VERSION" ]]; then
  warn "Version mismatch between SKILL.md ($CURRENT_VERSION) and _meta.json ($META_VERSION)"
  if [[ "$META_VERSION" > "$CURRENT_VERSION" ]]; then
    CURRENT_VERSION="$META_VERSION"
  fi
fi

# 2. Content fingerprint
CURRENT_FP="$(compute_fingerprint "$SKILL_DIR")"
info "Current fingerprint: ${CURRENT_FP:0:12}..."

# 3. Check if anything changed
if [[ "$FORCE" != true ]] && [[ "$CURRENT_FP" == "$LAST_FP" ]]; then
  ok "No content changes detected since last publish (fp match). Use --force to override."
  exit 0
fi

# 4. Bump version
NEW_VERSION="$(bump_version "$CURRENT_VERSION" "$BUMP")"
info "Bumping version: $CURRENT_VERSION → $NEW_VERSION ($BUMP)"

if [[ "$DRY_RUN" == true ]]; then
  info "[dry-run] Would bump to $NEW_VERSION, sync docs, and publish."
  exit 0
fi

# 5. Update SKILL.md frontmatter version
sed -i "s/^version: .*/version: $NEW_VERSION/" "$SKILL_MD"
ok "Updated SKILL.md → v$NEW_VERSION"

# 6. Update _meta.json
sed -i "s/\"version\": \"[^\"]*\"/\"version\": \"$NEW_VERSION\"/" "$META_JSON"
# Update publishedAt timestamp
TIMESTAMP_MS=$(date +%s%3N)
sed -i "s/\"publishedAt\": [0-9]*/\"publishedAt\": $TIMESTAMP_MS/" "$META_JSON"
ok "Updated _meta.json → v$NEW_VERSION"

# 7. Sync skill-card.md version
if [[ "$NO_DOCS" != true ]]; then
  if [[ -f "$CARD_MD" ]]; then
    sed -i "s/^[0-9]\+\.[0-9]\+\.[0-9]\+.*$/$NEW_VERSION (source: server release metadata)/" "$CARD_MD"
    ok "Synced skill-card.md → v$NEW_VERSION"
  fi

  # 8. Update CHANGELOG.md
  DATE_NOW="$(date +%Y-%m-%d)"
  if [[ -z "$CHANGELOG" ]]; then
    CHANGELOG="Automated release v$NEW_VERSION"
  fi

  if [[ ! -f "$CHANGELOG_MD" ]]; then
    echo "# Changelog" > "$CHANGELOG_MD"
    echo "" >> "$CHANGELOG_MD"
  fi

  # Prepend new entry
  TMP_CHANGELOG=$(mktemp)
  {
    echo "# Changelog"
    echo ""
    echo "## $NEW_VERSION — $DATE_NOW"
    echo ""
    echo "- $CHANGELOG"
    echo ""
    # Append existing entries (skip the header line)
    tail -n +2 "$CHANGELOG_MD" 2>/dev/null || true
  } > "$TMP_CHANGELOG"
  mv "$TMP_CHANGELOG" "$CHANGELOG_MD"
  ok "Updated CHANGELOG.md → v$NEW_VERSION"
fi

# 9. Publish to ClawHub
if [[ "$NO_PUBLISH" != true ]]; then
  info "Publishing to ClawHub..."
  PUBLISH_ARGS=(
    publish "$SKILL_DIR"
    --slug "$SKILL_NAME"
    --name "CamSnap"
    --version "$NEW_VERSION"
    --changelog "$CHANGELOG"
  )

  if clawhub "${PUBLISH_ARGS[@]}"; then
    ok "Published camsnap v$NEW_VERSION to ClawHub!"
  else
    err "Publish failed! Rolling back version files..."
    # Roll back version bumps
    sed -i "s/^version: .*/version: $CURRENT_VERSION/" "$SKILL_MD"
    sed -i "s/\"version\": \"[^\"]*\"/\"version\": \"$CURRENT_VERSION\"/" "$META_JSON"
    die "Publish failed. Version files rolled back to $CURRENT_VERSION."
  fi

  # 10. Update origin.json with new fingerprint
  if [[ -f "$ORIGIN_JSON" ]]; then
    sed -i "s/\"installedVersion\": \"[^\"]*\"/\"installedVersion\": \"$NEW_VERSION\"/" "$ORIGIN_JSON"
    sed -i "s|\"fingerprint\": \"[^\"]*\"|\"fingerprint\": \"$CURRENT_FP\"|" "$ORIGIN_JSON"
    sed -i "s/\"installedAt\": [0-9]*/\"installedAt\": $TIMESTAMP_MS/" "$ORIGIN_JSON"
    ok "Updated .clawhub/origin.json"
  fi
else
  info "Skipping publish (--no-publish). Version files updated to $NEW_VERSION."
fi

echo ""
ok "=== Release v$NEW_VERSION complete ==="
