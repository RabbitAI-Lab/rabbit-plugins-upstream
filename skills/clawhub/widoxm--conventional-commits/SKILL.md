---
name: conventional-commits
description: Write git commit messages that follow the Conventional Commits spec. Use whenever the user asks to write, draft, or improve a commit message, or says "commit".
---

# Conventional Commits

Write concise, conventional commit messages based on the current diff.

## Format

```
<type>(<scope>): <subject>

<body>       # optional, explain the "why"
<footer>     # optional, e.g. "BREAKING CHANGE: ..." or issue refs
```

## Types

- `feat` — new feature
- `fix` — bug fix
- `docs` — documentation only
- `style` — formatting, no logic change
- `refactor` — code change that neither fixes a bug nor adds a feature
- `perf` — performance improvement
- `test` — adding/updating tests
- `build` — build system or external dependencies
- `ci` — CI configuration
- `chore` — other maintenance

## Rules

1. Subject is imperative, present tense, no trailing period (e.g. "add", not "added" or "adds").
2. Keep the subject under 72 characters.
3. Include `scope` only when it clarifies the affected area.
4. Body explains *why*, not *what* — the diff already shows what.
5. Separate subject from body with a blank line.

## Workflow

1. Read the diff: `git diff` (staged) or `git diff HEAD`.
2. Identify the single primary intent — pick one `type`.
3. Draft the message, then apply the rules above.
4. Output only the final message in a fenced code block for easy copy-paste.
