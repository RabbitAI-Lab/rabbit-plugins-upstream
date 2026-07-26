# Signal Dreaming V3 Protocol

Follow every gate in order. Any failed deterministic gate means no further live writes.

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

Generate a delta plan with `delta-state.mjs plan`.

The planner:

- matches only top-level `memory/YYYY-MM-DD*.md`;
- hashes file content instead of relying on dates or mtimes;
- detects same-day appends and new suffix logs;
- ignores recall JSON and native Dreaming artifacts;
- selects changed logs oldest-first;
- returns at most 32 logs and 512 KiB per run;
- uses only the most recent 7 calendar days when state is absent;
- persists that bootstrap cutoff so older unprocessed history remains manual;
- refuses corrupt or unknown state rather than guessing;
- reports a read-only no-op when no hash changed.

The plan field `"batchCapped": true` means additional eligible logs were deferred by the per-run count or byte ceiling. It is independent of the 7-day bootstrap window.

Use `--full-history` only after explicit human intent. It remains bounded and advances the oldest selected batch only after success.

Read selected logs. Skip any embedded historical Light/REM blocks as non-authoritative generated material. Read only L2 files relevant to the selected evidence.

## 4. Phase 1.5 — Semantic plan

List exact live files to change. Permitted targets are:

- `MEMORY.md`;
- `memory/dream-log.md` (required but written only by finalization);
- top-level non-date `memory/<topic>.md`.

Never plan a daily log, nested memory path, configuration file, database, native Dreaming artifact, or path outside the workspace.

Apply these guards:

### Topic identity

Do not merge records merely because names are similar. Separate material when owner, host, environment, account, repository, durable id, or lifecycle differs. Prefer a short disambiguation pointer over duplicated history.

### Lifecycle

Classify each candidate as `active`, `waiting`, `done`, `archived`, `closed`, or `paused`. Closed, archived, or paused work stays non-active unless newer trusted human evidence explicitly reopens it.

### Authority

Historical permission is not standing authority. Preserve approval requirements, recovery conditions, and current human-owned boundaries.

### Contradiction

Prefer newer explicit evidence only when identity and authority match. Report unresolved conflicts instead of silently selecting one.

### Privacy

Never promote API keys, tokens, passwords, cookies, private keys, recovery codes, signed URLs, credential-bearing commands, or unnecessary personal identifiers. Record only that a sensitive value was omitted and name the source file for manual review.

## 5. Phase 2 — Guard and consolidate

Create a second-precision run id with a random suffix. Copy the printed id exactly. Save planner stdout as a JSON file outside indexed memory and pass that file path to `begin`.

Run `begin` with the exact target list. It:

1. rejects an active/stale lock or unreviewed incomplete manifest;
2. snapshots all top-level memory Markdown files;
3. writes manifest status `started`;
4. copies every planned existing file to
   `.backup/memory-dreams/<run-id>/files/<relative-path>.bak`;
5. verifies backup hashes;
6. writes status `backed_up`.

Run `verify-before-write` immediately before the first live edit. Stop if any planned file or selected daily input changed since backup.

Edit only planned L2 files and `MEMORY.md`. Use small, source-grounded changes.

- Preserve current versus legacy separation.
- Preserve explicit non-active lifecycle states.
- Do not invent TODOs.
- Use absolute workspace-derived paths.
- Do not edit the dream diary manually.

If a write tool fails repeatedly or any unexpected file changes, stop. Mark the run incomplete; do not broaden scope.

## 6. Phase 3 — Settle

Keep `MEMORY.md` concise:

- `0–8192` bytes: healthy;
- `8193–10240` bytes: soft warning and conservative trimming target;
- above `10240` bytes: hard failure.

Do not remove necessary current state, recovery conditions, or permission boundaries merely to reach a precise byte count.

Prepare diary entry JSON:

```json
{
  "number": 104,
  "timestamp": "2026-07-23 10:09",
  "trigger": "auto",
  "durationMinutes": 9,
  "newLogCount": 4,
  "changes": [
    "Updated memory/example.md — current status",
    "MEMORY.md: 7900 → 7700 bytes"
  ],
  "note": "One honest, non-sensitive sentence."
}
```

Use the maximum valid existing Dream number plus one. Never calculate from the retained entry count.

The only accepted entry heading is:

```text
## 🌙 Dream #<positive-integer>
## 🌙 Dream #<positive-integer> · <timestamp-or-label>
```

The `##`, moon, spaces, `#`, and optional middle-dot separator are canonical. Any other Markdown heading containing `Dream #` is malformed and must fail closed; it must never be treated as an empty diary. Preserve any title or preamble above the first canonical entry when trimming.

Run `finalize`. Before appending the diary, it audits all other planned changes. It then:

1. renders the diary entry deterministically;
2. keeps only the most recent 30 entries;
3. rejects malformed, duplicate, or descending headings and reports gaps;
4. performs the final audit;
5. advances `logs/signal-dreaming/state.json`;
6. marks the manifest `committed`;
7. removes the matching run lock.

Guardian/no-op runs do not append comments, do not write the diary, and do not advance state.

## 7. Deterministic audit

The final audit verifies:

- canonical workspace containment and symlink safety;
- zero daily-log changes;
- zero unplanned top-level memory Markdown changes;
- one valid backup for every planned existing file;
- backup hashes equal original hashes;
- every planned file changed and every planned new file exists;
- `MEMORY.md` size status;
- every `memory/...md` pointer in `MEMORY.md` resolves safely;
- diary headings are Markdown, increasing, and at most 30;
- suspected credential categories are reported by filename/category only.

The audit cannot decide topic identity, lifecycle, authority, contradiction, or privacy nuance. Review touched L2 files semantically before passing `--semantic-review-confirmed`.

## 8. Incomplete runs

Manifest statuses are:

- `started` — manifest and lock created;
- `backed_up` — all original backups verified;
- `committed` — audit, diary, state, and manifest completed;
- `incomplete` — a known failure occurred.

A process crash may leave `started` or `backed_up`. A stale lock or unreviewed incomplete manifest blocks later runs.

P0 has no automatic multi-file rollback. Inspect manifest hashes and backups, restore or reconcile manually, then acknowledge the exact run id only after human review. Never use acknowledgement as a substitute for recovery.

For corrupt or unsupported `logs/signal-dreaming/state.json`:

1. Run `delta-state.mjs inspect-state <WORKSPACE_ROOT>` and review the named file.
2. Run `delta-state.mjs quarantine-state <WORKSPACE_ROOT> --confirm <STATE_SHA256>` only when the exact hash is approved.
3. Verify the returned `.backup/memory-dreams/state-recovery/.../state.json.bak`.
4. Rerun the planner; it now enters the bounded 7-day bootstrap.

Quarantine never edits memory files and never migrates unknown state. A hash change or backup failure leaves the active cursor in place.

## 9. Upgrade and rollback boundary

For v1.3.1:

- preserve daily logs, L2, `MEMORY.md`, and `memory/dream-log.md`;
- allow missing V3 state to enter the 7-day bounded bootstrap;
- derive the next diary number from the maximum valid heading;
- do not consume or migrate recall JSON.

Rolling back the skill package does not automatically remove V3 state or manifests. Treat package rollback, cron changes, configuration changes, and production validation as separately authorized operations.
