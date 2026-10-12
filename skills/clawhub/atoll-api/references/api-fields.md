# Atoll API Field Reference

## Table of Contents

- [Auth Context](#auth-context)
- [Error Responses](#error-responses)
- [OAuth Agent Profiles](#oauth-agent-profiles)
- [Task Fields](#task-fields)
- [Goal Fields](#goal-fields)
- [KPI Fields](#kpi-fields)
- [KPI Snapshots](#kpi-snapshots)
- [Initiative Fields](#initiative-fields)
- [Automation Rule Fields](#automation-rule-fields)
- [Custom View Fields](#custom-view-fields)
- [Board Column Mutation Fields](#board-column-mutation-fields)
- [Board Context Response](#board-context-response)
- [Webhook Fields](#webhook-fields)
- [Private Inbox Fields](#private-inbox-fields)
- [Setup Proposal Fields](#setup-proposal-fields)
- [Heartbeat Response](#heartbeat-response)
- [Artifact Fields](#artifact-fields)
- [Analytics Response](#analytics-response)
- [Plan Limit Errors](#plan-limit-errors)
- [Agent Fields](#agent-fields)
- [Avatar Upload Response](#avatar-upload-response)
- [Enums](#enums)

---

## Auth Context

`GET /api/auth/me` returns the caller's organization role and scopes alongside
live per-project authorization. OAuth-bound agents also include provenance for
the selected agent connection:

```json
{
  "auth": {
    "type": "agent",
    "role": "guest",
    "scopes": [],
    "oauth": {
      "authorizedByMemberId": "human-member-uuid",
      "clientId": "oauth-client-uuid",
      "resource": "https://atollhq.com/mcp",
      "connectionId": "connection-uuid",
      "profileRef": "profile-grant-uuid"
    },
    "projectAccess": [
      { "projectId": "project-uuid", "accessLevel": "admin" }
    ]
  }
}
```

Project-scoped agents intentionally remain organization guests. Role and
project-access changes are read live and do not require key rotation.

## Error Responses

Shared missing-auth failures return `401` JSON with `error: "Unauthorized"`
and `code: "unauthorized"`. Unknown `/api/*` paths return `404` JSON with
`error: "Not found"` and `code: "not_found"`. The `code` field is additive;
other route-specific legacy errors may contain only `error`.

## Local runner presence

`GET`, `PUT`, and `DELETE /api/orgs/{id}/runners/self` are agent-only. The
organization and agent member come from authentication. `PUT` accepts
`instanceId`, optional `hostId` (the server-bound host routing identity), `platform` (`darwin`, `linux`, or `windows`), `arch` (`arm64`,
`x64`, or `amd64`), `capabilities` (unique values from `codex` and `git`),
`clientVersion` (numeric semantic version). Intake state is server-owned and
is not accepted from runner self refresh. Human members use the hosted fleet
control endpoint to pause or resume new intake. The server derives the display name. Responses include computed
`presence_state`: `connected`, `stale` after 10 minutes, or `offline` after
explicit disconnect. They contain no API keys, profile names, prompts,
process IDs, or local/machine/worktree paths. Refreshes are limited to 60
per authenticated agent per minute and return `429` with `Retry-After`. If the
shared rate-limit check fails, the route fails closed with `503` and
`code: "RATE_LIMIT_CHECK_FAILED"`. Rate-limit responses also include
`code: "RATE_LIMITED"`, `retryAfterSeconds`, `limit`, and `currentCount`;
recent-instance conflicts use `code: "RUNNER_INSTALLATION_CONFLICT"`.

## Local runner leases

`POST /api/orgs/{id}/runner-leases/claim` atomically claims an assigned,
accessible, dependency-satisfied issue for the authenticated agent's current
runner. The body accepts `issueId` and `idempotencyKey`; `attention_resume`
also requires `attentionItemId`, `runnerHostId` (maximum 255 characters), `preservedThreadId`, and
`actionKind`. The response returns an ephemeral token; only its SHA-256 hash is
stored. An untouched, unexpired, pre-intent `active` replay returns a new token
with `token_reissued: true` and invalidates the original token. During overlapping recovery retries, the four newest prior recovery tokens remain valid for one minute or until one is used, which promotes it. Other replays
return `token: null`; terminal attention replays are acknowledgement-only. `PATCH /api/orgs/{id}/runner-leases/{leaseId}` accepts fenced renew,
progress, turn-milestone, terminal, reconciliation, and acknowledgement
transitions, including `model_completed`. Organization, agent, runner, generation, token, and sequence must
match. Exact mutation retries are idempotent, and `uncertain_outcome` blocks
automatic replacement. Disconnected, stale, or replaced runners cannot mutate
or replay. A paused current runner may mutate or reconcile an already-held
lease, but cannot acquire a new claim. Lease rows enforce a composite
`(issue_id, org_id)` foreign key.
Mutation metadata is closed: `progress` accepts `preparing`,
`turn_intent_persisted`, `sdk_accepted`, `running`, `model_completed`, or
`finalizing`; `errorCode` accepts `runner_error`, `sdk_error`, `model_error`,
`timeout`, `cancelled`, or `unknown`. Free-form runtime details are rejected.

For verified workflow resume, set GitHub verification mode to `resume` in
Workspace Settings. This mode is disabled by default, requires a current Codex
runner for the delivery agent, and adds `verificationEventId` to a verified
workflow `attention_resume` claim. The server binds the completed issue lease to the
repository ID, PR number, exact head SHA, source lease generation, runner
installation, runner host, and preserved thread.
Only a matching `verification.completed` item is routed to
`resume_agent_thread`; uncertain or mismatched identity remains review-only.
`RUNNER_LEASE_VERIFICATION_BINDING_MISMATCH` is a definite 409 claim
rejection; the local attempt closes while the notification remains unread for
the next review pass. There is no new-thread fallback. Terminal replay is
acknowledgement-only.

## Hosted runner fleet control

`GET /api/orgs/{id}/runners` is human-session only. It returns one current or
most recently disconnected installation for each manageable agent, with safe
presence, lease, project-access, heartbeat, and unambiguous execution context.
Hidden work is represented as restricted busy state. Repository mappings remain
on the canonical project repository endpoint; local checkout paths, secrets,
prompts, process IDs, and raw logs are never returned.

`PATCH /api/orgs/{id}/runners/{runnerId}/intake` accepts only
`{ "intake_state": "active" | "paused" }`. It requires a human member who
can manage the bound agent and fences the exact current installation. A stale
but current installation may be controlled; a disconnected or replaced row is
rejected. Same-state requests are idempotent and create no duplicate Activity
history. Pausing blocks only new lease claims; already-held leases remain
eligible for fenced renewal, progress, finalization, or reconciliation.

## OAuth Agent Profiles

`GET /api/oauth/agent-profiles` and `atoll_list_agent_profiles` return only
currently usable grants for the authenticated OAuth connection:

```json
{
  "resource": "https://atollhq.com/mcp",
  "profiles": [{
    "profile_ref": "profile-grant-uuid",
    "display_name": "Product Planner",
    "designation": "Project-scoped agent",
    "organization": { "id": "org-uuid", "name": "Atoll" },
    "projects": [{
      "id": "project-uuid",
      "name": "Atoll HQ",
      "access_level": "edit"
    }]
  }]
}
```

`profile_ref` is an opaque connection-scoped selector, not a credential. Actor
calls return stable errors: `no_profiles_authorized`, `profile_required`
(including safe summaries), `invalid_profile`, or
`profile_selector_not_supported` for API-key callers.

## Task Fields

Request bodies accept **camelCase** (`assigneeId`, `projectId`). Snake_case also accepted for backward compatibility. Responses generally use snake_case; dependency responses retain camelCase release fields (`releaseColumnId`, `releaseColumn`, and nested `projectId`) plus the `release_column_id` compatibility alias.

## Avatar Upload Response

Successful `POST` uploads and `PATCH` preset selections at `/api/orgs/{id}/members/{memberId}/avatar` return
`200` with exactly:

```json
{
  "member": {
    "id": "member-uuid",
    "avatar_url": "https://..."
  }
}
```

No other member, invitation, onboarding, or account metadata is included.
When removal of a retired Storage object is durably queued, POST returns `202`
with the same `member` projection plus `"cleanup_pending": true`; DELETE
returns `{ "success": true, "cleanup_pending": true }`. Concurrent pointer
changes return `{ "error": "Avatar changed concurrently" }` with `409` and may
add `"cleanup_pending": true` when cleanup of a staged or retired object remains
queued. An authenticated 15-minute worker drains due jobs independently, with
avatar requests providing an additional opportunistic sweep. Uploads over 2MB
return `413`.

```json
{
  "title": "Fix login bug",
  "description": "Markdown supported",
  "status": "todo",
  "priority": 1,
  "assigneeId": "member-uuid",
  "assigneeIds": ["member-uuid-1", "member-uuid-2"],
  "projectId": "project-uuid",
  "milestoneId": "milestone-uuid",
  "teamId": "team-uuid",
  "startDate": "2026-03-01",
  "dueDate": "2026-04-01",
  "recurrenceType": "weekly",
  "recurrenceInterval": 1,
  "recurrenceDays": ["mon", "wed", "fri"],
  "recurrenceMaterializationMode": "schedule",
  "recurrenceTime": "09:00",
  "recurrenceTimezone": "Europe/Stockholm",
  "labelIds": ["label-uuid-1", "label-uuid-2"]
}
```

Most fields work on both POST (create) and PATCH (update). `labelIds` is accepted on task create and bulk create. For existing tasks, use the label endpoints or `atoll label add/remove`.

- **Multiple assignees**: Use `assigneeIds` (array). Legacy `assigneeId` (single) still works. Responses include `assignees` array with `id`, `display_name`, `type`, `avatar_url`.
- **Start date**: Sets when work begins. Combined with `dueDate`, defines the Gantt time span.
- **Recurring tasks**: Set `recurrenceType` + optional `recurrenceInterval` (default 1). Completion mode is the default and creates the next occurrence when the current task is marked `done`. Set `recurrenceMaterializationMode` to `schedule` with `recurrenceTime` (`HH:MM`) and an IANA `recurrenceTimezone` to create occurrences from the maintenance sweep even while older tasks remain open; completing a scheduled occurrence does not create another task. Scheduled weekly series can set unique `recurrenceDays` values from `mon` through `sun`; Atoll sorts them into calendar order. Weekday arrays, including `[]`, require scheduled mode; `null` can clear selected weekdays in completion mode too. Scheduled intervals must be at most `10000`; completion mode retains its existing positive PostgreSQL integer range. Responses include normalized `recurrence_days` and `recurrence_schedule: { type, interval, days }`; the internal `recurrence_next_run_at` cursor is omitted. Appearance and due dates are separate, and the root due date is not advanced. Chains that have never entered scheduled mode retain and edit each occurrence's completion settings locally. Activating scheduled mode through a child adopts that child's cadence on the authorized root unless overridden. Once a chain has entered scheduled mode, the root owns recurrence settings even after a later switch back to completion; authorized list, detail, and update responses use those settings while preserving each child's identity. In those chains, send child-local task edits separately from root recurrence edits. Root deletion preserves completion-mode child recurrence, while scheduled-mode children become ordinary tasks. Do not PATCH `recurrenceParentId`.
- **Archived tasks**: Have `archived_at` timestamp. Excluded by default; pass `includeArchived=true`.
- **GET detail** returns enriched data: `milestone`, `creator`, `assignee`, `assignees`, `sub_tasks`, `issue_labels`, `isBlocked`.

Full `GET /api/orgs/{id}/issues` list items include the canonical
project-prefixed `identifier` and collision-free `projectSlug` for project
issues, or `null` for projectless issues. Compact `view=board` and `view=list`
items do not include these fields.

MCP assigned-work filters: `scope: "mine"` returns issues assigned to the
selected profile, including multi-assignee links; `open_only: true` excludes
archived, done and cancelled issues. Either input selects the existing compact
REST `view=list` path. Mine maps to `scope=mine`; true maps to `open=true`, while
false does not enable open filtering. The exact envelope remains unchanged.
Compact rows may omit identifiers and keep existing `q_exact` restrictions.
Complete all `nextOffset` pages before claiming exact totals.

The MCP `atoll_list_issues` projection exposes optional nullable
`identifier` and `projectSlug`, drops undeclared REST enrichment including the
CLI-derived `url`, and normalizes both legacy `{ issues, total, limit, offset }`
and CLI-compatible `{ resource: "issues", items, ... }` responses into the
exact public list envelope. The full profile exposes it in `structuredContent`;
the public plugin exposes it under `structuredContent.result.data`. Project-
scoped calls may add `project_context` alongside the envelope.

**Bulk create** (`POST /issues/bulk`):
```json
{ "issues": [{ "title": "Task 1", "status": "todo", "priority": 1, "projectId": "..." }] }
```
Returns `{ issues: [...], count: N }` (201). Max 50 per request.

## Plan Limit Errors

Creation endpoints may return `402` when an org reaches its billing plan limit:

```json
{
  "error": "Plan limit reached",
  "code": "PLAN_LIMIT_REACHED",
  "resource": "activeProjects",
  "plan": "free",
  "limit": 2,
  "usage": 2
}
```

`resource` is one of `humans`, `agents`, `activeProjects`, or `activeIssues`.

## Member Directory Fields

`GET /api/orgs/{id}/members?shape=envelope` returns the bounded member
directory. Supplying `q`, `limit`, or `offset` also selects this directory
mode. It returns a list envelope with exact `total`, `limit`, `offset`,
`nextOffset`, `truncated`, and `hint` values.

Each `items[]` row contains only:

| Field | Description |
|-------|-------------|
| `id` | Stable organization member UUID. Use this in issue `assignee_id` or `assignee_ids` writes. |
| `display_name` | Safe display name; missing names use `Unknown member`. |
| `type` | `human` or `agent`. |
| `role` | Current organization role. |
| `avatar_url` | Avatar URL or `null`. |

Directory inputs are `projectId`, `type=human|agent`, case-insensitive
display-name `q`, `limit` (default 25, maximum 100), and `offset` (default 0).
Project results require caller access and follow existing collaborator
visibility rules. Unprojected directory results exclude guests. `includeEmail`
does not add email to this response. A request without `shape`, `q`, `limit`, or
`offset` keeps the legacy member response for web consumers.

## Agent Fields

Create org-wide agents with `{ "name": "...", "role": "member", "setupScoped": false }`; org-wide creation is owner/admin-only. Create project-scoped agents with non-empty `projectIds`, for example `{ "name": "...", "projectIds": ["project-uuid"] }`; `projectId` remains accepted as a legacy/default-project alias and is merged with `projectIds`. Project-scoped agents are created as guests, and human members may only scope them to projects they can access. Create personal agents with `{ "name": "...", "personal": true }`; personal agents inherit their human owner's project access and reject explicit `projectId`/`projectIds`. Any create form may include an allowlisted `avatarPreset` ID. Arbitrary URLs are rejected. Existing agent presets are changed with `{ "preset": "codex" }` on the avatar PATCH endpoint.

Key-minting agent creation responses contain the one-time raw `apiKey` and its stable `apiKeyId`. Creation with `oauthOnly: true` omits both fields.

Manageable-agent rows always include nullable `key_prefix`, `last_used_at`, and `activity_last_used_at`. `key_prefix` and `last_used_at` describe only the selected active API key. `activity_last_used_at` is the latest timestamp from an active API key or a non-revoked OAuth agent profile. Historical OAuth use is not backfilled.

Workforce read rows from `GET /api/orgs/{id}/agents/workforce` contain bounded identity fields, safe `projects` summaries, `project_ids`, `created_at`, nullable aggregated `last_used_at`, nullable personal-agent `owner` display metadata, `scope` (`personal`, `project`, or `organization`), and `capabilities` with `can_view`, `can_manage_access`, `can_manage_keys`, `can_disable`, and `can_revoke` booleans. Project-admin visibility sets only `can_view` unless an existing creator/personal-owner management rule independently grants more. `key_prefix` is optional and is returned only when existing key-management authority allows it. The response never includes emails, auth IDs, hidden projects, credentials, OAuth grants, prompts, raw activity, lifecycle fields, or organization capacity.

`GET /api/orgs/{id}/agents/manageable` remains human-only. For organization owners/admins, each row adds `personal_owner: { id, display_name } | null`, resolved only from referenced human members in the same organization. Missing legacy owners return `null`. Other callers receive `personal_owner: null`. The top-level `capacity: { plan, usage, limit } | null` is admin-only and uses the same agent allowance check as creation with zero increment; `limit: null` means unlimited. Normal agents and API-key integrations both consume this allowance. Non-admin responses contain `capacity: null` and do not run owner or capacity queries. Failed owner, project, heartbeat, or capacity reads fail the response rather than return a partial reconciliation. Plan-limit database errors fail closed instead of becoming free-plan or zero-usage results.

## Agent Heartbeat Policy Fields

Heartbeat policy replacement uses a complete object with `sections` booleans for `goals`, `standalone_kpis`, `standalone_initiatives`, `assigned_issues`, `project_context`, `signals`, and `attention`; `signal_categories` booleans for `task`, `initiative`, `kpi`, and `project`; `project_ids`; `initiative_ids`; and `columns` entries shaped as `{ "project_id": "...", "column_id": "..." }`. Empty focus arrays mean all. Policy fields narrow proactive attention and never grant access. Management `saved_policy` retains stale IDs so saved previews and real heartbeats fail closed; `effective_policy` is the sanitized editable form, `stale_selections` reports removals, and saving it clears stale restrictions. Manageable-agent list rows include visible `project_ids`, named `accessible_projects`, and `heartbeat_policy_summary.{status,focus_summary}`.

## Goal Fields

Goal reads are available to organization members. Creating, updating, and deleting goals requires owner/admin Strategy access.

```json
{
  "title": "Reach 100 paying customers by Q2",
  "description": "Our primary growth objective",
  "owner_id": "member-uuid",
  "status": "active",
  "target_date": "2026-06-30"
}
```

## KPI Fields

```json
{
  "name": "paying_customers",
  "description": "Total active paying customers",
  "goal_id": "goal-uuid",
  "unit": "count",
  "unit_label": "customers",
  "target_value": 100,
  "target_direction": "increase",
  "source_type": "manual",
  "stale_after_hours": 168
}
```

Calculated task-completion KPIs use `source_type: "formula"` and are calculated from linked work instead of snapshots:

```json
{
  "name": "mvp_tasks_done",
  "goal_id": "goal-uuid",
  "source_type": "formula",
  "source_config": {
    "formula": "goal_linked_issue_completion",
    "done_statuses": ["done"]
  }
}
```

For `goal_linked_issue_completion`, `current_value` is the count of non-archived directly linked issues and milestone-linked issues in `done` status and `target_value` is the total non-archived directly linked issue and milestone-linked issue count under initiatives for the goal.

## KPI Snapshots

```json
{
  "value": 34,
  "source": "agent",
  "attribution_note": "Checked Stripe dashboard",
  "attributed_to_initiative_id": "initiative-uuid",
  "attributed_to_issue_id": "issue-uuid"
}
```

Recording a snapshot auto-updates the KPI's `current_value`.

KPI-to-initiative impact links are separate from snapshot attribution. A link means the initiative is expected to move the KPI; snapshot attribution identifies the initiative and/or issue that produced one measurement.

Calculated KPIs do not accept manual snapshots.

`api_poll` snapshots are written by published KPI HTTP Syncs and include provenance: `source_sync_id`, `source_sync_run_id`, `source_config_hash`, `source_recorded_for`, `observed_at`, and optional `provider_recorded_at`.

Snapshot list/create responses keep an explicit legacy projection. Use
`projection=provenance_v1` on the list route to add nullable
`source_window_start` and `source_window_end` calendar dates. Before the
source-window migration is active, both opt-in fields are `null`. Existing
clients and snapshot-create responses do not receive the added fields.

## KPI detail relationship fields

KPI detail includes `initiative_impacts` for initiatives visible to the caller
across all statuses. Each row carries the impact identifiers,
`expected_impact`, and a compact visible `initiative` object (`id`, `title`,
`name`, and `status`). This is intended-impact context, not snapshot
attribution.

## KPI HTTP Syncs

```json
{
  "name": "PostHog visitors",
  "schedule": "daily",
  "request_config": {
    "method": "GET",
    "url": "https://us.posthog.com/api/projects/123/query/",
    "headers": {
      "Authorization": {
        "secretRef": "posthog_api_key",
        "format": "Bearer {value}"
      }
    }
  },
  "extraction_config": {
    "contentType": "json",
    "pointer": "/results/0/value",
    "numeric": {
      "mode": "number",
      "percentageScale": null
    }
  },
  "freshness_config": {}
}
```

V1 syncs are `GET` only, `https` only, JSON only, exact-host allowlisted, no redirects, no request bodies, no inline query strings, and no secret values. Machine actors can create drafts and validate configs only after the host is allowlisted. Human admins manage allowlists, secrets, dry-runs, publishing, disabling, and snapshot-writing run-now actions in Atoll.

Both MCP profiles expose `atoll_create_kpi_http_sync_draft` and
`atoll_validate_kpi_http_sync_config` for this draft-only workflow. The tools
reject inline secret values and return safe draft metadata rather than request
configuration. Public MCP does not expose secret entry, network dry runs,
publishing, disabling, or snapshot writes.

## Initiative Fields

```json
{
  "title": "Launch self-serve onboarding flow",
  "description": "Reduce friction for new signups",
  "goal_id": "goal-uuid",
  "owner_id": "member-uuid",
  "status": "active",
  "target_date": "2026-05-15",
  "project_id": "project-uuid"
}
```

Create accepts `projectId` as a camelCase alias for `project_id`. Guest/project-scoped callers must pass a project they can edit when creating initiatives.

For portfolio-style initiatives (grouping projects):
```json
{
  "title": "Q2 Platform Rewrite",
  "description": "Migrate all services to new architecture",
  "owner_id": "member-uuid",
  "start_date": "2026-04-01",
  "target_date": "2026-06-30"
}
```

Use `title` for create/update requests; create also accepts legacy `name`. Atoll keeps the legacy `name` field in sync for compatibility. Create accepts `goalId`, `ownerId`, and `targetDate` aliases for `goal_id`, `owner_id`, and `target_date`.

Add/remove projects with `{ "project_id": "uuid" }`.

Initiative detail includes `kpi_impacts` only for linked KPIs readable by the
caller. Each row carries the relationship IDs, `expected_impact`, and creation
time. Unreadable KPI relationships are omitted. These rows do not attribute a
KPI snapshot.

## Initiative Target Fields

Targets attach to initiatives and track commitments separately from business KPIs. Use `mode: "progress"` for initiative outputs and `mode: "gate"` for hard launch prerequisites. Gate target heartbeat signals use stateful copy such as `0/5 retailers complete`; agents must not convert them into fractional KPI pace.

```json
{
  "title": "Get 5 retailers live by July 5",
  "description": "Prerequisite before price comparison launch",
  "mode": "gate",
  "unit": "count",
  "unit_label": "retailers",
  "current_value": 0,
  "target_value": 5,
  "target_direction": "increase",
  "target_date": "2026-07-05",
  "due_soon_days": 7
}
```

Target issue links use `{ "issue_id": "..." }` at `.../targets/{targetId}/issues`.
The issue value accepts an issue UUID, bare number, `#number`, `ATOLL-number`,
`TSK-number`,
or an unambiguous project-derived prefix. Target milestone links still use
`{ "milestone_id": "milestone-uuid" }` at `.../targets/{targetId}/milestones`.
Target response rows include linked `issueIds` and `milestoneIds` when returned
by the target list/get endpoints, filtered to resources readable through the
caller's project access.

Initiative-level issue links use the same `issue_id` formats, and initiative
milestone links accept either a milestone UUID or its exact name. Successful
writes persist canonical resource UUIDs within the initiative's authorized
scope; malformed, concealed, ambiguous, and resolver-failure outcomes are
`400`, `404`, `409`, and `500` respectively.

## Public MCP typed product fields

Public plugin calls use snake_case fields and accept the opaque per-call
`profile_ref` selector. Project references accept a UUID, exact slug, or exact
name. Issue references accept UUIDs, bare numbers, `#number`, `ATOLL-number`,
`TSK-number`, and unambiguous project-derived prefixes. Label references accept
a UUID or exact label name. Initiative milestone-link creation also accepts an
exact milestone name; unlink operations use the canonical milestone UUID.

Core typed tools include issue archive/unarchive and dependency-chain reads;
label and subtask list/create/update/delete; strategy audit; organization
activity; notification list/acknowledgement; project create/delete and board
column creation; and goal/KPI create/update. `atoll_get_strategy_audit` accepts
`severity: "critical" | "warning" | "info"`; the returned summary and type
counts match the filtered findings. `atoll_list_activity` accepts filter
`by_me` or `mine`, `limit: 1..100`, and non-negative `offset`.

Goal update accepts `goal_id` as a UUID or exact goal title. KPI create and
update accept `goal_id` as a UUID or exact goal title; KPI update accepts
`kpi_id` as a UUID or exact KPI name. These lookups are exact and scoped to
the selected organization. Missing names return `reference_not_found`, and
duplicate exact names return `ambiguous_reference`; neither writes a mutation.
Archive and unarchive emit the normal `issue.updated` webhook event. The
project, label, subtask, board-column, goal, and KPI writes listed in the API
endpoint reference can return `core_write_uncertain` with `retryable: false`
when transport failure, HTTP 5xx, or invalid success output leaves the outcome
unclear. Use the error's readback steps to reconcile state before a replay;
authoritative 4xx responses are preserved.

Subtask creation accepts `{ title }`; update accepts `title`, `completed`, or
both. Board-column creation accepts `project_id`, lowercase `key`, `label`,
optional inline `description`, and optional `color`; MCP has no file-input
field. Project deletion requires the exact `confirmation: "DELETE"` value and
owner/admin access. Linked Artifacts and active executions can still block
deletion. Goal writes remain owner/admin-only. KPI update changes configuration;
use `atoll_record_kpi_snapshot` to record `current_value` measurements.

Examples:

```json
{
  "org_id": "org-uuid",
  "profile_ref": "profile-grant-uuid",
  "project_id": "atoll-hq",
  "title": "Launch planning parity"
}
```

Initiative creation accepts either a non-empty `title` or the legacy `name`
alias; updates use `title` only. Initiative, target, and milestone due dates use `YYYY-MM-DD`.

## Read-only repository context fields

`atoll_list_project_repositories` accepts `org_id` and `project_id`;
`project_id` supports a UUID, exact slug, or exact name. Its response contains
`project`, mapped `repositories`, and `truncated`. Each repository includes an
opaque `repo_ref`, safe repository and project identities, `default_ref`, and
`read_only_app.status: "connected"`.

The other four tools accept that `repo_ref`. Tree, file, search, and commit
results include `requested_ref` and `resolved_commit_sha`, which identifies the
exact commit used for the read. Tree entries contain `name`, `path`, `type`,
nullable `sha`, and nullable `size`; the response keeps `truncated`. File
results contain `path`, bounded `content`, `encoding: "utf-8"`, and `size`.
Search results contain `query`, nullable `path`, verified `hits`, `total_count`,
and `incomplete_results`; each hit includes `name`, `path`, `sha`, nullable
`html_url`, and `verified_at_commit_sha`. Commit results contain `sha`, nullable
`html_url`, bounded `message`, `message_truncated`, nullable `author` and
`committer` snapshots, valid `parents` with nullable `html_url`, and
`parents_truncated`. Public and full/private MCP output schemas reject
undeclared fields.

Repository errors preserve the REST `{ error, code, retryable }` fields. Codes
include `repository_not_connected`, `repository_access_denied`,
`github_installation_unavailable`, `github_permission_missing`,
`repository_ref_invalid`, `git_ref_not_found`, `repository_path_not_found`,
`repository_search_ref_unsupported`, `repository_file_too_large`,
`repository_file_encoding_unsupported`, and `repository_context_unavailable`.
Public plugin responses also wrap the same data in `result: { ok, data }` or
`result: { ok, error }`.
Initiative target writes use the existing target fields above. Public milestone
create and upsert accept `status: "active" | "closed"`; closed creation is
persisted in the same downstream write. Public milestone upsert compares exact-name fields and returns `unchanged` for an identical
sequential request; its list-then-create/update implementation is not an
atomic concurrency deduplication guarantee. It returns
`{ "action": "created" | "updated" | "unchanged", "milestone": { ... } }`. Public feedback
uses `{ "type": "bug" | "feature", "description": "...", "url"?: "..." }`
and deliberately does not accept `userEmail` or `userName`; the server records
the MCP client marker and treats the submitted description as untrusted. If
multiple exact-name milestones already exist, upsert returns a structured
`ambiguous_milestone` error before mutation instead of choosing one.

### Feedback error contract

| HTTP | `code` | Additional structured fields |
| --- | --- | --- |
| 400 | `MISSING_DESCRIPTION`, `INVALID_TYPE`, `INVALID_FILE_TYPE`, `FILE_TOO_LARGE` | `error`, `code` |
| 429 | `RATE_LIMITED` | `retryAfterSeconds`, `rateLimitWindow`, `currentCount`, `limit`, and a `Retry-After` header |
| 500 | `FEEDBACK_NOT_CONFIGURED`, `UPSTREAM_ISSUE_ID_MISSING`, `UPSTREAM_ISSUE_CREATOR_MISSING`, `SCREENSHOT_ATTACHMENT_FAILED`, `INTERNAL_ERROR` | `error`, `code` |
| 500 | `UPSTREAM_ISSUE_CREATE_FAILED` | `upstreamStatus` and safe `upstreamError` |
| 503 | `RATE_LIMIT_CHECK_FAILED` | `retryAfterSeconds: null` |

## Automation Rule Fields

```json
{
  "schema_version": 1,
  "name": "Auto-assign urgent bugs",
  "trigger_event": "issue.created",
  "conditions": [{ "kind": "field", "field": "priority", "operator": "eq", "value": 0 }],
  "actions": [{ "type": "set_assignee", "value": "member-uuid" }],
  "enabled": true,
  "project_id": "project-uuid"
}
```

`issue.assigned` matches both assignment changes and issue creation with at
least one assignee. This includes recurring occurrences that inherit an
assignee from their recurrence root.

Time-based rules use the same definition with `trigger_event:
"schedule.issue_time"` and a required `schedule_config`:

```json
{
  "trigger_event": "schedule.issue_time",
  "schedule_config": {
    "anchor": "due_date",
    "offset_minutes": -60
  }
}
```

`anchor` is `updated_at`, `status_changed_at`, or `due_date`. An `updated_at`
rule represents inactivity; a `status_changed_at` rule represents time in the
current status; and a `due_date` rule represents deadline timing. Offsets for
`updated_at` and `status_changed_at` must be non-negative. A `due_date` offset
may be negative (before due), zero (at due), or positive (after due). Date-only
due dates are evaluated at midnight UTC. Scheduled rules reject change
conditions; combine a status field condition with `status_changed_at` when the
rule targets a specific status. Event-triggered rules must omit or clear
`schedule_config`.

Atoll evaluates scheduled rules from the existing authenticated maintenance
sweep every 15 minutes in bounded batches with a durable rotating rule cursor.
Busy workspaces can take multiple sweeps. It catches up occurrences whose time has
passed, excludes archived issues, and deduplicates each `(rule, issue,
scheduled_for)` occurrence. A condition mismatch is terminal for that
occurrence and is recorded as skipped. Scheduled execution reuses the existing
condition evaluator, action path, and `automation.executed` Activity history;
it does not add cron expressions, recurrence rules, calendars, or a second rule
store.

Supported action values are: `set_status` (canonical project status key),
`set_assignee` (replace the full assignee set with one member UUID, or `null` to
clear it), `add_assignee` (add a member UUID without removing others), `unassign`
(omit `value`), `set_priority` (integer `0` through `3`), `add_label` and
`remove_label` (label UUID), `post_comment` (non-empty text, at most 10,000
characters), and legacy `close_issue` (omit `value`, targets the valid `done` key).
`send_webhook` accepts only `{ "type": "send_webhook", "webhook_id": "webhook-uuid" }`.
The destination must be enabled, same-org, and purpose `automation` or `both`.
Queued transport retries do not re-run the automation action. Activity exposes
`webhook_delivery_id` plus safe latest-attempt `webhook_delivery` state.
Automation payloads use schema v3 with current tenant-scoped project and issue
fields, safe sorted `trigger.changedFields`, and optional artifact counts; CI
uses `issue: null` and `changedFields: []`. Subscription broadcasts and `ping`
remain schema v2. Manual redelivery uses a new header and rewrites a payload
delivery ID only for legacy v2 automation bodies that contain that field.
Already satisfied assignments, priorities, statuses, and label relationships
succeed without duplicate mutation events. Invalid references still fail.
Unsupported action types or malformed values return `400` and are not saved.

`create_issue` requires `project_id` (UUID), `status` (that project's column key),
and `title` (1–500 characters). Optional fields are `description` (up to 10,000
characters), `priority` (0–3), `assignee_ids` (member UUID array), and `label_ids`
(label UUID array). The member and label arrays accept at most 100 entries each.
At most one create action is allowed per rule. Configure the new issue inside
this action; later actions still target the original issue. Target-project access,
references, limits, and normal creation rules remain authoritative.

Creation content supports fixed text and approved `{{repository}}`, `{{workflow}}`,
`{{conclusion}}`, and `{{run_url}}` fields only. Missing event fields and invalid or
oversized rendered content fail before creation. Current issue triggers do not
provide those external fields; use fixed text for issue triggers. The
`ci.run.completed` trigger supplies them from a signed GitHub completion event.
CI rules require organization scope (`project_id: null`) and support only
`create_issue` and `send_webhook`. CI rules accept only event conditions. Issue triggers reject event conditions.
Event conditions use `kind: "event"`, `eq` or `neq`, and fields
`conclusion`, `repository`, `workflow`, `branch` (strings), `has_pr`, or
`has_linked_issue` (booleans). Use conclusion `failure` and
`has_linked_issue: false` to create an issue only for an unlinked failed run.
The first receipt freezes link state; duplicate repository/run/attempt deliveries
reuse it. A new run attempt is a distinct event. CI dry runs use marked example
values and never execute actions.

A durable action result records `created_issue_id` in the same transaction as
canonical creation. Repeated execution of that action cannot create another issue.
If a process stops after creation but before effects finish, the created ID remains
visible and the interrupted action fails closed; this does not prove all effects
completed. Deleting the created issue does not permit automatic recreation.
Dry runs create no issue and fail clearly when required content fields are missing.

**CI dry-run test:** Send `{}` with no event or issue overrides. The result has
`preview_source: "example"`, fixed `test_ci` values, and `test_issue: null`.
Custom repository or branch conditions can fail to match this example; a preview
does not verify a live run.

**Scheduled dry-run test:** Send `{ "issue_id": "issue-uuid" }` for a real
issue, or `{ "issue": { "updated_at": "2026-01-01T00:00:00Z", "status_changed_at": "2026-01-01T00:00:00Z", "due_date": "2026-01-03" } }`
for a sample. The existing test endpoint returns `scheduled_for`, `due`, and
`conditions_matched`, plus `matched` and `actions_that_would_run`. A scheduled
preview uses an issue, not a canonical event, and remains side-effect free.

**Issue dry-run test**: Send `{ "issue_id": "uuid" }` or `{ "issue": { "status": "todo", "priority": 2 } }`. Returns `{ matched, actions_that_would_run }`.

**Rule definition V1:** `schema_version` defaults to `1`. Conditions are ANDed;
actions run in array order. A field condition uses `kind: "field"`, a field
(`status`, `priority`, or `assignee_id`), `eq` or `neq`, and a typed `value`.
A change condition uses `kind: "change"` with `changed` (omit `value`),
`changed_from`, or `changed_to` (require a typed `value`). Change conditions
require an issue change trigger; `issue.created` and `pr.merged` reject them.
Priority values are integers `0`–`3`; status values are lowercase workflow keys;
assignee values are organization member UUIDs or `null`.

Create and partial `PUT` requests reject unknown keys, unsupported versions,
malformed conditions/actions, and invalid references with `400` and
`issues: [{ path, code, message }]`. A partial update is merged with the stored
definition and the complete result is validated. If another edit changes the rule
during validation, `PUT` returns `409`; reload the rule before retrying. An enabled
rule must be disabled by a separate exact `{ "enabled": false }` request before
changing `project_id`; combining disable with a scope change is rejected. An
enabled invalid rule must also be disabled separately before repair. A disabled
invalid rule accepts a valid repair only while remaining disabled; repair and
enable must be separate. Project-scoped status values
must exist in that workflow; project, member, and label references must belong
to the organization. A request containing only `{ "enabled": false }` can
disable an invalid rule without changing its definition; owner/admin access
is still required. Enabling requires a valid definition.

**List filter:** `GET /api/orgs/{id}/automation-rules` accepts optional
`project_id`. A project UUID returns only rules assigned to that exact project;
it does not include organization-wide rules. Use `project_id=none` for only
organization-wide rules (`project_id IS NULL`). Omit the parameter to preserve
the existing list of all rules in the organization. Empty or invalid values
return `400`. A project UUID requires both organization membership and caller
read access to that project; cross-organization, inaccessible, or missing
projects return `404`. Organization-wide and unfiltered requests retain existing
organization-member access. Results remain newest first and include disabled
or invalid rules with their validation diagnostics. Both MCP profiles accept
the same optional `project_id` UUID or `none` filter; the CLI does not add
filter flags.

GET/list rules can include `validation: { valid, issues: [{ path, code, message }] }`.
Invalid saved rows remain readable. Runtime validation rejects the whole invalid
rule before any action; valid actions are not salvaged from a malformed rule.
Legacy missing `schema_version` and condition `kind` normalize to `1` and `field`;
priority strings `"0"`–`"3"` normalize to integers. Stored legacy `close_issue`
with `value: null` normalizes to no value, and stored empty `set_assignee` values
normalize to `null`. New writes must omit `close_issue.value`. Prefer `unassign` to clear all
assignees; legacy `set_assignee` with `null` remains supported.

**Change-condition dry runs:** Send `{ "event": <canonical IssueDomainEventV1> }`
to the existing `/test` endpoint. The event must match the organization and rule
project scope. Its derived triggers and before/after change map determine the
result. An issue snapshot alone returns `400` for a change-aware rule. Dry runs
perform no actions and create no run history.

**Automation run history**: `GET /api/orgs/{id}/automation-rules/{ruleId}/activity`
returns `{ runs }` to owner/admin members, newest first and limited to the
latest 100 runs. Each run contains its status,
timestamps, safe error fields, a safe source-event projection, and ordered
`automation_action_runs` for actions that were actually attempted. Non-matching
events, dry runs, and rules with no executable actions create no run row. The
response excludes event payloads, action inputs, request headers, credentials,
and third-party response bodies.

Run status is `running`, `succeeded`, `failed`, or `skipped`. A repeated exact
rule revision, trigger, issue, and relevant before/after state within one
correlation stops with `status: "skipped"`, `skip_reason: "loop_detected"`,
`suppressed_by_run_id` pointing to the earlier run, and zero action rows.
Optional nullable `correlation_id` and `causation_id` identify the chain and
immediate parent event; old history may omit these fields or return null.
Evaluation fingerprints stay server-side and are never returned.
A loop stop leaves earlier mutations committed and is terminal. Duplicate
delivery never replays succeeded, failed, skipped, or action-bearing runs;
only a proven running run with zero action rows can resume. There is no
explicit retry endpoint or new MCP tool.
When another run in the same event blocks replay with terminal or action evidence,
an interrupted run with no attempted actions is finalized as failed without
executing its actions.
If a saved rule changes before an interrupted run resumes, Atoll marks the run
failed without executing its actions.

This foundation release keeps automation-originated child events suppressed.
Chaining activation requires a separate reviewed forward migration after the
loop-safe application is live. Historical suppressed events are not replayed.

If a definitive action-audit start fails after an earlier action, the run is
terminal with safe `error_code: "automation_execution_partial"` and message
`automation execution stopped after one or more earlier actions`; earlier
action evidence is not replayed. Deleting a rule or its project preserves the
run and action rows with the original rule UUID as an immutable snapshot, so
authorized Activity lookup remains possible. Deleting the organization may
remove its organization-owned history.

## Custom View Fields

```json
{
  "name": "My Sprint View",
  "filters": { "status": ["in_progress", "todo"], "priority": [0, 1] },
  "sort": { "field": "priority", "direction": "asc" },
  "display_mode": "board",
  "color": "#6B7280",
  "icon": "list"
}
```

`display_mode`: `board`, `list`. `filters` and `sort` are freeform JSON.

## Board Column Mutation Fields

Delete a board column with
`DELETE .../board-columns/{columnId}?reassignTo={targetColumnId}&releaseReassignTo={releaseTargetColumnId}`.
`reassignTo` is required when the source column contains issues and
`releaseReassignTo` is required when it has dependency release references;
the targets are independent, must belong to the same project, and reassignment
and deletion are atomic. The board-column list reports `issue_count` and
`release_reference_count` so clients can fail closed before deletion.
The final board column cannot be deleted. Reorder with
`{ "columns": [{ "id": "column-uuid", "position": 0 }] }` and include the
complete current column set. Duplicate, missing, partial, or mixed-project IDs
and duplicate, negative, or non-integer positions are rejected before any
positions change. New columns append to the board; create and patch requests
reject `position`.

## Board Context Response

`GET /api/orgs/{id}/projects/{projectId}/board-context` returns the strategy data used by the board filter toolbar:

```json
{
  "strategyContext": {
    "milestones": [{
      "id": "milestone-uuid",
      "name": "Public beta",
      "status": "active",
      "issueCount": 4,
      "completedCount": 2,
      "progress": 50,
      "linkedInitiatives": [{
        "id": "initiative-uuid",
        "title": "Activation launch",
        "status": "active",
        "progress": 40,
        "kpiImpactCount": 1,
        "linkedMilestoneIds": ["milestone-uuid"]
      }]
    }],
    "initiatives": [{
      "id": "initiative-uuid",
      "title": "Activation launch",
      "status": "active",
      "issueCount": 5,
      "completedCount": 2,
      "progress": 40,
      "kpiImpactCount": 1,
      "linkedMilestoneIds": ["milestone-uuid"]
    }],
    "issueInitiativeLinks": [{
      "issueId": "issue-uuid",
      "initiativeIds": ["initiative-uuid"]
    }]
  }
}
```

`issueInitiativeLinks` includes direct `initiative_issues` links and links inherited from an issue's milestone.

## Webhook Fields

Bearer secrets must contain only printable ASCII characters. Switching from none to Bearer requires a token and returns HTTP 400 if it is missing. The optional `standard_webhooks` setting accepts a receiver-supplied `whsec_` secret; it is write-only and must be canonical standard Base64 after the prefix, decoding to 24-64 bytes. Lists expose only `standard_webhooks.configured`.

`PATCH /api/webhooks/{id}` preserves omitted fields. A blank or omitted Bearer
secret preserves the token; `auth.type: none` clears it. URL/auth/Standard signing changes create
a new private destination version; pending deliveries retain their pinned version.

```json
{
  "url": "https://example.com/webhook",
  "events": ["issue.created", "issue.updated"],
  "enabled": true,
  "purpose": "subscription",
  "auth": { "type": "none" },
  "standard_webhooks": {
    "enabled": true,
    "secret": "whsec_<canonical-standard-base64>"
  }
}
```

URL must be an HTTPS DNS hostname. IP literals, `localhost`, and `.local` hosts are rejected at creation; delivery refuses non-public DNS results and does not follow redirects. The create response includes an Atoll-generated `secret` for HMAC signature verification. Store it immediately; it is shown only once. This is distinct from the receiver-supplied Standard Webhooks `whsec_` secret. Use purpose `automation` or `both` with `auth: { "type": "bearer", "secret": "..." }` for automation destinations; responses expose only `auth.type` and `auth.configured`.

`atoll_create_webhook` is available only in the full/private MCP profile because
normal MCP tool output may be retained in client conversation history. The
public plugin exposes redacted webhook listing and deletion but never the
one-time signing secret.

List responses include `destination_display` and a deprecated `url` compatibility field containing only the origin plus `/…`. Automation action payloads use schema version `3` with current tenant-scoped project and issue fields; subscription broadcasts and `ping` remain schema version `2`. Delivery requests include `X-Atoll-Signature`, `X-Atoll-Signature-Version`, versioned `X-Atoll-Signatures`, `X-Atoll-Delivery-Id`, and `Idempotency-Key`. When Standard Webhooks is enabled, they also include `webhook-id`, `webhook-timestamp`, and `webhook-signature`. Delivery history includes `delivery_id`, `status`, `status_code`, `error_code`, `delivered_at`, and `next_retry_at`, never payloads, receiver response bodies, or raw errors.

## Private Inbox Fields

| Field | Description |
|-------|-------------|
| `status` | `untriaged`, `triaged`, `action_required`, `waiting`, `resolved`, `ignored`, or `quarantined` |
| `category` | `support`, `security`, `sales`, `partnership`, `press`, `personal`, `spam`, `other`, or `null` |
| `priority` | `0` (urgent) through `4` (low) |
| `body_html_sanitized` | Stored HTML with active content and remote images removed |
| `ingestion_status` | `pending`, `complete`, `failed`, or `quarantined` |
| `retain_until` | One-year retention deadline |
| `linked_issue_id` | Optional issue UUID in the same organization |
| `attachments[]` | Private metadata; use the authenticated attachment content route for bytes |
| `actions[]` | Append-only ingestion and operator audit actions |
| `drafts[]` | Saved plain-text replies that have not been sent |

Collection responses omit bodies and headers. Fetch one selected message before
acting on its untrusted content.

## Setup Proposal Fields

First-run setup proposals are editable drafts. Setup-scoped local agents and ChatKit tools can submit or revise drafts; owner/admin humans apply them.

```json
{
  "setupSessionId": "setup-session-uuid",
  "proposal": {
    "projects": [{ "name": "Launch v1", "description": "..." }],
    "goals": [{ "title": "Reach 100 paying customers", "target_date": "2026-06-30" }],
    "kpis": [{ "name": "paying_customers", "target_value": 100, "target_direction": "increase" }],
    "initiatives": [{ "title": "Content pipeline", "description": "Publish and distribute launch content", "expected_impact": "Increase qualified signups" }],
    "milestones": [{ "name": "Public beta", "description": "Launch the public beta workspace", "due_date": "2026-05-15" }],
    "issues": [{ "title": "Instrument signup funnel", "description": "Track signup start, completion, and activation", "priority": 1 }]
  },
  "evidence": {
    "summary": "Optional notes about repo files or user answers that informed the proposal"
  }
}
```

Proposal JSON currently supports at most one item in each collection: `projects`, `goals`, `kpis`, `initiatives`, `milestones`, and `issues`. A revision replaces the active draft and preserves the previous revision as history. ChatKit tools and setup-scoped agents cannot apply proposals. Setup keys are temporary and are revoked when setup is applied, skipped, or failed; they are never promoted by removing the setup scope.

## Heartbeat Response

`GET /api/orgs/{id}/heartbeat` returns compact delivery by default for REST
and private CLI/MCP callers. Compact responses contain `mode: "compact"`,
`agent`, `timestamp`, `attention_items`, `attention_summary`, private
`execution_attention` and `execution_attention_summary`, grouped `signals`, `recommended_action`,
`counts`, `delta`, and `page`. Full legacy context is available only with
`view=full` (or the CLI `--full` flag).

### Compact heartbeat fields

| Field | Notes |
|---|---|
| `signals[]` | Grouped actionable signal or dependency-blocker groups. Each group has `key`, `revision`, `severity`, `kind`, `action_reason`, root and impact counts, readiness, bounded `evidence`, and optional `suggested_read`. |
| `attention_items` | Bounded direct attention projections with required `id`, `event_type`, `severity`, `title`, `resource_type`, and `ack_endpoint`; optional `resource_id` is included when present. |
| `attention_summary` | Counts for included direct attention items. |
| `execution_attention` | Private queues with `resolved_unread` answers and `open` requests. Resolved answers remain until explicit receipt acknowledgement or the exact requester `waiting -> running` transition. |
| `execution_attention_summary` | Private exact counts for `resolved_unread`, `open`, and `total`. |
| `counts` | `actionable_groups`, severity counts, `direct_blocked`, `downstream_blocked`, `ready_if_released`, `unknown_readiness`, `restricted`, and `suppressed_expected_waits`. |
| `delta` | `since`, `new_count`, `changed_count`, `escalated_count`, `ready_count`, suppression counts, and `reset_required`. |
| `page` | Requested `max_bytes` (1,024-16,384) and `max_items` (1-25), returned counts/bytes, `has_more`, `next_cursor`, and terminal `ack_cursor`. |

Compact pages are deterministic and use opaque, server-issued cursors. Request
the next page with the exact `next_cursor` from the immediately previous page;
do not manufacture, skip, or replay a page cursor. Cursors are single-use in sequence. Acknowledge only the terminal `ack_cursor` using
`POST /api/orgs/{id}/heartbeat/ack`, then use that acknowledged cursor as
`since` on a later request. Invalid cursors return `400`; stale pages or an
unacknowledged `since` return `409`. An expired acknowledged baseline returns a
fresh compact response with `delta.reset_required: true`. If the requested
`max_bytes` cannot fit the mandatory actionable record and compact response
envelope, the route returns `413` with `code: "heartbeat_budget_too_small"`;
no page cursor or terminal receipt advances. Retry with a larger `max_bytes` or
omit it for the 16,384-byte default. Policy, authorization, or candidate
changes while paging invalidate the cursor.

Expected waits are suppressed for an unsatisfied dependency when the readable
blocker is before its release column and there is no active stall, threatened or
overdue commitment, or explicit deadline, gate, permission, or stale anomaly.
An unowned backlog or Todo blocker by itself is an ordinary wait and never
alerts. Actionable groups surface active stalls, threatened or overdue
commitments, and explicit anomalies; escalation metadata alone does not surface
an expected wait. Initiative-target and stalled aggregates are also suppressed
when every underlying dependency is an expected wait. Dependency blockers are grouped by
root and release condition. A dependency chain may
include readable nodes and edges, opaque restricted node tokens, readiness,
release-condition satisfaction, and explicit permission flags; unknown
readiness remains unknown. Suggested reads are safe GET/CLI/private-MCP calls.

The public plugin MCP heartbeat keeps its legacy full response and does not
expose compact acknowledgement or dependency-chain tools. Private MCP supports
compact heartbeat, `atoll_ack_heartbeat`, and `atoll_get_dependency_chain`.

```json
{
  "agent": { "id": "...", "display_name": "Growth Agent" },
  "timestamp": "2026-03-29T12:00:00Z",
  "goals": [{
    "goal": { "id", "title", "status", "target_date" },
    "days_remaining": 93,
    "kpis": [{
      "kpi": { "name", "current_value", "target_value" },
      "pace_needed": 0.71,
      "pace_actual": 0.42,
      "trend": "accelerating",
      "is_stale": false,
      "is_off_pace": true,
      "snapshots_recent": [...]
    }],
    "initiatives": [{
      "initiative": { "title", "status" },
      "expected_impacts": [{ "kpi_id", "expected_impact" }],
      "total_issues": 8,
      "completed_issues": 3,
      "stalled_issues": 2,
      "blocked_issues": 1,
      "project_ids": ["..."],
      "linked_issues": [{
        "id": "...",
        "title": "Publish comparison page",
        "status": "todo",
        "priority": 1,
        "assignee_id": "...",
        "project_id": "...",
        "milestone_id": null,
        "number": 42,
        "blocked": false,
        "updated_at": "2026-03-28T12:00:00Z"
      }]
    }]
  }],
  "standalone_kpis": [...],
  "assigned_issues": [...],
  "project_context": [{
    "project_id": "...",
    "project_name": "Product",
    "board_columns": [{
      "key": "approval_gate",
      "label": "Approval Gate",
      "description": "Use when implementation is complete but needs approval."
    }]
  }],
  "signals": [
    { "type": "kpi_off_pace", "severity": "warning", "message": "..." }
  ],
  "recommended_action": {
    "id": "create_work:...",
    "action_type": "create_work",
    "title": "Create Content pipeline work for paying_customers",
    "target_type": "initiative",
    "target_id": "...",
    "goal_id": "...",
    "kpi_id": "...",
    "initiative_id": "...",
    "source_signal_ids": ["kpi_off_pace:..."],
    "why_now": "paying_customers is off pace, and Content pipeline has no active linked issue.",
    "expected_impact": "Create the missing execution path for the initiative expected to move paying_customers: +30 signups/mo.",
    "evidence": ["KPI \"paying_customers\" is off pace..."],
    "first_step": "Open Content pipeline and define the smallest task that can move paying_customers.",
    "success_criteria": ["Create or update concrete follow-up actions tied to paying_customers."],
    "suggested_write": {
      "operation": "issue.create",
      "title": "Create Content pipeline work for paying_customers",
      "body": "<h2>Why now</h2>...",
      "status": "todo",
      "priority": 1,
      "project_id": "...",
      "initiative_id": "...",
      "kpi_id": "...",
      "initiative_target_id": "..."
    },
    "confidence": "high",
    "caveats": [],
    "quality_checks": [{ "id": "kpi_link", "status": "pass", "message": "Recommendation includes a KPI link." }],
    "usage_guidance": {
      "instructions": [
        "Prefer suggested_write.operation when it matches the current board state and the recommendation is still current.",
        "Preserve goal, KPI, initiative, initiative target, why-now, expected impact, first step, suggested_write, and success criteria evidence in any issue, status update, KPI refresh, or comment you create.",
        "Do not copy deferred busywork, unrelated tasks, or caveat text into write payloads unless it is directly needed for the recommended action."
      ],
      "preserve_fields": ["goal_id", "kpi_id", "initiative_id", "initiative_target_id", "why_now", "expected_impact", "first_step", "success_criteria", "suggested_write"],
      "avoid_payload_sources": ["deferred_busywork", "unrelated_assigned_issues", "stale_recommendations_after_board_change"]
    }
  }
}
```

Heartbeat is org-scoped, but project-bound goals, KPIs, initiatives, issue health, milestone signals, assigned work, and `project_context` are filtered by the caller's project access. Project-scoped guests receive every explicitly accessible board while idle; personal agents retain relevant inherited-project context. Non-guest members can also see unprojected org-level strategy. Shared initiatives can appear with counts and signals based only on accessible work.

Heartbeat also includes `attention_items` for direct current-member notifications such as mentions, assignments, direct replies, assignee comments, and creator-visible status changes. Authorized REST and CLI heartbeat calls can also include `verification.completed`; the public MCP heartbeat excludes this private event type. Verification items include a validated `verification` object with bounded repository, PR, workflow, run attempt, head SHA, conclusion, canonical run URL, and `next_action` fields. They contain no raw payloads, secrets, logs, or thread identifiers. Each attention item includes `id`, `source`, `event_type`, `severity`, `action_kind`, resource fields, `comment_id`, `reply_to_comment_id`, optional validated parent `routing`, `target_path`, `created_at`, and `ack_endpoint`; after handling the referenced item, call `ack_endpoint` so the notification is acknowledged and removed from later heartbeat attention results. `attention_summary` includes counts such as `mentions`, `assignments`, `blockers`, and `total_unread`.

Current-member notifications can use `event_type` values such as `mention.created`, `issue.assigned`, `comment.added`, and `issue.status_changed`. Notification preferences use `event_type`, `channel` (`in_app` or `google_chat`), and `enabled` for current-member delivery preferences. The single Google Chat preference is stored under `mention.created` and controls mentions, assignments, and direct-reply comments; ordinary comments and status changes are excluded. Setting `enabled: false` for `google_chat` stops future Chat delivery without acknowledging in-app notifications. Setting `enabled: false` for in-app `mention.created` also attempts to acknowledge that member's currently unread mention notifications; when cleanup succeeds, they no longer appear in notification lists or heartbeat `attention_items`. New direct-message installations receive a welcome before configuration. Classic Chat interaction apps link humans through a short-lived `REQUEST_CONFIG` session after `connect`; Workspace add-ons use `basic_authorization_prompt`. Both flows retain display-safe Chat identity fields and memberships owned by the signed-in human. Add-on callbacks require the endpoint URL audience and exact per-project add-on service account email; classic callbacks continue to trust Google's Chat service account and can use a project-number audience. Connect-session and member endpoints require a human web session; a one-time `connect <token>` command remains a manual fallback.

The Google Chat callback recognizes message text or `message.argumentText` for `help` and `connect`. Help also accepts classic `message.slashCommand.commandId: 1` and Workspace add-on `chat.appCommandPayload.appCommandMetadata.appCommandId: "1"`; add-on command metadata can include `appCommandType`. Plain `help`, `/help`, and an `@Atoll help` mention are equivalent.

Google Chat mention cards include the task title, a safely formatted plain-text comment preview limited to 500 characters, and an **Open in Atoll** button. Rich-text markup is removed and Google Chat card formatting characters are escaped. Delivery rows are queued with mention notifications, dispatched asynchronously immediately, and reclaimed by a 15-minute recovery drain. Deterministic Google request/message IDs make retries idempotent; exponential backoff stops after five attempts. An unused link token expires after 10 minutes, while identical replay after a successful link returns the existing member link without changing it.

Agents should follow `recommended_action.usage_guidance`: prefer `suggested_write.operation` when it still matches the board, preserve KPI/initiative/initiative-target/why-now/expected-impact/first-step/success-criteria evidence in any write, and avoid copying deferred busywork or unrelated assigned tasks into issue or comment payloads. When `start_work` uses `suggested_write.operation: "issue.update"` with a body, apply the status update and preserve that body as an issue comment; `PATCH /issues/{issueId}` accepts `comment_body` for this same-request progress note.

`recommended_action` is a deterministic strategy-backed next action built from heartbeat context. Action types are `create_work`, `start_work`, `escalate_blocker`, `refresh_metric`, and `investigate`; suggested writes may prefill issue creation, issue status updates, blocker comments, or KPI refresh requests, while an investigation can use `suggested_write.operation: "none"` when heartbeat lacks enough detail for a safe write. Issue-create bodies are HTML for Atoll's rich-text issue description; blocker/comment and metric-refresh bodies are plain text.

Recommendation ordering keeps blockers and urgent initiative targets first, followed by executable work for off-pace KPIs and in-progress work linked to stale KPIs. Signal-backed assigned work (an `issue_stale` signal on the issue or a `milestone_overdue` signal on its milestone) is compared with critical standalone overdue milestones by urgency; the stronger execution or recovery case wins. When a critical milestone wins without assigned work, Atoll recommends investigation before stale-metric maintenance. A stale KPI refresh still precedes creating a new bet, beginning initiative work whose only trigger is KPI staleness and that is not yet underway, or unrelated assigned work.

## Strategy Audit Response

`GET /api/orgs/{id}/strategy/audit` returns findings (sorted critical → warning → info), each with a concrete `suggested_fix`, plus summary counts.

```json
{
  "findings": [
    {
      "type": "initiative_orphaned",
      "severity": "warning",
      "title": "\"Content pipeline\" is not attached to a goal",
      "message": "This initiative is not linked to any goal...",
      "suggested_fix": "Attach it to a goal: PATCH /api/orgs/{orgId}/initiatives/<id> { \"goal_id\": \"<goalId>\" }",
      "initiative_id": "..."
    }
  ],
  "summary": { "total": 7, "critical": 1, "warning": 4, "info": 2 },
  "counts_by_type": { "initiative_orphaned": 2, "goal_missing_kpi": 1 }
}
```

Each finding carries whichever entity ids apply: `goal_id`, `kpi_id`, `initiative_id`, `initiative_target_id`, `issue_id`, `milestone_id`, `project_id`. Finding `type` values:

- Structural: `initiative_orphaned`, `kpi_orphaned`, `goal_missing_kpi`, `goal_missing_initiative`, `dangling_initiative_project`, `dangling_initiative_issue`, `dangling_initiative_milestone`
- KPI health: `kpi_unrecorded`, `kpi_missing_target`, `kpi_stale`, `kpi_off_pace`
- Initiative health: `initiative_missing_impact`, `initiative_missing_execution`, `initiative_stalled`, `initiative_target_missing_execution`, `initiative_target_overdue`, `initiative_target_blocked`
- Execution: `issue_blocked`, `issue_overdue`, `milestone_overdue`

## Artifact Fields

### Revision source provenance

An Artifact revision can keep one optional source from an existing External
Reference linked to the same issue or project. The source is an immutable
pointer snapshot. Atoll does not fetch, copy, or synchronize provider content.

Create accepts optional `source_external_reference_link_id` (the Context link
UUID). Revise uses three states: omit the field to inherit the current snapshot,
supply a live link UUID to set or replace it, or send `null` to clear it on the
new revision. A source-only change is valid and still requires the exact
`expected_revision_id` or `expected_revision_number`. An unchanged title,
content, and source is rejected. An unrelated or removed link cannot be selected.

Source selection returns `404 source_reference_unavailable` for a missing,
concealed, or concurrently removed link; these cases are indistinguishable.
A link on an unrelated Artifact target returns `400 source_target_mismatch`.
Choose another source or clear the selection. A stale expected revision still
returns `409 CONFLICT` and requires rereading the Artifact before retrying.

Add `?projection=source_provenance_v1` to Artifact create, revision create, or
single-revision GET to receive `revision.source_reference`. Default responses
and revision lists remain unchanged. Unknown or duplicate projections return
`400`. The projection is `null` when no source exists or the caller cannot read
the recorded source target. Otherwise it contains `external_reference_id`,
`target_type`, `target_id`, `canonical_url`, `provider`, `object_type`,
`provenance`, nullable `label`, and live `currently_linked`.

The URL is HTTP(S), has no credentials, and is limited to 2048 UTF-8 bytes;
provider, object type, and provenance are each limited to 64 bytes, and the
label to 240 characters (at most 960 UTF-8 bytes). All fields except `currently_linked` come from the saved
snapshot. Removing the live Context link preserves history and permits
inherit or clear. Later reference changes cannot rewrite a saved source.
Linking the Artifact to another target does not grant access to its source.

The web editor and CLI support this workflow. Typed MCP source inputs and
outputs are not yet available; their existing Artifact contract is unchanged.


`atoll_list_artifacts` accepts optional `issue_id` for a compact issue manifest
or `project_id` for direct project links; these selectors are mutually
exclusive. All modes accept `limit` (1-100, default 50) and `offset`
(0-10000, default 0). Project filtering can return an empty page with
`hasMore: true`; continue with `offset + limit`.

MCP creation accepts `type`, `title`, `content`, optional `content_format`
(default `markdown`), and optional `links` containing `target_type` and UUID
`target_id`. `atoll_get_artifact` accepts UUID `artifact_id` and optional UUID
`revision_id`. Revision writes accept UUID `artifact_id`, an expected current
revision ID or number, and changed `title` and/or `content` with optional
`content_format`. Link writes use `artifact_id`, `target_type`, and `target_id`;
unlink uses `artifact_id` and `link_id`. The live typed schema defines required
fields. See [Artifact workflow](artifact-workflow.md) for readback and conflict handling.

Artifacts contain `id`, `org_id`, `type`, `title`, `current_revision_id`,
`created_by`, `created_at`, and `updated_at`. Artifact links contain `id`,
`artifact_id`, canonical `artifact_type`, `target_type` (`issue` or `project`), `target_id`, `created_by`,
and `created_at`. Revisions contain `id`, `artifact_id`, `revision_number`, immutable `title_snapshot`,
`content_format`, `content_digest`, `created_by`, and `created_at`; the full
revision endpoint also returns sanitized `content`. Revision summaries never
return content. Content formats are `markdown` and `html`; both are stored as
sanitized HTML. Titles are limited to 200 UTF-8 bytes and revisions to 256 KiB.
If a member is deleted, creator provenance is retained as `null`.
The opt-in issue manifest contains only `id`, `type`, `title`,
`current_revision_id`, `created_at`, and `updated_at`. Issue PRD and
Implementation Plan links are limited to one slot per issue, and each such
Artifact can be authoritative for only one issue.

Artifact list and detail responses also include `can_edit` and `can_unlink`.
`can_edit` is true when the current member can create a revision. `can_unlink`
is true when the current member can remove a visible link; removing a final link
requires owner or admin access, while a member with write access can remove a
link when another link remains.

## Agent execution fields

Execution projections contain `id`, `issue_id`, `current_project_id`,
`project_id_at_creation` (provenance only), normalized `state`, `state_version`,
bounded lifecycle summaries, safe harness/external-run metadata, timestamps,
and actor objects `{ id, display_name, type, deleted }`. `harness_kind` and
`external_run_id` reject credentials, tokens, and local filesystem paths;
legacy unsafe values are redacted as `null` in projections. Deleted agent or actor
rows use immutable AH-2095 snapshots. Detail adds ordered `transitions` and
existing `evidence` references `{ id, issue_id, link_type, target_id,
created_by, created_at }`.

Create requires `issue_id`, `agent_member_id`, and `idempotency_key`; it always
returns state `assigned`. Transition requires `expected_state_version`,
`to_state`, and `idempotency_key`. HTTP bodies are strict and omit actor
provenance; the server derives safe OAuth provenance. The generic transition
enum excludes `needs_human`.

The local runner uses `harness_kind: "atoll_local_runner"` and the lease UUID
as `external_run_id`. Its private job record stores the exact execution state
and version plus one bounded pending management operation. Canonical human
attention adds private claim fields `attention_source: "human_attention"`,
`execution_id`, `human_attention_item_id`, `expected_attention_version`, and
`expected_execution_version`; those identities are separate from notification
`attention_item_id`. The runner sends only canonical IDs and the closed
resolution outcome enum to the retained thread.

## Analytics Response

```json
{
  "statusDistribution": [{ "status": "done", "count": 42 }],
  "priorityBreakdown": [{ "priority": 1, "count": 15 }],
  "assigneeWorkload": [{ "assignee_id": "...", "display_name": "...", "count": 8 }],
  "dailyCounts": [{ "date": "2026-03-01", "created": 5, "completed": 3 }]
}
```

---

## Human attention fields

Attention list/detail projections contain `id`, `status` (`open`, `resolved`, or
`cancelled`), `kind` (`approval`, `clarification`, `access`, `decision`,
`destructive_action`, or `other`), bounded `title`, `request_summary`,
`why_needed`, `resume_condition`, `requested_at`, `closed_at`,
`resolution_outcome`, `resolution_summary`, `attention_version`, and the
execution, issue, and project projections. `target` contains the exact target
type plus a live member/team projection when it still exists and immutable
snapshot fields. `requester` and `closed_by` contain `{ id, display_name,
type, deleted }` snapshots. Detail adds
`execution_state_version_at_request` and `execution_state_version_at_close`.

Create targets are one of `{ target_type: "member", target_member_id }`,
`{ target_type: "team", target_team_id }`, or
`{ target_type: "project_admins" }`. Mutation requests use
`expected_attention_version`, `expected_state_version`, and
`idempotency_key`; resolve also accepts `resolution_outcome` and an optional
bounded `resolution_summary`. Free-form text rejects secret-like values.
Internal requester/actor provenance, hashes, response snapshots, and mutation
metadata are never returned by the public API.

Private heartbeat execution-attention items contain bounded execution, issue,
project, kind, title, request summary, request time, status, attention version,
execution state version, resolution outcome/summary when resolved, the close
state version, and an `ack_endpoint`. The receipt ack body is
`{ expected_attention_version, expected_execution_state_version_at_close,
idempotency_key }`. It is requester-only, checks current project access, is
idempotent for the same key and body, and never resumes work. Stale versions return `409`, including after consumption; current versions after another consumer return `already_consumed: true` without consuming again.

The full/private and public plugin MCP profiles expose typed execution tools
for list, detail, assigned creation, version-fenced transition, evidence list,
and existing-evidence link, plus requester attention list, detail, create,
cancel, and receipt acknowledgement. These tools preserve the REST projections
and require explicit lifecycle idempotency/version inputs on writes. Their
schemas exclude local file content and do not expose human resolution,
administrator recovery/retarget/cancel, or runner and harness controls. Public
actor-dependent calls use the selected connection-scoped `profile_ref`.

## Enums

| Domain | Field | Values |
|--------|-------|--------|
| Task | `status` | Project-defined stored board-column key matching `^[a-z0-9_]+$`; defaults are `backlog`, `todo`, `in_progress`, `done`, with system status `cancelled` |
| Board column | `description` | Optional stage criteria or agent guidance |
| Board column | `recommendationRole` / `recommendation_role` | Nullable workflow role request field: `candidate`, `active`, or `excluded`; both aliases must match when both are present. Responses use `recommendation_role`; `null` means unconfigured and not eligible for future recommendations. |
| Task | `priority` | `0` (urgent), `1` (high), `2` (medium), `3` (low) |
| Task update request | `comment_body` | Optional Markdown/plain text or rich-text HTML comment body created with the issue update; stored and returned as sanitized HTML |
| Task update request | `comment_mentions[].member_id` | Stable Atoll org member ID to mention in the issue update comment created by `comment_body`; not an auth user ID or display name |
| Task update request | `comment_source_metadata` | Optional explicit agent provenance using the same validated shape as direct comment `source_metadata` |
| Comment create request | `reply_to_comment_id` | Optional comment ID that this flat, one-level reply addresses; target must be an active comment on the same task |
| Comment create request | `source_metadata` | Optional agent-only routing object: `harness`, real `thread_id` and/or `session_id`, optional `host_id`; omit it when the host lacks a real identifier, and never invent one |
| Comment response | `author_type` | `human`, `agent`, or `automation`; automation comments have null `author_id` and null comment routing `source_metadata` |
| Comment response | `reply_to_comment` | Parent context including `id`, `body`, `author_type`, and routing-safe `source_metadata` |
| Comment list response | `comments[].mentioned_members[]` | Persisted mention recipient summary with `id`, nullable `display_name`, and nullable `type`; empty when no mentions are recorded |
| Comment create request | `mentions[].member_id` | Stable Atoll org member ID to mention in a direct comment API request; recommended for agents and integrations |
| Comment create response | `outcome.persistence` | `{ status: "persisted", comment_id }`; comment durability is reported independently of notification or transport state |
| Comment create response | `outcome.mentions.created` | Count of new notification rows created for resolved mention recipients |
| Comment create response | `outcome.mentions.deduped` | Count of existing idempotent notification rows reused for duplicate or retried mentions |
| Comment create response | `outcome.mentions.notification_rows` | Creation/deduplication/skip/failure counts; `status: "failed"` does not make the persisted comment a failure |
| Comment create response | `outcome.mentions.transport` | Asynchronous Google Chat dispatch state; `dispatch: "scheduled"` is not final delivery, `final` is null while any result is unknown, `mixed` means terminal recipient results differ, and `error` exposes safe lookup/scheduling failure details |
| Comment create response | `outcome.mentions.skipped[]` | Mention targets that did not create notification rows; each entry includes `member_id` and `reason` |
| Task | `recurrenceType` | `daily`, `weekly`, `biweekly`, `monthly`, `custom` |
| Scheduled task | `recurrenceMaterializationMode` | `completion` or `schedule` |
| Scheduled task | `recurrenceTime` | Local `HH:MM` time used with `schedule` |
| Scheduled task | `recurrenceTimezone` | IANA timezone used with `schedule` |
| Scheduled weekly task | `recurrenceDays[]` | Unique `mon`, `tue`, `wed`, `thu`, `fri`, `sat`, `sun` values |
| Goal | `status` | `active`, `achieved`, `missed`, `paused`, `cancelled` |
| KPI | `unit` | `count`, `percentage`, `currency`, `duration`, `ratio`, `custom` |
| KPI | `target_direction` | `increase`, `decrease`, `maintain` |
| KPI | `source_type` | `manual`, `webhook`, `api_poll`, `formula` |
| KPI snapshot | `source` | `manual`, `webhook`, `api_poll`, `formula`, `agent` |
| KPI HTTP sync | `status` | `draft`, `published`, `disabled` |
| KPI HTTP sync secret | `placement` | `authorization_bearer`, `x_api_key` |
| KPI HTTP sync run | `status` | `queued`, `running`, `success`, `error` |
| Initiative | `status` | `proposed`, `active`, `completed`, `paused`, `cancelled` |
| Status update | `status` | `on_track`, `at_risk`, `off_track` |
| Member | `role` | `owner`, `admin`, `member`, `guest` |
| Project member | `accessLevel` | `view`, `edit`, `admin` |
| Automation | `trigger_event` | `issue.created`, `issue.status_changed`, `issue.assigned`, `issue.priority_changed`, `pr.merged`, `ci.run.completed`, `schedule.issue_time` |
| Heartbeat signal | `type` | `kpi_off_pace`, `kpi_stale`, `issue_stale`, `issue_blocked`, `milestone_overdue`, `initiative_stalled`, `initiative_target_due_soon`, `initiative_target_overdue`, `initiative_target_blocked`, `webhook_failing` |
| Heartbeat signal | `severity` | `info`, `warning`, `critical` |
| Custom view | `display_mode` | `board`, `list` |

## Attachment

Upload with multipart field `file`. The file must be non-empty and no larger
than 10 MiB. Declared images must be signature-valid PNG, JPEG, GIF, or WebP;
SVG and other declared image types are rejected.

| Response field | Type | Notes |
|---|---|---|
| `id` | UUID | Attachment identifier |
| `filename` | string | Original filename, limited to 255 Unicode characters |
| `file_size` | integer | Size in bytes |
| `mime_type` | string | Declared upload type |
| `uploaded_by` | UUID or null | Uploading member |
| `created_at` | timestamp | Creation time |
| `url` | string | Relative authenticated content API path; resend auth when fetching |

Storage bucket and path fields are intentionally not returned. Project-scoped
reads require project access; upload and delete require `edit` or `admin`.
Guests cannot access attachments on unprojected issues.

## Dependencies

Dependency creation requires the blocking issue to belong to a project because
the persistent release point is a board column there. A projectless issue may
be the blocked target when the caller has permission to use it.

`GET /api/orgs/{id}/issues/{issueId}/dependencies` returns `blocking` and
`blockedBy` arrays. Each dependency includes:

| Response field | Type | Notes |
|---|---|---|
| `id` | UUID | Dependency identifier |
| `issue` | object or null | Authorized target projection with `id`, `number`, `identifier`, `projectSlug`, `title`, and `status`; inaccessible targets are `null` |
| `issue.identifier` | string or null | Canonical project-prefixed issue reference for navigation; `null` for projectless targets |
| `issue.projectSlug` | string or null | Collision-free project route segment; `null` for projectless targets |
| `createdAt` | timestamp | Dependency creation time |
| `releaseColumnId` | UUID | Persistent release column in the blocking issue's project; present when the blocking issue is authorized |
| `release_column_id` | UUID | Compatibility alias for `releaseColumnId`; present with the canonical field |
| `releaseColumn` | object or null | `{ id, key, label, position, projectId }` release column projection |
| `satisfied` | boolean or null | Whether the blocker is archived or cancelled, or reached the release column position |

Archiving a blocker preserves the dependency edge and configured release column while satisfying the dependency. Restoring it re-evaluates that same release point and can block the dependent again. Configurable release-point and cancelled-blocker behavior are unchanged.

The dependency-release migration backfills existing dependencies to the
blocking project's `done` column. During a rolling deployment, compatibility
reads may omit release fields from older rows; treat missing release metadata as
the legacy open-blocker behavior until the migration is applied.

### Dependency chain fields

`GET /api/orgs/{id}/issues/{issueId}/dependencies?view=chain` returns a bounded
normalized graph:

| Field | Notes |
|---|---|
| `root_issue_id` | Authorized root issue UUID. |
| `direction` | `upstream`, `downstream`, or `both`; default `both`. |
| `depth` | Traversal depth, default `2`, capped at `5`. |
| `nodes[]` | Readable issue projections with readiness and dependency counts, or opaque restricted tokens with `readiness: "unknown"` and `permissions.read: false`. |
| `edges[]` | Upstream/downstream node IDs, permission flags, optional `release_condition`, `satisfied`, and reason (`release_reached`, `release_not_reached`, or `readiness_unknown`). |
| `counts` | Returned/known nodes and edges, direction counts, readiness counts, restricted nodes, and unsatisfied release conditions. |
| `page` | `limit`, `truncated`, and opaque `next_cursor`. |

The chain is read-only. Use `limit` and `cursor` for bounded traversal; do not
infer restricted issue identity from the token. Chain cursors are signed,
opaque, and bound to the current graph revision, root, direction, depth, limit,
and caller scope. If the graph changes while paging, the route returns `409 Stale dependency chain cursor`; restart without `cursor`.

## External References

External-reference response items contain `link_id`, `id`, `org_id`,
`target_type` (`issue` or `project`), `target_id`, `provider`, `object_type`,
`provider_object_id`, `provider_container_id`, `canonical_url`, bounded
`display_metadata`, `provenance`, `resolvable`, `resolution_error`,
`last_observed_at`, `created_at`, `updated_at`, and `linked_at`. The REST POST
request accepts `url` plus optional `provider: "github"` and
`object_type: "pull_request"`; provider identity fields are not caller
inputs. GitHub links require numeric immutable IDs from the authorized live
provider response or return `422` with
`code: "github_identity_unavailable"`. Link and unlink writes emit the
metadata-only Activity actions `external_reference.linked`,
`external_reference.updated`, or `external_reference.unlinked`.

Manual Web links use the same scoped endpoints with the explicit body
`{ "url": "https://example.com/document", "provider": "external_document", "object_type": "document" }`.
Omitted selectors still mean a verified GitHub pull request; failed verification
never falls back to manual creation. Web links require HTTPS, reject credentials
and control characters, and allow at most 2048 UTF-8 bytes after URL normalization.
Atoll does not fetch, embed, verify, or sync their content. Query strings and
fragments remain part of the URL identity. Repeated links to the same normalized
URL and target reuse the existing association; unlink affects only that target.

Manual responses use `provenance: "external_document"`, `resolvable: false`, and
`resolution_error: "not_verified"`. This means verification was not attempted,
not that the URL failed. Provider IDs are server-derived URL identity keys, not
provider proof. `last_observed_at` records URL submission; `linked_at` is the
target association's Added date. No provider freshness is claimed.

Task and Project Context show manual links in Documents. The Context v1 index
remains provider-only; use the canonical external-reference list/get routes to
discover manual links. Typed MCP creation remains GitHub-only. Existing MCP
reference list/get/unlink tools preserve the scoped REST behavior.

### External operational delivery context

Manual `workflow_dispatch` evidence requires one distinct current linked PR,
canonical numeric PR and repository identity, and matching head SHA and branch.
Several issue links to that same PR are allowed. Provider PR membership remains
required for `pull_request` runs. Unresolved dispatch identity creates no signal.

`GET /api/orgs/{id}/issues/{issueId}/external-operational-signals` returns
`{ deliveryContext }`. The value is `null` without a linked PR. With several
links, selection prefers an open PR, then the latest `updated_at`, then the
highest PR number. Otherwise it
contains `repository`, `pull_request`, nullable `review`, `workflows`,
`required_checks`, `freshness`, nullable `strongest_blocker`, and `partial`. PR,
review, and workflow evidence includes nullable `observed_at`,
`provider_updated_at`, `provider_event_id`, and `source_url`. The PR includes
the exact `head_sha`.
Review state is `pending`, `approved`, or `changes_requested`; workflow state is
`pending`, `passed`, `failed`, or `cancelled`. Older-head evidence is not
current. Workflow `required` is always `false` because configured workflow
paths do not prove GitHub branch protection. Raw payloads, review bodies,
actors, logs, and credentials are excluded. A `pending` review or workflow with
null provenance has no current-head observation; this absence does not by
itself set `partial`. Disabled verification stops new projections. Workflow
conclusions map `success`/`neutral` to `passed`,
`cancelled`/`stale`/`skipped` to `cancelled`, and other supported terminal
conclusions to `failed`.
The selected PR-link state is authoritative. If a same-head PR observation
disagrees, its `observed_at`, `provider_updated_at`, and `provider_event_id` are
null, `source_url` uses the link URL, the observation is excluded from
`freshness`, and `partial` is true.
`required_checks.state` is `disabled`, `complete`, `partial`, or `unavailable`;
`required_checks.aggregate` is `none`, `pending`, `passed`, `failed`,
`cancelled`, or `unknown`. Each item includes `context`, nullable
`integration_id`, `policy_sources` (`classic`, `ruleset`, or both), normalized
`state`, bounded nullable provider state/conclusion, a safe nullable GitHub
`url`, and nullable `provider_updated_at`. The collection has at most 200
items, plus nullable safe `error_code` and `observed_at`. The server-only
`ATOLL_GITHUB_REQUIRED_CHECKS_READ_ENABLED=1` flag enables the read-only
provider collection; disabled is the default. With reads disabled, state
`disabled` and aggregate `none` do not set `partial`. When enabled, partial or
unavailable collection, stale, ambiguous, or missing evidence remains `unknown`
and sets `partial`.
A policy endpoint returning GitHub's exact plan-limit HTTP 403 is classified
as `plan_restricted`; other 401/403 responses remain permission failures.
The collection is `partial` if one policy source succeeds, or `unavailable`
if both fail, and its aggregate remains `unknown`. The first policy error
(rulesets before classic protection) supplies `error_code` when errors differ.
Configured workflow results remain separate evidence with `required: false`.

Review aggregation keeps each reviewer's latest exact-head opinion, ignores
comments, and removes dismissed opinions. Change requests win; `approved`
means at least one effective approval and no effective change request. It does
not prove required-review counts or branch protection.

## Task Activity

`GET /api/orgs/{id}/activity` returns `{ data, currentMemberId, limit, offset,
hasMore }` and accepts `filter=all|by_me|mine`. `GET
/api/orgs/{id}/issues/{issueId}/activity` returns `{ data, items, limit, offset,
hasMore }`. Items retain the `activity_events` fields. Top-level `actor` is a
current member projection and can reflect later profile changes; the immutable
event-time actor snapshot is `metadata.actor` with `id`, `display_name`, `type`,
and `avatar_url`. The
canonical actions cover task lifecycle, comments, assignees, labels,
dependencies, initiative/target links, GitHub PR links and updates, attachments,
and subtasks. Notification, webhook, realtime, and delivery records are excluded.
The exact canonical `action` values are `issue.created`, `issue.updated`,
`issue.archived`, `issue.unarchived`, `comment.created`, `comment.updated`,
`comment.deleted`, `assignee.added`, `assignee.removed`, `label.added`,
`label.removed`, `dependency.added`, `dependency.removed`, `dependency.release_updated`,
`initiative.linked`, `initiative.unlinked`, `initiative_target.linked`,
`initiative_target.unlinked`, `github_pr.linked`, `github_pr.updated`,
`attachment.added`, `attachment.removed`, `subtask.created`,
`subtask.completed`, `subtask.reopened`, `subtask.removed`, `subtask.updated`,
`external_reference.linked`, `external_reference.updated`, and
`external_reference.unlinked`.
Use `limit` in `1..100` and a non-negative `offset`; older history may be
partial because pre-contract events are not fabricated or backfilled.

## Response Format

Most endpoints return JSON; attachment content returns binary bytes. Successful:
`200`, `201`, or `202` when durable follow-up remains pending. Errors:
`{ "error": "message" }` with `400`, `401`, `402`, `403`, `404`, `409`,
`413`, or `500`.

Issue-child endpoints, including activity, PR links, dependencies, subtasks,
labels, and initiative links, return `404` for a missing, wrong-organization,
wrong-parent, or unreadable directly requested issue. Readable issues with
insufficient write access return `403`; collection reads can omit unreadable
linked resources. Other endpoints may use `403` for organization-membership or
role failures.

REST list responses use resource-specific keys by default. Main list endpoints support `?shape=envelope` or `?response_shape=cli` to return `{ resource, items, total, limit, offset, nextOffset, truncated, hint }`.

## Notes

- All timestamps are ISO 8601 in UTC
- Descriptions support Markdown; comment bodies accept Markdown/plain text or rich-text HTML and are stored as sanitized HTML
- Board columns (statuses) are customizable per project -- query `/board-columns` for available statuses and optional descriptions
- Default statuses for new projects: `backlog`, `todo`, `in_progress`, `done`
- `cancelled` is always valid but not shown on the board
- Agent actions appear in the activity feed with the agent's name
- Changes via API appear in real-time on the web board


### Local runner UI boundary

The optional `atoll-runner run --ui` / `atoll-runner ui` interface is loopback-only,
not a hosted API or MCP surface. Its browser projection excludes credentials,
raw configuration, prompts, and model output. Local bindings use `repo_ref` but
do not grant project/repository access. Intake is read-only locally; hosted
Workspace Settings → Runners owns pause/resume. See the CLI local-runner guide.

## MCP Events subscription fields

The modern public OAuth MCP endpoint (`https://atollhq.com/mcp`, version `2026-07-28`) advertises `events` and supports `events/list`, `events/subscribe`, and `events/unsubscribe`. Legacy 2025 tool calls remain supported. No event subscriptions are available to API-key, private or stdio identities.

The authenticated adapter uses `POST /api/mcp-events/subscriptions` to create/refresh and `DELETE /api/mcp-events/subscriptions` to unsubscribe. Resolve the OAuth connection and optional `X-Atoll-Agent-Profile` through existing auth. Request fields are the protocol `name`, `arguments`, `delivery`, optional `ttlMs`, and optional `cursor: null`. Profile selection travels in the header, not business filters.

Events: `issue.status_changed` (`project_id`, optional `issue_id`, `from_status`, `to_status`); `attention.created` (`project_id`, optional `kind`); `execution.state_changed` (`project_id`, optional `issue_id`, `to_state`). Project and issue UUIDs must be readable in the selected profile; status keys must exist in the project's workflow.

Subscribe requires `{ mode: "webhook", url: "https://…", secret: "whsec_…" }` with a canonical Base64 key of 24–64 bytes. Unsubscribe uses the same name/arguments/callback identity and does not require a secret. The principal is the resolved OAuth connection plus profile grant. IDs use canonical JSON and callback URLs. POST returns `{ id, refreshBefore, cursor: null, truncated: false }`; DELETE returns `{}`. Secrets are never returned.

Every grant is bounded by validated OAuth access-token expiry and a shorter finite `ttlMs`, if requested. Even `ttlMs: null` receives a finite grant. Refresh rotates secrets with overlap through the previous grant's expiry. Callback verification is cached only through its granted expiry. Delivery rechecks connection/profile/project access and uses the existing SSRF-safe HTTPS boundary and 15-minute maintenance runner. One compact immutable occurrence is sent per request with stable event ID and Standard Webhooks headers; retries stop at the grant deadline active when the event occurred, even if fanout is delayed. Shorter refreshes clamp cached verification; reactivation requires a fresh challenge. Quiet expiry/revocation and expired rotation overlap clear signing material through bounded maintenance batches. No replay; 410/413 are terminal. Callback errors use `callback_endpoint_error` with a categorized `reason`, mapped to MCP `-32015`. Temporary service failures map to MCP `-32603`.

## MCP App extension (not a REST endpoint)

Public plugin discovery adds the app-only `atoll.open` global entrypoint,
input `{}`, initial result `{page:"home"}`, and resource
`ui://atoll/command-center` with MIME `text/html;profile=mcp-app`.
`_meta.ui.resourceUri`, app-only visibility, a monochrome tool icon and
`_meta["openai/ui"].entrypoints:[{type:"global"}]` identify the UI.
Existing business reads keep their `profile_ref` and authorization contract.
No REST field, write endpoint or persistent profile preference is added.

## Bounded collection search

Projects, goals, KPIs and initiatives accept `q` for case-insensitive literal
substring matching of the display name/title, `q_exact=true` for the complete
name, and `limit`/`offset` for server-side pagination. Defaults in bounded mode
are 25 results, maximum 100, and offset 0. Filtering and authorization precede
pagination; offsets beyond matching results return an empty page with the exact
total. KPI pages include current calculated values. Use `shape=envelope`
(or `response_shape=cli`) for `resource`, `items`, `total`, `limit`, `offset`,
`nextOffset`, `truncated` and `hint`. Supplying a search or pagination parameter
also selects bounded retrieval. Calls without these parameters retain their
legacy resource-key response and full-list behavior.

Members add `member_id=<UUID>` and `q_exact=true` in bounded directory mode.
Identity filtering uses the same collaborator visibility rules and safe fields
as name search; it does not grant access or return credentials or account email.
Members and initiatives also accept `scope=accessible_projects` for a bounded
union under the current actor. The server derives project IDs; callers cannot
supply ID arrays. Guests see only accessible project-linked initiatives and
eligible collaborators. Existing member/admin projectless initiative rights
remain. Empty project access gives guests an empty page. Unknown scope or scope
combined with an explicit project returns `400`. Explicit project scope remains
`project_id` for initiatives and `projectId` for members.

Full issue lists resolve authorized human identifiers such as `AH-123`,
`ATOLL-123`, `#123` or a number before loose title/description matching. They also
accept `q_exact=true` for the full title. The exact flag is rejected with `400`
for compact `view=board`/`view=list`; existing compact search stays unchanged.
The existing issue filters and actor/project authorization still apply.

CLI list commands for projects, goals, KPIs, initiatives and members use
`--search`, `--exact`, `--limit` and `--offset`; issue list uses `--q` with
`--exact`. Member list also supports `--member-id`. These filters are evaluated
by the API. Existing public/private MCP list tools expose `q`, `q_exact`,
`limit` and `offset`; `atoll_list_members` adds `member_id`. Member and initiative
lists expose `--accessible-projects` in the CLI and `scope=accessible_projects`
in MCP. The initiative flag suppresses a configured default project and cannot
combine with `--project` or `--org-wide`. Normal MCP goal/KPI/initiative calls
without query, exact, paging or scope options retain legacy full-list responses.
Composer search uses a constant number of bounded list calls per profile and
entity kind, independent of the number of accessible projects.

### Interactive forms and create identity

`POST /api/orgs/{id}/issues` optionally accepts HTTP `Idempotency-Key: <UUID>`.
The API scopes it to the authenticated member/org. One transaction consumes it;
concurrent/later/changed-body replay returns 409 without another issue/effect,
even after deletion. Invalid key returns 400; definite validation failure does
not consume it. No header preserves independent create. Never retry an uncertain
result automatically. The interactive tool generates this identity internally;
ordinary CLI/MCP arguments do not expose it.

`atoll_create_issue_interactive` seeds: required profile_ref; optional title,
description, project_id UUID, project_query, milestone_query, priority 0-3 (0 Urgent, 1 High, 2 Medium, 3 Low),
assignee_query, assignee_ids (max 10), start_date and due_date. Explicit forms
confirm basic then project-dependent fields; cancel/refusal/expiry/invalid data
creates nothing. State expires after ten minutes and binds grant, actor, profile,
tool and original arguments. Both standard form and OpenAI rich-form capabilities
are required. Normal atoll_create_issue is unchanged.

Project milestone GET accepts optional q/q_exact/limit 1-100/offset>=0 and
shape=envelope. Filter/paging happen before materialization; current calculated
issueCount/completedCount/progress/statusCounts remain. Empty pages retain total
and pagination. Default calls preserve the unpaged milestones alias.

Forms retain at most 25 choices per collection. A truncated project or milestone
page returns `issue_create_refine_project` or `issue_create_refine_milestone`;
restart with a narrower `project_query` or `milestone_query`. A known accessible
`project_id` can be supplied directly. No-match or truncated assignee search
returns `issue_create_refine_assignee`; revise `assignee_query` rather than
silently dropping the assignment. Recovery includes confirmed basic field seeds.
Refinement creates no issue.


## Vercel deployment context

Vercel deployment observations use `provider: "vercel"`, `object_type: "deployment"`,
and `provenance: "vercel_api"` in existing scoped External Reference reads.
Metadata contains only label, environment, state, optional exact revision, and
provider effective time. A complete authenticated repository/SHA tuple proves
identity. Later missing fields cannot erase that proof; contradictory known
identity is rejected. Partial observations are never combined to invent proof.
The mapped project always receives the reference. An issue receives it only
when exactly one unarchived issue in that project has the same numeric GitHub
repository ID and exact SHA. Preview/staging supersession is chronological;
production supersession follows an authenticated project production target and
supports rollback to an older build. Deployment evidence does not change issue
status, authorize release, or prove acceptance. Generic list/get/unlink work;
manual link remains GitHub-pull-request-only. Unlink does not suppress later
verified ingestion. See https://docs.atollhq.com/integrations/vercel.

### Vercel connection and recovery fields


Vercel deployment `display_metadata` has only `label`, `environment`, `state`,
optional `revision`, and `provider_effective_at`, within 2 KiB. Environment is
`preview|staging|production`; state is
`queued|building|ready|failed|cancelled|superseded`. Revision is lowercase
40-hex and is omitted when unavailable. Provider time is an RFC 3339 UTC
string. Resolution errors also include `identity_unavailable`,
`repository_mismatch`, and `provider_unavailable`. Unlink is association-only;
a later verified observation can restore it.

The owner/admin human-session endpoint is
`/api/orgs/{id}/integrations/vercel`. GET returns `{ connections }` with safe
`id`, `team_id`, `state`, `health_status`, nullable `health_code`,
`last_health_checked_at`, `disabled_at`, `created_at`, `updated_at`,
`webhook_url`, and `mappings`. Mapping fields are `id`, `connection_id`,
`vercel_project_id`, `project_id`, `github_app_repository_id`, and `updated_at`.
No credential value or ciphertext is returned.

PUT requires all of these fields and rejects extras:

| Field | Contract |
| --- | --- |
| `connection_id` | Proposed UUID for a new connection; saved UUID for edits |
| `expected_updated_at` | `null` for a new connection, exact saved timestamp for edits |
| `team_id`, `vercel_project_id` | 1–200 letters, digits, underscores, or hyphens |
| `project_id`, `github_app_repository_id` | Same-org UUIDs; repository must be enabled and verified |
| `api_token`, `webhook_secret` | Write-only non-empty strings, at most 4,096 UTF-8 bytes each |

PUT validates the live Vercel project/repository and returns
`{ connection_id, updated_at, webhook_url }`. Credentials must be supplied
again on edit. Include every mapped Vercel project in the account webhook’s
project scope, using the same callback URL and signing secret for the connection;
Atoll does not change Vercel webhook settings. A mapping with history cannot change its Atoll project or
repository. DELETE requires `{ connection_id, expected_updated_at }` and
returns `{ disabled: true, updated_at }`. It clears credentials and revokes
resolvability while preserving history.

An organization supports at most 50 team connections, including disabled
connections. Existing connections can reconnect and update mappings at that
limit; new teams return `409 connection_limit`.

POST `/api/orgs/{id}/integrations/vercel/reconcile` requires
`{ connection_id }`; optional `vercel_project_id` selects one saved mapping.
The response is `{ complete, results }`. Each result contains `mapping_id`,
`environment`, `discovered`, `ingested`, `skipped`, `failed`, `truncated`, and
`codes`. It reads one page of at most 50 per environment, plus the current
production target when it is outside that page (at most 151 deployments per
mapping). The extra target counts in `discovered`; history remains `truncated`
when the provider has more pages. It stops new work after a bounded request budget. No raw provider response or credential is
returned. Partial results use HTTP 200 with `complete=false`.

Setup errors use `{ error: <safe code> }`: 400 for invalid input/provider
proof, 403 for a non-human/non-admin caller, 404 for a missing connection or mapping,
409 for `configuration_changed`, `mapping_has_history`, `mapping_limit`, or `connection_limit`,
and 503 for transient provider, secret-key, or storage failure. Connection
configuration uses an exact version fence; read the saved state before
retrying an uncertain write.

## Compact Context index

`GET /api/orgs/{id}/issues/{issueId}/context` and
`GET /api/orgs/{id}/projects/{projectId}/context` return `{ context }` after
normal target authorization. Inaccessible targets are concealed. Projectless
issues retain their existing access rules; setup-only agents receive no Artifact
items. Project reads include directly linked records only.

Use optional `group` (`development`, `design`, `discussion`, `documents`,
`deployments`, or `production`) and `limit` (1–25, default 5 per group).
Without `group`, all six groups are returned. Design and Discussion are reserved
empty groups. `cursor` requires one group and the same target and limit as its
previous page. Unknown or repeated query keys and invalid cursors return 400.
Each group has its own `page.next_cursor` and `page.has_more`; these are live
keyset pages, not a historical snapshot. Refresh to restart after evidence changes.
Deduplicate continued items by `id`.

The version-1 response contains `target`, `groups`, and `partial`. Each group has
`key`, `state` (`available`, `empty`, `partial`, or `unavailable`), `items`, `page`
(`limit`, `returned_count`, `has_more`, `next_cursor`), and safe `errors`.
Items contain a namespaced `id`, `kind`, `group`, `authority`, `availability`,
`summary`, `freshness`, `current_identity`, `follow_up`, and action capabilities.
Artifact identities carry the current revision; revision-bound delivery and
provider evidence carry an available commit SHA. Null means unknown, not current.
External evidence is stale after 24 hours. Partial evidence stays explicit.

Artifact summaries contain only title and type. Reference summaries contain a
safe label/URL, provider/object type, environment, state, and provider time.
Delivery summaries contain PR number/state, review, configured-workflow and
required-check aggregates, and a fixed blocker code. Atoll records,
provider references, and operational evidence have separate authority. A passed
check, merged PR, ready deployment, current production target, and human
acceptance are separate facts.

Follow-ups are `artifact_revision` (Artifact and optional revision UUID),
`external_reference` (reference UUID), or `issue_delivery_context` (issue UUID).
Use existing authorized detail reads only when needed. The index never returns
Artifact bodies, digests, revision history, provider payloads, credentials, or
unbounded signal/check collections. Mutation capabilities are display hints;
every mutation rechecks access. Responses are capped below 64 KiB; a larger
request returns 413 `context_response_too_large`, so retry with a smaller limit.
An individual source failure affects its group; a total read failure returns
500 `context_unavailable`.

CLI: `atoll context list --issue ATOLL-42 --json` or
`atoll context list --project project-slug --group documents --limit 5 --json`.
Pass exactly one target. Continue with `--group`, `--limit`, and `--cursor`.
JSON preserves the REST envelope; human output includes explicit follow-up
commands. The full/private MCP tool is `atoll_list_context`, with exactly one
`issue_id` or `project_id` UUID and the same optional group, limit, and cursor.
Public MCP Context and delivery-detail tools are not available; AH-3067 owns
post-freeze parity. Existing public Artifact and External Reference reads remain
available. No existing issue, heartbeat, or public tool schema changes.

## Work recommendation fields

The project `work-recommendations` REST response has:

| Field | Meaning |
| --- | --- |
| `recommendations[].issue` | `id`, `number`, `title` (at most 240 Unicode characters), `status`, nullable `priority` and `due_date`, `created_at`, `updated_at` |
| `action_kind` | `start`, `continue`, or `review_assignment`; not permission to execute |
| `reasons` | At most three fixed-code explanations, each with `summary` (at most 300 characters) and one authorized source |
| `limitations` | At most five deduplicated limitations, ordered by code and visible source ID; hidden context never includes type, identity, title, or count |
| `limitations_truncated` | More visible limitations exist than the returned five |
| `page` | `limit` (1–5), `has_more`, nullable `next_cursor` |
| `evaluation` | `evaluated_at`, `eligible_count`, `excluded_count`, `primary_exclusion_reason_counts` across the entire bounded scan |

Ranking reason codes: `urgent_blocked_downstream`, `overdue_milestone`,
`current_kpi_relevance`, `explicit_strategy_link`, `issue_overdue`, `issue_due`,
`issue_priority`. Each has `source_type` (`issue`, `milestone`, `initiative`, or
`kpi`), `source_id`, optional `source_title`, and optional `source_as_of`.

Limitation codes: `kpi_stale`, `kpi_current_unknown`, `strategy_link_absent`,
`kpi_evidence_absent`, `linked_context_not_visible`,
`assignment_requires_review`, `linked_context_unavailable`, `strategy_inactive`.
A limitation may include one authorized source reference; missing or hidden
sources have none. `linked_context_unavailable` applies only to visible
downstream work with an absent or unconfigured recommendation workflow.

Primary exclusion codes: `project_inactive`, `issue_archived`, `issue_cancelled`,
`workflow_role_unconfigured`, `workflow_role_excluded`,
`dependency_evidence_invalid`, `unresolved_dependency`.

`due_date` is a valid `YYYY-MM-DD` UTC calendar date. Source timestamps are UTC;
`evaluated_at` has canonical milliseconds and `Z`. KPI freshness uses elapsed
hours and includes the exact staleness threshold. Null timestamps or current
values are unknown. A future timestamp or malformed evidence fails the request.
Cursors expire after 15 minutes, are limited to 2 KiB, and require a fresh read
when expired. They do not freeze database state or authorize mutations.

### Agent lifecycle boundary

Agent rows add `lifecycle_state` and `lifecycle_version`; lease rows add immutable `agent_lifecycle_version`. Only enabled agents can authenticate, receive new assignments, mint keys, change access/policy, or use runner authority. Disable preserves history and capacity; revoke retains identity but releases capacity and is terminal. Enable requires fresh credentials/consent and never resumes work automatically. Human-only management uses `POST /api/orgs/{id}/agents/{agentId}/lifecycle` with action, expected_version, and idempotency_key. CLI/MCP callers cannot use it. Authorized workforce `capabilities` report the available transitions and management controls; historical visibility does not grant effective access. See API endpoints for replay and conflict behavior.

### Recurring task destination

Create, update, and bulk create accept optional nullable `recurrenceSpawnColumnId`
(or `recurrence_spawn_column_id`). Use a real column UUID from the project workflow.
The column must belong to the task project and have a key other than `done` or
`cancelled`. Omission preserves a saved target; new recurrence resolves the project
default. Explicit `null` resets to `todo`, or the first eligible column by position
and ID. A project with no eligible column rejects materialization. Projectless
recurrence retains a null target. Disabling recurrence clears the stored target.

Responses keep `recurrence_spawn_column_id` as the addressed row's stored value.
`recurrence_spawn_owner` is null for ordinary tasks, an authorized
`{state: "available", issue_id, project_id, spawn_column_id}` projection, or
`{state: "unavailable"}` without owner IDs. Read access permits the projection;
write access is checked independently.

Target-only edits do not move the current task or reset its schedule. Root-owned
child edits update the authorized root; send local status, title, assignment, and
project edits separately. Moving a series root keeps historic children in their
projects. Include a valid destination target with the project move, or omit it to
resolve the new project's default atomically. The next task uses the series'
current project and selected column even when an older occurrence is completed.
A deliberate root move or root preference action establishes root ownership for
legacy completion too; untouched legacy completion remains local. Completing a
scheduled occurrence creates no immediate successor. The maintenance sweep
materializes its next scheduled occurrence in the current series destination.
Unreadable owners reveal no IDs; denied destination writes create no successor.

Delete a referenced board column with independent `reassignTo` (issue statuses),
`releaseReassignTo` (dependency release points), and `recurrenceReassignTo`
(nonterminal recurrence targets) mappings. An eligible `reassignTo` is the
compatibility fallback for recurring targets. Remaps and deletion are atomic.
Explicit new-field requests fail with 503 while the additive migration is
unavailable; ordinary requests retain compatibility.

## Actor work recommendation fields

`actor` contains the authorized target `id`, `type`, and agent `lifecycle`
(`state`, `version`; null for humans/integrations). `scope.project_id` is nullable.
`recommendations` reuse project reason/limitation fields and add the authorized
`project` (`id`, `name`, `slug`). `current_work` contains compact `issue`, nullable
`project`, inspection `action`, `assignment_conflict`, and nullable minimal
`execution` (`id`, canonical `state`, `state_version`). It has no summaries,
private URLs, logs, prompts, credentials, provenance, or hidden counts.
`current_work_truncated` reports only visible display truncation. `can_assign`
is an advisory current-scope flag; mutation routes remain authoritative.
`availability` is `available_for_recommendation`, `occupied`,
`availability_not_established`, or `inactive`. `caveats` contains
`snapshot_not_reservation` and optionally `availability_not_established`.
`evaluation.evaluated_at` fixes UTC ranking time; `page` has `limit`, `has_more`,
and nullable signed `next_cursor`. Actor pages reject drift with 409.
