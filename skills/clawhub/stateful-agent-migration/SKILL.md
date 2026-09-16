---
name: "stateful-agent-migration"
description: "Migrate or upgrade heavy stateful OpenClaw agents with rehearsal, embedding safety, rollback, and live proof."
---

# Migrate a Stateful OpenClaw Agent

Use this for major OpenClaw upgrades where Gateways own SQLite state, multiple agents, shared workspaces, credentials, automations, plugins, local embeddings, or external supervisors. Keep secrets and user content out of artifacts. End with live proof or an exact blocker.

## Gather

1. Identify current and target versions, install method, executable, service manager, state and agent directories, workspaces, port, and rollback release. Confirm paths from live service metadata and `openclaw --version`; finish when both releases and the running owner are unambiguous.

2. Inventory every writer and restart owner: Gateways, sibling instances sharing writable assets, agents, detached sessions, automations, recovery timers, monitors, backup jobs, plugin workers, canaries, and terminals. Treat an unclassified writer as a blocker; finish when each owner has pause and resume actions.

3. Record a redacted baseline:

```
openclaw config validate
openclaw doctor --non-interactive
openclaw gateway status --deep --json
openclaw channels status
openclaw models status
openclaw plugins list --json
```

Record restart count, readiness and health, agent ids, model routes, channel status, automations, plugins, and non-sensitive counts or hashes. Never record credentials, raw config, transcripts, messages, or SQLite rows; finish when each acceptance row has a baseline.

4. Read target release notes, migration code, backup documentation, breaking changes, plugin compatibility, runtime prerequisites, and interactive setup requirements. Check credential kind against provider API route. For local memory, record each agent's model identity, cache root, index identity, vector state, chunk ceiling, and physical batch; finish when every schema, auth, runtime, plugin, and embedding change has a check.

5. Create and verify a recovery point outside live state and workspaces:

```
openclaw backup create --output <private-backup-directory> --verify
openclaw backup verify <archive>
```

Take an offline filesystem, volume, or VM snapshot when byte-exact volatile recovery is required. Protect backups like live state; finish when verification passes and the rollback release is accessible.

## Mutate

1. Restore the archive to a fresh private rehearsal directory:

```
openclaw backup restore <archive> --target <fresh-private-directory>
```

Run the target against the copy on a non-production port with outbound delivery and side effects blocked. Never point a canary, old binary, or test at live migrated state; finish when startup and offline migrations complete on the copy.

2. Run interactive migration and managed setup in a real PTY. Match prompts semantically, time out, and fail on an unexpected prompt. Record only prompt categories and status. Never accept a default that replaces an unrelated model, plugin, or credential; finish when the intended branch repeats successfully.

3. Validate the copy with config, Doctor/lint, first-class SQLite backup verification, plugin loading, route inspection, and redacted state comparison. Move deprecated or conflicting legacy files to timestamped rollback locations instead of deleting them; finish when no legacy file shadows canonical state.

4. Prepare one idempotent cutover helper with explicit stages, timeouts, a private temporary directory, status summary, and automatic rollback trap. Pin candidate and helper by version or checksum. Accept already-empty sources and never overwrite target credentials; finish when a second dry run changes nothing.

5. Pause inbound work, sessions, automations, recovery timers, canaries, task monitors, supervisors, sibling Gateways sharing writable assets, and every inventoried writer. Require zero running or queued tasks and no active turn claim. Stop production last and fence supervisor recovery; finish after a stable quiet window.

6. Take the offline recovery point when required, then activate the candidate through its supported update path while writers stay fenced. Apply config with validated OpenClaw commands; never edit generated managed-provider files. Use the canonical model URI for a managed default; preserve per-agent memory identity unless a planned reindex accepts the change. Verify the generated embedding preset can batch the largest chunk. Never force-restart with active tasks; finish when candidate, provider preset, and service metadata agree.

7. Start only the migrated Gateway through a controlled restart. Verify service metadata, executable, cgroup or supervisor owner, reported version, and absence of stale run or turn claims. Do not rely only on command-line text; finish when all identity and ownership checks agree.

## Repair

1. Diagnose before repair:

```
openclaw doctor --non-interactive
openclaw config validate
openclaw gateway status --deep --json
openclaw channels status
openclaw models status
```

Use `openclaw doctor --fix --non-interactive` only as a separately approved repair; finish when each finding is pre-existing, migration-caused, or release-caused.

2. Repair the smallest owner: release metadata for code identity, validated config for routes and paths, canonical SQLite for credentials and approvals, plugin tooling for plugins, and service metadata for restart behavior. Preserve credentials and database ownership; finish when the repair and rollback are explicit.

3. Reproduce reusable OpenClaw defects against isolated minimal state. Remove hostnames, agent names, chat data, credentials, private paths, and infrastructure layout. Add a regression test before proposing code; finish when reproduction needs no operator data.

## Prove

1. Verify core health:

```
openclaw --version
openclaw config validate
openclaw doctor --non-interactive
openclaw gateway status --deep --json
curl -fsS http://127.0.0.1:<port>/readyz
curl -fsS http://127.0.0.1:<port>/healthz
```

Require expected version, healthy service, stable restart count, readiness, and health in two observations separated by a settling interval.

2. Prove behavior: check channels, model routes, required plugins, automations, and a representative tool; run real inference through each auth family. For local memory, run deep status. After an accepted identity change, complete a full reindex and require `dirty=false`, complete vectors, semantic availability, valid identity, and embedding probe success. Embed input longer than the previous failure threshold, run a relevant memory search, then repeat inference and session-turn smokes; finish when every acceptance row passes.

3. Compare post-migration non-sensitive counts and hashes with baseline. Explain schema, cache, and index differences. Treat unexplained loss, duplicate owners, auth fallback, delivery replay, stale paths or claims, and degraded recall as failure; finish when invariants hold.

4. Resume owners one class at a time and verify after each class, then check sibling Gateways. Remove restart fences only after production proof. Do not run a full reindex only to delete an orphan temporary artifact; honor retention and let a later justified reindex clean it. Finish when intended owners run and retired helpers cannot touch live state.

## Rollback

1. Roll back on failed identity, integrity, auth, readiness, channel, model, plugin, preservation, or writer-ownership gates. Stop and fence candidate writers first; finish when failed state cannot change.

2. Preserve failed state and redacted logs. Attempt code-only rollback first. Restore pre-migration state only when the known-good release cannot read migrated config or databases; state restore discards later changes and can desynchronize ratcheted channels. Finish when the rollback layer is justified.

3. Activate rollback through the supported mechanism and repeat Prove against the known-good version. Service startup alone is not success; finish when live behavior and preservation checks pass.

## Report

Report versions, migration boundary, verified backup, paused and resumed writers, rehearsal, mutations, quarantined artifacts, repair classification, acceptance result, rollback readiness, and residual risks. Use only redacted category/count/hash evidence. State `PASS` only after every Prove gate succeeds; otherwise state `BLOCKED` or `ROLLED BACK` with the failed stage and live version.
