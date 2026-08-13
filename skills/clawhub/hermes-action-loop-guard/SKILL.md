---
name: "hermes-action-loop-guard"
description: "Adds pytest-free deterministic verification for tool progress guard installs."
---

# Hermes Action Loop Guard

Use the bundled installers for deterministic changes. Never hand-edit a live Hermes installation when preflight reports an unsupported layout.

## Workflow

1. Identify the target host, `HERMES_HOME`, Hermes source directory, and gateway service.
2. Run `bash scripts/install-hermes-action-guard.sh status`.
3. Run `bash scripts/install-hermes-action-guard.sh test-compat`; both supported source-layout fixtures must pass.
4. Inspect the affected session read-only: message/token count, recent `finish_reason`, tool calls per turn, repeated failures or repeated successful results, compression, and reset policy.
5. Classify it as `promise_stop`, `tool_failure_loop`, `tool_no_progress_loop`, or `polluted_session`.
6. For promise-only stalls, use `install-hermes-action-guard.sh`. For real tool-call loops, use `install-hermes-tool-progress-guard.sh`.
7. Run the relevant installer with `install --dry-run`. Stop if any source anchor is missing or ambiguous.
8. Run `install`. The installer creates a timestamped manifest backup, stops the gateway only for the patch window, compile-checks Python, runs focused tests, restores automatically on error, and restarts only if it was active before.
9. Run `verify`, then confirm the messaging WebSocket reconnects.
10. Validate with fixtures covering repeated failures, repeated successful-but-identical results, real progress, and total per-turn caps.
11. After a Hermes upgrade, rerun status, compatibility tests, and dry-run before reinstalling.

## Tool progress policy

When hard stops are enabled:

- Block an identical failed call at the configured failure threshold.
- Treat repeated calls with the same tool name, canonical arguments, and identical normalized result as no progress even when the tool reports success.
- Apply successful-result no-progress detection to configured tools including `execute_code`; do not rely on a tool's mutating classification alone.
- Reset the successful no-progress streak when arguments or normalized results change, or when a verified file mutation lands.
- Enforce a configurable total tool-call cap per user turn.
- On halt, return a specific blocker and end the turn; do not compress and replay the polluted turn.

Recommended smallclaw thresholds: identical failure 3, successful identical no-progress 3, same-tool failure 5, and total calls 20.

## Explicit rollback

Use the exact backup path printed by the relevant installer:

`bash scripts/<installer>.sh rollback --backup /exact/backup/path`

Rollback restores only manifest-recorded targets, compile-checks restored Python, and restores the gateway's prior active/inactive state.

## Safety

- Promise recovery is bounded to two nudges per user turn.
- Do not intercept questions, completed actions, failures, or explicit blockers.
- Successful-result detection must require the same tool, same canonical arguments, and the same normalized result.
- Never reset every session globally.
- Session reset requires exact route evidence and recoverable backup.
- A compatibility failure is fail-closed; do not patch an unknown Hermes version.
