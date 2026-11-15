# CamSnap — Automated Release Pipeline

This document describes the automated publishing workflow for the camsnap skill.

## Architecture

```
skills/camsnap/
├── SKILL.md                          # Skill definition (version in frontmatter)
├── _meta.json                        # ClawHub metadata (version, owner, publishedAt)
├── skill-card.md                     # ClawHub listing card (version synced)
├── CHANGELOG.md                      # Auto-generated changelog
├── Makefile                          # `make` convenience targets
├── scripts/
│   ├── camsnap                       # CLI wrapper (symlink to PATH)
│   ├── camsnap-release.sh            # Core release pipeline
│   ├── camsnap-quick-publish.sh      # Fast dev publish (dev versions)
│   ├── camsnap-autopublish.sh        # Change-detect + publish (CI/hooks)
│   └── git-hooks/
│       └── pre-push                  # Git hook for auto-publish on push
└── .clawhub/
    └── origin.json                   # Tracks last published fingerprint & version
```

## Commands

### Full Release (production)

```bash
# Auto-detect changes, bump patch, sync docs, publish
make release

# Bump minor version
make release BUMP=minor

# With changelog
./scripts/camsnap-release.sh --bump minor --changelog "Added watch mode"

# Dry run (preview only)
make dry-run
```

### Quick Dev Publish

```bash
# Publishes a dev version like 0.1.1-dev.202608011200 with "dev" tag
make quick

# Or use the CLI wrapper
camsnap quick
```

### Auto-Publish (CI/CD)

```bash
# Only publishes if content changed since last release
make autopublish
```

### Local CLI

```bash
# Install the CLI wrapper
sudo ln -sf $(pwd)/scripts/camsnap /usr/local/bin/camsnap

camsnap release --bump patch
camsnap quick
camsnap version
camsnap check
camsnap help
```

## How It Works

### 1. Change Detection

The pipeline computes a SHA-256 fingerprint of all skill files (excluding `.clawhub/`, `_meta.json`, and `CHANGELOG.md`) and compares it against the fingerprint stored in `.clawhub/origin.json` from the last publish. If they match, nothing is published.

### 2. Version Bumping

- **patch** (default): 0.1.0 → 0.1.1
- **minor**: 0.1.0 → 0.2.0
- **major**: 0.1.0 → 1.0.0
- **dev**: 0.1.1-dev.202608011200 (timestamped, tagged "dev")

### 3. Doc Sync

After version bump:
- `SKILL.md` frontmatter `version:` field updated
- `_meta.json` version and `publishedAt` updated
- `skill-card.md` version line updated
- `CHANGELOG.md` prepended with new entry

### 4. Publishing

Calls `clawhub publish` with the new version and changelog. On failure, version files are rolled back automatically.

### 5. Fingerprint Update

On success, `.clawhub/origin.json` is updated with the new fingerprint and version, preventing duplicate publishes.

## CI/CD Integration

### GitHub Actions

The workflow at `.github/workflows/camsnap-publish.yml`:
- Triggers on push to `main`/`master` when `skills/camsnap/**` changes
- Can be manually triggered with bump type selection
- Commits version bumps back to the repo

**Setup:** Add `CLAWHUB_TOKEN` as a repository secret.

### Git Hook

The pre-push hook auto-detects changes and publishes before push:

```bash
# Install
ln -sf ../../skills/camsnap/scripts/git-hooks/pre-push .git/hooks/pre-push

# Skip if needed
git push --no-verify
```

### Cron (optional)

```bash
# Check for unpublish changes hourly
0 * * * * cd /path/to/workspace && ./skills/camsnap/scripts/camsnap-autopublish.sh --bump patch
```

## Safety Features

- **Idempotent**: Running twice without changes does nothing (fingerprint match)
- **Rollback**: Failed publish rolls back version file changes
- **Dry run**: `--dry-run` previews all actions
- **Dev tags**: Quick publishes use `--tags dev` so they don't replace `latest`
- **Force override**: `--force` flag bypasses fingerprint check when needed
