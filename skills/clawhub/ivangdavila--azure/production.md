# Production — Reliability, Failover, and the Day It Breaks

Scope: taking something that works into something you are on call for. The gate at the bottom is the checklist; everything above it explains why each item is on it.

**Contents:** [Availability Is a Number You Choose and Pay For](#availability-is-a-number-you-choose-and-pay-for) · [Composite SLA Math](#composite-sla-math) · [Zones, Regions and Pairs](#zones-regions-and-pairs) · [Backup Is Not Replication](#backup-is-not-replication) · [The Restore Drill](#the-restore-drill) · [Failover Patterns](#failover-patterns) · [Deploy and Rollback](#deploy-and-rollback) · [Patching and Maintenance](#patching-and-maintenance) · [Capacity Headroom](#capacity-headroom) · [The Production Gate](#the-production-gate)

## Availability Is a Number You Choose and Pay For

Pick the target before designing, because each nine changes the architecture and the bill.

| Target | Downtime per month | What it takes |
|---|---|---|
| 99% | ~7.2 hours | Single instance, restore from backup, humans in the loop |
| 99.9% | ~43 minutes | Multiple instances in one region, health probes, automated restart, a tested restore |
| 99.95% | ~22 minutes | Zone-redundant compute and data, no single instance in the request path |
| 99.99% | ~4.3 minutes | Zone redundancy everywhere, automated failover, load shedding, deploys that cannot take the system down |
| Beyond | — | Multi-region active/active, and an organization built around it |

State the target out loud with its cost. Most teams asking for four nines want three and a restore they trust.

## Composite SLA Math

Dependent components multiply. An app on a 99.95% compute SLA in front of a 99.99% database has a composite of 99.94% — every service you add lowers it, and no individual component's marketing number describes the system.

- Multiply the SLAs of everything in the request path, including the front door, the gateway, the identity provider and the third-party API.
- Redundant components at the same layer *add* nines instead: two independent instances at 99.9% give roughly 99.9999% for that layer alone, which is why redundancy beats better components.
- Anything without an SLA — a free tier, a preview feature, a single-node cache — makes the composite undefined. Free-tier AKS control planes and Basic-tier Redis are the two that appear most often in "production" architectures.
- Verify the current published numbers before quoting them in writing; the ordering is stable, the digits are not.

## Zones, Regions and Pairs

- **Availability zones** are physically separate datacentres within a region. Zone-redundant services spread automatically; zonal resources are pinned to a zone you chose at creation and cannot move.
- Not every region has zones, and not every service is zone-redundant in every region that does. Check both before promising zone resilience.
- **Region pairs** matter for platform-managed geo-replication and for how Azure sequences updates across regions. Some services replicate only to the pair.
- Cross-zone traffic within a region is cheap and low-latency; cross-region is neither. A synchronous cross-region dependency turns a resilience feature into a latency problem.
- Data residency constrains region choice before availability does when `compliance_regime` is set.

## Backup Is Not Replication

| Mechanism | Recovers from | Does not recover from |
|---|---|---|
| Zone redundancy | A datacentre failing | Deletion, corruption, a bad deployment |
| Geo-replication | A region failing | Anything logical — it replicates the mistake |
| Point-in-time restore | Human error within the window | Anything older than retention |
| Azure Backup (vaulted) | Deletion of the source, including the resource | Nothing, if never restored |
| Immutable vault / WORM | Ransomware and malicious deletion | Poor retention choices |
| Soft delete | Accidental delete within days | Deleting the whole account or subscription |

Rules worth stating every time: **replication is not backup**; a backup you have not restored is a hypothesis; and backups in the same subscription, with the same credentials, protect against accidents but not against a compromise. Immutable vaults and separate access paths are what change that.

Retention comes from the agreed RPO, not from a default. Write the agreed RPO and RTO into the architecture decision artifact — otherwise every future argument restarts from opinion (`memory-template.md`).

## The Restore Drill

The deliverable is a measured number, not a document.

1. Pick the most valuable database or workload.
2. Restore it into a scratch resource group, from the same backup a real incident would use.
3. Time it end to end: not the restore operation, but the moment an application could serve traffic from it.
4. Write down everything that was missing: firewall rules, private endpoint and DNS, Key Vault access for the app identity, connection strings, licence keys, a parameter that only existed in the portal.
5. Fix the gaps in code, then delete the scratch environment.
6. **Record the measured RTO and the gap list in `deploys/<year>.md` under `## Restore and Failover Drills`, and set the next date in `## Due`** (`memory-template.md`).

Quarterly is the cadence that keeps the number honest. The first drill always finds something; the third one usually does too.

## Failover Patterns

| Pattern | RTO shape | Cost | Right for |
|---|---|---|---|
| Backup and restore | Hours | Lowest | Internal tools, anything with a tolerant business |
| Pilot light (data replicated, compute minimal) | Tens of minutes | Low | Most business applications |
| Warm standby (scaled-down full stack) | Minutes | Medium | Revenue-bearing workloads |
| Active/active multi-region | Seconds | Highest | Systems where minutes are unacceptable |

- **Failover speed is bounded by the slowest mechanism in the chain**, and DNS-based failover is bounded by the record TTL plus resolver behaviour. Anycast at the edge fails over faster than any DNS design (`networking.md`).
- Data is the hard part: asynchronous replication means an RPO greater than zero, and a failover with unreplicated writes is a data-loss event that needs a documented decision, made in advance, about whether to accept it.
- Failback is a separate plan, and it is the one nobody writes. After a region recovers, the data lives in the wrong place.
- Test failover with a real, scheduled exercise. A failover mechanism that has never run is a configuration, not a capability.

## Deploy and Rollback

- Health-gated deployments: slots for App Service, revisions with traffic splitting for Container Apps, rolling updates with probes for AKS. The gate is a health signal, not a delay.
- **Name the rollback artifact before deploying** — the previous image digest, the previous slot, the previous template version — and record it in `deploys/<year>.md`. "Redeploy the old commit" is not a rollback plan when the pipeline is also broken.
- Database migrations must be expand-contract: add the new shape, deploy code that tolerates both, backfill, then remove the old shape. A migration that requires code and schema to change simultaneously has no rollback.
- Feature flags decouple deployment from release, which converts most rollbacks into a configuration change.
- Deploy during hours when the people who can diagnose it are awake. The cost of a Friday deploy is measured in weekend hours.

## Patching and Maintenance

- **Guest OS patching is yours.** Azure Update Manager schedules assessments and installations across VMs and Arc-connected machines, with maintenance windows and reboot policies.
- Platform maintenance on hosts is Azure's, mostly invisible, occasionally a reboot with notice via Scheduled Events (`vms.md`).
- Managed services patch themselves inside a maintenance window you can usually choose. Unset means Azure picks, and it will pick badly at least once.
- **AKS is the one with a deadline**: minor versions leave support roughly a year after GA, and the date belongs in `## Due` the day the cluster is created (`containers.md`).
- Certificates, client secrets and reservation terms are maintenance too. Everything with an expiry date goes in `## Due` at creation time, with the real date.

## Capacity Headroom

- Know which quota the design hits first and its current value (SKILL.md Rule 8). Request headroom before the launch: approvals are not instant, and zonal capacity may not exist at any price.
- Autoscale maximums must be survivable by everything downstream — the database connection arithmetic in `databases.md` is the usual ceiling.
- Load-test at the top of the autoscale range, not at expected traffic. The failure mode you care about lives at the maximum.
- Capacity reservations exist for events where scaling out must be guaranteed. They cost whether or not they are used, which is the honest price of that guarantee.

## The Production Gate

Nothing goes live until every line is true, or its absence is a written, accepted risk.

- The availability target is stated, and the composite SLA of the request path has been multiplied out
- Zone redundancy for every stateful component; no single instance in the request path
- Backups on, retention matching the agreed RPO, and a restore that has actually been timed
- Alerts on saturation and user-visible errors, with missing-data behaviour set deliberately, routed to a human who is awake (`monitoring.md`)
- Autoscale configured, with the downstream dependency verified to survive the top of the range
- The first quota the design will hit is named, its current value known, headroom requested
- The deploy path is health-gated with an identified rollback artifact; migrations are expand-contract
- Locks and deletion protection on data resources; state and templates in version control (`iac.md`)
- Secrets accessed by managed identity or Key Vault reference; nothing in configuration files
- Every expiry date — certificates, secrets, reservations, cluster version support — is in `## Due` with its real date
- A runbook exists for the top three failure modes, saved to `~/Clawic/data/azure/artifacts/` with its `## Boxes` line in `memory.md`, and the restore drill has been run once with a recorded time
