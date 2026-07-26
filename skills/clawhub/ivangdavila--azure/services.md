# Service Selection — Thresholds, Not Feature Lists

Azure offers several correct answers to every question. Decide by the hard limit you will hit and the point where the cost curves cross, then say the number out loud.

**Contents:** [Compute](#compute) · [The Compute Break-Evens](#the-compute-break-evens) · [Data](#data) · [Messaging and Events](#messaging-and-events) · [HTTP Entry Points](#http-entry-points) · [Storage](#storage) · [Identity for Applications](#identity-for-applications) · [AI and Search](#ai-and-search) · [Questions That Settle Arguments](#questions-that-settle-arguments)

## Compute

| Option | Scale to zero | Operational load | Hard ceilings | Choose when |
|---|---|---|---|---|
| Functions (Flex/Consumption) | Yes | Lowest | Execution timeout, plan-specific networking | Event-driven, spiky, short units of work |
| Container Apps | Yes | Low | Replica and environment limits, no Kubernetes API | Containers, microservices, jobs, no operator requirements |
| App Service | No | Low | 230s request wall, plan is the scale unit | Web apps and APIs, especially with slots and Windows/.NET |
| AKS | With extra components | Highest | Cluster and node limits, IP math, upgrade cadence | Kubernetes ecosystem, CRDs, mesh, multi-tenant namespaces |
| VMs / scale sets | No | High | Quota, capacity, everything is yours | Licensing, kernel access, legacy software, lift-and-shift |
| ACI | Per group | None | No orchestration or autoscaling | Short jobs and burst capacity |

Default path for a new workload: Functions if it is event-driven, App Service if it is a web application, Container Apps if it is containers. AKS when a requirement names something only Kubernetes has — and "the team knows Kubernetes" is a real requirement, just a more expensive one than it looks.

## The Compute Break-Evens

- **Consumption Functions vs a dedicated plan**: per-execution pricing wins while the app is idle most of the day. Once it is warm nearly all the time, a small always-on plan is cheaper and removes cold start. Estimate: executions per month × average duration versus the plan's monthly cost.
- **Container Apps vs AKS**: AKS costs a control plane (for the uptime SLA) plus a node pool big enough for system pods before your workload gets a core. Below roughly four always-on containers with no Kubernetes-specific need, Container Apps wins on both money and hours. Above it, or with any operator requirement, AKS.
- **App Service vs Container Apps**: App Service if slots, Windows hosting, or the deployment ergonomics of a web app matter. Container Apps if scale-to-zero or per-container scaling rules matter.
- **VMs vs anything**: the moment a workload needs OS-level control or a licence tied to a machine, the managed options stop being cheaper — they stop being possible.
- Add the operational cost to every comparison: upgrades, patching, on-call. A cluster nobody has time to upgrade is a security finding with a monthly bill.

## Data

| Need | Default | Switch when |
|---|---|---|
| Relational, transactional | Azure SQL (serverless small, GP steady) | Open-source engine, extensions, or per-vCore cost dominates (→ PostgreSQL Flexible Server) |
| Very large relational, fast restore | Azure SQL Hyperscale | Remember it is one-way |
| Many small tenant databases | Elastic pool | Peaks are correlated across tenants (then it is one big database) |
| Global, key-based, unbounded | Cosmos DB | Anything you would join, filter or report on (→ relational) |
| Cheap key-value at volume | Table Storage | You need queries beyond partition and row key (→ Cosmos) |
| Cache, sessions, rate limiting | Azure Cache for Redis | It is actually a database (→ relational) or a queue (→ Service Bus) |
| Analytics over large volumes | Fabric / Synapse / Databricks | Small volumes: a relational engine with columnstore is far simpler and cheaper |
| Files for lift-and-shift | Azure Files | Object semantics are acceptable (→ Blob, much cheaper) |

The pattern behind the table: match the **access pattern** to the engine, not the data volume. Volume decides the tier; access pattern decides the product, and it is the choice you cannot reverse (`databases.md`).

## Messaging and Events

| Product | Semantics | Message size | Use when |
|---|---|---|---|
| Storage Queue | Simple, at-least-once, cheap | Small (tens of KB) | Basic decoupling, cost matters, no ordering needs |
| Service Bus | Sessions, ordering, dead-letter, transactions, deduplication, topics | Standard tier is limited; premium allows much larger | Business messages that must not be lost or reordered |
| Event Hubs | High-throughput stream, partitioned, replayable within retention | Small events, batched | Telemetry, logs, event sourcing, anything measured per second |
| Event Grid | Push-based reactive events with filtering and dead-lettering | Small | Reacting to resource and application events, fan-out to handlers |

Two rules that resolve most designs: **ordering and exactly-once requirements point at Service Bus** (sessions plus deduplication); **throughput and replay point at Event Hubs** (partitions are the parallelism, and they are chosen at creation). Event Grid connects the two worlds without polling.

Every event-driven design needs a dead-letter or poison destination *and* an alert on its depth. That is the failure mode with no error page (`functions.md`).

## HTTP Entry Points

| Product | Layer | Scope | Adds |
|---|---|---|---|
| Load Balancer | L4 | Regional | Raw TCP/UDP distribution, internal load balancing |
| Application Gateway | L7 | Regional | Path/host routing, WAF, TLS termination near the backend |
| Front Door | L7 | Global | Anycast entry, edge caching, WAF at the edge, fast failover |
| API Management | L7 | Regional or multi-region | Policies, quotas, subscriptions, developer portal, transformation |
| Traffic Manager | DNS | Global | Failover between non-HTTP endpoints; bounded by TTL |

- Front Door plus Application Gateway is a legitimate layered pattern for global entry with regional WAF; lock the gateway to Front Door or the origin is public.
- API Management is for API governance — quotas, keys, versioning, transformation. Using it purely as a proxy is expensive; its consumption tier exists for small estates.
- Never place two WAFs in series without tuning both; the second one's false positives are invisible from the first one's logs.

## Storage

| Need | Default | Note |
|---|---|---|
| Application objects, backups, static assets | Blob, hot tier | Tier down only with a known long lifetime (`storage.md`) |
| Shared file system for lift-and-shift | Azure Files (SMB) | Identity-based auth needs domain services |
| High-performance shared POSIX | Azure NetApp Files or premium NFS shares | Expensive; justified by IOPS and latency requirements |
| VM disks | Premium SSD v2 for production, Standard SSD for dev | Size tiers round up on other premium types |
| Data lake for analytics | Storage with hierarchical namespace | Cannot be enabled after creation |
| CDN for public assets | Front Door | Cheaper than egress from the account, and faster |

## Identity for Applications

| Scenario | Mechanism |
|---|---|
| Azure resource calling an Azure resource | Managed identity, always |
| CI/CD pipeline deploying to Azure | Federated credential (OIDC) on an app registration |
| Kubernetes pod calling Azure | Workload identity with a federated service account |
| Workforce sign-in to an internal app | Entra ID, with Conditional Access |
| Customer sign-in for a consumer product | Entra External ID for new builds; verify B2C availability before designing on it |
| Partner or vendor access | B2B guest with access reviews, or a dedicated app registration with narrow scope |

Everything in this table exists so no application ever holds a password. The remaining cases go in Key Vault and are read by reference (`identity.md`).

## AI and Search

- **Azure OpenAI / AI Foundry model deployments** are provisioned per region with their own quota expressed in tokens per minute; the quota, not the code, is usually what limits throughput. Request it before the launch, and record the granted limits in `## Current Infrastructure`.
- Deployment types differ in price and predictability: pay-as-you-go throughput versus provisioned capacity that reserves it. Provisioned is for latency guarantees, not for savings.
- **AI Search** is the retrieval layer: its tier determines index size, replica count and semantic features, and index schema changes usually mean a rebuild.
- Regional availability of models is uneven and changes; verify before promising a region, especially in sovereign clouds (`cloud_environment`).
- Content filtering and abuse monitoring are on by default and configurable within policy limits — a factor for regulated workloads.
- Anything holding customer data in prompts inherits the compliance regime of the data, not the novelty of the technology.

## Questions That Settle Arguments

1. **What is the hard limit this design hits first, and what is its current value?** An unanswered question here means the design is not finished (SKILL.md Rule 8).
2. **What does it cost per month at expected load, and at the top of the autoscale range?** Both numbers, in the actual region.
3. **What cannot be changed later?** Partition key, network plugin, address space, region, redundancy, Hyperscale, hierarchical namespace, API choice.
4. **Who operates it at 3am, and what do they read?** If the answer requires a cluster upgrade skill nobody has, the cheaper option was never cheaper.
5. **What is the composite SLA of the request path?** Multiply, do not quote the best component (`production.md`).

**When a selection is made after real comparison, it is an architecture decision**: write it to `~/Clawic/data/azure/artifacts/decision-<name>.md` with the alternatives rejected, the break-even that decided it, the estimated monthly cost, and the first quota and timeout — then add its `## Boxes` line to `memory.md`. Six months later, the reasoning is worth more than the conclusion (`memory-template.md`).
