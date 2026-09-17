# CLI operations

Read this reference for routine Atoll CLI installation and resource operations. Load a more specific reference as well when the task involves the local runner, strategy heartbeat, execution lifecycle, or an integration.

## Quick Start — CLI (recommended)

Install globally or use via npx:

```bash
npm install -g @atollhq/cli   # or: npx @atollhq/cli ...
```

Configure once:

```bash
atoll auth login --key sk_atoll_...
atoll config set-org org-uuid
```

`atoll issue list` and `atoll issue create` apply the selected default team unless a command-level `--team` override is passed. Issue command `--project` flags accept a project ID, slug, or exact name, including list and bulk defaults. In bulk JSON items, `project` accepts those references while `projectId` and `project_id` are canonical IDs. `--milestone` accepts a milestone ID, or an exact milestone name when a project is selected with `--project` or the active profile's default project.

Moving a blocker issue between projects requires one explicit destination release
column per dependency. REST callers pass
`dependencyReleaseMappings: [{ dependencyId, releaseColumnId }]`; REST also
accepts `dependency_release_mappings` and legacy `releaseColumnMappings`, with
`dependency_id` and `release_column_id` item aliases. MCP callers use
`dependency_release_mappings: [{ dependency_id, release_column_id }]`. The CLI
accepts `--dependency-release-mappings` with camelCase items
`[{ dependencyId, releaseColumnId }]`. A projectless move is rejected when the
issue blocks other work. Do not infer a destination column from a label or
position.

`atoll issue list --open` excludes terminal statuses `done` and `cancelled`,
plus archived issues, while preserving every custom and other non-terminal
status. It composes with other list filters, ordering, pagination, and JSON,
and cannot be combined with `--include-archived`.

Full REST issue-list items include the canonical project-prefixed `identifier`
and collision-free `projectSlug` for project issues, or `null` for projectless
issues. Compact board/list views do not include these fields.

Common commands:

