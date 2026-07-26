# Storage — Blob, Files, and the Account as a Throttle

The storage account, not the container, is the unit of throughput, redundancy, firewall and identity. Most storage surprises — cost, throttling, exposure — come from decisions made at account creation.

**Contents:** [Account Choices That Stick](#account-choices-that-stick) · [Redundancy](#redundancy) · [Access Tiers and Early Deletion](#access-tiers-and-early-deletion) · [Lifecycle Management](#lifecycle-management) · [Throughput and Throttling](#throughput-and-throttling) · [Access Control and SAS](#access-control-and-sas) · [Protecting Data](#protecting-data) · [Azure Files](#azure-files) · [Data Movement](#data-movement)

## Account Choices That Stick

Set at creation, painful or impossible to change later:

- **Kind and performance**: StorageV2 Standard for almost everything; Premium block blob for high transaction rates and low latency; Premium file shares for SMB performance; Premium page blobs for unmanaged disks. Performance tier is not convertible.
- **Redundancy**: some conversions are supported live, others require a migration request or a manual copy. Choose per purpose, not per habit.
- **Hierarchical namespace (Data Lake Gen2)**: cannot be toggled after creation, and changes the semantics of directory operations and ACLs. Enable it only if analytics workloads need it.
- **Region**: an account cannot move. Copying petabytes across regions is a project.
- **Name**: globally unique, and soft-deleted names remain reserved for a period. Validate the name before the deployment.

Split accounts by purpose rather than accumulating one giant account: throughput, firewall rules, lifecycle policy and blast radius are all per account.

## Redundancy

| Option | Copies | Survives | Notes |
|---|---|---|---|
| LRS | 3 in one datacentre | Disk and rack failures | Cheapest; correct for reproducible data |
| ZRS | 3 across zones in one region | A datacentre | The sensible default for production in zone-enabled regions |
| GRS | LRS + async copy to the paired region | Region loss | Secondary is not readable |
| RA-GRS | As GRS | Region loss | Secondary readable, eventually consistent |
| GZRS / RA-GZRS | ZRS + geo copy | Datacentre and region | Most expensive |

Geo-redundancy replicates corruption and deletion too — it is availability insurance, not backup. Failover to the secondary is customer-initiated for most account types, takes time, and returns you to an unprotected state until re-replication finishes.

## Access Tiers and Early Deletion

| Tier | Storage price | Read price | Minimum retention |
|---|---|---|---|
| Hot | Highest | Lowest | None |
| Cool | Lower | Higher | 30 days |
| Cold | Lower still | Higher still | 90 days |
| Archive | Lowest | Highest, plus hours of rehydration | 180 days |

- **Early deletion is billed as if the blob stayed for the minimum.** Moving short-lived data to cool then deleting it costs more than leaving it hot. The tiering decision belongs to data whose lifetime is known and long.
- **Read costs rise as storage costs fall.** A cool blob read weekly is more expensive overall than a hot one. Compute the crossover with the real access frequency: monthly cost = storage + (reads × per-operation + GB read × per-GB).
- Archive is offline: retrieval takes hours at standard priority and cannot be read in place. Anything a person might request interactively does not belong there.
- Tier can be set per blob; the account default only applies to new blobs without an explicit tier.

## Lifecycle Management

- Rules run once a day and act on blob age, prefix, tag or last-access time. Last-access tracking must be enabled and has its own cost.
- Version and snapshot rules are separate from the current-version rules — the usual mistake is a policy that tiers current blobs while old versions pile up at hot prices forever.
- The first run after a policy change can move a very large number of blobs, and each move is a billed transaction. Estimate the transaction cost of a policy over a big account before applying it.
- Deleting is the cheapest tier. A retention rule that deletes beats a tiering rule that keeps.

## Throughput and Throttling

- The **account** has request-rate and bandwidth ceilings (on the order of tens of thousands of requests per second for standard accounts). Exceeding them returns 503 `ServerBusy` — the fix is spreading load across accounts, partitions or prefixes, not a bigger SKU.
- Within an account, throughput is partitioned by blob name range: sequential keys such as timestamps concentrate load on one partition. A hashed or reversed prefix spreads it.
- Single-blob throughput is capped independently of the account; parallel block uploads are how large files go fast.
- Premium block blob accounts exist for high transaction rates at low latency; they cost more per GB and less per operation, which inverts the arithmetic for small-object-heavy workloads.
- Egress to the internet is billed per GB after a small free allowance. Serving public assets through a CDN or Front Door is cheaper and faster than serving them from the account (`costs.md`).

## Access Control and SAS

Ordered from best to worst:

1. **Entra ID with data-plane roles** (`Storage Blob Data Reader`/`Contributor`) plus `allowSharedKeyAccess=false`. Revocable, auditable, no secret. This is the target state.
2. **User delegation SAS** — a SAS signed with an Entra credential rather than the account key. Short-lived, revocable by revoking the delegation key, and attributable to a principal.
3. **Stored access policy SAS** — service SAS bound to a policy you can revoke without rotating keys.
4. **Account SAS or account keys** — the whole account, and revoking means rotating a key that everything else uses.

Rules that follow:

- Keys rotate in pairs (key1/key2) so a rotation is not an outage: switch consumers to key2, rotate key1, switch back.
- Any URL containing `sig=` is a credential. It never goes into a note, a ticket, or anything under `~/Clawic/data/` — record `azure-kv:<vault>/<secret>` or the account name only (`memory-template.md`).
- A SAS expiry policy at the account level stops the "one-year SAS" habit.
- Public blob access is off at the account level in a hardened estate; genuinely public assets are served through a CDN or Front Door with the origin locked down (`security.md`).
- The storage firewall's "trusted Microsoft services" exception is broader than it sounds — pair it with a resource-instance rule naming the specific resource where possible.

## Protecting Data

| Feature | Protects against | Note |
|---|---|---|
| Blob soft delete | Accidental delete or overwrite, within the retention window | On by default for new accounts, but verify the number of days |
| Container soft delete | Deleting a whole container | Separate setting from blob soft delete |
| Versioning | Overwrites | Every version bills; pair with a lifecycle rule or costs grow forever |
| Point-in-time restore | Bulk accidental changes | Requires versioning, change feed and soft delete together |
| Immutability policies (WORM) | Ransomware and compliance-mandated retention | A locked time-based policy cannot be shortened by anyone, including you |
| Azure Backup for blobs | Operational and vaulted backup with its own retention | The only mechanism that survives deletion of the account itself |
| Resource lock | Deleting the account | Does not protect the data inside it |

Soft delete is not backup: deleting the account deletes everything, and account deletion is a single click that no soft-delete setting protects.

## Azure Files

- **SMB** for Windows and general file-share workloads; **NFS** requires a premium file share and has different auth (no identity-based auth — network-level control only).
- Identity-based access for SMB works with on-prem AD or Entra Domain Services; without it, the share is authenticated by the account key, which is the wrong credential to distribute.
- Premium file shares provision IOPS with size; standard shares are pay-as-you-go with lower, burst-based performance. A "slow file share" is usually a standard share doing metadata-heavy work.
- Azure File Sync turns Windows servers into a cache tier with cloud tiering — the practical answer for branch offices and lift-and-shift file servers.
- Files snapshots are share-level and cheap; they are not offsite protection.

## Data Movement

- **AzCopy** for anything scripted: parallel, resumable, and the tool to reach for over portal uploads. Authenticate with Entra rather than a SAS where possible.
- Storage-to-storage copies within a region are server-side and fast; cross-region copies pay egress.
- Object replication mirrors blobs between accounts asynchronously, with its own rules and no ordering guarantees.
- **Data Box** for terabyte-to-petabyte physical transfer when the network path would take weeks. Compute the crossover honestly: available bandwidth × the window versus the appliance's lead time (`migration.md`).
- Change feed gives an ordered log of blob changes — the supported way to drive downstream processing without polling.

**When an account's purpose, redundancy, tier policy or firewall posture is decided, record it** in `## Current Infrastructure` in `~/Clawic/data/azure/memory.md`: account name, redundancy, what it holds, whether public access and shared-key access are disabled. The next audit starts from that line instead of from a portal tour.
