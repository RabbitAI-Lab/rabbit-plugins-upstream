# Virtual Machines, Disks and Scale Sets

VMs are the fallback when a managed service does not fit — licensing, legacy software, kernel-level control, or a migration that has not happened yet. Everything here costs by the hour whether or not anyone uses it.

**Contents:** [Picking a Family](#picking-a-family) · [Sizing and Right-Sizing](#sizing-and-right-sizing) · [Stop vs Deallocate](#stop-vs-deallocate) · [Disks](#disks) · [Availability](#availability) · [Spot](#spot) · [Scale Sets](#scale-sets) · [Capacity and Quota Errors](#capacity-and-quota-errors) · [Maintenance and Scheduled Events](#maintenance-and-scheduled-events) · [Images and Patching](#images-and-patching)

**Read `~/Clawic/data/servers/servers.md` before sizing or recommending anything** — the estate that already exists sets the family, the region and the price the user is used to.

**After creating, resizing, discovering or deleting a VM or scale set, write its row** to `~/Clawic/data/servers/servers.md` in the same turn: `Name | azure | subscription/resource group | region | size | role | monthly with currency | access pointer`. Deletion means deleting the row and noting the date in `memory.md` (`memory-template.md`).

## Picking a Family

| Letter | Optimized for | Typical use |
|---|---|---|
| B | Burstable, credit-based | Dev boxes, low-traffic services with spikes |
| D | General purpose, balanced | Web and app servers, most workloads |
| E | Memory (roughly 8 GB per vCPU) | Databases, caches, JVM heaps, analytics |
| F | Compute (high clock, low memory ratio) | Batch, encoding, CPU-bound APIs |
| L | Local NVMe storage | Storage-heavy databases, Cassandra, big local scratch |
| N | GPU | Training, inference, rendering |
| M | Very large memory | SAP HANA and equivalents |

Suffix letters matter as much as the letter: `s` for premium storage support, `d` for a local temp disk, `a` for AMD, `p` for ARM64 (Ampere). ARM64 and AMD variants are usually cheaper per vCPU than the Intel equivalent for the same generation — worth a benchmark before dismissing them, and worth checking that every dependency has an ARM build.

Prefer the newest generation available in the region: newer generations are typically cheaper per unit of performance, not more expensive.

## Sizing and Right-Sizing

- Start at the smallest viable size. Scaling up is a resize with a reboot; an oversized fleet bleeds every hour.
- Heuristic (canonical for this skill, SKILL.md Rule 3): average CPU below 20% over 14 days → step down one size, which roughly halves compute cost per step. Sustained above 70% → step up or scale out.
- **CPU percentage lies on B-series.** Burstable VMs accrue credits while below their baseline and spend them above it; once credits are exhausted the VM is throttled to baseline and CPU reads as high while the workload is actually being starved. Check the credit-remaining and credit-consumed metrics before concluding anything about a B-series machine.
- CPU alone under-diagnoses memory-bound workloads. The guest OS must be sending memory metrics (the Azure Monitor agent, not the platform) — without it, "memory looks fine" means "nothing is measuring memory".
- Resizing between some families requires a deallocate, and a size may be unavailable on the current host cluster: the fix is stop-deallocate-resize-start, which changes the host.
- Ephemeral OS disks (stored on the host, free, faster boot, lost on deallocate) suit stateless nodes and scale sets. Not for anything whose OS disk carries state.

## Stop vs Deallocate

| Action | Compute billing | IP | Disks |
|---|---|---|---|
| Shutdown from inside the guest | **Still billed** — the VM stays allocated | Kept | Billed |
| Portal/CLI Stop (deallocate) | Stopped | Dynamic IP released, static kept and billed | Billed |
| Delete | Stopped | Static IP kept unless deleted | **Disks survive** unless delete-with-VM was set |

Consequences worth stating out loud: a "stopped" VM in the guest costs full price; a deallocated VM still costs disks and static public IPs; a deleted VM leaves disks, NICs and IPs that nobody sweeps. Auto-shutdown schedules on dev VMs are the highest-yield cost control on most estates (`costs.md`).

## Disks

- **Types**: Standard HDD (backup, archive), Standard SSD (dev, light production), Premium SSD (production, tiered IOPS by size), Premium SSD v2 (IOPS and throughput configured independently of size — usually the better modern default), Ultra (extreme IOPS, zone-pinned, more constraints).
- **Premium and Standard sizes come as tiers that round up.** Asking for 200 GB bills the next tier up; provisioning to the tier boundary is free performance.
- **Disks can grow, never shrink.** Shrinking means create-copy-swap with downtime.
- **Bursting**: smaller premium disks accrue burst credits, which flatters a benchmark and disappears under sustained load. Test at steady state.
- **Host caching**: ReadOnly for OS disks and read-heavy data, None for write-heavy logs and database transaction logs. Wrong caching on a database log disk is a common, invisible performance ceiling.
- The VM size caps disk IOPS and throughput independently of the disk. A fast disk on a small VM is money spent on a ceiling you cannot reach.
- Snapshots of managed disks are incremental; images are for reuse. Neither is a backup policy (`production.md`).
- Encryption: platform-managed keys are on by default. **Encryption at host** covers OS, data and temp disks and is the simplest full-coverage option; customer-managed keys via a disk encryption set are for regimes that require key ownership; in-guest disk encryption is a third, heavier mechanism. Choose one deliberately and write which, per disk set, to `## Current Infrastructure` in `~/Clawic/data/azure/memory.md`; the mechanics of each are in `security.md`.

## Availability

| Configuration | Typical SLA shape | Cost |
|---|---|---|
| Single VM with premium/ultra disks | Lowest tier of the three | Cheapest |
| Availability set (fault and update domains, single datacentre) | Middle tier | Free |
| Two or more VMs across availability zones | Highest tier | Cross-zone traffic, duplicated compute |

Verify the current numbers in the SLA document before quoting them; the ordering has been stable for years, the digits have not. Zones protect against a datacentre; availability sets protect against a rack and a host update; neither protects against a region, a bad deployment, or a `DROP TABLE`.

Zonal placement is chosen at creation and cannot be changed afterwards — moving a VM between zones means recreating it from a snapshot.

## Spot

- Up to very large discounts for interruptible capacity, with a **30-second eviction notice** — far shorter than other clouds, which rules out most graceful-drain designs that assume minutes.
- Eviction policy: *Deallocate* keeps the disk and lets you restart when capacity returns; *Delete* is for stateless nodes in a scale set.
- Correct for: batch, CI runners, dev environments, stateless scale-set nodes with a healthy on-demand base. Wrong for: anything holding a session, a queue lease, or un-checkpointed state.
- Spot capacity is per size per region and can be unavailable for days. Design so that zero spot instances is a slow day, not an outage.

## Scale Sets

- **Flexible orchestration** is the modern default: VMs are first-class, mixed sizes and spot/on-demand mixes are possible, and it integrates with availability zones cleanly. Uniform is the older model with faster homogeneous scaling.
- Autoscale rules need a cooldown that reflects boot time. Scale out aggressively, scale in slowly: flapping costs more than the extra instance.
- Upgrade policy — manual, automatic, or rolling — decides whether a model change touches production instantly. Rolling with a health probe is the safe default.
- The application health extension or a load-balancer probe is what makes automatic repair meaningful; without one, unhealthy instances stay in rotation.
- Record the scale set as **one row** in `servers.md`, with the current instance count in the role cell.

## Capacity and Quota Errors

- `SkuNotAvailable` — the size is not offered here, or is restricted for this subscription type. `az vm list-skus --location <region> --all` lists restrictions and their reason.
- `AllocationFailed` / `ZonalAllocationFailed` — physical capacity is exhausted right now. Options, cheapest first: another zone, another size in the same family, Flexible orchestration so the platform can place freely, another region, or a capacity reservation if the workload must be guaranteed.
- `QuotaExceeded` — administrative, per family per region. Self-service in the Quotas blade for most families; a support request for the rest. Approvals are not instant, which is why headroom is requested before the launch (SKILL.md Rule 8).
- **Capacity reservations** hold capacity for a fee whether or not it is used, and are the only real answer to "we must be able to scale out on Black Friday".
- Write any quota change to `## Current Infrastructure` with the date and the new ceiling: it is the number the next design needs.

## Maintenance and Scheduled Events

- Most platform maintenance is memory-preserving and invisible. The rest reboots the VM, with notice.
- **Scheduled Events** on the instance metadata endpoint publishes `Freeze`, `Reboot`, `Redeploy`, `Preempt` and `Terminate` with a lead time — typically minutes for maintenance, 30 seconds for spot preemption. Reading it and draining is the difference between a rolling restart and an incident.
- Maintenance configurations let you declare a window for host updates on supported families; without one, Azure picks the time.
- Guest OS patching is yours: Azure Update Manager schedules it, with a maintenance window and a reboot policy, across VMs and Arc-connected machines (`production.md`).
- Resource Health records every platform-initiated event after the fact — it is the answer to "why did it reboot at 3am".