```bash
# Agent orientation
atoll heartbeat
atoll heartbeat --signals-only
atoll heartbeat --severity critical
atoll heartbeat --json
atoll agent-context

# List tasks
atoll issue list --json
atoll issue list --open
atoll issue list --status todo --priority 1 --limit 25
atoll issue list --scope blocked --initiative initiative-uuid --order-by due_date --order-dir asc

# View a task
atoll issue get ATOLL-42
atoll issue view ATOLL-42   # alias kept for humans
atoll issue delivery-context ATOLL-42

# Discover compact issue Artifacts, then fetch one body explicitly
atoll artifact list ATOLL-42
atoll artifact get <artifact-id> --issue ATOLL-42
atoll artifact create ATOLL-42 --kind implementation_plan --title "Implementation Plan" --body-file plan.md
atoll artifact update <artifact-id> --issue ATOLL-42 --expected-revision-id <revision-id> --body-file plan.md

# Create a task
atoll issue create --title "Fix login bug" --status todo --priority 1
atoll issue create --title "Plan rollout" --project project-slug --milestone "Launch"
atoll issue create --title "Weekly status review" --due-date 2026-07-06 --recurrence weekly
atoll issue create --title "MWF status review" --due-date 2026-07-06 --recurrence weekly --recurrence-days mon,wed,fri --recurrence-mode schedule --recurrence-time 09:00 --recurrence-timezone Asia/Singapore
atoll issue upsert --match-title --project <project-id> --title "Fix login bug" --status todo
atoll issue bulk-create --file ./issues.json --continue-on-error

# Update a task
atoll issue update ATOLL-42 --status in_progress
atoll issue update ATOLL-42 --status in_progress --comment-body "Starting this because the activation KPI is off pace."
atoll issue upsert ATOLL-42 --status in_progress
atoll issue bulk-update --file ./updates.json --dry-run

# Assign a task
atoll issue assign ATOLL-42 --to <user-id>
atoll issue assign ATOLL-42 --to self

# Comments
atoll comment add ATOLL-42 --body "Working on this now"
atoll comment add ATOLL-42 --body "tagging..." --mention-member <member-id>
atoll comment add ATOLL-42 --body "tagging..." --mention "Raphael Ubales"
atoll comment add ATOLL-42 --body "Agent update" --source-harness codex --source-thread-id <thread-id>
atoll comment add ATOLL-42 --body "Continuing this" --reply-to-comment <comment-id>

# --mention-member uses a stable Atoll org member ID; --mention exact-matches display names and fails on ambiguity.

# Labels, notifications, subtasks, activity
atoll label list
atoll label add ATOLL-42 bug
atoll notification list --json
atoll notification ack notification-uuid
atoll inbox list --json
atoll inbox view email-uuid --json
atoll inbox triage email-uuid --category support --priority 1 --status action_required
atoll inbox resolve email-uuid --note "Handled in ATOLL-123"
# Draft only; this does not send:
atoll inbox draft email-uuid --from support@atollhq.com --to user@example.com --subject "Re: Help" --body-file ./reply.txt
atoll subtask create ATOLL-42 --title "Verify recurrence"
atoll activity issue ATOLL-42

`atoll activity issue` reads the canonical task Activity timeline. It accepts
`--limit` (`1..100`) and `--offset` (default `0`) and excludes notification,
webhook, realtime, and delivery records; history from before the atomic
Activity contract can be partial.

# Read-only API fallback for uncommon inspection gaps
atoll api get /api/orgs/$ATOLL_ORG_ID/labels --json

# Dependencies
atoll dependency bulk-add --file ./dependencies.json --continue-on-error

Dependency reads include a target issue `identifier` and `projectSlug` when the target belongs to a project. Inaccessible targets remain `issue: null`; projectless targets have both fields set to `null`.
Dependencies persist a release point in the blocking project's ordered board columns. Add `releaseColumnId` when creating an edge, or omit it to default to that project's `done` column. Use the dependency API PATCH route to change the release point; reads include `releaseColumnId`, `releaseColumn`, and `satisfied`.
Archiving a blocker preserves the dependency edge and configured release column while satisfying the dependency. Restoring it re-evaluates the same release point and can block the dependent again. Configurable release-point and cancelled-blocker behavior are unchanged.
The blocking issue must belong to a project because its release point is a board
column there; a projectless issue may be the blocked target.
The dependency-release migration backfills existing dependencies to the
blocking project's `done` column. During a rolling deployment, compatibility
reads may omit release fields from older rows; treat missing release metadata as
the legacy open-blocker behavior until the migration is applied.
Dependency reads preserve `release_column_id` as a compatibility alias where
snake_case consumers need it; POST and PATCH accept either `releaseColumnId` or
`release_column_id`. When deleting a board column, migrate issue
statuses and dependency release references with separate explicit targets.

# Graph plans
atoll plan validate --file ./plan.json
atoll plan apply --file ./plan.json --dry-run

# Safe removal
atoll issue archive ATOLL-42
atoll issue unarchive ATOLL-42
atoll issue delete ATOLL-42 --dry-run
atoll issue delete ATOLL-42 --force

# Report friction to Atoll maintainers
atoll feedback "The status error should list custom board statuses"

# Projects & milestones
atoll project list
atoll board-column create --project <project> --key review --label "In Review" --description "Ready for review"
atoll project delete <project-id> --confirm DELETE
atoll milestone list --project <project-id>
atoll milestone upsert --project <project-id> --name "v1.0" --date 2026-06-01

# Goals, KPIs, and initiatives
atoll goal create --title "Reach 100 paying customers by Q2" --target-date 2026-06-30
atoll kpi create --name paying_customers --goal "Reach 100 paying customers by Q2" --unit count --target 100 --current 34
atoll kpi create --name mvp_tasks_done --goal "Launch MVP" --internal-task-completion
atoll initiative create --title "Content pipeline" --goal "Reach 100 paying customers by Q2" --status active
atoll initiative kpi link "Content pipeline" paying_customers --impact "+30 customers/mo"
atoll initiative target create "Content pipeline" --title "Publish 10 comparison posts" --mode progress --target 10 --current 0 --unit count --unit-label posts
atoll initiative target create "Retailer coverage" --title "Get 5 retailers live by July 5" --mode gate --target 5 --current 0 --unit count --unit-label retailers --target-date 2026-07-05 --due-soon-days 7
atoll initiative target issue link "Retailer coverage" "Get 5 retailers live by July 5" ATOLL-42
atoll kpi snapshot add paying_customers --value 42 --initiative "Content pipeline" --issue ATOLL-42 --note "End-of-week Stripe check"
atoll kpi snapshot list paying_customers --include-attribution --json
atoll heartbeat --explain-kpi paying_customers --json

# Audit the strategy chain for gaps (orphaned initiatives, goals with no KPI, etc.)
atoll strategy audit
atoll strategy audit --severity critical --json
```

