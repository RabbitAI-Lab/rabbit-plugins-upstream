# Best Practices

Source: <https://antigravity.google/docs/cli/best-practices/>. Permission preset behavior: `references/security-permissions.md`.

## Verify, then edit

Give the agent a test, build, or formatter.

1. Confirm the workspace has a test suite.
2. If it does not, ask for the test first.
3. After the change, tell it to run that command and iterate on the output.

```text
Implement feature X in main.py. Run npm test afterward to verify the build.
```

Hard change, in order: explore how the code already solves it; ask for a plan artifact listing files, dependencies, and logic changes (`/plan`); approve; then apply.

```text
Explore how our router resolves `/docs/:page`. Write down an implementation plan to add `/docs/best-practices`.
```

## Context and local rules

`@` inserts a file or directory as a full path: <https://antigravity.google/docs/at-mentions?tab=cli>. For a visual bug, copy a screenshot or recording and press `Ctrl+V`.

A workspace-root `GEMINI.md` or `AGENTS.md` is read on startup. Put directory standards, style, test commands, and deprecation warnings there.

Presets named on this page: `request-review` (default; prompt before writes, Bash, and network), `proceed-in-sandbox` (safe sandboxed commands run; risky ones prompt), `strict` (prompt for every non-read). `always-proceed` is in the settings catalog but is not recommended here. `--dangerously-skip-permissions` stays off unless the skill workflow's risk condition is met.

```json
{
  "toolPermission": "proceed-in-sandbox",
  "enableTerminalSandbox": true
}
```

## Recover, then automate

`Esc` interrupts a bad turn. `/rewind` or `/undo` rolls back after a run of bad edits. For an uncertain approach: stabilize, `/fork`, try it, and `/resume` the stable thread if it fails.

One-shot mode fits hooks and pipelines. The official example passes `--cwd`; follow the skill gotcha and launch `agy` from the repo.

```bash
agy -p "Review this git diff and draft a conventional commit message"
```

For a wide sweep, have the primary agent spawn background subagents and keep the main screen. `/agents` monitors them.
