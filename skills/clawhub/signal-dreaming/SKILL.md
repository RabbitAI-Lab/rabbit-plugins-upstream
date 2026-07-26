---
name: "signal-dreaming"
description: "Safe single-owner bounded memory consolidation with guarded backups, recovery, and deterministic audits."
---

# Signal Dreaming

Consolidate daily logs into L2 topic files and a compact `MEMORY.md` index. Preserve the proven v1.3.1 `Sense → Consolidate → Settle` model while adding deterministic P0 safety guards.

Release candidate: `3.0.0-rc.1`.

## Ownership contract

Use exactly one memory consolidation writer.

- Require built-in OpenClaw Dreaming to be disabled before any write.
- Refuse write mode when more than one enabled signal-dreaming cron is visible.
- Treat missing CLI fields, schema drift, unsafe paths, or ambiguous ownership as read-only failures.
- Never modify OpenClaw configuration, cron, Gateway, another agent, or memory-core internals.
- Do not read private plugin state, SQLite, recall locks, `DREAMS.md`, `memory/dreaming/**`, or `memory/.dreams/**`.

Collect three fixed read-only public CLI outputs into a private temporary directory, then run preflight:

```bash
openclaw --version > <EVIDENCE_DIR>/version.txt
openclaw config get plugins.entries.memory-core.config.dreaming.enabled --json > <EVIDENCE_DIR>/dreaming.json
openclaw cron list --all --json > <EVIDENCE_DIR>/cron.json
node <SKILL_DIR>/scripts/preflight.mjs <WORKSPACE_ROOT> \
  --version-file <EVIDENCE_DIR>/version.txt \
  --dreaming-file <EVIDENCE_DIR>/dreaming.json \
  --cron-file <EVIDENCE_DIR>/cron.json
```

If any collection command fails, stop. Keep evidence local; do not paste cron payloads into chat.
Create the evidence directory with owner-only permissions and remove it after preflight.
Use the raw command outputs; do not hand-author alternative evidence schemas.

Use `--read-only` only for diagnosis when built-in Dreaming is enabled. A read-only pass does not authorize writes.
Zero scheduled writers is acceptable for an explicitly invoked manual run and produces a warning. Every scheduled invocation must add `--scheduled`; it then fails unless exactly one enabled writer is visible.

## Runtime support

- Minimum and tested OpenClaw: `2026.7.1-2`.
- Minimum and tested Node.js: `22.23.1`.
- Tested platform for this release candidate: macOS arm64.
- Linux and Windows are not supported by `3.0.0-rc.1` until their isolated acceptance matrices pass.
- No third-party npm packages or Bash runtime are required.

Future OpenClaw releases may work only when the public CLI fields still match the validated contract. Unknown fields fail closed.

## Durable model

- `memory/YYYY-MM-DD*.md` — immutable daily source logs; never move, delete, or edit.
- `memory/<topic>.md` — durable L2 topic detail.
- `MEMORY.md` — compact current-state index and L2 pointers.
- `memory/dream-log.md` — human-readable diary, at most 30 entries.
- `logs/signal-dreaming/state.json` — rebuildable hash cursor outside memory indexing.
- `.backup/memory-dreams/<run-id>/manifest.json` — run status, plan, hashes, and backup map.

Do not depend on recall JSON. Detect work from daily-log SHA-256 changes, including same-day appends and suffixed logs.

## Workflow

Read `references/dream-protocol.md` completely before a write run.

1. Run `preflight.mjs`.
2. Generate a read-only delta plan:

   ```bash
   node <SKILL_DIR>/scripts/delta-state.mjs plan <WORKSPACE_ROOT> > <PLAN_FILE>
   ```

   `<PLAN_FILE>` is the saved JSON file path passed to `begin`.

3. Inspect the saved plan. Stop with zero writes when it says `"noop": true`.
   `"batchCapped": true` means additional eligible logs were deferred by the per-run count or byte ceiling; it does not describe the 7-day bootstrap window.