Prefer the CLI for routine task operations, heartbeat checks, comments, feedback, and strategy setup. Use direct API calls when the CLI does not expose the needed endpoint yet.

CLI JSON conventions:

- Use `--json` for machine-readable output.
- List commands return `{ resource, items, total, limit, offset, nextOffset, truncated, hint }`.
- Project-scoped `atoll issue list --json` includes `project_context`; `atoll issue get/view --json` includes `status_column` plus `project_context` when available.
- For initiative execution context via API, `GET /api/orgs/{id}/initiatives/{initiativeId}/issues?details=1` returns accessible task details from linked projects, direct issue links, and linked milestones.
- Diagnostics and errors go to stderr.
- Machine-readable JSON preserves API strings exactly; human terminal output removes ANSI/VT, control, and bidirectional formatting characters from API-supplied strings.
- Interactive CLI update notices also go to stderr and are suppressed for JSON/non-TTY/CI/completion flows.
- `atoll agent-context` returns a versioned command/flag manifest, available profile context, and structured `cli.update_available` metadata.
- Weekly issue recurrence accepts unique selected weekdays with `--recurrence weekly --recurrence-days mon,wed,fri --recurrence-mode schedule --recurrence-time 09:00 --recurrence-timezone Asia/Singapore`. Read JSON exposes normalized `recurrence_days` and `recurrence_schedule`; unrelated updates preserve the schedule. Scheduled recurrence intervals are limited to `10000`. Use `--recurrence-mode schedule` with `--recurrence-time HH:MM` and `--recurrence-timezone IANA/Zone` to create the next task from the maintenance sweep while the current task remains open; `completion` remains the default and can retain larger positive intervals.
- `atoll heartbeat --json` includes the same structured `cli` update metadata for agents, plus `attention_items`, `attention_summary`, and `recommended_action` when Atoll can propose one concrete strategy-backed next action. `atoll heartbeat --signals-only --json` preserves filtered `signals`, `attention_items`, `attention_summary`, and `recommended_action` for short polling. Handle direct attention items first, then call each handled item's `ack_endpoint`. Follow `recommended_action.usage_guidance`: prefer `suggested_write.operation` when it still matches the board, preserve KPI/initiative/initiative_target/why-now/expected-impact/first-step/success-criteria evidence, and avoid copying deferred busywork into issue or comment payloads. If a `start_work` recommendation uses `issue.update` with a body, update the issue status and preserve that body as an issue comment; `PATCH /issues/{issueId}` accepts `comment_body` for this same-request progress note.
- Authorized humans can configure an agent's included heartbeat sections and generated-signal focus in the Atoll **Heartbeats** UI. The saved policy is applied by the API before CLI or MCP request-level narrowing; it never changes project access, and existing heartbeat commands require no new arguments.
- GitHub `workflow_run` signals are accepted only when HMAC-signed and completed, then reread and matched exactly by repository, PR, workflow path, run attempt, and head SHA. Workflow verification is disabled by default and observe-only until an owner/admin enables it in **Settings > Integrations > GitHub**. `attention` mode can add one bounded `verification.completed` attention item through authorized REST or CLI heartbeat for exactly one eligible current agent assignee or, when there is no unambiguous assignee, an eligible configured delivery agent. The public MCP heartbeat excludes this private event type. Unresolved recipients and cancelled, obsolete, superseded, mismatched, or unreadable runs create no attention. Owners and admins can configure 1–10 workflow paths of at most 255 characters each; the bounded evidence list defaults to 25 items and accepts a maximum `limit` of 100. Signed pull-request writes and reconciliation bind PR links to the stable GitHub repository ID, so repository renames keep existing workflow evidence linked. Do not expect raw payloads, secrets, logs, or thread IDs in evidence; owner/admin reconciliation retries pending evidence after current GitHub and PR-link readback.
- Release-added required GitHub hook events mark existing reconciled and already-pending connections pending. The bounded 15-minute service sweep verifies immutable repository identity and upgrades hooks automatically; transient failures remain pending for retry, and owners/admins can reconcile manually.
- Issue delivery context is read with `atoll issue delivery-context <identifier>`; `--json` preserves `{ deliveryContext }`, while TTY output includes the full head SHA, review, actual required checks, configured verification, freshness, blocker, and partial state. The endpoint selects an open PR first, then the latest updated link, then the highest PR number. Required checks union active rulesets and classic branch protection for the base branch and use exact-head check-run/status evidence. `pending` review/workflow state with null provenance means no current-head observation and does not by itself set `partial`. Required-check collection is disabled by default; with the reader disabled, state `disabled` and aggregate `none` do not set `partial`. The server-only `ATOLL_GITHUB_REQUIRED_CHECKS_READ_ENABLED=1` flag enables read-only provider GETs; when enabled, partial or unavailable collection or aggregate `unknown` sets `partial`. This result does not authorize merge, deployment, production testing, or human acceptance. Configured workflows report `required: false`.
- Aggregate review state keeps each reviewer's latest exact-head opinion, ignores comments, and removes dismissed opinions. Change requests win. `approved` means at least one effective approval and no effective change request; it does not prove required-review counts or branch protection.
- `atoll plan validate/apply` consumes `schemaVersion: "atoll.plan.v1"` files with `milestones`, `issues`, `dependencies`, `initiativeLinks`, and `milestoneLinks`; local `key` values can be referenced by `milestoneKey`, `issueKey`, `dependsOn`, `blockedBy`, or `blocks`.

