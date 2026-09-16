# Strategy and heartbeat

Read this reference for goals, KPIs, initiatives, targets, heartbeat signals, autonomous prioritization, and strategy-linked execution workflows.

## The Heartbeat Loop

The primary pattern for autonomous agents. Prefer `atoll heartbeat --json` when the CLI is available; it wraps `GET /api/orgs/{id}/heartbeat` and returns the same computed briefing:

- **Goal status** with days remaining
- **KPI pace**: `pace_needed` vs `pace_actual`, trend (`accelerating`/`decelerating`/`flat`), staleness
- **Initiative progress**: total/completed/stalled/blocked issue counts, expected KPI impacts, and initiative targets
- **Assigned work** for this agent
- **Project context**: relevant board columns, including optional descriptions that explain stage criteria for agents. Project-scoped guests receive every explicitly accessible board while idle; personal agents retain relevant inherited-project context.
- **Signals** sorted by severity — the agent's prioritized to-do list
- **Attention items**: direct current-member notifications such as mentions, assignments, assignee comments, and creator-visible status changes, with an `ack_endpoint` to call after handling
- **Recommended action**: one deterministic strategy-backed next action when Atoll has enough evidence (`create_work`, `start_work`, `escalate_blocker`, `refresh_metric`, or `investigate`), including why-now, expected impact, first step, success criteria, quality warnings, and any suggested write. An investigation can use `suggested_write.operation: "none"` when heartbeat lacks enough detail for a safe write.

Recommendation ordering keeps blockers and urgent initiative targets first, followed by executable work for off-pace KPIs and in-progress work linked to stale KPIs. Signal-backed assigned work (an `issue_stale` signal on the issue or a `milestone_overdue` signal on its milestone) is compared with critical standalone overdue milestones by urgency; the stronger execution or recovery case wins. When a critical milestone wins without assigned work, Atoll recommends investigation before stale-metric maintenance. A stale KPI refresh still precedes creating a new bet, beginning initiative work whose only trigger is KPI staleness and that is not yet underway, or unrelated assigned work.

Heartbeat is org-scoped, but project-bound payload details are filtered by the caller's project access. Owners/admins receive full org context; members/guests only receive project-bound strategy, work health, assigned work, milestone signals, and board context for accessible projects. Project-scoped guests receive every explicitly accessible board while idle; personal agents retain relevant inherited-project context. Non-guest members can also see unprojected org-level strategy. Shared initiatives can appear with counts and signals based only on accessible work.

Signal types: `kpi_off_pace`, `kpi_stale`, `issue_stale`, `issue_blocked`, `milestone_overdue`, `initiative_stalled`, `initiative_target_due_soon`, `initiative_target_overdue`, `initiative_target_blocked`, `webhook_failing`. Severity: `info`, `warning`, `critical`.

Targets under initiatives are commitments, not business KPIs. KPIs measure business outcomes such as MRR, traffic, paying customers, or onboarding success. Use progress targets for initiative outputs such as "publish 10 comparison posts." Use gate targets for launch prerequisites such as "get 5 retailers live by July 5." Gate targets emit stateful due/blocked messages and should not be converted into fractional KPI pace such as "0.07 retailers/day."

Useful CLI forms:

```bash
atoll heartbeat
atoll heartbeat --signals-only
atoll heartbeat --severity critical
atoll heartbeat --json
```

**The agent loop:**
1. Call heartbeat
2. Handle direct `attention_items` that need a reply, task update, or blocker follow-up
3. Call each handled item's `ack_endpoint`
4. Read remaining signals (highest severity first)
5. Reason about highest-leverage action given direct attention, gate targets, KPI pace, and initiative state
6. Execute (unblock issues, update KPIs, create work, report progress)
7. Repeat

## Other Common Workflows

### Pick up and complete a task

```bash
atoll heartbeat --signals-only                        # orient first
atoll issue list --status todo --assignee self --json # find assigned work
atoll issue update ATOLL-42 --status in_progress --comment-body "Starting because the linked KPI is off pace." # start work with durable context
atoll comment add ATOLL-42 --body "Progress update…"  # report progress
atoll issue update ATOLL-42 --status done              # complete
```

### Set up the strategy chain

1. `POST /api/orgs/{id}/goals` -- create goal with `target_date`
2. `POST /api/orgs/{id}/kpis` -- attach KPI with `goal_id`, `target_value`, `target_direction`; for launch-style goals you can use `source_type: "formula"` with `source_config.formula: "goal_linked_issue_completion"` to calculate done directly linked and milestone-linked tasks over total linked tasks
3. `POST /api/orgs/{id}/kpis/{kpiId}/snapshots` -- record measurement (auto-updates `current_value`)
4. `POST /api/orgs/{id}/initiatives` -- create initiative linked to goal
5. `POST /api/orgs/{id}/initiatives/{id}/kpi-impacts` -- declare expected KPI impact
6. `POST /api/orgs/{id}/initiatives/{id}/targets` -- create progress or gate targets for initiative commitments
7. Link issues and milestones to the initiative and to specific targets when the work exists to satisfy that target

CLI equivalent:

