# App Service — Plans, Slots, Certificates and the 230-Second Wall

App Service is the fastest way to run a web application on Azure and the easiest to misconfigure quietly: the plan is the unit of cost and scale, the app is the unit of deployment, and several of the platform's rules are invisible until traffic arrives.

**Contents:** [The Plan Is the Scale Unit](#the-plan-is-the-scale-unit) · [Tiers and What They Unlock](#tiers-and-what-they-unlock) · [The 230-Second Rule](#the-230-second-rule) · [Always On and Cold Apps](#always-on-and-cold-apps) · [Configuration and Key Vault References](#configuration-and-key-vault-references) · [Deployment Slots](#deployment-slots) · [Scaling](#scaling) · [Networking](#networking) · [Custom Domains and Certificates](#custom-domains-and-certificates) · [Diagnosing a Sick App](#diagnosing-a-sick-app)

## The Plan Is the Scale Unit

- You pay for the **plan**, not the apps. An empty plan costs the same as a busy one; ten small apps on one plan cost one plan.
- Every app on a plan shares its CPU, memory and instance count. Scaling out scales all of them. Co-locate apps with similar load shapes, and give a noisy neighbour its own plan.
- **Linux and Windows apps cannot share a plan**, and a plan cannot change OS. Deciding this wrong means recreating the plan and re-binding every domain.
- Plans are per region. A multi-region app is multiple plans plus a global front door.
- Delete empty plans. They are the most common invisible line item on an Azure bill (`costs.md`).

## Tiers and What They Unlock

| Tier | Gets you | Watch out |
|---|---|---|
| Free / Shared | Sandbox, CPU-minute quotas | No Always On, no custom domain TLS on Free, no SLA — never production |
| Basic (B) | Custom domains, TLS, manual scale, Always On | No slots, no autoscale |
| Standard (S) | Slots, autoscale, daily backups | Older hardware generation than Pv3 |
| Premium v3 (Pv3) | More memory per core, better price/performance than older Premium, zone redundancy, more slots | Requires a plan created in a region/zone combination that supports it |
| Isolated (ASE) | Dedicated environment inside your VNet, high scale limits | A large fixed monthly cost — justified only by compliance or scale |

Rule of thumb: dev on B1, production on Pv3 with at least two instances. Standard exists mostly for estates that predate Pv3 pricing.

## The 230-Second Rule

An HTTP request through App Service is terminated at roughly **230 seconds** by the front end. This is not the app's timeout, it is not configurable, and no framework setting changes it.

Consequences:

- Long jobs must be asynchronous: accept the request, return 202 with a status URL, process in a queue-triggered worker (`functions.md`).
- Report generation, large imports and slow third-party calls all eventually hit it — usually in production, on the biggest customer's data.
- WebSockets and streaming responses are governed by their own idle behaviour, not this limit; a long-lived socket is fine, a single long request is not.
- If a client sees exactly ~4 minutes and no server-side error, this is the cause. There is no other Azure timeout at that value.

## Always On and Cold Apps

- With Always On off, an idle app is unloaded after about 20 minutes and the next request pays a cold start — including any startup migration or cache warm-up.
- Always On is unavailable on Free and Shared, which is why those tiers feel broken for anything with real traffic.
- Timer-based work inside a web app does not run while the app is unloaded. That work belongs in a function or a WebJob with Always On, not in a background thread hoping for traffic.
- Startup time is a deployment property: heavy dependency graphs, JIT warm-up and migrations at boot all extend it, and slot swaps depend on it (below).

## Configuration and Key Vault References

- App settings are environment variables to the app, with platform-specific name mangling for nested keys. Connection strings are a separate section, injected with a prefix and visible to the platform.
- Changing a setting **restarts the app**. Batch changes rather than making them one at a time in production.
- **Key Vault references** put `@Microsoft.KeyVault(...)` in a setting and let the platform resolve the value at startup using the app's managed identity. Requirements: identity assigned, `Key Vault Secrets User` on the vault, and network access from the app to the vault. Failures surface as an empty setting and a status message in the app's configuration blade — not as an exception at deploy time.
- Never write a secret into an app setting when a Key Vault reference is available, and never write either into `~/Clawic/data/` — record the pointer `azure-kv:<vault>/<secret>` instead (`memory-template.md`).

## Deployment Slots

Slots are a full app on the same plan — same CPU, same memory. Their value is the swap.

- **Swap warms the target first**: the platform starts the new instance, waits for it to respond, then switches routing. This is the closest thing App Service has to a zero-downtime deploy.
- **Sticky settings**: app settings and connection strings marked as slot settings stay with the slot; everything else travels with the app during a swap. A connection string not marked sticky sends staging traffic to the production database at swap time — and, worse, the reverse afterwards.
- Warm-up can be driven by an explicit initialization path so the swap waits for something meaningful rather than for the first 200.
- **Rollback is swapping back**, which is why slots are the rollback artifact worth recording in `deploys/<year>.md`.
- Slots share the plan's resources: a staging slot running load tests degrades production. Use a separate plan for load testing.
- Traffic percentage routing to a slot gives canary releases without a second front end.

## Scaling

- **Scale up** = bigger plan (vertical, restarts). **Scale out** = more instances (horizontal, no restart).
- Autoscale rules: scale out on a metric with a short cooldown, scale in with a long one. Instances take minutes to become useful, so a tight scale-in rule produces flapping and worse latency than no autoscale at all.
- Scale on the metric that predicts saturation for the workload — CPU for compute-bound, HTTP queue length or response time for I/O-bound. CPU on an app that waits on a database never triggers.
- **The downstream dependency must survive the top of the range.** Ten instances opening pools against a small database is a scaling design that takes the database down (`databases.md`).
- Session affinity (ARR cookie) is on by default and pins users to instances, which undermines scale-out and slows failover. Turn it off unless the app genuinely holds session state in memory.

## Networking

- **Outbound**: VNet integration gives the app a route into a VNet (delegated subnet required, sized for the maximum instance count). Without it, the app egresses from a shared platform address range that changes.
- **Inbound**: access restrictions filter by IP or service tag; private endpoints make the app reachable only from the VNet. An app behind Front Door should restrict inbound to Front Door's service tag plus the header identifying your profile — otherwise the origin is public and the WAF is decorative (`networking.md`).
- The SCM/Kudu endpoint is a separate hostname with its own access restrictions. Locking the app while leaving SCM open leaves the deployment surface exposed.
- Apps needing to reach private endpoints must resolve the privatelink zone — which means VNet integration plus DNS, in that order.

## Custom Domains and Certificates

- Verify the domain (TXT), then bind it (CNAME, or an alias/A record for the apex), then add TLS. The order matters: binding before verification fails.
- **App Service managed certificates** are free and renew automatically, provided the validation records stay in place and the domain remains bound. They cover the common cases and not every case — confirm coverage before relying on one for a wildcard or an unusual configuration.
- Bring-your-own certificates live in Key Vault; the app's identity needs read access, and renewal is yours to schedule.
- Whatever the mechanism, **the expiry date goes in two places in the same turn**: the row in `~/Clawic/data/domains/domains.md` (domain, where DNS is hosted, what it points to, certificate and renewal date) and a line in `## Due` in `memory.md`. Automatic renewal still fails when someone deletes a validation record, and the failure surfaces as a browser warning on a Saturday (`memory-template.md`).

## Diagnosing a Sick App

| Symptom | First look |
|---|---|
| 502.5 or "application error" page | Startup failure: startup command, port binding (the app must listen on the port the platform provides), missing runtime version |
| Works locally, 500 on Azure | App settings absent, Key Vault reference unresolved, or a file path that only exists on a developer machine |
| Requests die at ~230s | The platform limit above |
| Intermittent 503 under load | Plan saturation or a downstream limit; check instance count against the metric that actually saturates |
| Slow first request after quiet periods | Always On off, or the app unloading between requests |
| Swap made production worse | A non-sticky setting travelled with the swap, or warm-up finished before the app was ready |
| Deployment succeeded, old code still served | Build ran in the wrong place (local vs remote build), or the wrong slot was deployed |
| Disk full or file writes failing | `/home` is the persistent share; other paths are ephemeral, and the share has a quota per plan tier |

Log stream for live output, App Service diagnostics for platform findings, and diagnostic settings shipping to Log Analytics for anything you want to query later (`monitoring.md`).
