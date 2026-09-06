---
name: commit-helper
description: Generate conventional commit messages from staged git changes. Use when you need help writing a clear, structured commit message from git diff. Supports feat/fix/docs/refactor/chore/test/perf/ci/build/scopes.
metadata:
  openclaw:
    emoji: "📝"
---

# Commit Helper

Generate a conventional commit message from your staged changes.

## When to use

- You have staged changes and need a commit message
- You want structured conventional commits (feat:, fix:, etc.)
- You're unsure what type or scope to use

## Prerequisites

- `git` available in PATH
- Changes are staged (`git add`)

## Steps

1. Run `git diff --cached --stat` to see what changed
2. Run `git diff --cached` for full staged diff
3. Classify changes:
   - `feat:` new feature
   - `fix:` bug fix
   - `docs:` documentation only
   - `refactor:` code change that neither fixes a bug nor adds a feature
   - `perf:` performance improvement
   - `test:` adding or fixing tests
   - `chore:` build process, tooling, or library changes
   - `ci:` CI configuration changes
   - `build:` build system or dependency changes
4. Determine scope from changed paths (e.g., `auth`, `api`, `ui`, `deps`)
5. Write subject line in imperative mood, ≤72 chars
6. Add body explaining **why** if the change is non-trivial
7. Present the commit message and offer to commit

## Output format

```
<type>(<scope>): <imperative-subject>

<optional body — explain motivation, not mechanics>
```

## Examples

```
feat(auth): add email verification flow

fix(api): handle empty response from payment webhook

docs(readme): update installation instructions

refactor(db): extract query builder into separate module
```

## Notes

- Never use past tense ("added" → "add")
- Don't end the subject line with a period
- Keep the subject under 72 characters
- Use the body to explain what and why, not how
- If the diff is large, summarize major categories first
