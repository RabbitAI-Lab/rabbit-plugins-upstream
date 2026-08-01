# Native capability contract

Read this file completely before any v2 Markdown write or v1 migration. This is a fail-closed contract for OpenClaw 2026.7.1 and newer; a version number alone is never sufficient.

## Required read-only evidence

Collect without mutation:

1. `openclaw --version`
2. `openclaw memory status --json`
3. `openclaw memory promote --json --include-promoted`
4. successful help lookup for `memory promote-explain`
5. successful help lookup for `memory rem-harness`
6. `openclaw cron list --all --json`

Do not persist raw cron output. Build a sanitized JSON envelope containing only:

- `openclawVersion`;
- `capabilities.promoteExplain` and `capabilities.remHarness`;
- the unmodified read-only `status` and `promote` JSON;
- `cron.jobs[]` with only `id`, `name`, `enabled`, `schedule`, and `payload.message`.

Delivery targets, session identifiers, account data, and unrelated payload fields must be omitted.

## Classify

Pass the sanitized envelope over stdin:

```bash
node <SKILL_DIR>/scripts/migration-preflight.mjs \
  <WORKSPACE_ROOT> < <SANITIZED_PREFLIGHT_JSON>
```

Writes are permitted only when the classifier exits zero and returns `ready=true` with `mode="write-preflight-ready"`.

The classifier requires:

- OpenClaw 2026.7.1 or newer;
- exactly one status entry whose canonical workspace matches the requested workspace;
- builtin memory backend;
- a `dreamingAudit.issues` array with no issues;
- exactly one promotion result for the same workspace;
- promotion `audit.issues` and `candidates` arrays;
- both read-only diagnostic command capabilities;
- a known `cron.jobs` array;
- exactly one enabled native Dreaming job;
- no enabled v1 memory writer;
- no more than one enabled v2 curator.

## Fail closed

Any command failure, parse failure, absent field, unknown schema, workspace mismatch, native audit issue, ambiguous cron ownership, unsupported version, or extra enabled writer means:

- remain in audit or preview mode;
- do not begin a transaction;
- do not mark the gate;
- report the failed contract item without exposing raw cron payloads or private state.

A later OpenClaw version with schema drift is unsupported until this contract and self-test are updated. Never infer compatibility from similar-looking fields.

## Bounded candidate use

Use `promote-explain` only for a few relevant candidates after the base contract passes. Candidate output is a lead, not durable evidence. Do not run promotion apply/backfill/staging commands and do not inspect plugin-state paths reported by native status.
