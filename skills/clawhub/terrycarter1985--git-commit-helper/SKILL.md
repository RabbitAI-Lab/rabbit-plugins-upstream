---
name: git-commit-helper
description: >
  Generate conventional commit messages from git diffs and staged changes.
  Use when: (1) user asks to write/generate/commit a commit message, (2) running
  git commit and needs a message, (3) user asks "what should my commit message be?"
  or "help me commit", (4) preparing changes for a PR and the commit message
  follows Conventional Commits format. NOT for: running git commands directly
  (use exec for that), rebasing, or resolving merge conflicts.
---

# Git Commit Helper

Generate high-quality Conventional Commit messages from staged or unstaged diffs.

## Quick Start

1. Get the diff: `git diff` (unstaged) or `git diff --cached` (staged)
2. Analyze the changes and classify the type (see Types below)
3. Write a concise message following the format
4. Present to user or pass to `git commit -m`

## Commit Message Format

```
<type>(<scope>): <subject>

<body>
```

- **type** (required): one of the Types listed below
- **scope** (optional): affected area/module, e.g. `auth`, `api`, `db`
- **subject** (required): imperative mood, ≤72 chars, no trailing period
- **body** (optional): what & why, not how; wrap at 72 chars

## Types

| Type     | Meaning                                      |
|----------|----------------------------------------------|
| feat     | New feature                                  |
| fix      | Bug fix                                      |
| docs     | Documentation only                           |
| style    | Formatting, no logic change                  |
| refactor | Code change, no feature/fix                  |
| perf     | Performance improvement                      |
| test     | Adding or correcting tests                   |
| build    | Build system or dependency changes           |
| ci      | CI configuration changes                     |
| chore    | Maintenance, no production code change       |
| revert   | Reverting a previous commit                  |

## Steps

1. Run `git diff --cached` first; if empty, fall back to `git diff`
2. Classify the change type using the table above
3. Identify scope from filenames/paths when obvious
4. Write the subject line in imperative mood
5. If the diff is large (>50 lines), add a body summarizing key changes
6. Present the final message to the user

## Script

Use `scripts/analyze_diff.py` to extract structured info from a diff:

```bash
python3 scripts/analyze_diff.py <diff-file>
# or pipe from stdin:
git diff --cached | python3 scripts/analyze_diff.py
```

Outputs JSON with: changed files, added/removed lines, likely commit type,
and suggested scope.

## Examples

**Small fix:**
```
fix(auth): handle null token in middleware
```

**Feature:**
```
feat(api): add pagination to /v1/users endpoint

Adds cursor-based pagination with limit param. Defaults to 20 per page.
Requires auth header.
```

**Docs:**
```
docs(readme): update installation steps for v2
```

## Rules

- Always use imperative mood ("add", not "added" or "adds")
- Subject ≤72 characters
- No period at end of subject
- Use `!` after type/scope for breaking changes: `feat(api)!: remove v1 endpoints`
- Prefer specificity over generic "update files"
