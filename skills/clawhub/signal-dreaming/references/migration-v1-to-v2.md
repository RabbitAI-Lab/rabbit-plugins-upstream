# v1.3.1 → v2 migration

Read completely before changing cron. Migration is a reversible ownership cutover, not a memory import. Also read `native-capability-contract.md`.

## Invariants

- Preserve `memory/dream-log.md`, daily notes, top-level L2 files, nested historical material, and backups in place.
- The v1 diary stays read-only evidence; never import it as authority.
- Never run the v1 daily writer beside native Dreaming.
- Disable the legacy cron instead of deleting it; its exact ID is the rollback handle.
- This skill never edits config, cron, native state, or Gateway by itself.

## Read-only evidence

Collect the evidence and sanitized envelope defined in `native-capability-contract.md`. Pass it over stdin and do not persist raw cron output:

```bash
node <SKILL_DIR>/scripts/migration-preflight.mjs <WORKSPACE_ROOT> < <SANITIZED_PREFLIGHT_JSON>
```

The classifier requires OpenClaw 2026.7.1+, the exact supported read-only schemas, a clean native Dreaming audit, exactly one enabled native job, no enabled v1 writer, and no duplicate v2 curator. It hashes the legacy diary without writing it. Any error means audit-only.

## Cutover

1. If preflight finds an enabled v1 job, inspect its exact ID, name, schedule, and payload.
2. Ask for explicit approval, then disable only that ID. Keep the job disabled and undeleted.
3. Establish native memory-core Dreaming through the supported OpenClaw setup path. Configuration changes and Gateway restarts require separate authorization.
4. Rerun the sanitized preflight until `ready=true`.
5. Add at most one v2 curator after native Dreaming. Daily gate or weekly low-frequency operation are deployment choices; every Markdown write uses the transaction.

## Verify

- Preflight returns `ready=true` and `mode="write-preflight-ready"`; native is enabled once; v1 remains disabled.
- The legacy diary hash is unchanged.
- Start with v2 audit or preview; do not force a write to prove installation.
- After scheduled runs, confirm no new v1 diary entry and no second Dreaming artifact.

## Rollback

Disable the v2 curator first. Roll back any unwanted v2 transaction by exact run ID. Re-enable the preserved v1 job only with explicit approval and only when intentionally returning to v1. Do not delete history, native artifacts, or `.backup/memory-dreams/`. Native configuration remains unchanged unless separately authorized.
