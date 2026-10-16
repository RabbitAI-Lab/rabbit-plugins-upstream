---
name: git-commit-message-helper
description: >
  Suggest conventional-commit messages from a staged diff summary. Use when
  the user asks for a commit message after staging changes.
metadata: {"clawdbot":{"emoji":"💬","requires":{"bins":["git"]}}}
---

# Git Commit Message Helper

## Purpose / Overview
Produces a short conventional-commit subject (+ optional body) from changes.

## When to Use
- User says "write a commit message"
- After `git add` when they paste `git diff --cached --stat`

## Usage / Instructions
1. Prefer user-provided diff/stat; if missing, ask them to paste it.
2. Choose type: feat|fix|docs|refactor|test|chore.
3. Subject ≤ 72 chars, imperative mood, no trailing period.
4. Offer one primary message and two short alternatives.

## Examples
Input stat: "auth/login.ts | 12 +++++"
Output: `fix(auth): handle empty password field`

## Requirements / Dependencies
git (optional; only if the user wants you to run `git diff --cached --stat`).

## Limitations / Caveats
Does not commit or push.

## Security / Permissions
May run read-only git commands the user approves. No network.

## Attribution / License
MIT-0
