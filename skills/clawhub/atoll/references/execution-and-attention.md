# Execution and human attention

Read this reference for agent execution records, evidence, human-attention requests, resolution, recovery, and version-fenced lifecycle transitions.

## Execution and attention CLI workflow

Use `atoll execution list|get|create|transition`, `execution evidence list|add`,
and `atoll attention create|list|get|cancel` with the selected profile and `--json`.
Creation requires `--issue`, `--agent <member-id|self>`, and an explicit
`--idempotency-key`; it returns `assigned` at state version 1. Start with a
separate `execution transition <id> --to running --expected-state-version 1
--idempotency-key <start-key>`. Atoll records state; it does not start a harness.

Generic transition targets are `running|waiting|succeeded|failed|cancelled`.
For `succeeded`, supply `--outcome-summary` unless the execution already has
linked evidence. The server validates this requirement.
Use `attention create` to move `running|waiting` to `needs_human`; generic
transitions cannot enter or leave `needs_human`. Attention kinds are exactly
`approval|clarification|access|decision|destructive_action|other`. Supply the
execution's expected state version, title, request summary, why needed, resume
condition, exactly one member/team/project-admin target, and an idempotency key.
Never put credentials, access tokens, private paths, prompts, logs, or other
secrets in attention text. Server permissions and concealed 404 responses remain
authoritative; do not try another identity to bypass them.

Read `attention get <id>` for the human's resolution and current attention and
execution versions. Human resolution returns the execution to `waiting`; it
does not resume a model or harness. Requester `attention cancel` also returns it
to `waiting` and requires `--expected-attention-version`,
`--expected-state-version`, and `--idempotency-key`. Human resolve, administrator
retarget/cancel, and recovery discovery are REST/UI operations, not CLI commands.
Harness acceptance and the later explicitly fenced `waiting -> running` resume
remain the separate AH-2122 integration.

Every write uses the caller's explicit idempotency key; transitions and attention
writes use the caller's expected versions. Never silently fetch a new version
and write against it. After a POST timeout, network failure, or HTTP 5xx, the
outcome is uncertain and the CLI does not retry. Read `execution get <id>`,
`attention get <id>` (or `attention list --execution <id>` when create returned no
attention ID), or `execution evidence list <id>`. Stop if the result is visible.
For execution create without an ID, replay the identical create command with
the same key, then read the returned ID. If replay is needed for another write,
keep the exact body and key. Stop for operator reconciliation if changed state
or versions make the outcome ambiguous; never use a new key to force progress.

Evidence add links only an existing authorized issue object using
`--type <comment|activity_event|issue_pr_link|attachment> --target-id <uuid>
--idempotency-key <key>`. It does not upload files, URLs, text, or raw logs.

## Human attention

When an execution needs a human, use the attention contract. `POST
/api/orgs/{id}/attention` records a bounded request and atomically moves the
execution to `needs_human`; generic execution transitions cannot perform this
edge. Poll `GET /api/orgs/{id}/attention` or use the exact item endpoint.
Resolve, cancel, or retarget with both expected versions and an idempotency
key. Reuse the same key only with the same input. Use `mode=recovery` only as
an authorized human administrator when the original target is no longer
eligible. Keep request text concise and never include secrets, credentials,
logs, prompts, or local paths. The public projection provides current and
snapshot actor/target fields, execution state, issue, and project context.

## Agent execution REST API

Use the canonical org-scoped execution routes for lifecycle management:
`GET|POST /api/orgs/{id}/executions`, `GET
/api/orgs/{id}/executions/{executionId}`, `POST
/api/orgs/{id}/executions/{executionId}/transitions`, and `GET|POST` on the
matching `/evidence` route. Create starts in `assigned`; transition writes
require `expected_state_version` and an idempotency key. Generic transitions
cannot enter or leave `needs_human`; use the attention contract. Reads follow
the issue's current project access. Non-guest organization members may also read
projectless executions; setup-scoped agents and guest members cannot. Creation-
project metadata does not grant access, and unreadable records are concealed.
Responses are bounded management projections, not logs or harness controls.
