---
name: "hermes-action-loop-guard"
description: "Diagnose and repair Hermes promise-only action stalls, repeated failures, and polluted sessions."
---

# Hermes Action Loop Guard

Use the bundled installer for deterministic changes. Never hand-edit a live Hermes installation when preflight reports an unsupported layout.

## Workflow

1. Identify the target host, `HERMES_HOME`, Hermes source directory, and gateway service.
2. Run `bash scripts/install-hermes-action-guard.sh status`.
3. Run `bash scripts/install-hermes-action-guard.sh test-compat`; both supported source-layout fixtures must pass.
4. Inspect the affected session read-only: message/token count, recent `finish_reason`, tool calls per turn, repeated failures, compression, and reset policy.
5. Classify it as `promise_stop`, `tool_failure_loop`, or `polluted_session`.
6. Run `install --dry-run`. Stop if the source anchor is missing or ambiguous.
7. Run `install`. The installer creates a timestamped manifest backup, preserves whether the guard file preexisted, stops the gateway only for the patch window, compile-checks Python, restores automatically on error, and restarts only if it was active before.
8. Run `verify`, then confirm the messaging WebSocket reconnects.
9. Validate using an action request. Success requires a real tool call with execution evidence or a specific blocker; promise-only narration is failure.
10. After a Hermes upgrade, rerun `status`, `test-compat`, and `install --dry-run` before reinstalling.

## Explicit rollback

Use the exact backup path printed by install:

`bash scripts/install-hermes-action-guard.sh rollback --backup /exact/backup/path`

Rollback reads the backup manifest, restores only the recorded config/source/guard targets, compile-checks restored Python, and restores the gateway's prior active/inactive state. Never guess a backup or roll back all Hermes state globally.

## Safety

- Recovery is bounded to two nudges per user turn.
- Trigger only on a high-confidence action request plus unfinished promise.
- Do not intercept questions, completed actions, failures, or blockers.
- Never reset every session globally.
- Session reset requires exact route evidence and recoverable backup.
- A compatibility failure is fail-closed; do not patch an unknown Hermes version.
