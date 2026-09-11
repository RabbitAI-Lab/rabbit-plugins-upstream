# Local runner

Read this reference before installing, diagnosing, configuring, or operating `atoll-runner`, its repository bindings, loopback UI, leases, or recovery behavior.

### Local runner presence

Authenticated agents can register and refresh one local runner installation with
`PUT /api/orgs/{id}/runners/self`, read it with `GET`, and disconnect it with
`DELETE`. The organization and agent member are derived from authentication, not
the request body. The strict body contains `instanceId`, optional `hostId`, `platform`, `arch`,
`capabilities`, `clientVersion`. Intake state is server-owned and is not accepted
from self refresh; human pause/resume uses the hosted fleet control endpoint.
Platform, architecture,
and capabilities use closed documented values; the server derives the display name.
Recent competing installations return `409`; an installation silent for 10
minutes can be replaced. Refresh is limited to 60 requests per agent per
minute. Responses expose only bounded operational metadata and computed
`presence_state` (`connected`, `stale`, or `offline`), never keys, prompts, or
local filesystem paths.

### Local runner leases

`POST /api/orgs/{id}/runner-leases/claim` atomically claims one assigned,
accessible, dependency-satisfied issue for the authenticated agent's current
runner. The body accepts `issueId` and `idempotencyKey`; `attention_resume`
first claims require an unread `attentionItemId`, `runnerHostId` (maximum 255 characters), `preservedThreadId`,
and `actionKind`. The response returns an ephemeral token; only its SHA-256
hash is stored. An untouched, unexpired, pre-intent `active` replay returns a
new token with `token_reissued: true` and invalidates the original token. During
overlapping recovery retries, the four newest prior recovery tokens remain valid for one minute or
until one is used, which promotes it. Other replays return `token: null`; terminal attention replays are acknowledgement-only, including after notification acknowledgement.
Only a proven pre-intent orphan can be replaced. Lease rows enforce the composite `(issue_id, org_id)` tenant fence. `PATCH /api/orgs/{id}/runner-leases/{leaseId}` accepts fenced
renew, progress, turn-milestone, terminal, reconciliation, and acknowledgement
transitions, including `model_completed`. Exact mutation retries are idempotent, and `uncertain_outcome`
blocks automatic replacement. Disconnected, stale, or replaced runners cannot
mutate or replay. A paused current runner may mutate or reconcile an already-held
lease but cannot acquire a new claim. These routes do not create candidates, schedules,
arbitrary commands, automation events, or action history.
Optional `progress` and `errorCode` metadata uses documented closed operational
codes; free-form values and sensitive runtime details are rejected.

## CLI runner

Builds that include the real headless runner provide a separate `atoll-runner`
binary. It uses an existing named Atoll profile. The server controls identity,
intake, assignment, repository authorization, and lease eligibility.

```bash
atoll-runner --profile agent-a doctor
atoll-runner --profile agent-a repositories list
atoll-runner --profile agent-a repositories bind repo-ref /path/to/checkout --issue issue-uuid
atoll-runner --profile agent-a repositories validate repo-ref
atoll-runner --profile agent-a status
atoll-runner --profile agent-a run --once --dry-run
atoll-runner --profile agent-a run
atoll-runner --profile agent-a run --ui
atoll-runner --profile agent-a ui
```

`run` uses the pinned Codex SDK and runtime `0.153.4`. Codex must be
authenticated. Each issue requires exactly one verified repository on its
project and a matching machine-local `repo_ref` binding. A local binding does
not grant server access. The runner checks the origin identity and exact base
commit, then creates an owned branch and worktree without changing the primary
checkout. Codex uses `workspace-write`, approval policy `never`, and disabled
sandbox network access. It does not use a global Codex executable as a fallback.

`--dry-run` performs a read-only dispatch check. Manage pause/resume in hosted
Atoll under Workspace Settings → Runners. Local intake is read-only; legacy
`pause` and `resume` commands return `RUNNER_INTAKE_HOSTED_ONLY`. Pausing new
intake does not cancel a held lease. The runner keeps local thread/worktree evidence
and never submits a replacement turn after an uncertain post-intent outcome.
An attention resume requires the exact retained thread and validated ownership;
there is no fallback to a new thread. Terminal branches and worktrees remain
available for inspection and are not deleted automatically.

Use `atoll-runner --profile agent-a repositories remove repo-ref` to remove an
unused local binding. This does not remove the server repository mapping or
local Git checkout.

`run --ui` enables the optional setup and diagnostics page at
`http://127.0.0.1:4735`; `--ui-port` selects another local port. `ui --port 4735`
opens diagnostics without starting work, including for a stopped runner or
malformed local config. Select the existing credential profile with `--profile`
at process start. Credentials never enter browser forms or responses.
The page lists server-authorized repositories, local bindings, Codex health,
local jobs/worktrees, uncertainty, and bounded redacted logs. Bindings use the
same runner config writer and never grant server authorization. Bind/remove
are blocked while a current job exists. Refresh, config validation, and Codex
preflight are non-destructive; there is no model retry or cleanup button.
A UI port or asset failure does not stop headless execution. Do not proxy this
loopback interface to another host. Service installation remains separate.
