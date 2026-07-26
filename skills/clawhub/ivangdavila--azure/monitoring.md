# Monitoring — Azure Monitor, Log Analytics, KQL and Alerts

Azure collects almost nothing about your workload by default, and everything it does collect can be expensive. Both halves of this file exist because of that: turn on what matters, and stop paying for what does not.

**Contents:** [What Exists Without You](#what-exists-without-you) · [Diagnostic Settings](#diagnostic-settings) · [Metrics vs Logs](#metrics-vs-logs) · [Application Insights and Sampling](#application-insights-and-sampling) · [Controlling Ingestion Cost](#controlling-ingestion-cost) · [KQL That Earns Its Keep](#kql-that-earns-its-keep) · [Alerts That Fire When They Should](#alerts-that-fire-when-they-should) · [Resource Graph for Inventory](#resource-graph-for-inventory) · [Dashboards and Workbooks](#dashboards-and-workbooks)

**Before writing a query, read `## Saved Queries` in `~/Clawic/data/azure/memory.md`** (or `queries.md` if `## Boxes` points there) — the question has often been asked before, and the earlier query already knows the table names and the workspace.

**After a query answers something worth asking again, save it**: name, where it runs, what it answers, and the query text, in `## Saved Queries` (`memory-template.md`). Queries longer than a few lines become `artifacts/query-<name>.md` with a `## Boxes` line.

## What Exists Without You

| Signal | On by default | Retention | Note |
|---|---|---|---|
| Platform metrics | Yes | About 3 months | Free, per-minute, no configuration |
| Activity Log (control plane) | Yes | About 90 days | Every write, with caller and correlation ID |
| Resource logs (data plane) | **No** | — | Requires a diagnostic setting per resource |
| Guest OS metrics (memory, disk) | **No** | — | Requires the Azure Monitor agent |
| Application telemetry | **No** | — | Requires Application Insights instrumentation |
| Service Health | Yes | — | Alerts must be created |

The gap that catches teams: "we have monitoring" usually means platform metrics only, which cannot tell you why a request was slow, who deleted the resource group, or whether memory is exhausted.

## Diagnostic Settings

- One setting per resource (or per resource type via Policy `DeployIfNotExists`), routing selected log categories and metrics to a destination.
- **Destinations have different economics**: Log Analytics for querying and alerting; a storage account for cheap long retention; Event Hubs for streaming to another system. Sending everything everywhere triples the cost of the noisiest tables.
- Deploy them with Policy, not by hand. A resource created next month without a diagnostic setting is invisible in exactly the incident where it matters.
- Categories worth enabling almost always: Activity Log to the workspace, Key Vault audit events, App Gateway/Front Door access and WAF logs, SQL errors and timeouts, storage read/write for accounts holding sensitive data.
- Categories to think twice about: full request logging on high-traffic gateways, verbose SQL query store telemetry, everything from a chatty AKS namespace.

## Metrics vs Logs

| | Metrics | Logs |
|---|---|---|
| Shape | Numeric time series, pre-aggregated | Rows with structure, queried with KQL |
| Latency | Near-real-time | Seconds to minutes of ingestion delay |
| Cost | Free for platform metrics | Per GB ingested and retained |
| Alerting | Fast, cheap, evaluated frequently | Flexible, slower, priced per rule and query |
| Use for | Saturation, availability, throughput thresholds | Correlation, root cause, anything needing text |

The practical rule: **alert on metrics, investigate in logs**. A log alert that could have been a metric alert is slower, costlier and easier to break.

## Application Insights and Sampling

- Workspace-based: its data lives in a Log Analytics workspace and bills at that workspace's rate.
- **Adaptive sampling is on by default in most SDKs.** It keeps volume bounded by discarding a proportion of telemetry, preserving statistical accuracy for aggregate metrics — and it is the reason a specific intermittent error cannot be found. Item counts are scaled at query time, so counts stay roughly right even when individual traces are gone.
- When hunting a rare failure, raise the sampling rate temporarily and put a reminder to lower it in `## Due`. Leaving it at 100% on a busy app is a line item.
- Live Metrics is unsampled and free of ingestion cost — the right tool during a deploy.
- Distributed tracing across services only works when every hop propagates the correlation headers; a single service that drops them severs the trace and looks like the failure.
- Availability tests from multiple regions cost almost nothing and catch DNS, certificate and regional failures that internal monitoring cannot see.

## Controlling Ingestion Cost

In order of yield:

1. **Find the top tables.** A single query over the usage table names the guilty ones in seconds; on most estates it is AKS container stdout, gateway access logs, or a chatty application logger.
2. **Fix the source.** A log level set to debug in production is a configuration change, not a monitoring problem.
3. **Transform at ingest.** A data collection rule can drop columns and filter rows *before* billing — the highest-value control available, and the one nobody knows exists.
4. **Table-level tiers and retention.** Basic Logs for high-volume, rarely-queried tables (cheaper ingestion, restricted query, shorter retention); long retention only for tables with a compliance reason.
5. **Daily cap.** A blunt instrument that stops the bleeding: data past the cap is dropped, so set an alert on hitting the cap too.
6. **Commitment tiers** once steady ingestion clears the first tier threshold.

Record any change and its measured monthly saving in `### Optimization Log` (`costs.md`).

## KQL That Earns Its Keep

Shape of an efficient query: **filter by time first, then by the most selective column, then project, then aggregate.**

```kusto
requests
| where timestamp > ago(24h)
| where success == false
| summarize count(), p95 = percentile(duration, 95) by name, resultCode
| order by count_ desc
```

- `ago()` on the timestamp column first — the time filter is what prunes the data actually scanned.
- `search` and `union *` across all tables are convenient and expensive; name the table.
- `summarize ... by bin(timestamp, 5m)` is the standard shape for a time series.
- `join` defaults to inner and is memory-bound; put the smaller table on the left and consider `lookup` for dimension tables.
- `materialize()` a subquery used more than once in the same statement.
- `parse` and `extract` on unstructured messages work but scan text; if you need a field often, emit it as a structured property instead.
- Cross-resource queries (`workspace()`, `app()`) work across a bounded number of resources — beyond that, consolidate workspaces.
- Query timeouts exist (on the order of ten minutes); a query that times out needs a tighter time filter before anything else.

## Alerts That Fire When They Should

| Type | Evaluation | Right for |
|---|---|---|
| Metric alert | Frequent, near-real-time | Saturation, error rate, availability, resource health |
| Log search alert | Scheduled, minimum frequency measured in minutes, priced per rule | Anything needing correlation or text matching |
| Activity Log alert | Event-driven | Deletions, role assignments, policy changes, service health |
| Smart detection / anomaly | Automatic | Cheap early warning, not a paging signal |

- **Alert on symptoms users feel** (error rate, latency, queue age), not on causes (CPU). A CPU alert on an I/O-bound app never fires; a latency alert always does.
- **Absence of data is a failure mode.** A metric that stops publishing looks healthy to a threshold rule — configure how missing data is treated deliberately, and add a heartbeat alert for anything whose silence would be indistinguishable from health.
- Dynamic thresholds are useful for seasonal metrics and dangerous for metrics with a hard SLO. Use a static threshold where the number is contractual.
- **Action groups** have documented rate limits per group — roughly one SMS and one voice call per five minutes per recipient, and email in the low hundreds per hour. An alert storm silently drops notifications, which is why a single noisy rule can hide a real one.
- Alert processing rules suppress notifications during a known maintenance window without disabling the rules and forgetting to re-enable them.
- Queue depth, poison-queue length and dead-letter count deserve alerts on every event-driven design; they are the failure modes with no error page (`functions.md`).
- Every alert needs an owner and a runbook link. An alert nobody acts on trains the team to ignore the channel.

## Resource Graph for Inventory

Resource Graph queries ARM metadata across every subscription in seconds, with KQL. It is the correct tool for inventory (SKILL.md Rule 1) and for finding waste, and it does not hit per-subscription API throttling the way iterating resources does.

Questions it answers instantly: every resource by type and location; VMs by size and power state; unattached disks; public IPs with no owner; storage accounts allowing public network access; NSG rules with an `Internet` source on admin ports; resources missing a required tag; Kubernetes clusters and their versions.

Results feed straight into `## Current Infrastructure`, and the queries themselves into `## Saved Queries` (`commands.md` has the invocation details).

## Dashboards and Workbooks

- **Workbooks** are the durable artifact: parameterized, versioned as JSON, shareable, and they mix metrics, logs and Resource Graph in one document. Anything a human reads more than twice belongs in one.
- Portal dashboards are per-user unless published, and they rot silently when resources are recreated.
- Azure Managed Grafana is the answer when the organization already lives in Grafana; it queries Azure Monitor as a data source and avoids maintaining two truths.
- A workbook the user relies on is a durable artifact: record what it answers and where it lives in `## Boxes`, so it is not rebuilt from scratch next quarter (`memory-template.md`).
