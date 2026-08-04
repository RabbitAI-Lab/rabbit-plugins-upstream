---
name: "signal-dreaming"
description: "Safe single-owner staged memory consolidation with autonomous bounded index compaction."
---

# Signal Dreaming

Consolidate daily logs into L2 topic files and a compact `MEMORY.md` index. Preserve the proven v1.3.1 `Sense → Consolidate → Settle` model while adding deterministic P0 safety guards.

Release candidate: `3.0.0-rc.3`.

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
- Linux and Windows are not supported by `3.0.0-rc.3` until their isolated acceptance matrices pass.
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
2. Generate and save a read-only plan:

   ~~~bash
   node <SKILL_DIR>/scripts/delta-state.mjs plan <WORKSPACE_ROOT> > <PLAN_FILE>
   ~~~

   The planner combines changed daily logs and index maintenance. Stop only when `"noop": true`. A hard-limit index must produce a non-noop `compact-first` plan even when no daily log changed.
3. Read selected daily logs and relevant L2 files. When `plan.index.maintenanceRequired` is true, prioritize semantic compaction: keep current state, recovery conditions, authority boundaries, and L2 pointers; move detail to L2 before removing it from the index.
4. Begin the guarded candidate transaction:

   ~~~bash
   node <SKILL_DIR>/scripts/run-guard.mjs create-run-id <WORKSPACE_ROOT>
   node <SKILL_DIR>/scripts/run-guard.mjs begin <WORKSPACE_ROOT> <RUN_ID> <PLAN_FILE> MEMORY.md memory/dream-log.md memory/<topic>.md
   node <SKILL_DIR>/scripts/run-guard.mjs verify-before-write <WORKSPACE_ROOT> <RUN_ID>
   ~~~

5. Edit only the manifest's candidate files under `.backup/memory-dreams/<RUN_ID>/candidate/`. Never edit live `MEMORY.md`, live L2, or the diary during the candidate phase.
6. Prepare the diary entry JSON and semantically review candidate L2 files.
7. Finalize:

   ~~~bash
   node <SKILL_DIR>/scripts/run-guard.mjs finalize <WORKSPACE_ROOT> <RUN_ID> <ENTRY_JSON> --semantic-review-confirmed
   ~~~

Finalization audits the candidate, rechecks every live hash, renders the diary in the candidate tree, then commits planned files and advances state. Candidate rejection leaves live memory untouched. Omit `--semantic-review-confirmed` only when no L2 candidate is touched.


## Limits

- Missing state: process only the most recent 7 calendar days.
- Per run: at most 32 daily logs and 512 KiB total input.
- `--full-history` is manual only and remains bounded.
- `MEMORY.md` at `0–8192` bytes is healthy.
- `8193–10240` bytes is a soft trimming band.
- More than `10240` bytes is a hard failure for candidates and a mandatory `compact-first` trigger for the planner.
- A soft-band index triggers maintenance when it changed since the last successful review or that review is at least 7 days old. An unchanged recently reviewed soft-band index does not loop nightly.
- A maintenance-only candidate must reduce `MEMORY.md`; otherwise reject it without writing a diary or advancing state.


## Failure and recovery

Manifest states distinguish candidate failure from uncertain live state.

- `candidate_rejected`: deterministic candidate failure; live memory was not changed, the lock is released, and no acknowledgement is required.
- `incomplete`: a live commit may be partial or an older live-edit run needs reconciliation. Inspect backups and live hashes before acknowledgement.
- `committed`: candidate audit, live hash recheck, planned-file commit, diary, and state all completed.

Never start over an active, stale, or unreviewed incomplete run. For an incomplete run:

~~~bash
node <SKILL_DIR>/scripts/run-guard.mjs ack-incomplete <WORKSPACE_ROOT> <RUN_ID> --confirm <RUN_ID>
~~~

Acknowledgement records review; it does not restore files.

Inventory retained V2 and V3 transactions without mutating them:

~~~bash
node <SKILL_DIR>/scripts/transaction-list.mjs <WORKSPACE_ROOT>
~~~

The inventory accepts legacy V2 `workspace/entries` manifests and V3 `root/plannedFiles` manifests. It recognizes the legacy backup lock directory and the V3 `logs/signal-dreaming/run.lock` file, fails closed when both lock formats are present, and rejects mixed or conflicting manifest identities. V3 results are diagnostic only and never emit automatic rollback commands.

For `STATE_INVALID` or `STATE_SCHEMA_UNSUPPORTED`, inspect and quarantine only the exact reviewed state hash:

~~~bash
node <SKILL_DIR>/scripts/delta-state.mjs inspect-state <WORKSPACE_ROOT>
node <SKILL_DIR>/scripts/delta-state.mjs quarantine-state <WORKSPACE_ROOT> --confirm <STATE_SHA256>
~~~

Run standalone audit and isolated acceptance tests with:

~~~bash
node <SKILL_DIR>/scripts/dream-audit.mjs <WORKSPACE_ROOT>
node <SKILL_DIR>/scripts/self-test.mjs
~~~

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
