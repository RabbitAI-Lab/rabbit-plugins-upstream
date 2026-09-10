---
name: atoll
description: Use Atoll for project, issue, goal, KPI, initiative, milestone, comment, dependency, runner, and workflow operations. Activate for Atoll planning, execution, project-management, local-runner, or integration requests.
---

# Atoll

Base URL: `https://atollhq.com`

Use the available Atoll connection for live data and controlled actions. Prefer
the Atoll CLI for routine operations when it is installed. MCP tool schemas,
CLI help, and the linked references are authoritative for parameters and
validation.

## Route to the relevant reference

Read only the references required for the current task:

- Authentication, saved profiles, organization or project selection, and
  environment conflicts: [authentication-and-profiles.md](references/authentication-and-profiles.md)
- Routine CLI commands for issues, comments, goals, KPIs, initiatives,
  dependencies, artifacts, and other resources:
  [cli-operations.md](references/cli-operations.md)
- Installing, diagnosing, configuring, or operating the headless local runner,
  repository bindings, loopback UI, leases, or recovery:
  [local-runner.md](references/local-runner.md)
- Strategy, KPI pace, initiatives, heartbeat signals, autonomous prioritization,
  and common strategy workflows:
  [strategy-and-heartbeat.md](references/strategy-and-heartbeat.md)
- Agent executions, evidence, human-attention requests, resolution, and
  version-fenced lifecycle transitions:
  [execution-and-attention.md](references/execution-and-attention.md)
- Remote MCP setup, AI-assisted setup, KPI HTTP sync, or advanced REST access:
  [integrations-and-api.md](references/integrations-and-api.md)
- Cross-resource authorization, privacy, automation, attachment, feedback, and
  other platform-specific rules: [platform-rules.md](references/platform-rules.md)
- Exact endpoint inventory: [api-endpoints.md](references/api-endpoints.md)
- Request and response fields, enums, and validation:
  [api-fields.md](references/api-fields.md)

Do not load every reference by default. Start with this entrypoint and load a
topic reference only when the requested operation needs it.

## Workflow contract

### Select the actor and project

For actor-dependent MCP calls:

1. Reuse the `profile_ref` already established in the current conversation.
2. If none is established, call `atoll_list_agent_profiles` before an
   actor-dependent read or write.
3. Select a profile directly when the user names it. Otherwise select a unique
   profile only when the organization or project clearly identifies it.
4. Ask when multiple authorized profiles remain plausible.
5. Include the chosen `profile_ref` in every later actor-dependent call.

A `profile_ref` is an opaque selector, not a credential. Do not persist it,
expose it as a secret, silently switch actors, or infer identity from a mutable
server-side active profile. If the selector is invalid, rediscover profiles. If
no profile is authorized, explain that the user must authorize one.

For CLI work, use the named profile required by the repository or user. Resolve
the organization and project from live accessible data. Do not carry mutable
IDs or board mappings across conversations without checking them.

### Read before write, then verify

For state-changing work:

`resolve actor -> resolve organization/project -> read the target -> inspect
linked context when relevant -> make the smallest required write -> read back
the changed resource -> verify the requested final state`

Before creating work, search for a matching issue, milestone, goal, KPI, or
initiative. Update the existing resource when it represents the request. Never
invent an ID, success response, stored value, or visible state.

Readback is mandatory for requested mutations. Report both the stored value and
the user-visible value when both exist, and state anything that could not be
verified.

Use the narrowest available typed command or tool. Use raw REST only when the
typed surface does not cover the operation. Do not duplicate tool schemas from
memory.

### Preserve the Atoll model

- Goals describe directional business outcomes and deadlines.
- KPIs measure business outcomes and pace.
- Initiatives are bets expected to move one or more KPIs.
- Initiative targets measure commitments or launch gates.
- Milestones are delivery checkpoints.
- Issues are executable work.

Preserve links between these layers. Do not turn them into interchangeable
standalone tasks.

### Resolve workflow from live data

Board columns belong to projects. Use `atoll_get_project_workflow`, then
`atoll_move_issue` (or the corresponding typed CLI operation), instead of
guessing. Match the visible destination label and verify both the stored status
key and visible label after the move. Never treat a key such as
`ready_to_build` as universal.

### Plan implementation-ready work

For implementation planning, inspect the relevant project and existing work
first. The result must let another coding agent start without repeating the
product reasoning. Include only the sections that matter:

- Outcome
- Context and current behavior
- Product behavior
- Relevant repository or API surfaces
- Edge cases and compatibility
- Tests
- Acceptance criteria

Keep product decisions, security boundaries, and unresolved questions
explicit. Do not add project-specific workflow keys as universal instructions.

## Safety boundaries

- Credentials belong in approved local configuration or environment variables.
  Never print, store in Atoll content, or include them in commands shown with
  real values.
- Project and organization authorization remain authoritative. Do not retry as
  another identity to bypass a concealed or denied resource.
- Preserve idempotency keys and expected versions for lifecycle writes. After a
  timeout or ambiguous failure, read state before retrying.
- Keep attention requests, comments, evidence, and feedback free of credentials,
  private paths, prompts, logs, or raw sensitive payloads.
- Publication, deployment, production mutation, destructive deletion, and
  external communication require the authority applicable to the current task.
