---
name: changelog-writer
version: 1.0.0
description: Write a user-facing changelog from a commit range or release notes: grouped, plain-language, honest about breaking changes. Use at every release.
---

# Changelog Writer

## Overview

Developers write commits for themselves; changelogs are for users. This workflow translates a raw commit list into grouped, plain-language entries that say what changed for the reader — and never hides a breaking change in the middle.

## When to use

At release time, or when maintaining a public changelog for a product or tool.

## Workflow

1. **Collect the raw changes** — commits, PRs, issues closed in the range
2. **Filter for user impact** — drop refactors, chores and internal cleanups unless they change behavior
3. **Group** — New, Improved, Fixed, Deprecated, Removed, Security
4. **Translate each entry** — what the user can now do, or what changed for them, in one sentence, no internal codenames
5. **Surface breaking changes** — first in the document, with the migration step spelled out
6. **Version and date it** — matching the actual release tag

## Guardrails

- Never describe unshipped or partially working features as released
- Security fixes get their own section even when details must stay vague
- If a fix repairs something a previous changelog claimed worked, say so plainly

## Output format

A changelog entry: version, date, grouped sections, breaking changes first with migration steps.

---

Part of the Manteclaw free skill series. These workflow skills are free forever; Manteclaw's paid automation tools (runnable code, not just prompts) live at payhip.com/Manteclaw.
