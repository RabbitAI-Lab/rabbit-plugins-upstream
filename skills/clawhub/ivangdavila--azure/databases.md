# Databases — Azure SQL, PostgreSQL, Cosmos DB, Redis

Four engines with four cost models and four different meanings of "high availability". Pick by access pattern and by the constraint that cannot be changed later.

**Contents:** [Choosing an Engine](#choosing-an-engine) · [Azure SQL](#azure-sql) · [PostgreSQL and MySQL Flexible Server](#postgresql-and-mysql-flexible-server) · [Cosmos DB](#cosmos-db) · [Azure Cache for Redis](#azure-cache-for-redis) · [Connections and Pooling](#connections-and-pooling) · [Backup, Restore and HA](#backup-restore-and-ha) · [Access Without Passwords](#access-without-passwords)

## Choosing an Engine

| Access pattern | Engine | Why |
|---|---|---|
| Relational, joins, reporting, transactions | Azure SQL | Deepest managed feature set on Azure; serverless tier makes small workloads cheap |
| Relational, open source, extensions (pgvector, PostGIS), portability | PostgreSQL Flexible Server | Extension support and per-vCore cost; no licence component |
| Known-key reads and writes, global distribution, unbounded scale | Cosmos DB | Predictable single-digit-ms at any size — for the queries the partition key supports |
| Cache, sessions, rate limits, transient state | Azure Cache for Redis | Sub-millisecond; not a database |
| Cheap key-value at volume, no query needs | Table Storage | Order-of-magnitude cheaper than Cosmos for the same rows, with a fraction of the capability |

Anything you would filter, join or report on belongs in a relational engine. Cosmos DB punishes exactly those queries with cross-partition fan-out, and the partition key that makes them possible cannot be changed afterwards.

## Azure SQL

**Purchasing models.** DTU (bundled, simple, legacy) versus vCore (compute and storage priced separately, Hybrid Benefit applies, all new work). Convert legacy DTU databases at the next review — vCore is where the features land.

**Service tiers.**

| Tier | Storage/compute shape | Right for |
|---|---|---|
| General Purpose | Remote storage, single compute node | Most workloads |
| Business Critical | Local SSD, replica set, free readable secondary | Latency-sensitive OLTP, read scale-out |
| Hyperscale | Distributed storage, fast restore regardless of size, many read replicas | Databases beyond a few TB, or restore-time requirements |

**Hyperscale is one-way.** Moving into it is a migration; moving out is an export and import. Decide before, not after.

**Serverless** auto-pauses after an idle delay (a minimum of one hour) and bills per vCore-second while active. Correct for dev and spiky production; wrong when a cold resume in front of a user is unacceptable, because resume takes tens of seconds.

**Elastic pools** share compute across many databases with uncorrelated peaks — the standard answer for multi-tenant estates with one database per tenant.

Other specifics that bite:

- **Connection policy** — Redirect gives lower latency but requires the client to reach a range of ports beyond 1433; Proxy works through restrictive networks at a latency cost. A driver that hangs on connect from inside a locked-down VNet is usually this.
- **Transient errors are normal.** Codes in the 40000s (for example 40197, 40501, 40613) mean the platform moved or throttled your database. Retry with backoff is a requirement, not a nicety.
- **Storage grows and does not shrink**; max size is a property of the tier.
- The server-level firewall rule labelled "Allow Azure services" corresponds to 0.0.0.0 and admits resources from **other tenants**. Turn it off and use a private endpoint or explicit VNet rules (`security.md`).
- Auditing and diagnostic settings are off by default; the compliance requirement is discovered later than the data.

## PostgreSQL and MySQL Flexible Server

- **Compute tiers**: Burstable (B-series, credit-based — the same lie about CPU as burstable VMs), General Purpose, Memory Optimized. Burstable is dev-only for anything with steady load.
- **Storage grows and never shrinks**, and IOPS is tied to storage size unless the tier allows independent provisioning. Growing storage for IOPS is a legitimate, badly-signposted move.
- **High availability**: zone-redundant HA doubles the compute bill because it runs a standby. Same-zone HA protects against a node, not a datacentre. Neither is a backup.
- Failover to the standby takes tens of seconds and drops connections — the application must reconnect, and connection strings must point at the server FQDN, never a node.
- **Built-in connection pooling (PgBouncer)** is available and should be on for anything with many short-lived clients; PostgreSQL connections are processes, and a few hundred idle ones will exhaust memory (below).
- Extensions must be allow-listed at the server level before `CREATE EXTENSION` works. `pgvector` and `PostGIS` are the two that most often gate a design.
- Major version upgrades are in-place and irreversible. Snapshot, test on a restored copy, then upgrade.
- Maintenance windows are configurable; unset means Azure picks, and it will pick badly at least once.

## Cosmos DB

**Three decisions that cannot be undone**: the partition key, the API (NoSQL, MongoDB, Cassandra, Gremlin, Table), and the account's consistency default. Everything else is tuning.

- **Partition key** — choose the value that appears in the `WHERE` clause of the queries you run most, with enough cardinality to spread writes. The hard ceiling is 20 GB of data per logical partition (one distinct key value), which is a design constraint, not a quota to raise.
- **RU/s is the currency.** Every operation returns its charge in `x-ms-request-charge`; measure the real query rather than estimating. A point read of a small item is about 1 RU; a cross-partition query can be hundreds.
- **Throughput modes**: manual (fixed, cheapest at steady load), autoscale (floors at 10% of maximum, bills at a 1.5× per-RU rate, right for variable load), serverless (per-operation, right for dev and bursty low volume, with lower ceilings).
- **Default indexing indexes every path**, and writes pay for it. Excluding unqueried paths is often the largest single RU saving available.
- **429 means throttled, not down.** The SDK retries using `x-ms-retry-after-ms`. Persistent 429s mean a hot partition or an expensive query, and raising RU/s treats the symptom at a monthly cost.
- Consistency: Session is the default and the right answer for most applications. Strong costs more RU and restricts multi-region write topologies; Eventual is cheapest and requires the application to tolerate it.
- Multi-region writes need conflict resolution designed in; multi-region reads are a switch.
- Change feed is the supported way to react to writes — it powers materialized views, search indexing and event propagation without dual writes.
- TTL on items is the cheapest possible retention policy; deletes cost RU, expiry does not.

## Azure Cache for Redis

- Tiers: Basic (single node, **no SLA, no replica** — dev only), Standard (replicated), Premium (persistence, clustering, private endpoint, larger sizes). Newer Redis SKU families exist with different price/performance; verify what the region offers before quoting.
- Data loss on failover is normal without persistence, and persistence is a Premium feature. Design the application to repopulate.
- Memory policy matters: with `noeviction`, a full cache starts failing writes instead of evicting. Pick an eviction policy deliberately.
- Do not use it as a database, a queue, or a lock manager without understanding what a failover does to each of those.
- Connection storms after a failover are the classic outage: use a client with backoff and a bounded pool.

## Connections and Pooling

The most common database outage on Azure is not the database.

- Every app instance keeps a pool. Total connections = `instances × pool_size`. An App Service plan autoscaling to 10 instances with a 100-connection pool asks for 1,000 connections — an ask that most managed tiers refuse.
- Compute the number **before** setting autoscale maximums, and state it (SKILL.md Rule 8). If the number exceeds the tier's ceiling, the fix is a pooler or a smaller pool, not a bigger database.
- PostgreSQL: use the built-in pooler for many short-lived clients. Azure SQL: pool in the driver, and prefer fewer, longer-lived connections.
- Serverless and function workloads multiply this: every instance is a client, and scale-out is unbounded by design. Identity-based connections do not change the arithmetic.
- Symptoms of exhaustion look like slowness, not errors, until the moment they look like a total outage.

## Backup, Restore and HA

| Mechanism | Protects against | Does not protect against |
|---|---|---|
| Zone-redundant HA / replicas | Node or datacentre failure | Bad data, dropped tables, ransomware |
| Point-in-time restore (SQL, Flexible Server) | Human error, within the retention window | Anything older than retention |
| Long-term retention (SQL) | Compliance-length recovery | Nothing, if never tested |
| Cosmos continuous backup | Restore to a timestamp within the window | A restore into a *new* account, which means a cutover |
| Geo-restore / geo-replica | Region loss | Correlated logical corruption, which replicates |

- **Replication is not backup.** A `DROP TABLE` replicates in milliseconds.
- Restore always lands somewhere new — a new database, server or account. The cutover (connection strings, firewall rules, Key Vault access, DNS) is the part that takes the time, which is why the drill is the deliverable.
- **Time a restore quarterly** and write the measured RTO and everything that was missing into `deploys/<year>.md` under `## Restore and Failover Drills`, with the next date in `## Due` (`memory-template.md`). An untested restore is a hypothesis.

## Access Without Passwords

- Azure SQL, PostgreSQL Flexible Server and Cosmos DB all support Entra ID authentication. A managed identity plus a database-level role removes the connection-string password entirely — which is the only reliable way to stop it being pasted into a config file, a ticket, or a memory file (`identity.md`).
- Set an Entra administrator on the server, then create contained users mapped to the identity. Local SQL authentication can then be disabled.
- Where a password is genuinely unavoidable, it lives in Key Vault and the application reads it by reference. In any note, runbook or artifact, only the pointer is written: `azure-kv:<vault>/<secret>` (`memory-template.md`).

**When a tier, HA posture, or connection ceiling is chosen, record it** in `## Current Infrastructure`: engine, tier, HA mode, backup retention, and the maximum connection count the design assumes.
