# Cost Control

Prices: West Europe, pay-as-you-go, recorded early 2026. The **ratios and break-evens are stable**; verify the absolute number on the pricing calculator before committing money. Every threshold below scales with `monthly_budget`.

**Contents:** [Where the Money Is Visible](#where-the-money-is-visible) · [Alarms Before Resources](#alarms-before-resources) · [Diagnosing a Surprise Bill](#diagnosing-a-surprise-bill) · [The Fixed-Cost Resources](#the-fixed-cost-resources) · [The Ten Biggest Line Items](#the-ten-biggest-line-items) · [Discounts, In the Order They Pay Off](#discounts-in-the-order-they-pay-off) · [Storage and Log Economics](#storage-and-log-economics) · [Monthly Review Checklist](#monthly-review-checklist)

**Before answering any spend question**, read `## Spend` in `~/Clawic/data/azure/memory.md` — or `spend-log.md` if the `## Boxes` index points there. A current-month number with no prior months is not an answer.

**After any bill review or saving**, write it back in the same turn: the month row with its `As of` date, the top three services, and any optimization (`memory-template.md`).

## Where the Money Is Visible

`billing_model` decides which of these exists and who may use it. Getting this wrong wastes an hour before the first number appears.

| Model | Cost data | Budgets | Reservations bought by | Notes |
|---|---|---|---|---|
| `payg` | Cost Management on the subscription | Anyone with Cost Management Contributor | Subscription owner | Simplest; list price |
| `mca` | Cost Management at billing profile / invoice section | Billing profile roles, plus subscription scope | Billing profile owner | Negotiated prices show up here, not on the pricing page |
| `ea` | Cost Management, but the enrolment portal holds the commitment balance | Enterprise admins for the enrolment, subscription owners below | Enterprise admin | Overage vs prepaid balance is invisible from a subscription scope |
| `csp` | Partner's portal is authoritative; Cost Management shows partner-set prices | Often disabled for the customer | Partner | If the numbers disagree with the invoice, the partner's margin is the difference |
| `devtest` | As payg | As payg | Limited SKUs | No Windows/SQL licence charge; no SLA — never production |

Cost Management data lags: figures settle within a day or two, and the current month is always incomplete. Compare closed months to closed months, and mark month-to-date rows as such.

## Alarms Before Resources

Order matters — the anomaly alert needs somewhere to send, and the budget needs a scope.

1. **Budget** at the subscription (or resource group, for a client workload): amount `monthly_budget`, with alerts at 80% actual and 100% forecast. Forecast alerts are the ones that fire early enough to matter; actual-only alerts arrive after the money is spent.
2. **Anomaly alert** on the subscription, threshold ≈ `monthly_budget ÷ 30`. A monthly-sized threshold never fires, because anomaly detection compares against daily spend. Worked example: 300/mo budget → 10/day threshold, not 300.
3. **Tag enforcement** before the first workload, because tagging later never backfills (SKILL.md Rule 6). A Policy `Modify` rule that inherits `Environment`, `Workload`, `Owner` and `CostCenter` from the resource group, plus a remediation task for what already exists (`iac.md`).
4. **Log Analytics daily cap** at a number you picked deliberately, not the default of none. An uncapped workspace is the single most common way an Azure bill triples in a week.

Record what you created in `### Alerts Configured` and the cadence in `## Due`.

## Diagnosing a Surprise Bill

Work top-down; each step halves the search space.

1. **Cost Analysis, group by service, last 30 days, daily granularity.** The day the line steps up is the day something was deployed or a switch was flipped. Note the date before looking at anything else.
2. **Group by resource** within the guilty service. Azure charges are per resource, so this names the object.
3. **Group by meter** on that resource. This is the step people skip, and it is the one that distinguishes "the VM is expensive" from "the VM's premium disk is expensive" or "egress from that VM is expensive".
4. **Match the date to a change.** Deploys in `deploys/<year>.md`, the Activity Log for that resource group, and the tenant's change history.
5. **Then quantify the fix** in monthly terms and write it to `### Optimization Log` with the number.

Classic causes, in the order they appear: a gateway or firewall left running after a test; Log Analytics ingestion after someone raised a log level; a Cosmos DB container provisioned at a floor nobody revisited; a Premium disk chosen by the portal default; egress from a chatty cross-region pattern; a forgotten dev environment scaled like production.

## The Fixed-Cost Resources

Azure's expensive resources bill by the hour whether or not they are used. These are the ones that show up on a bill nobody can explain, because none of them appear in application metrics.

| Resource | Order of magnitude | When it is genuinely required |
|---|---|---|
| Azure Firewall Standard | ~1.25/hr + data processing | Centralized egress filtering with FQDN rules across many spokes; regulated estates |
| Azure Firewall Basic | ~0.4/hr | Small estates that still need the control, not the throughput |
| Application Gateway v2 (+WAF) | ~0.25/hr fixed + capacity units | Regional L7 with WAF and backend autoscaling |
| Front Door Standard / Premium | ~35/mo vs ~330/mo base | Premium only for Private Link origins and the full managed rule set |
| VPN Gateway (VpnGw1) | ~0.19/hr | Site-to-site or point-to-site connectivity |
| Bastion (Basic) | ~0.19/hr | Continuous admin access; the Developer SKU or just-in-time covers occasional use |
| NAT Gateway | ~0.045/hr + per GB | Any subnet with outbound traffic and SNAT pressure — cheap, and now usually mandatory (`networking.md`) |
| Private endpoint | ~0.01/hr each + per GB | Per endpoint, and estates accumulate dozens without noticing |
| AKS Standard control plane | ~0.10/hr | The uptime SLA; the Free tier has none |

Rule of thumb: any hourly resource in a non-production environment gets a shutdown schedule or does not get created.

## The Ten Biggest Line Items

| Driver | Why it bites | Fix |
|---|---|---|
| Log Analytics ingestion | Per-GB and an order of magnitude above storage; AKS stdout, App Gateway access logs and verbose app logs dominate | Daily cap, Basic Logs for high-volume low-query tables, DCR transformation dropping columns at ingest (`monitoring.md`) |
| VM compute at list price | Reservations and savings plans go unused for months | Right-size first, then commit (below) |
| Premium disks by default | The portal preselects Premium SSD; most dev disks never approach the IOPS | Standard SSD for dev, Premium SSD v2 where IOPS is the real requirement (`vms.md`) |
| Orphaned disks, NICs, public IPs | A deleted VM leaves them behind unless delete-with-VM was set | Monthly sweep; a Resource Graph query finds all three in seconds (`commands.md`) |
| Cosmos DB provisioned throughput | Bills at the floor forever, and default indexing charges write RU on every path | Serverless for bursty; autoscale floors at 10% of max and bills 1.5× the manual rate per RU (`databases.md`) |
| SQL over-provisioned | GP vCore is billed per vCore-hour whether idle or not | Serverless with auto-pause for dev and spiky prod; elastic pool for many small databases |
| Egress and peering traffic | Inter-region egress bills, and peering bills on both sides | Co-locate chatty pairs; Private Link instead of a chatty peer; CDN for public assets |
| Idle App Service plans | The plan bills, not the app; an empty plan costs the same as a busy one | Consolidate apps onto one plan per scaling profile; delete empty plans |
| Backup and snapshot sprawl | Vault storage grows monotonically; nobody deletes old restore points | Retention that matches the agreed RPO, reviewed in the monthly checklist (`production.md`) |
| Non-production running 24/7 | Dev environments cost the same per hour as production | Auto-shutdown on VMs, scale-down schedules on plans and clusters, dev/test pricing where eligible |

## Discounts, In the Order They Pay Off

Applied in the wrong order, each one locks in waste.

1. **Delete what nobody uses.** Free, instant, and it shrinks every subsequent commitment.
2. **Right-size.** SKILL.md Rule 3. Two weeks of observation, then act.
3. **Azure Hybrid Benefit** if Windows Server or SQL Server licences with Software Assurance exist. This is often the largest single lever on a Windows estate and costs nothing to apply.
4. **Dev/test subscriptions** for non-production, where the organization is eligible.
5. **Savings plan for compute** — flexes across VM series and regions, smaller discount. Correct when the fleet churns.
6. **Reservations** — deeper discount, locked to a SKU family and region (with instance-size flexibility inside a family). Correct when the shape is stable.
7. **Capacity commitments** on Log Analytics once ingestion is steady above the first commitment tier.

Two rules that save the most pain: commit only to the *floor* of your usage, not the average; and put every term end date in `## Due` the day it is bought, along with whether auto-renew is on. A reservation that lapses unnoticed returns the whole fleet to list price, and the bill moves before anyone reads an email.

## Storage and Log Economics

- **Blob tiers have minimum retention**: cool 30 days, cold 90, archive 180. Moving a blob down and deleting it early costs the remainder of the minimum as an early-deletion fee, so lifecycle rules that shuffle short-lived data cost more than doing nothing. Lifecycle management is for data with a known, long shape (`storage.md`).
- **Archive rehydration takes hours** and costs per GB read. Archive is for data you accept waiting for, not cheap cold storage.
- **Redundancy multiplies everything**: GRS is roughly double LRS, and ZRS sits between. Pick per-container purpose, not per-account habit — logs rarely need geo-redundancy.
- **Log Analytics retention** includes an initial free period per table, then bills per GB-month; archive tier is far cheaper but query needs a restore or a search job. Set retention per table, not workspace-wide: audit tables long, chatty telemetry short.
- **Application Insights bills through its workspace.** Adaptive sampling is on by default in most SDKs — cheaper, and the reason intermittent errors vanish from the data (`monitoring.md`).

## Monthly Review Checklist

Run it on `cost_review_day` (config), or the 15th by default.

| Check | Action |
|---|---|
| Cost Analysis, last two closed months, grouped by service | Anything up more than ~20% gets a resource-level look |
| Unattached disks, idle public IPs, empty App Service plans, NICs with no owner | Delete; a Resource Graph query lists all of them |
| Hourly resources in non-production | Schedule or delete |
| Log Analytics ingestion by table | Cap, downgrade to Basic Logs, or transform at ingest |
| Reservation and savings plan utilization | Below ~95% utilization means over-committed; large uncovered steady spend means under-committed |
| Reservation and secret expiry dates | Confirm each against `## Due` |
| Advisor cost recommendations | Triage; dismiss with a reason rather than leaving them to rot |
| Untagged spend | Anything unattributable is next month's argument — fix the Policy and run remediation (SKILL.md Rule 6) |

Record the date this ran in the `## Due` table of `memory.md`, and the month row in `## Spend`. A checklist with no last-run date gets skipped for a quarter and nobody notices.
