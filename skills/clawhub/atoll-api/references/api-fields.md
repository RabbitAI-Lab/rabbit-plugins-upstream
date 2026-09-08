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
`clientVersion` (numeric semantic version), and `intakeState` (`active` or
`paused`). The server derives the display name. Responses include computed
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
automatic replacement. Paused, disconnected, stale, or replaced runners cannot
mutate or replay. Lease rows enforce a composite `(issue_id, org_id)` foreign key.
Mutation metadata is closed: `progress` accepts `preparing`,
`turn_intent_persisted`, `sdk_accepted`, `running`, `model_completed`, or
`finalizing`; `errorCode` accepts `runner_error`, `sdk_error`, `model_error`,
`timeout`, `cancelled`, or `unknown`. Free-form runtime details are rejected.

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

Successful `POST /api/orgs/{id}/members/{memberId}/avatar` requests return
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
  "labelIds": ["label-uuid-1", "label-uuid-2"]
}
```

Most fields work on both POST (create) and PATCH (update). `labelIds` is accepted on task create and bulk create. For existing tasks, use the label endpoints or `atoll label add/remove`.

- **Multiple assignees**: Use `assigneeIds` (array). Legacy `assigneeId` (single) still works. Responses include `assignees` array with `id`, `display_name`, `type`, `avatar_url`.
- **Start date**: Sets when work begins. Combined with `dueDate`, defines the Gantt time span.
- **Recurring tasks**: Set `recurrenceType` + optional `recurrenceInterval` (default 1). Weekly series can set unique `recurrenceDays` values from `mon` through `sun`; Atoll sorts them into calendar order. When marked `done`, one next instance is auto-created in the same series. Responses include normalized `recurrence_days` and `recurrence_schedule: { type, interval, days }`.
- **Archived tasks**: Have `archived_at` timestamp. Excluded by default; pass `includeArchived=true`.
- **GET detail** returns enriched data: `milestone`, `creator`, `assignee`, `assignees`, `sub_tasks`, `issue_labels`, `isBlocked`.

Full `GET /api/orgs/{id}/issues` list items include the canonical
project-prefixed `identifier` and collision-free `projectSlug` for project
issues, or `null` for projectless issues. Compact `view=board` and `view=list`
items do not include these fields.

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

## Agent Fields

Create org-wide agents with `{ "name": "...", "role": "member", "setupScoped": false }`; org-wide creation is owner/admin-only. Create project-scoped agents with non-empty `projectIds`, for example `{ "name": "...", "projectIds": ["project-uuid"] }`; `projectId` remains accepted as a legacy/default-project alias and is merged with `projectIds`. Project-scoped agents are created as guests, and human members may only scope them to projects they can access. Create personal agents with `{ "name": "...", "personal": true }`; personal agents inherit their human owner's project access and reject explicit `projectId`/`projectIds`.

Key-minting agent creation responses contain the one-time raw `apiKey` and its stable `apiKeyId`. Creation with `oauthOnly: true` omits both fields.

Manageable-agent rows always include nullable `key_prefix`, `last_used_at`, and `activity_last_used_at`. `key_prefix` and `last_used_at` describe only the selected active API key. `activity_last_used_at` is the latest timestamp from an active API key or a non-revoked OAuth agent profile. Historical OAuth use is not backfilled.

Workforce read rows from `GET /api/orgs/{id}/agents/workforce` contain bounded identity fields, safe `projects` summaries, `project_ids`, `created_at`, nullable aggregated `last_used_at`, nullable personal-agent `owner` display metadata, `scope` (`personal`, `project`, or `organization`), and `capabilities` with `can_view`, `can_manage_access`, `can_manage_keys`, `can_disable`, and `can_revoke` booleans. Project-admin visibility sets only `can_view` unless an existing creator/personal-owner management rule independently grants more. `key_prefix` is optional and is returned only when existing key-management authority allows it. The response never includes emails, auth IDs, hidden projects, credentials, OAuth grants, prompts, raw activity, lifecycle fields, or organization capacity.

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

## Public MCP planning fields

The public plugin uses snake_case MCP fields and adds `profile_ref` to each
actor-dependent call. `project_id` accepts a project UUID, exact slug, or exact
name for initiative and milestone operations; the MCP server resolves it to a
canonical UUID before writing. Issue references accept UUIDs, bare numbers,
`#number`, `ATOLL-number`, `TSK-number`, and unambiguous project-derived
prefixes. Initiative milestone-link creation also accepts an exact milestone
name through the backing API resolver; unlink operations use the canonical
milestone UUID.

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
  "name": "Auto-assign urgent bugs",
  "trigger_event": "issue.created",
  "conditions": [{ "field": "priority", "operator": "eq", "value": 0 }],
  "actions": [{ "type": "set_assignee", "value": "member-uuid" }],
  "enabled": true,
  "project_id": "project-uuid"
}
```

Supported action values are: `set_status` (lowercase status key using letters,
digits, and underscores), `set_assignee` (member UUID or `null`),
`set_priority` (integer `0` through `3`), `add_label` (label UUID),
`post_comment` (non-empty text), and `close_issue` (no value or `null`).
Unsupported action types or malformed values return `400` and are not saved.

**Dry-run test**: Send `{ "issue_id": "uuid" }` or `{ "issue": { "status": "todo", "priority": 2 } }`. Returns `{ matched, actions_that_would_run }`.

**Automation run history**: `GET /api/orgs/{id}/automation-rules/{ruleId}/activity`
returns `{ runs }` to owner/admin members, newest first and limited to the
latest 100 runs. Each run contains its status,
timestamps, safe error fields, a safe source-event projection, and ordered
`automation_action_runs` for actions that were actually attempted. Non-matching
events, dry runs, and rules with no executable actions create no run row. The
response excludes event payloads, action inputs, request headers, credentials,
and third-party response bodies.

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

```json
{
  "url": "https://example.com/webhook",
  "events": ["issue.created", "issue.updated"],
  "enabled": true
}
```

URL must be an HTTPS DNS hostname. IP literals, `localhost`, and `.local` hosts are rejected at creation; delivery refuses non-public DNS results and does not follow redirects. The create response includes a `secret` for HMAC signature verification. Store it immediately; it is shown only once.

List responses include `destination_display` and a deprecated `url` compatibility field containing only the origin plus `/…`. Payload schema version `2` is allowlisted. Delivery requests include `X-Atoll-Signature`, `X-Atoll-Signature-Version`, versioned `X-Atoll-Signatures`, and `X-Atoll-Delivery-Id`. Delivery history includes `delivery_id`, `status`, `status_code`, `error_code`, `delivered_at`, and `next_retry_at`, never payloads, receiver response bodies, or raw errors.

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
| Weekly task | `recurrenceDays[]` | Unique `mon`, `tue`, `wed`, `thu`, `fri`, `sat`, `sun` values |
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
| Automation | `trigger_event` | `issue.created`, `issue.status_changed`, `issue.assigned`, `issue.priority_changed` |
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

### External operational delivery context

`GET /api/orgs/{id}/issues/{issueId}/external-operational-signals` returns
`{ deliveryContext }`. The value is `null` without a linked PR. With several
links, selection prefers an open PR, then the latest `updated_at`, then the
highest PR number. Otherwise it
contains `repository`, `pull_request`, nullable `review`, `workflows`,
`freshness`, nullable `strongest_blocker`, and `partial`. PR, review, and
workflow evidence includes nullable `observed_at`, `provider_updated_at`,
`provider_event_id`, and `source_url`. The PR includes the exact `head_sha`.
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
