# Functions — Hosting Plans, Triggers and Why It Stopped Firing

A function app is code plus a hosting plan plus a storage account. Most production problems are the plan (wrong scaling and timeout semantics) or the storage account (an invisible hard dependency).

**Contents:** [Choosing a Hosting Plan](#choosing-a-hosting-plan) · [The Storage Account Dependency](#the-storage-account-dependency) · [Timeouts](#timeouts) · [Triggers and Scaling](#triggers-and-scaling) · [Cold Start](#cold-start) · [Durable Functions](#durable-functions) · [Poison Messages and Retries](#poison-messages-and-retries) · [Networking and Identity](#networking-and-identity) · [When Nothing Fires](#when-nothing-fires)

## Choosing a Hosting Plan

| Plan | Scale to zero | VNet | Timeout | Cold start | Use when |
|---|---|---|---|---|---|
| Consumption | Yes | No | 5 min default, 10 max | Yes | Spiky, cheap, no private networking |
| Flex Consumption | Yes | Yes | Longer, configurable | Reduced, with always-ready instances | The modern default when available in the region |
| Premium | No (min instances) | Yes | 30 min default, longer configurable | Eliminated by pre-warmed instances | Steady traffic, private endpoints, latency SLOs |
| Dedicated (App Service plan) | No | Yes | Effectively unbounded on Always On | None | Reusing an existing plan's spare capacity |
| Container Apps hosting | Yes | Yes | Container semantics | Depends on min replicas | The team already runs Container Apps |

Break-even: Consumption stops being cheap when the app is warm most of the day. If executions run near-continuously, a Premium instance or a shared dedicated plan is usually less than the per-execution bill — and removes the cold start argument entirely.

`compliance_regime` other than `none` usually forces private networking, which rules out plain Consumption.

## The Storage Account Dependency

Every function app is bound to a storage account that holds far more than deployment artifacts: **timer schedules, blob-trigger receipts, singleton leases, the host's key material, and Durable Functions state.**

Consequences that surprise people:

- Deleting, firewalling or key-rotating that storage account **stops the app**, usually with no application error — timers stop firing and blob triggers go silent.
- Sharing one storage account between several function apps causes lease and receipt collisions. One account per app, or at minimum distinct prefixes with deliberate configuration.
- Locking the storage account behind a private endpoint requires the app to have VNet integration and correct DNS, or the host cannot start (`networking.md`).
- Deployment-from-package points at a blob; if that blob or its SAS expires, the app serves the old code or none.
- The account name belongs in `## Current Infrastructure`, because the connection between "the function is dead" and "someone hardened a storage account" is otherwise unfindable.

## Timeouts

Three different limits, frequently confused:

1. **`functionTimeout`** — how long one execution may run. Consumption caps it at 10 minutes; Premium and Dedicated allow much longer.
2. **The HTTP front-end limit** — an HTTP-triggered function is still behind the same ~230-second platform wall as App Service. A 10-minute `functionTimeout` does not help an HTTP caller (`appservice.md`).
3. **The trigger's own visibility or lease window** — a queue message becomes visible again if processing exceeds its lease, producing duplicate work that looks like a bug in the function.

Design rule: HTTP triggers accept and enqueue; queue or Durable triggers do the work. Anything that might take minutes must be asynchronous from the first version, because retrofitting the pattern means changing the client contract.

## Triggers and Scaling

- **HTTP** — scales on request pressure; concurrency per instance is configurable and is the knob that matters for downstream connection counts.
- **Queue / Service Bus** — scales on queue depth; batch size and concurrency multiply into the real parallelism hitting your database.
- **Event Hubs** — scales by partition: **parallelism is capped by partition count**, so a single-partition hub processes serially no matter how many instances exist. Partition count is chosen at creation.
- **Blob trigger** — polling-based and can lag by minutes on Consumption for accounts with many blobs; Event Grid-based blob triggers are the low-latency answer.
- **Timer** — runs on one instance with a lease. Schedules are UTC unless configured otherwise, which is the cause of most "it ran an hour early" reports. A missed timer while the app was down does not automatically catch up unless the trigger is configured to.
- **Event Grid** — push, with its own retry and dead-letter policy independent of the function's.

Every trigger's scale-out multiplies pressure on whatever it writes to. State the downstream ceiling when recommending concurrency (SKILL.md Rule 8).

## Cold Start

- Causes, in order of impact: large dependency graphs, non-precompiled code, VNet integration on plans that must warm a network path, and infrequent invocation.
- Mitigations: Flex Consumption always-ready instances or Premium pre-warmed instances; trimming dependencies; precompiled or isolated-worker builds; avoiding heavy static initialization.
- Warm-up pings are a workaround, not a fix, and on Consumption they cost executions all day to save latency on a few.
- Measure before optimizing: the platform reports cold-start latency separately in Application Insights.

## Durable Functions

For orchestration that outlives one execution: fan-out/fan-in, human approval, long chains, sagas.

- Orchestrator code must be **deterministic and replayed-safe**: no `DateTime.Now`, no random, no direct I/O, no non-durable timers. The framework replays history from the beginning on every await, so nondeterminism produces silent corruption rather than an error.
- Activity functions do the I/O; entities hold state.
- History lives in the function app's storage account and grows without bound unless purged — a real cost line on busy orchestrations.
- Eternal orchestrations must call `ContinueAsNew` or the history grows until replays time out.

## Poison Messages and Retries

- Queue triggers retry a message a small fixed number of times (five by default) before moving it to a `<queue>-poison` queue. Nobody watches poison queues by default — an alert on their length is the difference between "it silently dropped orders" and "we knew in five minutes" (`monitoring.md`).
- Service Bus has its own dead-letter queue with its own max-delivery count, independent of the function's retry policy. Configure one of them deliberately; two retry layers multiply.
- Retry policies in the function host apply to the execution, not to the message's visibility, so a long retry can overlap a re-delivery.
- Idempotency is not optional: at-least-once delivery plus retries means every handler must tolerate seeing the same message twice.

## Networking and Identity

- Plain Consumption cannot join a VNet. If the function must reach a private endpoint or a database with public access disabled, the plan choice is already made.
- Managed identity for every binding that supports it — Storage, Service Bus, Event Hubs, Cosmos DB and SQL all accept identity-based connections, which removes the connection string entirely (`identity.md`).
- Function keys are credentials: they authenticate HTTP callers and they live in the storage account. Never write one into `~/Clawic/data/`; if a runbook needs to mention one, use the pointer form (`memory-template.md`).
- For public HTTP functions, put Front Door or API Management in front rather than relying on function keys as an authorization model.

## When Nothing Fires

Work down this list; the cause is almost always in the first three.

1. **Storage account reachable?** Firewall, private endpoint DNS, rotated keys, deleted container. This is the top cause of a silently dead app.
2. **Is the function disabled?** An app setting, a portal toggle, or a deployment that dropped the function.
3. **Did the deployment actually land?** Package deployment pointing at a stale or expired artifact serves old code, or none.
4. **Scaling stopped?** Consumption apps stop scaling when the plan hits a limit or when the scale controller cannot read the trigger source.
5. **Timer semantics?** UTC, and no catch-up for missed runs unless configured.
6. **Event Hubs parallelism?** Partition count, and a checkpoint that stalled on a poison event.
7. **Host errors?** The `Function Execution Logs` and the host's own startup trace in Application Insights show binding failures that never reach your code.

**When the hosting plan, the timeout or the trigger topology is decided, record it** in `## Current Infrastructure` in `~/Clawic/data/azure/memory.md` — plan, timeout, storage account, and the first ceiling the design will hit. If the decision needed comparison work, it is an architecture decision and belongs in `artifacts/` with its `## Boxes` line (`memory-template.md`).