4. Read only the selected daily logs and relevant L2 files. Build an exact list of intended L2 and `MEMORY.md` changes.
5. Create a unique run id and begin guarded backup:

   ```bash
   node <SKILL_DIR>/scripts/run-guard.mjs create-run-id <WORKSPACE_ROOT>
   node <SKILL_DIR>/scripts/run-guard.mjs begin <WORKSPACE_ROOT> <RUN_ID> <PLAN_FILE> MEMORY.md memory/dream-log.md memory/<topic>.md
   node <SKILL_DIR>/scripts/run-guard.mjs verify-before-write <WORKSPACE_ROOT> <RUN_ID>
   ```

   Copy the exact id printed by `create-run-id` into every `<RUN_ID>` position.

6. Edit only the planned L2 files and `MEMORY.md`. Do not edit `memory/dream-log.md`; finalization appends and trims it deterministically.
7. Prepare the diary entry JSON described in the protocol.
8. Semantically review touched L2 files for topic identity, lifecycle, authority, contradictions, and privacy.
9. Finalize:

   ```bash
   node <SKILL_DIR>/scripts/run-guard.mjs finalize <WORKSPACE_ROOT> <RUN_ID> <ENTRY_JSON> --semantic-review-confirmed
   ```

Finalization audits paths, backups, daily-log immutability, planned-file scope, sizes, pointers, diary numbering, and credential categories before advancing state. Omit `--semantic-review-confirmed` when no L2 file is touched.

## Limits

- Missing state: process only the most recent 7 calendar days.
- Per run: at most 32 daily logs and 512 KiB total input.
- `--full-history` is manual only and still processes one bounded oldest-first batch.
- `MEMORY.md` at `0–8192` bytes is healthy.
- `8193–10240` bytes is a soft warning.
- More than `10240` bytes is a hard failure and cannot commit.

## Failure and recovery

Never start over an active, stale, or unreviewed incomplete run.

- On a known failure, record it:

  ```bash
  node <SKILL_DIR>/scripts/run-guard.mjs fail <WORKSPACE_ROOT> <RUN_ID> <REASON>
  ```

- Inspect `.backup/memory-dreams/<run-id>/manifest.json` and its `files/` backups.
- Restore or reconcile files manually; P0 does not provide automatic rollback.
- Only after human review, acknowledge the exact run id:

  ```bash
  node <SKILL_DIR>/scripts/run-guard.mjs ack-incomplete <WORKSPACE_ROOT> <RUN_ID> --confirm <RUN_ID>
  ```

Acknowledgement does not restore files. It records review and clears only that stale lock.

For `STATE_INVALID` or `STATE_SCHEMA_UNSUPPORTED`, do not delete or edit the state cursor. Inspect its hash, review the file, then quarantine that exact version:

```bash
node <SKILL_DIR>/scripts/delta-state.mjs inspect-state <WORKSPACE_ROOT>
node <SKILL_DIR>/scripts/delta-state.mjs quarantine-state <WORKSPACE_ROOT> --confirm <STATE_SHA256>
```

Quarantine verifies a recoverable `.bak` copy under `.backup/memory-dreams/state-recovery/` before removing the active cursor. The next plan uses the normal bounded 7-day bootstrap.

Run a standalone read-only audit when needed:

```bash
node <SKILL_DIR>/scripts/dream-audit.mjs <WORKSPACE_ROOT>
```

Run the isolated acceptance suite:

```bash
node <SKILL_DIR>/scripts/self-test.mjs
```

## Scheduling

Provide cron only as a template; never create or modify it automatically. Schedule one isolated agent turn and include the workspace root. The job must run preflight and stop on no-op or any ambiguity.

```json
{
  "name": "signal-dreaming-v3-daily",
  "schedule": { "kind": "cron", "expr": "<MINUTE> <HOUR> * * *", "tz": "<TIMEZONE>" },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "timeoutSeconds": 900,
    "message": "Run signal-dreaming as a scheduled invocation. Read its SKILL.md and references/dream-protocol.md completely. Workspace root: <WORKSPACE_ROOT>. Run preflight with --scheduled. Stop on preflight failure, no-op, ambiguity, or an unfinished run."
  },
  "delivery": { "mode": "announce", "channel": "<CHANNEL>", "to": "<TARGET>" }
}
```

For a v1.3.1 upgrade, leave existing memories and diary in place. Missing V3 state triggers the bounded 7-day bootstrap; diary numbering uses the maximum valid existing Dream number plus one.
