# Signal Dreaming V3 Protocol

Follow every gate in order. Candidate work happens outside indexed memory. Any failed deterministic gate means no live commit.

## 1. Invariants

1. Keep one owner for `MEMORY.md`, L2 files, and the dream diary.
2. Keep daily logs immutable and indexed in place.
3. Keep `MEMORY.md` as a current-state index; keep detail in L2.
4. Preserve lifecycle state and human authority over automation.
5. Omit secrets and unnecessary private detail.
6. Back up every planned existing file before the first write.
7. Treat state as a rebuildable cursor, never as a factual source.
8. Leave incomplete work visible; never silently overwrite it.

## 2. Phase 0 — Preflight

Collect `openclaw --version`, the public Dreaming config value, and
`openclaw cron list --all --json` with the fixed commands in `SKILL.md`.
Run `preflight.mjs` in write mode with those three evidence files.
Use raw command output rather than hand-authored evidence.
For a cron or other scheduled invocation, pass `--scheduled`.

It must confirm:

- OpenClaw and Node.js meet the release-candidate floor.
- all three required public CLI commands completed successfully;
- public OpenClaw config and cron JSON fields match the expected types;
- built-in Dreaming is disabled;
- no more than one enabled signal-dreaming writer exists;
- `MEMORY.md`, `memory/`, and `memory/dream-log.md` are safe and available;
- state, backup, plan, and output paths resolve inside the workspace.

Do not repair configuration. Do not continue from a missing field, malformed JSON, schema change, or ownership ambiguity.
Zero enabled writers is allowed only for an explicitly invoked manual run. With `--scheduled`, zero or multiple enabled writers fail closed.


## 3. Phase 1 — Sense

Generate a plan with `delta-state.mjs plan`. It snapshots both daily inputs and `MEMORY.md`.

Daily-log trigger:

- match only top-level `memory/YYYY-MM-DD*.md`;
- detect same-day appends and suffix logs by SHA-256;
- select oldest-first, at most 32 logs and 512 KiB;
- bootstrap only the most recent 7 calendar days when state is absent;
- refuse corrupt or unknown state.

Index-maintenance trigger:

- `0–8192` bytes: healthy;
- `8193–10240` bytes: maintenance when the index changed since its last successful review, when no prior index review exists, or when the last review is at least 7 days old;
- above `10240` bytes: mandatory `compact-first`, regardless of daily-log deltas.

The plan records index SHA-256, bytes, band, previous review, reasons, and run mode. It is a true no-op only when there are no selected daily logs and no index maintenance trigger. An unchanged recently reviewed soft-band index does not trigger a nightly loop.

Use `--full-history` only after explicit human intent. Read only selected daily logs and relevant L2 files. Ignore recall JSON and native Dreaming artifacts.


## 4. Phase 1.5 — Semantic plan

List exact candidate files. Permitted targets remain `MEMORY.md`, `memory/dream-log.md`, and top-level non-date `memory/<topic>.md`.

Apply topic identity, lifecycle, authority, contradiction, and privacy guards. Historical permission is not standing authority. Closed or paused work stays non-active unless newer trusted human evidence reopens it. Never promote credentials or unnecessary personal identifiers.

When index maintenance is required, perform semantic compaction before adding index detail:

1. Keep each active section to one current-status line, two to four decision-critical bullets, and an L2 pointer.
2. Keep closed or paused sections as a short recovery condition plus pointer.
3. Remove or shorten a core fact only when it already exists in L2, is moved to L2 in the same candidate transaction, or is explicitly superseded by newer matching evidence.
4. Preserve current blockers, recovery triggers, permission boundaries, fixed red lines, and identity disambiguation.
5. Prefer L2 detail over raising the byte ceiling.

A hard-band run is `compact-first`: new detail goes to L2 first, and the candidate index must return to at most 10240 bytes before commit. The healthy target remains 8192 bytes.


## 5. Phase 2 — Guard and consolidate in staging

Create a run id, save planner stdout, and call `begin` with the exact target list. It rejects unfinished ownership, backs up every planned existing file, and seeds a private candidate workspace at:

`.backup/memory-dreams/<run-id>/candidate/`

Run `verify-before-write` before editing. It proves that live memory, selected daily inputs, and the candidate base still match the manifest.

Edit only candidate paths. Never edit live memory during this phase. Do not edit the candidate diary manually; finalization renders it deterministically.

If candidate editing fails, call `fail`. Before live commit this becomes `candidate_rejected`, releases the lock, leaves live memory untouched, and does not advance state.


## 6. Phase 3 — Settle

Prepare the canonical diary entry JSON. Use the maximum valid Dream number plus one.

`finalize` verifies live scope, audits the candidate, requires semantic confirmation for L2, rejects maintenance-only no-progress, renders the diary inside staging, audits again, rechecks live hashes, commits L2 then `MEMORY.md` then diary, advances state with the successful index hash/bytes/review time, and removes the lock.

A candidate above 10240 bytes is rejected. A successful candidate in the soft band records a warning. Necessary current state and authority boundaries must not be deleted merely to hit an exact byte count.


## 7. Deterministic audit

Candidate and commit checks verify workspace containment, symlink safety, backup hashes, zero unplanned candidate changes, zero concurrent live or daily-log changes, every planned candidate, index size and maintenance progress, resolving pointers, canonical diary headings, and suspected credential categories by filename/category only.

The audit cannot decide semantic identity, lifecycle, authority, contradiction, or privacy nuance. Review candidate L2 files before confirming semantic review.


## 8. Candidate rejection and incomplete runs

Manifest states:

- `started` / `backed_up` / `staged`: transaction preparation;
- `candidate_rejected`: candidate failed before live commit; live memory is unchanged and the run is terminal;
- `ready_to_commit`: candidate passed and live commit is starting;
- `committed`: all planned files, diary, state, and manifest completed;
- `incomplete`: live commit may be partial or a legacy live-edit run needs reconciliation.

Only active, stale, or unreviewed incomplete work blocks a later run. Candidate rejection keeps evidence but releases the lock. Never auto-restore over later human edits.

For an incomplete run, inspect the manifest and backups, reconcile live files manually, then acknowledge the exact run id. State quarantine remains hash-confirmed and bounded as documented in `SKILL.md`.

## 9. Upgrade and rollback boundary

For v1.3.1:

- preserve daily logs, L2, `MEMORY.md`, and `memory/dream-log.md`;
- allow missing V3 state to enter the 7-day bounded bootstrap;
- derive the next diary number from the maximum valid heading;
- do not consume or migrate recall JSON.

Rolling back the skill package does not automatically remove V3 state or manifests. Treat package rollback, cron changes, configuration changes, and production validation as separately authorized operations.