```bash
atoll goal create --title "Reach 100 paying customers by Q2" --target-date 2026-06-30
atoll kpi create --name paying_customers --goal "Reach 100 paying customers by Q2" --unit count --target 100 --current 34
atoll initiative create --title "Content pipeline" --goal "Reach 100 paying customers by Q2" --status active
atoll initiative kpi link "Content pipeline" paying_customers --impact "+30 customers/mo"
atoll initiative target create "Content pipeline" --title "Publish 10 comparison posts" --mode progress --target 10 --current 0 --unit count --unit-label posts
atoll initiative target create "Retailer coverage" --title "Get 5 retailers live by July 5" --mode gate --target 5 --current 0 --unit count --unit-label retailers --target-date 2026-07-05 --due-soon-days 7
atoll kpi snapshot add paying_customers --value 42 --initiative "Content pipeline" --issue ATOLL-42 --note "End-of-week Stripe check"
atoll kpi snapshot list paying_customers --include-attribution --json
```

Project-scoped agent profiles apply their default project to `atoll initiative list` and `atoll initiative create`. Use `--project <id-or-slug>` to override that project, or `--org-wide` to intentionally suppress the default project. API callers can pass `project_id` or `projectId` on create, and `?project_id=...` on list; guest/project-scoped callers must use a project they can access, and create requires edit/admin project access. Projectless organization-wide initiative creation requires an organization owner/admin.

Project-linked initiative reads require access to at least one linked project.
The authoritative set includes explicit project links and projects inferred
from direct issue/milestone links. Updating an initiative or mutating its issue,
milestone, or target links requires edit/admin access to every linked project;
a requested issue or milestone project must already be linked when it is
project-bound. Eligible non-guests may link and unlink writable projectless
issues; projectless milestones are unsupported. KPI-impact reads omit
unreadable KPIs; linking or unlinking a KPI impact requires write access to the
initiative and read access to the same-org KPI, but not KPI Strategy write
access.
The initiative issue-link and initiative-target issue-link POST bodies accept
issue UUIDs, bare numbers, `#number`, `ATOLL-number`, `TSK-number`, or
unambiguous project-derived prefixes. The initiative-level milestone-link POST
body accepts a milestone UUID or exact name; target milestone links remain
UUID-addressed. These changed routes persist canonical UUIDs and return stable
`400` invalid, `404` concealed/out-of-scope, `409` ambiguous, or `500` resolver
errors.
Goal reads are available to organization members; creating, updating, and deleting goals requires owner/admin Strategy access.
Projectless initiative writes require an organization owner/admin.
Treat `404` as concealed absence or unreadable scope and `403` as insufficient
write access to a readable initiative.

KPIs are organization-wide Strategy resources. Owners/admins may read and
write; other non-guest organization members may read values, snapshots, and
redacted per-KPI sync metadata but cannot create, update, delete, or record
snapshots. Guest/project-scoped agents receive `403` for the collection and
concealed `404` responses for direct KPI, snapshot, and per-KPI sync
read/draft routes. Verify the active profile's organization-wide role before
running KPI commands.

Every KPI snapshot can be attributed to an initiative or issue, building a record of *what actually moved the numbers*. Keep KPI-to-initiative impact links separate from snapshot attribution: an initiative link means the initiative is expected to move the KPI, while snapshot attribution records the source of one measurement. Heartbeat reports one canonical status per KPI and can explain a KPI with `atoll heartbeat --explain-kpi <kpi> --json`.

### Audit and improve the strategy

Use the audit to review the strategy chain visible to the caller at a high level and fix structural problems — the common one being initiatives created without a goal.

```bash
atoll strategy audit            # human-readable, grouped by severity
atoll strategy audit --json     # findings[] for programmatic remediation
```

`GET /api/orgs/{id}/strategy/audit` returns `findings[]` (each with a `type`, `severity`, the relevant entity id, and a concrete `suggested_fix`) plus `summary` counts. It diagnoses; you remediate with the normal write endpoints. Typical loop:

The audit follows the caller's project access. Owners/admins receive
organization-wide execution evidence. Other non-guests receive project-bound
issues, milestones, target links, and target findings only for readable
projects. A restricted caller with no readable projects receives no issue or
target execution evidence. Guests cannot run the audit.

1. `atoll strategy audit --json` to get findings.
2. For each finding, apply its `suggested_fix`, e.g.:
   - `initiative_orphaned` → `atoll initiative update "<initiative>" --goal "<goal>"` (or `PATCH .../initiatives/{id} { goal_id }`)
   - `goal_missing_kpi` → `atoll kpi create --goal "<goal>" --name ... --target ...`
   - `kpi_missing_target` → `atoll kpi update <kpi> --target ... --direction increase`
   - `kpi_unrecorded` / `kpi_stale` → `atoll kpi snapshot add <kpi> --value ...`
   - `initiative_missing_impact` → `atoll initiative kpi link "<initiative>" <kpi> --impact "..."`
3. Re-run the audit to confirm the findings cleared.

This is the structural-health lens (is the strategy well-formed?), complementary to `heartbeat`, which is the operational lens (what should I do today?).
