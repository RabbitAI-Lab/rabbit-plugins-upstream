# Migration — Moving In From On-Prem or Another Cloud

Migrations fail on the parts nobody assessed: identity, DNS, licences, egress bills and the application nobody owns. Assess first, land the platform second, move workloads third.

**Contents:** [The Order That Works](#the-order-that-works) · [Assessment](#assessment) · [The Six Dispositions](#the-six-dispositions) · [AWS to Azure Service Mapping](#aws-to-azure-service-mapping) · [Moving Data](#moving-data) · [Databases](#databases) · [Identity](#identity) · [Licensing](#licensing) · [The Cutover](#the-cutover) · [After](#after)

## The Order That Works

1. **Landing zone first.** Subscriptions, management groups, policy baseline, networking, identity (`governance.md`). Workloads migrated into an unstructured subscription get migrated twice.
2. **Assess.** Inventory, dependencies, and a cost model that includes egress and licences.
3. **Pick dispositions** per workload — not per estate.
4. **Migrate a low-risk workload end to end**, including its cutover and rollback, before scheduling the rest. The first migration teaches what the assessment missed.
5. **Wave the rest** by dependency cluster, never by convenience.
6. **Decommission**, and only then count the savings.

## Assessment

- **Azure Migrate** discovers servers, databases and web apps, maps dependencies from network traffic, and produces sizing and cost estimates. Its dependency map is the deliverable that changes plans: the forgotten integration always appears here.
- Dependency clusters, not individual servers, are the migration unit. Splitting a chatty pair across the internet turns a working system into a latency incident.
- Cost model must include: compute at the right sizes (Migrate's recommendation is a starting point), storage with its redundancy, **egress**, licences with and without Hybrid Benefit, and the platform services the landing zone needs whether or not anything is using them yet.
- Baseline the current performance before moving. Without it, "it is slower on Azure" is unfalsifiable.
- Record the inventory, the dispositions and the estimate as an artifact: `~/Clawic/data/azure/artifacts/migration-<estate>.md`, with its `## Boxes` line in `memory.md` (`memory-template.md`).

## The Six Dispositions

| Disposition | Means | Right when |
|---|---|---|
| Rehost | Lift and shift to VMs | Deadline-driven moves, unsupported software, datacentre exit |
| Replatform | Move to a managed service with minimal change | Databases to Flexible Server, web apps to App Service — the highest-yield option |
| Refactor | Re-architect for cloud-native | The workload is strategic and the team has capacity |
| Repurchase | Replace with SaaS | Commodity workloads: mail, CRM, file shares |
| Retire | Turn it off | Always more workloads than anyone expects — assess usage before assuming |
| Retain | Leave it where it is, possibly with Azure Arc | Latency, licensing or regulatory constraints |

Most estates are mostly rehost and replatform with a long retire list. A plan that refactors everything is a plan that finishes late.

## AWS to Azure Service Mapping

Approximate equivalents — the operational models differ, so treat these as starting points rather than drop-ins.

| AWS | Azure | Difference that bites |
|---|---|---|
| EC2 | Virtual Machines | Stop still bills unless deallocated; 30-second spot notice instead of two minutes |
| Auto Scaling group | VM scale set (Flexible) | Different health and upgrade semantics |
| Lambda | Functions | HTTP still hits the ~230s platform wall; a storage account is a hard dependency |
| Fargate / ECS | Container Apps | No task definitions; revisions and KEDA scalers instead |
| EKS | AKS | Version support window and IP math are the operational differences |
| ELB / ALB | Load Balancer / Application Gateway | L4 and L7 are separate products |
| CloudFront | Front Door | WAF tiering and origin locking differ |
| S3 | Blob Storage | The **account** is the throttle and firewall boundary, not the bucket |
| EBS | Managed disks | Size tiers round up; caching is a per-disk setting that matters |
| RDS | Azure SQL / PostgreSQL Flexible Server | Tier semantics and HA models are not equivalent |
| DynamoDB | Cosmos DB | RU/s instead of RCU/WCU; 20 GB logical partition ceiling |
| ElastiCache | Azure Cache for Redis | Basic tier has no replica and no SLA |
| SQS | Storage Queue / Service Bus | Two products: cheap-and-simple versus ordering and sessions |
| SNS / EventBridge | Event Grid | Push with filtering, different retry and dead-letter model |
| Kinesis | Event Hubs | Partition count is chosen at creation and caps parallelism |
| IAM | Entra ID **plus** Azure RBAC | Two systems; directory roles are not resource roles (`identity.md`) |
| IAM policy documents | Role definitions and Azure Policy | No user-authored deny in RBAC; Policy does prevention |
| Secrets Manager / Parameter Store | Key Vault / App Configuration | Soft delete and purge protection change name reuse |
| CloudWatch | Azure Monitor + Log Analytics | Logs are billed per GB ingested and queried with KQL |
| CloudTrail | Activity Log | About 90 days by default; diagnostic settings for longer |
| CloudFormation | ARM / Bicep | No state file; incremental mode does not delete |
| Organizations / accounts | Management groups / subscriptions | The subscription is the quota boundary; the tenant is the identity boundary |
| Route 53 | Azure DNS | Private DNS zones must be linked to each VNet |
| Direct Connect | ExpressRoute | Partner-provisioned circuits with long lead times |

Two AWS habits that mislead on Azure: RBAC has no user-authored deny (prevention lives in Azure Policy), and a resource group is not an account-like boundary — it isolates lifecycle, not network or quota.

## Moving Data

- Compute the transfer time honestly: usable bandwidth × the window, versus the data volume. A 100 TB estate over a busy 1 Gbps link is weeks, not a weekend.
- **AzCopy** for object data — parallel, resumable, Entra-authenticated. Storage-to-storage copies within Azure are server-side.
- **Data Box** family for physical transfer when the network path cannot finish in time. Lead time is part of the plan, not an afterthought.
- **Egress from the source cloud is a real line item** and is usually the surprise in the cost model. Check whether a switching-related waiver applies before assuming the list rate.
- Incremental sync then a final delta at cutover: the last sync's duration is part of the outage window.
- Verify by checksum and count, not by "the copy finished".

## Databases

- **Azure Database Migration Service** handles offline and online (minimal-downtime) migrations for the common engines. Online replication means the cutover is a switch, not a copy.
- Test the restore of the migrated database into a scratch environment before the cutover, and time it. That number is the rollback budget (`production.md`).
- Version and feature parity is the usual blocker: extensions that must be allow-listed, collations, agent jobs, linked servers, and anything that assumed local filesystem access.
- Performance after migration is a tuning exercise; baseline before and compare like for like, at the same concurrency.
- Plan the connection-string change as part of the cutover, with Key Vault references so the change is one place (`identity.md`).

## Identity

- Directory first: sync or federate on-prem identities before the applications need them. Entra Connect topology and UPN suffixes are the two things that force a redesign late.
- Every service account in the old estate maps to a managed identity or a federated credential in the new one. Migrating a password to Key Vault is the fallback, not the goal.
- Application authentication is often the longest pole: SAML and OIDC integrations must be reconfigured, tested and cut over one at a time.
- Role assignments do not migrate. Take an access inventory in the source estate and rebuild it deliberately — a migration is the best chance to drop the accumulated over-grants.

## The Cutover

Written in advance, per workload, and rehearsed.

1. **Freeze** changes in the source, and announce the window.
2. **Lower DNS TTLs** at least a full old-TTL ahead of the window. This is the step that is skipped, and it is the reason a cutover takes hours instead of minutes.
3. **Final data sync** and verification.
4. **Switch** the endpoint: DNS, or a load balancer weight if the design allows both.
5. **Smoke test** against a written list, including the integrations that only run on a schedule.
6. **Watch** for a defined period with alerts already configured (`monitoring.md`).
7. **Rollback trigger**: a named condition and a named person who decides, with the source still intact and reachable. Rollback expires — after the source is decommissioned there is no going back, so the date it expires is part of the plan.
8. **Record it**: `deploys/<year>.md` for the event, and the cutover plan itself as an artifact with its `## Boxes` line.

## After

- **Right-size two weeks after**, not before: the assessment's sizing was a guess, and the real telemetry is now available (SKILL.md Rule 3).
- Only then buy reservations or savings plans, and put the term end date in `## Due` (`costs.md`).
- Decommission the source, and verify the savings actually appeared — a migration that leaves both estates running costs more than either.
- Update the shared inventory: every migrated host gets its row in `~/Clawic/data/servers/servers.md` with provider `azure`, and every retired host has its row deleted with the date noted in `memory.md` (`memory-template.md`).
- Move the domains: registrar, DNS hosting, and certificate arrangements go into `~/Clawic/data/domains/domains.md`, with renewal dates mirrored into `## Due`.
