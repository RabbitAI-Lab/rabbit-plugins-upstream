# Working File Templates — Azure

Read this file only when WRITING. `config.yaml` is what the user **declared**; `memory.md` and everything it indexes is what you **observed** or produced. An observation never overwrites a declaration.

## Where each thing goes

| Data | Home | How it grows |
|---|---|---|
| Declared preferences — table keys and preference areas alike | `~/Clawic/data/azure/config.yaml` | Key by key, read-modify-write |
| Subscription context, infrastructure, spend, saved queries, pain points, how they work, due dates, box index | `~/Clawic/data/azure/memory.md` | Rewritten in place; stays small |
| VMs and VM scale sets | `~/Clawic/data/servers/servers.md` (**shared**) | One row per host, every provider in one inventory |
| Custom domains, DNS zones, certificate expiry | `~/Clawic/data/domains/domains.md` (**shared**) | One row per domain |
| A person who owns a subscription, or the client an engagement belongs to | `~/Clawic/data/contacts/contacts.md` (**shared**) | One row per person; referenced here by name only |
| Subscriptions, their tenant, and who pays for them | `## Subscription Context` in `memory.md` while there is one; `~/Clawic/data/azure/subscriptions.md` from the second | One row per subscription |
| Things you produced that get re-read — runbooks, a custom role or Policy definition that finally worked, the VNet address plan, architecture decisions, migration cutover plans, postmortems | `~/Clawic/data/azure/artifacts/<kebab-name>.md` | Born as its own file, from the first one |
| Deploy records, restore and failover drills | `~/Clawic/data/azure/deploys/<year>.md` | Append-only, cut by year |
| **Anything durable this table does not name** | `~/Clawic/data/azure/<plural-noun>.md`, or `artifacts/<kebab-name>.md` if it is a long text read whole | Name the file after what it holds, never after when it was made; add its `## Boxes` line in the same turn |
| Credentials of any kind | Nowhere under `~/Clawic/data/` | Pointer only — see Secrets |

## When to write

No permission needed; every write is announced in one line that names the file. Writes and deletions stay inside the paths declared in this skill's `configPaths`. A deletion is named in that same line, and in a shared box only rows this skill itself wrote are ever updated or removed.

| It happened | Write |
|---|---|
| A VM or scale set was created, resized, discovered or retired | Its row in `servers.md` |
| An inventory or Resource Graph pass ran (Rule 1) | `## Current Infrastructure` |
| A quota was raised, or an allocation failure named a regional ceiling | `## Current Infrastructure` |
| A bill was reviewed, or a saving landed | `## Spend` |
| A budget or anomaly alert was created | `### Alerts Configured` |
| A subscription was added, or its tenant, owner or billing named | The subscriptions table |
| A custom domain was bound, a DNS zone created, or a certificate issued | Its row in `domains.md`, plus the expiry in `## Due` |
| Anything acquired an expiry date — client secret, certificate, reservation term, AKS version support | `## Due` |
| A deploy shipped, or a restore/failover drill was timed | `deploys/<year>.md` |
| A KQL or Resource Graph query answered something worth asking again | `## Saved Queries` |
| A runbook, a working role or Policy definition, an address plan, or an architecture decision came out of the session | `artifacts/` |
| The user declared a preference | Its key in `config.yaml` |
| Recurring work was scheduled or run | `## Due` |

## Start flat, split only when it hurts

Everything except artifacts, deploy records and the shared boxes begins inside `memory.md`. Splitting is a procedure, not a suggestion:

1. Before appending to a section, count its entries.
2. If the append would take it past **~15 entries or ~40 lines of real content** — scaffolding, headings and comments do not count — then, in the same turn: create the new file in `~/Clawic/data/azure/`, move the whole section into it, **delete the section from `memory.md`**, add its line to `## Boxes`, and append the new entry to the new file.
3. Keep the headings identical on both sides of the move, so the split is a copy-paste and never a rewrite.
4. Never leave a copy behind. If the same data ever appears in both places, the extracted file wins and the `memory.md` copy is deleted.

Artifacts are the exception: a runbook, an address plan or a decision is born as its own file whatever its size, because it is read whole and only when its subject comes up.

## Secrets

Nothing under `~/Clawic/data/` ever holds a secret value — not the files named here, not files you create, not text the user pastes in and asks you to keep. Azure text is dense in them: a connection string, a `kubectl config`, a publish profile and a Terraform state excerpt all carry live credentials in the middle of otherwise useful content. Store the pointer in its place, in this shape: `<kind>:<locator>`.

