# Integrations — Reachable, Authorized, Not Expiring, Not Throttled

Scope: every external service the setup depends on — APIs, tool servers, webhooks, remote hosts, notification channels.

**Before this pass**, read `## System Baseline` in `~/Clawic/data/analysis/memory.md` (or the file its `## Boxes` line names) for the integration inventory, `## Credential Inventory` for each one's token kind and expiry, and the shared `~/Clawic/data/servers/servers.md` for remote hosts already inventoried, so a known machine is not re-added under a second name. An integration that answers today but whose token expires in nine days is a WARNING today; that is the whole point of keeping the calendar.

**Contents:** [Reachability Ladder](#reachability-ladder) · [Status Code Decode](#status-code-decode) · [Scope Failures That Look Like Missing Objects](#scope-failures-that-look-like-missing-objects) · [Expiry Calendar](#expiry-calendar) · [Rate Limits](#rate-limits) · [Clock Skew](#clock-skew) · [Webhooks](#webhooks) · [Tool Servers](#tool-servers) · [Remote Hosts](#remote-hosts) · [Timeouts](#timeouts) · [Cost Of The Integration Itself](#cost-of-the-integration-itself) · [Sweep](#sweep) · [Write It Down](#write-it-down)

## Reachability Ladder

Four rungs, in order, stopping at the first failure — the rung that fails names the layer, which is the entire diagnostic.

1. **Name resolution.** Fails → DNS, a VPN-only hostname, or a service that was renamed.
2. **TCP and TLS.** Connects but the handshake fails → certificate expired, a corporate interception proxy, or a protocol version floor. Certificate expiry is worth reading while you are there: it is a dated failure you can schedule around.
3. **Unauthenticated liveness** (a status or health path, or any endpoint that answers without a credential). Fails → the service is down or blocking, and nothing about your credential is implicated.
4. **One authenticated call**, the cheapest read the API offers — an identity or "who am I" endpoint where one exists.

Rung 4 runs **once per integration per audit run**, never once per check. An audit that authenticates repeatedly against a rate-limited provider becomes the reason the next hour of real work fails.

## Status Code Decode

| Response | Means | First move |
|---|---|---|
| 401 | The credential was rejected: expired, revoked, rotated elsewhere, or malformed | Check expiry in the inventory before assuming compromise; a rotation somebody else did looks identical to a theft |
| 403 | Authenticated, not permitted | Compare the token's scopes to the call — a scope problem, not an identity problem |
| 404 on something that exists | Usually scope; several APIs return 404 rather than 403 so they do not confirm that the object exists | Below |
| 429 | Rate limited | Read `Retry-After` and the remaining-quota headers; back off with jitter, do not retry immediately |
| 5xx, intermittent | Provider side | Retry with backoff; three consecutive audit runs with the same 5xx makes it a provider finding worth a status-page link, not a local one |
| Connection reset mid-response | Interception proxy, MTU, or an idle timeout on a long request | Retry with a smaller payload to separate size from network |
| Hang with no response | Missing client timeout — the whole run stalls behind it | Below |

## Scope Failures That Look Like Missing Objects

A valid token plus a 404 on a resource the user can see in the browser is almost always a missing scope: the API refuses to confirm the resource exists to a caller not allowed to see it. Diagnose by calling the identity endpoint and reading the token's granted scopes, then compare against the operation. Never "fix" it by widening to a full-access token — that trades a broken feature for a `permissions.md` finding.

## Expiry Calendar

Every credential with a lifetime has a date, and outages on that date are always preventable. When an integration is inventoried, record kind, pointer, owner, issue date, expiry, and who can reissue it in `## Credential Inventory` in `memory.md`.

- Warn at **14 days** for anything the user can reissue alone.
- Warn at **30 days** when reissue needs another person, a vendor ticket, or an approval.
- Credentials with no expiry get an age check instead: older than `secret_rotation_days` becomes a WARNING whose action is "set a rotation date" (`secrets.md`).
- Certificates get the same treatment as tokens; a TLS certificate expiring in 12 days is the same finding as a token expiring in 12 days.

## Rate Limits

Read the limit rather than discovering it: most APIs return remaining-quota and reset headers on every response. Three findings live here.

- **Chronic proximity** — sustained use above ~80% of the window's quota. The fix is architectural (poll less, batch, use webhooks or a bulk endpoint), not a bigger retry.
- **Retry storms** — retries with no backoff or no jitter, which convert one 429 into a sustained block. Formula, same as everywhere in this skill: `sleep = min(cap, base × 2^attempt) × (0.5 + random()/2)`, attempts capped at 5.
- **Shared quota** — several jobs and one interactive session against the same provider all draw from one bucket. This is where the start-minute clustering in `scheduled.md` turns into 429s that look random.

## Clock Skew

Signed request schemes reject a request whose timestamp is too far from server time; **5 minutes** is the common tolerance. A machine that sleeps, a container without time sync, or a VM restored from a snapshot drifts past it, and every signed call fails with an authentication error that points at the credential. Check host time against a time source before rotating anything: rotating a credential to fix a clock produces a second outage on top of the first.

## Webhooks

Inbound integrations fail differently from outbound ones, and nothing tells you.

| Check | Failure it catches |
|---|---|
| The registration still exists at the provider | Deleted with an app, an environment, or a token rotation |
| The endpoint answers a signed test delivery | Endpoint moved, TLS expired, tunnel down |
| The signing secret matches on both sides | Every delivery rejected, provider retries then disables the hook |
| Delivery history shows recent successes | Silent disable — most providers stop after N consecutive failures |
| The endpoint responds fast enough | Providers time out in seconds; slow handlers must acknowledge first and work after |
| Replay and duplicate handling | Retries deliver the same event more than once; a non-idempotent handler doubles the effect |

## Tool Servers

For each connected tool or MCP-style server: is the process alive, does the handshake complete, how long does it take to start, and — the check nobody runs — **has its tool list changed**. A server that used to expose twelve tools and now exposes three has partially failed, usually because it cannot reach its own backend, and the agent silently loses capability instead of getting an error.

Compare the current tool list against the one in the baseline; a shrink is a WARNING, a schema change is INFO with the tool named. Where the server is third-party code, its trustworthiness is a `skill-audit` question and its grants are a `permissions.md` question.

## Remote Hosts

For hosts the setup depends on: reachability, authentication method (a key reference, never a key), disk headroom, and whether the services it hosts are answering. Any host discovered or verified here belongs in the shared inventory `~/Clawic/data/servers/servers.md`, not in a private list — the format, identity rule, and scale cut are in `memory-template.md`.

## Timeouts

An integration with no client timeout is not an integration, it is a way to hang the whole run. Defaults that work: 3s to connect, 10s total for a health check, and a bounded total for real calls. Note that some common clients — `curl` among them — have **no** default total timeout, so absence of a flag means infinite. Every health check in this audit sets its own explicit limit; a check that can hang is a check that will one day be the reason the audit never finished.

## Cost Of The Integration Itself

Paid services found here go in the shared `~/Clawic/data/finances/subscriptions.md` with amount and currency (`memory-template.md`). Two findings live in that file rather than in this one: a subscription nobody has called in 90 days, and a plan whose usage is consistently under 10% of its tier. Both are INFO, both pay for themselves.

## Sweep

| Check | Passing looks like |
|---|---|
| Every integration inventoried | Name, purpose, credential pointer, owner, expiry |
| Reachability ladder run once per integration | Failures attributed to a rung |
| No credential inside `expiry − warning window` | Or a reissue is already scheduled in `## Due` |
| Rate-limit headroom above 20% | Plus bounded, jittered retries |
| Host clock within tolerance | Verified before any credential is blamed |
| Webhooks registered, answering, not disabled | Recent successful deliveries visible |
| Tool servers' tool lists match the baseline | No silent shrink |
| Every client call has an explicit timeout | Nothing can hang the run |
| Paid services recorded with amount and currency | In the shared finances box |

## Write It Down

Same turn as the pass:

- The integration inventory, tool-server tool lists, and measured latencies → `## System Baseline` in `memory.md`.
- Credential kind, pointer, owner, issue date and expiry → `## Credential Inventory` (splits to `credentials.md`).
- Failures, expiring credentials, throttling posture → `## Open Findings`, one per integration.
- Reissue and rotation dates, and any recurring connectivity check → `## Due` rows.
- Hosts → the shared `~/Clawic/data/servers/servers.md`; paid services → the shared `~/Clawic/data/finances/subscriptions.md`; a paired phone or tablet → `~/Clawic/data/devices/devices.md`.
- A reconnection or re-authorization procedure that worked → `~/Clawic/data/analysis/artifacts/reconnect-<service>.md`, plus its `## Boxes` line.
