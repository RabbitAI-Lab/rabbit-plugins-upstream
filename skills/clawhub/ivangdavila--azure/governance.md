# Governance — Tenants, Subscriptions, Tags and Quotas

Applies when `tenancy_model` is `management-group`, and describes what a single-subscription setup is choosing not to have. The decision matters early: **moving live resources between subscriptions is a migration project, and moving a subscription between tenants destroys every access grant in it.**

**Contents:** [The Hierarchy](#the-hierarchy) · [When One Subscription Stops Being Enough](#when-one-subscription-stops-being-enough) · [A Layout That Ages Well](#a-layout-that-ages-well) · [Billing Models](#billing-models) · [Tags and Cost Attribution](#tags-and-cost-attribution) · [Naming](#naming) · [Quotas and Limits](#quotas-and-limits) · [Moving Things](#moving-things) · [Landing Zones](#landing-zones) · [Hybrid and Multi-Cloud Estate](#hybrid-and-multi-cloud-estate)

## The Hierarchy

| Level | What it is | What it bounds |
|---|---|---|
| Tenant (Entra ID directory) | The identity boundary | Users, groups, applications; a subscription belongs to exactly one |
| Management group | A grouping of subscriptions, nested several levels deep | Policy, RBAC and budget inheritance |
| Subscription | The billing and quota boundary | Quotas, limits, most policy scope, the hard blast-radius boundary |
| Resource group | A lifecycle container | Deployment, deletion, RBAC scope — **not** a network or security boundary |
| Resource | The thing | Its own RBAC, locks, tags |

Everything inherits downward and nothing inherits upward. A role assigned at a resource group never covers a sibling group; a policy assigned at a management group covers everything beneath it forever.

The root management group exists whether or not anyone uses it. Assigning policy there affects every subscription in the tenant, including ones created next year — which is exactly why the baseline belongs there and experiments do not.

## When One Subscription Stops Being Enough

Any one of these is sufficient reason to split:

- More than one person can touch production, and you want production and development separated by something stronger than a tag and good intentions.
- A compliance regime (`compliance_regime` other than `none`) that requires demonstrable isolation.
- Quotas: they are **per subscription per region per family**. A runaway development workload can consume the vCPU headroom production needed.
- Cost attribution that tags cannot deliver, because someone always forgets a tag and nobody forgets which subscription they deployed to.
- A client engagement whose costs must be invoiced separately, or whose data must be separable on exit.
- A subscription-level limit you are approaching (role assignments, resource groups, private endpoints).

Against splitting: every subscription multiplies shared resources, policy assignments, network plumbing and the operational surface. Two subscriptions is a decision; twelve is a platform team.

## A Layout That Ages Well

```
Tenant root
├── Platform            (identity, management, connectivity subscriptions)
├── Landing zones
│   ├── Corp            (internal workloads, private only)
│   └── Online          (internet-facing workloads)
├── Sandbox             (permissive policy, hard budget, no connectivity)
└── Decommissioned      (blocked from new resources, awaiting deletion)
```

- Policy baselines attach at Landing zones; exceptions attach lower, with an expiry.
- Sandbox gets a budget with a hard alert and no peering to anything real. It is the pressure valve that stops people building production in the wrong place.
- Decommissioned is where subscriptions go before they are cancelled — with a deny-everything policy and their data still restorable.
- Keep the hierarchy shallow. Depth makes inheritance hard to reason about, and reasoning about inheritance is the entire point.

## Billing Models

| Model | Structure | Practical consequence |
|---|---|---|
| Pay-as-you-go | Subscription pays list price | Simplest; budgets and reservations at subscription scope |
| Microsoft Customer Agreement | Billing account → profiles → invoice sections | Negotiated prices; budget and reservation scope moves up |
| Enterprise Agreement | Enrolment with a prepaid commitment | Overage vs balance is invisible from the subscription; enterprise admins hold the levers |
| Cloud Solution Provider | A partner owns the billing relationship | The partner's portal is authoritative; customers often cannot see true cost |
| Dev/Test | Discounted rates, no licence charges | No SLA, restricted SKUs — never production |

Record which one applies in `## Subscription Context` or the subscriptions table (`memory-template.md`): it determines where cost data lives, who can buy a reservation, and whether the numbers in Cost Management match the invoice (`costs.md`).

## Tags and Cost Attribution

- **Azure does not inherit tags.** A resource does not receive its resource group's tags unless a Policy `Modify` rule puts them there, and that rule only fixes existing resources when a remediation task runs (`iac.md`).
- Minimum set: `Environment`, `Workload`, `Owner`, `CostCenter`. Anything beyond four required tags gets dropped by humans and blocked by `Deny`, which makes deployments fail for a reporting reason.
- Cost allocation reports from tags forward. An untagged month cannot be attributed retroactively — which is why tagging is a day-one task (SKILL.md Rule 6).
- Not every resource type supports tags, and some child resources never appear in cost reports under their own tags. Resource group and subscription remain the reliable grouping dimensions.
- Cost Management allocation rules can distribute shared costs (a hub firewall, a shared cluster) across consuming subscriptions — the honest answer to "the platform team's bill is enormous".

## Naming

- Pattern comes from `naming_pattern` (config); the default is a CAF-style `<abbr>-<workload>-<env>-<region>-<nn>`.
- The value is not aesthetic: consistent names make Resource Graph queries, cost filters, access reviews and Policy conditions possible. Inconsistent names make all four manual.
- Constraints differ by type — storage accounts and Key Vaults are the tightest (short, restricted character sets, globally unique). A naming convention that ignores them breaks on the first storage account.
- Names cannot be changed. Renaming means recreating, which for most stateful resources is a migration.

## Quotas and Limits

- **Quotas** are adjustable ceilings, per subscription per region (usually per VM family). Most are self-service; some need a support request; regional capacity may not exist at any quota level (`vms.md`).
- **Limits** are structural and mostly unadjustable: about 980 resource groups per subscription, 800 resources per type per resource group, 800 deployments of history per resource group, 4,000 role assignments per subscription, 5 management-group levels below root.
- Private endpoints, public IPs, network interfaces and Key Vault operations all have their own per-subscription ceilings that estates reach quietly.
- Check before designing, not during the incident: `az vm list-usage` for compute, the Quotas blade for the rest, Resource Graph for counting what exists.
- **Write any raised quota and any hard limit you approached into `## Current Infrastructure`** with the date — the next design needs the number, and rediscovering it costs a support ticket (`memory-template.md`).

## Moving Things

- **Between resource groups or subscriptions**: supported for many resource types, not all. Both source and destination are locked during the move, and some resources (with peerings, certificates, locks, or a child dependency elsewhere) refuse. Validate the move first; the validation API lists the blockers.
- Moving does **not** change the region. A resource in the wrong region has to be recreated.
- Role assignments do not follow a resource across a subscription move; recreate them at the destination.
- **Between tenants** is the dangerous one: transferring a subscription to another tenant removes every role assignment and every system-assigned managed identity in it. Workloads keep running until their tokens expire, then fail as identities that no longer exist. Take an access inventory first, plan a reassignment, and expect an outage window (`identity.md`).
- Cancelling a subscription is reversible for a limited period, after which resources are deleted permanently. Move anything worth keeping first, and prefer parking it in a Decommissioned group.

## Landing Zones

- The accelerator deploys the hierarchy, policy baseline, connectivity and identity subscriptions in one go. It is a good starting point and a bad thing to fork without understanding.
- Whatever creates subscriptions must also apply the baseline: diagnostic settings to a central workspace, Defender plans, policy assignments, budget, tags, the standard roles, and network connectivity. A subscription created without its baseline is the one that appears in the next audit.
- Subscription vending (a pipeline that creates subscriptions with their baseline attached) is the mature form of this, and worth building once the count passes a handful.
- Start smaller than the reference architecture if the estate is small. A two-level management group hierarchy with a real policy baseline beats a six-level one nobody maintains.

## Hybrid and Multi-Cloud Estate

- **Azure Arc** projects servers, Kubernetes clusters and some data services from on-prem or another cloud into Azure's control plane: they get Policy, Update Manager, Defender and Monitor without moving. Correct when the workload cannot move and consistency matters; it is a management plane, not a migration.
- Arc-enabled servers appear as resources, so they inherit tags, policy and cost visibility — and they belong in `~/Clawic/data/servers/servers.md` like any other host, with their real provider recorded rather than `azure`.
- Multi-cloud estates should keep one inventory, which is exactly why the servers box is shared across cloud skills (`memory-template.md`).

**Record the subscription → tenant → purpose → owner → billing mapping** (`memory-template.md`): with one subscription it lives in `## Subscription Context`, from the second it is `~/Clawic/data/azure/subscriptions.md` with its `## Boxes` line. Per-subscription budgets are unactionable if nobody can say whose subscription it is. When a subscription belongs to a client, the client goes in the shared `~/Clawic/data/contacts/contacts.md` and is referenced here by name only.