`azure-kv:kv-prod/db-password` · `env:AZURE_CLIENT_SECRET` · `keychain:azure-prod` · `1password:Work/Azure/prod` · `vault:secret/azure/prod` · `file:~/.azure/msal_token_cache.json`

When the user pastes something to save, replace each secret value before writing and leave the pointer visible: `password: <azure-kv:kv-prod/db-password>`. Say in one line that you did it.

In this domain — **not secrets, keep them**: subscription IDs, tenant IDs, resource IDs and resource group names, application (client) IDs, object and principal IDs, managed identity names, role definition IDs, region names, storage account and Key Vault *names*, secret *names*, ACR login servers, address ranges. **Secrets, strip them**: client secrets, storage account keys, SAS tokens and any URL containing `sig=`, connection strings carrying `AccountKey`, `Password` or `SharedAccessKey`, Cosmos DB and Redis access keys, Service Bus and Event Hubs SAS policy keys, Function host and master keys, Application Insights connection strings and instrumentation keys, App Service publish profiles, kubeconfig admin certificates and tokens, PFX passwords, private keys, and the output of any `get-access-token` or `list-keys` call.

**Contents:** [config.yaml](#configyaml) · [memory.md](#memorymd) · [shared servers inventory](#shared-servers-inventory) · [shared domains inventory](#shared-domains-inventory) · [shared contacts](#shared-contacts) · [subscriptions.md](#subscriptionsmd) · [artifacts/](#artifacts) · [deploys/](#deploys) · [split-out files](#split-out-files)

## config.yaml

Keys come from the Configuration table in `SKILL.md`, plus free-form keys nested under a preference area. Write a key only when the user states the preference.

**Writing is read-modify-write**: load the existing file, set or replace only the key just declared, keep every other key byte for byte. Never emit a `config.yaml` from this template — the template shows shape, not content. Create `~/Clawic/data/azure/` if it does not exist.

```yaml
default_subscription: prod-platform
default_location: westeurope
iac_tool: bicep
monthly_budget: 250
tenancy_model: management-group
billing_model: mca
compliance_regime: none
cloud_environment: AzureCloud
naming_pattern: "<abbr>-<workload>-<env>-<region>-<nn>"

# Preference areas — free-form keys added as the user reveals them.
# A preference the user states is a declaration and belongs here, never in memory.md.
conventions:
  tags: [Environment, Workload, Owner, CostCenter]
  address_plan: "10.<env>.0.0/16, /24 subnets, hub 10.0.0.0/16"
platform:
  vm_families: [Dpdsv5]        # ARM64 standard
  paired_region: northeurope
safety_posture:
  destructive_commands: confirm-each
  locks: CanNotDelete on data resource groups
```

If you find a preference recorded in `memory.md`, move it here and note the move.

## memory.md

Write only the sections you have content for — a heading with nothing under it is noise, and it inflates the line count that decides a split. Never copy these hints into the user's file. `## Boxes` is the one section that is never dropped when `memory.md` is rewritten: deleting a line there orphans a file forever. This is what a populated file looks like:

```markdown
# Azure Memory

## Status
status: ongoing
last: 2026-07-26

## Boxes
- Spend history (14 months) → `spend-log.md`; read before any cost comparison
- Checkout latency runbook → `artifacts/runbook-checkout.md`; read the moment checkout is the symptom
- VNet address plan → `artifacts/address-plan.md`; read before creating any subnet, peering or gateway
- Subscriptions (3) → `subscriptions.md`; read before any billing, context-switch or cross-subscription question
- Deploys and restore drills → `deploys/2026.md`; read before a rollback or a DR question

## Due
| What | Every | Last run | Next due |
|------|-------|----------|----------|
| Cost review | month, day 15 | 2026-06-15 | 2026-07-15 |
| Restore drill (SQL PITR) | quarter | 2026-04-02 | 2026-07-02 |
| Access review (PIM eligible roles) | quarter | 2026-05-10 | 2026-08-10 |
| SP secret `sp-ci-deploy` expires | one-off | — | 2026-09-30 |
| Managed cert `app.example.com` renews | auto, verify | 2026-06-01 | 2026-08-01 |
| AKS 1.31 support ends | one-off | — | 2026-11-01 |
| Reservation term ends (D4s v5 ×3) | one-off | — | 2027-02-14 |

## Subscription Context
prod-platform (00000000-0000-0000-0000-000000000000), tenant contoso.onmicrosoft.com, MCA, two engineers, Bicep-managed, westeurope + northeurope pair.

## Current Infrastructure
Hub VNet 10.0.0.0/16 with NAT Gateway · spoke 10.1.0.0/16 · App Service P1v3 plan (2 apps, slots: staging) · Azure SQL GP serverless 2 vCore, zone-redundant off · Storage GRS behind private endpoints · Front Door Standard · Log Analytics workspace `log-platform-prod` with 30-day retention and a 5 GB/day cap.
Quotas: Dpdsv5 vCPU raised to 64 in westeurope (2026-05-11); zonal capacity for E-series unavailable in zone 3.

## Spend
### Monthly
| Month | Actual | As of | Budget | Top services | Notes |
|-------|--------|-------|--------|--------------|-------|
| 2026-06 | 412 EUR | 2026-06-30 | 500 EUR | App Service 130 · SQL 118 · Log Analytics 61 | closed |
| 2026-07 | 96 EUR | 2026-07-08 | 500 EUR | App Service 31 · SQL 28 · Log Analytics 14 | month-to-date |

### Alerts Configured
- Budget 500 EUR: alert at 80% actual, 100% forecast
- Anomaly alert: 17 EUR daily threshold

### Optimization Log
| Date | Change | Monthly saving |
|------|--------|----------------|
| 2026-05-11 | DCR transformation dropping AKS stdout debug rows | 48 EUR |

## Saved Queries
| Name | Where it runs | What it answers |
|------|---------------|-----------------|
| orphan-disks | Resource Graph | Managed disks with no owner VM, by resource group |
| slow-requests-p95 | Log Analytics | p95 duration per operation, last 24h |

## Pain Points
March 2026: 1,400 EUR month from AKS container stdout in Log Analytics. Sensitive to log cost since.

## How They Work
Strong on .NET and App Service, new to RBAC and networking. Wants the command, not the theory.

---
*Updated: 2026-07-26*
```

Rules that keep this readable next month:

- **`## Boxes`**: one line per file that exists — `<what> (<volume>) → <file>; read when <condition>`. Written in the same turn the file is created. Never delete a line without deleting the file it points to. A box with no index line does not exist.
- **`## Due`**: check it against today's date at the start of a session and state any overdue item in one line — a statement, not a question. Azure is unusually full of dated landmines: client secrets, certificates, reservation terms, AKS version support windows. Every one of them belongs here the moment it is created, with the real date, never "in a year".
- **`## Spend`**: `As of` is the day the number was read. A row whose `As of` is not the last day of the month is month-to-date and must never be compared against a closed month. Re-checking the current month **overwrites** its row; never a second row for the same month. Amounts always carry their currency. `Top services` is the top three, descending, always the same shape — it is what makes a six-month comparison possible without re-querying Cost Analysis.
- With `tenancy_model: management-group`, add a `Scope` column to `### Monthly`: one row for the billing-scope total, plus a row for any subscription above ~20% of it.
- **`## Saved Queries`**: name, where it runs (Log Analytics, Resource Graph, Cost Management), and what it answers. Keep the query text with the row; if a query grows past a handful of lines, it is an artifact — move it to `artifacts/query-<name>.md` and leave the row pointing at it.
- These headings are exactly the ones the split-out files get, so a split stays a copy-paste.

| Status | Meaning |
|-------|---------|
| `ongoing` | Still learning their estate |
| `complete` | Know their subscriptions and workflow well |

## Shared servers inventory

Lives at `~/Clawic/data/servers/servers.md` and is shared with every other infrastructure skill — the user may not have any of them installed, so the format travels with this skill.

```markdown
# Servers

| Name | Provider | Account / Project | Region | Type | Role | Monthly | Access reference |
|------|----------|-------------------|--------|------|------|---------|------------------|
| vm-api-prod-01 | azure | prod-platform / rg-api-prod | westeurope | D4ds_v5 | API | 148 EUR | keychain:azure-prod |
```

- **Identity is `Name` + `Provider`.** Read the file before adding. If that pair is already there, update the row in place — it is yours. The rule against rewriting protects rows whose `Provider` is not `azure`; never touch those.
- **Only real hosts.** VMs and VM scale sets (one row per scale set, with the instance count in `Role`). App Service plans, AKS clusters, SQL servers and storage accounts are not hosts — they go in `## Current Infrastructure`. AKS *node pools* are the exception worth a row when the user manages them as machines.
- **Retirement is part of the inventory.** When a host is deleted or deallocated for good, delete its row and note the date in `memory.md`. An inventory that only grows stops being an inventory.
- **Amounts carry their currency in the value** (`148 EUR`), because AWS rows next to yours are in USD and someone will add the column up.
- **`Monthly` is a planning estimate, not a bill.** Cost Analysis is the source of truth; after a cost review, refresh any Azure row whose real cost moved more than ~20%.
- **Scale cut**: one row per host while there are ≤15. Past that, one file per host at `~/Clawic/data/servers/<name>.md` with the same fields, and `servers.md` becomes the index (`Name | Provider | Role | → file`). If you arrive and the folder already looks like that, follow it — do not start a parallel `servers.md`.
- **Foreign columns win.** If `servers.md` already exists with a different column set, match its columns and add anything missing as a trailing note. Never rewrite its header.
- Access reference is a pointer only. Never a key, token, or password.

## Shared domains inventory

Lives at `~/Clawic/data/domains/domains.md`, shared with DNS, registrar and hosting skills. Azure touches it whenever a zone is hosted in Azure DNS, a custom domain is bound to App Service, Front Door or Container Apps, or a certificate is issued.

```markdown
# Domains

| Domain | Registrar | Expires | DNS hosted at | Points to | Certificate | Notes |
|--------|-----------|---------|---------------|-----------|-------------|-------|
| example.com | namecheap | 2027-03-04 | Azure DNS (rg-net-prod) | Front Door afd-prod | App Service managed, renews 2026-08-01 | apex via alias record |
```

- **Identity is the domain name.** Read before adding. If the domain is already there, update **only the cells this skill owns** — `DNS hosted at`, `Points to`, `Certificate`, and records you created. `Registrar` and `Expires` belong to whoever registered it; leave them alone rather than guessing.
- **Every date in this box also gets a `## Due` line** in `memory.md`, because a certificate that renews automatically still fails silently when the domain validation record is deleted. Dates are absolute (`2027-03-04`), never "in a year": the row outlives the session that wrote it.
- **Retirement is part of the inventory.** A domain transferred away, dropped or left to expire loses its row, with the date noted in `memory.md`, and every `## Due` line that pointed at it is deleted in the same turn — alerts about a domain the user no longer owns train them to ignore the whole table. When only the Azure side ended (zone deleted, custom domain unbound, certificate replaced), the domain still exists: blank the cells this skill owns and leave the row for its registrar.
- **Scale cut**: one table while it stays readable; past ~40 hostnames, group by apex — one `~/Clawic/data/domains/<apex>.md` per registered domain with the same fields, and `domains.md` left as the index (`Domain | Registrar | Expires | → file`). Follow the shape you find; never start a parallel `domains.md`.
- **Foreign columns win.** Match the header that exists; add anything missing as a trailing note.
- Never store a certificate, private key or PFX password here — the certificate cell says where it lives and when it expires, nothing more.

## Shared contacts

Lives at `~/Clawic/data/contacts/contacts.md`, shared with every skill that deals with people. Azure writes here when a subscription belongs to a client, or when an owner is a person rather than a team.

```markdown
# Contacts

| Name | Role | Preferred channel | Context |
|------|------|-------------------|---------|
| Marta Ruiz | Acme platform lead | marta@acme.example | owns the acme-delivery subscription; approves production changes |
```

- **Identity is the email or handle**, never the display name — two people share a name, nobody shares an inbox. Read the file before adding; if the address is already there, update in place and leave untouched every cell you did not learn yourself.
- **Only people the Azure work actually produced**: subscription owners, the client an engagement belongs to, whoever approves production changes. A name that appeared once in a ticket is not a contact.
- **Retirement**: when an engagement ends or the person leaves the account, delete the row if Azure work is the only reason it exists and note the date in `memory.md`; if other skills also write about them, strip the Azure sentence from `Context` and leave the row standing. A stale owner row is how an access review approves the wrong person.
- **Scale cut**: one table while there are ≤15 people; past that, one file per person at `~/Clawic/data/contacts/<name>.md` with the same fields, and `contacts.md` becomes the index. Follow the shape you find.
- **Foreign columns win.** If `contacts.md` already exists with a different column set, match its columns and add anything missing as a trailing note. Never rewrite its header.
- **The Azure boxes reference the person by name only** — subscriptions, artifacts and `memory.md` carry the name, never a copy of the record. Duplicating the person is the fastest way to make two skills contradict each other.
- Contact details only: an email or a handle is one, a portal login or a shared password is not, and nothing under `~/Clawic/data/` holds the second kind.

## subscriptions.md

One subscription lives in `## Subscription Context`. From the second, this file:

```markdown
# Azure Subscriptions

| Subscription | ID | Tenant | Purpose | Owner / client | Billing | Management group | Region |
|--------------|----|--------|---------|----------------|---------|------------------|--------|
| prod-platform | 0000…0000 | contoso | production SaaS | us | MCA, invoiced monthly | mg-prod | westeurope |
| acme-delivery | 1111…1111 | acme | Acme delivery work | Acme (see contacts) | CSP via partner | — | northeurope |
```

Record the tenant, not just the subscription: a subscription moved between tenants loses every role assignment and every system-assigned managed identity, so "which tenant" is the first question in half of all access incidents.

## artifacts/

One file per thing, at `~/Clawic/data/azure/artifacts/<kebab-name>.md`, created the first time it exists. Canonical types here: **runbook**, **custom role or Policy definition that finally worked**, **VNet address plan**, **architecture decision**, **migration cutover plan**, **postmortem**. Every artifact opens with when to read it, and gets its `## Boxes` line in the same turn.

```markdown
# Runbook — checkout latency spikes
*Read when: checkout p95 goes above 2s, or Front Door reports 504s. Written 2026-07-26.*

...steps, with every secret replaced by its pointer...
```

```markdown
# Address plan — contoso platform
*Read before creating any subnet, peering, gateway or private endpoint. 2026-07-26.*

Hub 10.0.0.0/16 — AzureFirewallSubnet 10.0.0.0/26, GatewaySubnet 10.0.1.0/27, shared 10.0.16.0/20
Spoke prod 10.1.0.0/16 — apps 10.1.0.0/22, data + private endpoints 10.1.8.0/22, AKS nodes 10.1.32.0/19
Reserved for the next spoke: 10.2.0.0/16. Never reuse: 10.9.0.0/16 (old on-prem VPN range).
Azure reserves 5 IPs per subnet; AKS sizing assumed max_pods 30.
```

```markdown
# Architecture decision — Container Apps, not AKS
*Read before any change to the request path, and before sizing anything. 2026-07-26.*

Decision: ...one sentence...
Diagram: ...mermaid or ASCII...
Rejected: AKS — 3 always-on containers, control plane plus node pool crossed the break-even the wrong way.
Estimated monthly: 210 EUR, westeurope.
First quota: 30 replicas per environment. First timeout: Front Door origin 60s.
```

If the user tracks this work as a project, the decision summary also belongs in the shared `~/Clawic/data/projects/<project>.md`, with the diagram staying here and referenced by name.

## deploys/

```markdown
# Deploys — 2026

| Date | Workload | Image digest / commit | Template version | Rollback target | Notes |
|------|----------|-----------------------|------------------|-----------------|-------|
| 2026-07-24 | api | sha256:9f2c… / a41b7e | bicep main@a41b7e | slot staging (previous swap) | — |

## Restore and Failover Drills
| Date | What was restored | Measured RTO | What was missing |
|------|-------------------|--------------|------------------|
| 2026-04-02 | SQL PITR → scratch server | 41 min | firewall rule, Key Vault access for the app identity |
```

## Split-out files

Created only by the split procedure above, never on day one. Each keeps the exact headings it had inside `memory.md`.

`spend-log.md` — `## Monthly`, `## Alerts Configured`, `## Optimization Log`. The optimization log is the reason this file exists: without it the same idle gateway gets rediscovered every quarter and nobody can say what the last cleanup was worth.

`resources.md` — the Azure-shaped inventory (`## Networking`, `## Compute`, `## Data`, `## Observability`, `## Quotas`, `## Known Gaps`), one `## <subscription-name>` heading per subscription when there is more than one.

`queries.md` — `## Saved Queries`, the same three columns, once the table passes the threshold or the query text starts dominating `memory.md`.
