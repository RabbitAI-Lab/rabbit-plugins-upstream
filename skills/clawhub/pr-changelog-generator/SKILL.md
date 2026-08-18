---
name: pr-changelog-generator
version: "1.0.0"
category: devops
tags:
  - git
  - github
  - pull-request
  - changelog
  - release-notes
  - documentation
  - automation
model: claude-sonnet-4-20250514
trigger_keywords:
  - PR description
  - pull request
  - changelog
  - release notes
  - commit message
  - git log
  - version release
  - semantic version
  - conventional commits
  - release draft
pricing: "$5.99 one-time"
---

# PR Description & Changelog Generator

> **Generate professional pull request descriptions, semantic changelogs, and release notes from git history.** Follows Conventional Commits spec, auto-categorizes changes, includes breaking change detection, and produces ready-to-publish release notes.

## Why This Skill Exists

Developers waste 5-10 minutes per PR writing descriptions from memory. Release notes are often incomplete or inconsistent. This skill analyzes the actual git diff and commit history to produce structured, accurate documentation that matches your team's house style.

## When to Activate

Activate when the user:
- Creates a pull request or asks for a PR description
- Requests a changelog or release notes
- Mentions semantic versioning, conventional commits, or release drafting
- Says "what changed since last release" or "summarize these commits"
- Runs `git log` and wants a human-readable summary

## Workflow

### Step 1: Analyze Git Context

Gather the following:
- **Current branch** and **base branch** (usually main/master)
- **Commit history** between base and current branch (`git log base..HEAD`)
- **Full diff** (`git diff base...HEAD`)
- **Changed files** list with additions/deletions
- **Existing CHANGELOG.md** (if present) to match format
- **Recent PRs** for style reference

### Step 2: Categorize Changes

Parse each commit and diff hunks to categorize into:

| Category | Prefix | Description |
|----------|--------|-------------|
| `feat` | ✨ New Features | New user-facing functionality |
| `fix` | 🐛 Bug Fixes | Fixes for existing issues |
| `breaking` | 💥 Breaking Changes | Changes that break backward compatibility |
| `perf` | ⚡ Performance | Performance improvements |
| `refactor` | ♻️ Refactor | Code restructuring without behavior change |
| `security` | 🔒 Security | Security-related fixes |
| `docs` | 📝 Documentation | Documentation changes |
| `test` | 🧪 Tests | Test additions or fixes |
| `chore` | 🔧 Maintenance | Build, deps, config changes |
| `ci` | 👷 CI/CD | Pipeline changes |
| `i18n` | 🌐 Internationalization | Translation updates |
| `revert` | ⏪ Reverts | Reverted changes |

### Step 3: Generate PR Description

```markdown
## Summary

[1-2 sentence high-level summary of what this PR does and why]

## Changes

### ✨ New Features
- Added `user.avatar` field to profile API response
- Implemented dark mode toggle in settings page

### 🐛 Bug Fixes
- Fixed race condition in WebSocket reconnection logic
- Resolved incorrect tax calculation for EU markets

### 💥 Breaking Changes
- `POST /api/users` now requires `email_verified: true` field
- Removed deprecated `GET /api/v1/users` endpoint (use v2)

### 🔒 Security
- Patched dependency vulnerability in `lodash@4.17.15` → `4.17.21`

## Testing
- [x] Unit tests pass (247 passed, 0 failed)
- [x] E2E tests pass for affected flows
- [x] Manual QA on staging environment
- [ ] Performance regression test

## Screenshots / Recordings
[If UI changes, describe what to look for]

## Checklist
- [x] Self-reviewed code
- [x] Added/updated tests
- [x] Updated documentation
- [x] No new warnings in CI
- [ ] Approved by team lead
```

### Step 4: Generate Changelog Entry

Match the format of existing CHANGELOG.md, or use default:

```markdown
## [1.4.2] - 2026-08-11

### ✨ Added
- User avatar upload with automatic resizing and CDN sync
- Dark mode preference persisted across sessions

### 🐛 Fixed
- WebSocket reconnection race condition causing duplicate messages
- EU tax calculation rounding error on invoices > €1,000

### 💥 Breaking
- `POST /api/users` now requires `email_verified: true`
- Removed deprecated `GET /api/v1/users` (replaced by v2)

### 🔒 Security
- Upgraded lodash to 4.17.21 (CVE-2021-23337)

### ♻️ Refactored
- Extracted tax calculation into `TaxService` for testability
- Consolidated WebSocket event handlers into single emitter
```

### Step 5: Suggest Semantic Version Bump

Based on changes detected:
- **Major** (x.0.0): Any breaking change
- **Minor** (x.y.0): New features, no breaking changes
- **Patch** (x.y.z): Bug fixes only

Output:
```
Recommended version: 1.4.2 → 1.5.0
Reason: Minor — new features added (avatar upload, dark mode), one breaking change detected (email_verified required)
If breaking change is acceptable → 2.0.0
```

### Step 6: Generate Release Notes (for GitHub Releases page)

```markdown
# Release v1.5.0

## 🎉 What's New
- **User Avatars**: Upload and manage profile pictures with automatic resizing
- **Dark Mode**: System-wide dark theme with automatic sunset/sunrise switching

## 🐛 Fixes
- Resolved WebSocket duplicate message issue on reconnect
- Fixed EU tax calculation rounding errors

## ⚠️ Breaking Changes
- `POST /api/users` now requires `email_verified: true` field
- Removed deprecated v1 users endpoint

## 📦 Dependencies
- lodash: 4.17.15 → 4.17.21 (security)

## 🙏 Contributors
- @username1 (5 commits)
- @username2 (3 commits)
```

## Output Constraints

- PR description: max 500 words, scannable in 30 seconds
- Changelog: follow existing file format if present, otherwise use default template
- Release notes: celebratory tone for features, clinical tone for fixes
- All code references must include file:line
- Breaking changes MUST be called out at the top, not buried
- Contributor list from `git shortlog -sn base..HEAD`

## What This Skill Does NOT Do

- Does not create PRs or releases via API (generates text only)
- Does not run tests or validate code quality
- Does not replace human review of changes
