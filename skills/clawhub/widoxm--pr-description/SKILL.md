---
name: pr-description
description: Draft a pull request description from the current branch's diff. Use when the user asks for a PR description, a merge request summary, or "what does this change do".
---

# PR Description

Generate a clear, review-friendly pull request description from the diff.

## Workflow

1. Get the diff against the base branch:
   - `git diff <base>...HEAD` (commits on this branch)
   - `git log <base>..HEAD --oneline` for the commit list
2. Summarize the change set into a template.

## Template

```markdown
## Summary
<!-- One or two sentences: what this change does and why. -->

## Changes
<!-- Bullet list of the notable changes. -->

## Testing
<!-- How was this verified: commands run, tests, manual steps. -->

## Notes / Follow-ups
<!-- Anything a reviewer should know, or deferred work. -->
```

## Rules

1. Lead with the *outcome*, not a list of files — a reviewer reads this first.
2. Keep bullets one line, imperative and specific.
3. Do not restate the code; explain intent and any non-obvious decisions.
4. Flag breaking changes and anything risky under "Notes".
5. If there are no tests, say so explicitly rather than omitting the section.
