---
name: feature-retcon
description: Reconcile a changed decision across an in-flight feature, with stage checks, a reversible file journal and independent closure evidence. Resume partial rounds or undo one on explicit request.
---

# Reconcile a changed decision

Start from the old decision, its replacement, authoritative artifacts and current authorization. A missed item under an unchanged goal belongs in the original task. A discussion of this skill is simply a discussion.

Keep progress in the existing plan or phase/task list. `RECONCILIATION.md` records the decision, scope, deepest synchronized stage, write-ahead journal and evidence for this round. Preserve a private recovery archive after closure. Undo requires a current explicit request.

## Assess the change

Resolve the authoritative topic using the user's location, project entry points and actual references. Use relevant standards and existing records. An impact-only review is read-only. If an active contract exists, read its decisions and run `status` and `verify` with the bundled [contract tool](scripts/contract.py) before resuming the same round. On a mismatch preserve the record and explain the failed check. If Python 3.9+ is unavailable, report what the sources establish and which contract checks could not run.

Use [the assessment guide](references/assessment.md) to identify affected behavior, writable roots, existing edits, deletions, hooks and baseline checks. Distinguish the deepest stage authorized now (`target_stage`) from the stage the round must reach for closure (`completion_stage`). An initial design-only pass on implemented behavior leaves downstream work. Continue from decisions and scope the user has already approved. Ask only about missing material decisions, scope expansion or side effects.

## Record and execute

Read [the journal protocol](references/contract-schema.md). The init command renders [the contract template](assets/RECONCILIATION.md) in the topic directory:

```sh
python3 <skill-dir>/scripts/contract.py init <topic-dir> \
  --target-stage <stage> --completion-stage <stage> \
  --version-control <git-or-none> --writable-root <authorized-root>
```

Fill in the confirmed assertion, authority, boundaries and baseline. Run `verify` before editing target files. Default embedded recovery preserves the actual starting bytes, including uncommitted work. Register new authorization with `scope` in the same round. A baseline commit is unnecessary.

Walk through the affected layers using [stage gates](references/stage-gates.md). Record each target write, create or delete, including repeated writes to a file:

```sh
python3 <skill-dir>/scripts/contract.py prepare <contract> --path <target>
# Make this authorized change.
python3 <skill-dir>/scripts/contract.py applied <contract> --path <target>
```

A file journal covers local files. External data and service actions require their own recovery arrangements. Use [task reconciliation](references/task-rebuild.md) when work has already been split. Preserve valid IDs and evidence, and put remaining work back in the original task list.

## Pause, close or restore

Check old terms and old behavior, run the applicable project checks and classify each residual. Record the deepest synchronized stage and stale downstream layers. Set `paused` when only the authorized portion is done, or `blocked` with the release condition for a failure or boundary. Keep the round and its journal.

Read [closure evidence](references/closure-evidence.md). Inspect the actual artifacts and assertions before marking checks passed. Only after the full completion stage and all required checks hold, with zero work left, run:

```sh
python3 <skill-dir>/scripts/contract.py verify <contract> --mark-ready --evidence <closure.json>
python3 <skill-dir>/scripts/contract.py close <contract> --archive <recovery.json>
```

Keep the private archive in an authorized unused location with an existing parent. Keep it outside version control. If a close fails, retain the active record. Mechanical validity alone establishes only file and journal consistency.

On an explicit undo request, use `restore` for an active round, including one already marked `ready_to_close`. For a closed round, inspect the archive, `reopen` with current authorization, then `restore`. Stop on drift and preserve later changes. Recheck the actual baseline and active references, then close with `outcome=restored` and a different archive. Report stages, remaining work, actual verification, residuals, record locations and Git state. See [worked cases](references/case-catalog.md) for partial rounds and recovery.