### Bulk create tasks from a plan

`POST /api/orgs/{id}/issues/bulk` with `{ "issues": [{...}, ...] }` (max 50).

## Automation rules

Use `atoll automation list`, `get <rule-uuid>`, `create --file rule.json`,
`update <rule-uuid> --file patch.json`, `test <rule-uuid> [--file preview.json]`,
`runs <rule-uuid> --limit 20`, `enable`, `disable`, and `delete --force`.
Use `delete <rule-uuid> --dry-run` to preview deletion. Use `--json`
for machine-readable results and `--file -` for standard input. Create defaults
to disabled when `enabled` is omitted, but the JSON must include an explicit
`project_id` UUID or `null` for Organization-wide scope; update preserves omitted
fields.
List uses the selected organization and applies a project filter only with
explicit `--project`; it does not inherit the default project.

Rule files use the canonical Automation Rule Fields contract. CI rules require
`project_id: null`, only `create_issue` or `send_webhook` actions, and event conditions. Use
conclusion `failure` and `has_linked_issue: false` for unlinked CI failures.
The action chooses its target project/status and accepts approved
`{{repository}}`, `{{workflow}}`, `{{conclusion}}`, `{{run_url}}` substitutions.
CI `test` sends `{}` by default, uses marked fixed examples, rejects overrides,
and executes no actions. Inspect the preview before explicitly enabling.
Rule writes, tests, and run history require owner/admin access; CLI does not bypass it.
`runs` preserves created issue IDs and interrupted-action evidence. For an invalid
rule, use separate `disable`, `update` while disabled, `test`, and `enable`
operations. Human `get` output includes invalid state and validation paths;
`--json` preserves the API response.
