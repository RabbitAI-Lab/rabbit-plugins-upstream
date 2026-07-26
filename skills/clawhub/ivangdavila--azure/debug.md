# Debugging Azure — Symptom to Cause

Azure errors are emitted by the layer that noticed, not the layer that is wrong: a DNS problem arrives as a connection timeout, a data-plane role problem arrives as `AuthorizationFailed`, a capacity problem arrives as a deployment failure. Work symptom-first.

**Contents:** [The Universal First Four](#the-universal-first-four) · [AuthorizationFailed](#authorizationfailed) · [Deployment Errors](#deployment-errors) · [Connectivity Failures](#connectivity-failures) · [HTTP Status Codes by Layer](#http-status-codes-by-layer) · [Throttling and 429](#throttling-and-429) · [Resource Vanished or Restarted](#resource-vanished-or-restarted) · [It Works in the Portal but Not in Code](#it-works-in-the-portal-but-not-in-code) · [When You Are Truly Stuck](#when-you-are-truly-stuck)

## The Universal First Four

1. **Who am I and where am I?** `az account show` — subscription and tenant. Half of "it worked yesterday" is a CLI context left where the last task put it.
2. **What did the control plane actually see?** The Activity Log records every write with the caller, the parameters, the status and a **correlation ID**. Find the failed operation and copy that ID before theorising; it links the deployment, the resource provider error and any Policy denial into one story.
3. **Control plane or data plane?** Did the *management* call fail (creating, listing, configuring) or the *usage* call (reading a blob, querying a database)? They have different roles, different logs, and different firewalls (`identity.md`).
4. **Is it me or is it Azure?** Service Health for the region and the subscription, and Resource Health for the specific resource. Rare, but it is the one cause you cannot fix — and Resource Health is where platform maintenance and host failures are recorded.

## AuthorizationFailed

The error text names the principal, the action and the scope. Read all three before doing anything.

| Detail in the message | Meaning | Next |
|---|---|---|
| Scope is a resource group you do not recognize | Wrong subscription context | `az account set` |
| Action is a `.../read` you know you have | Assignment is at a sibling scope, or the token predates it | Assignment list at `--all`; refresh the token |
| Action contains `/blobServices/`, `/secrets/`, `/dbs/` | Data-plane operation | Assign the data role, not Contributor (`identity.md`) |
| Message mentions a deny assignment | Platform-created deny — managed app, blueprint, deployment stack | Cannot be overridden by role; remove the source |
| Message names a policy assignment | Azure Policy `Deny`, not RBAC | `iac.md` — exempt or fix the resource |
| Principal is a GUID you cannot resolve | Deleted identity, usually a system-assigned managed identity whose resource was recreated | Reassign roles to the new principal |

## Deployment Errors

| Error | Cause | Fix |
|---|---|---|
| `MissingSubscriptionRegistration` | Resource provider not registered in **this** subscription | `az provider register --namespace Microsoft.X`; registration is per subscription and takes minutes |
| `SkuNotAvailable` | That size is not offered in that region/zone, or not for your subscription type | `az vm list-skus --location <region> --size <family> --all` shows restrictions and their reason |
| `AllocationFailed` / `ZonalAllocationFailed` | Physical capacity, not quota | Another zone, another size in the family, Flexible orchestration, or a different region |
| `QuotaExceeded` / `OperationNotAllowed` (vCPU) | Per-family regional quota | `az vm list-usage`, then request an increase; record the new ceiling in `## Current Infrastructure` |
| `ResourceGroupBeingDeleted` / `Conflict` | A prior delete has not finished, or a lock is present | Wait; check locks before assuming a race |
| `ResourceNameAlreadyExists` for a name you deleted | Soft delete — Key Vault, storage, App Service certificates and others hold the name | Purge it, or pick a new name; Key Vault holds names for 90 days |
| `InvalidTemplateDeployment` with a policy message | Policy `Deny` during pre-flight | The assignment name is in the message (`iac.md`) |
| `DeploymentQuotaExceeded` | 800 deployments of history in a resource group | Purge old deployment records; it fails deploys, not resources |
| `PropertyChangeNotAllowed` | You changed an immutable property | Redeploy as a new resource — this is the list in SKILL.md Rule 4 |
| `ReservedResourceName` / global uniqueness | Storage, Key Vault, ACR, App Service and Cosmos names are globally unique | Validate the name before the deployment, not inside it |

## Connectivity Failures

Timeout with no reset means routing, DNS or SNAT. A connection refused or a TLS error means you reached something.

1. Resolve the FQDN **from the source subnet**. A public IP for a Private Link name is the whole answer (`networking.md`).
2. Effective NSG rules and effective routes on the source NIC.
3. The destination service's firewall: Storage, SQL, Key Vault and Cosmos each have "selected networks" settings that exclude everything unlisted.
4. Health probes: if a load balancer is in the path, the backend health blade tells you more than any packet capture.
5. Intermittent only under load → SNAT exhaustion (`networking.md`).
6. On-prem involved → route advertisement and overlapping address space.

Database-specific: `Connection timed out` is network; `Login failed for user` or `password authentication failed` is credentials or the Entra login mapping; `Cannot open server ... requested by the login` on Azure SQL is the server firewall.

## HTTP Status Codes by Layer

| Code and context | Emitted by | Meaning |
|---|---|---|
| Request dies at ~230s | App Service front end | The platform idle limit; not configurable (`appservice.md`) |
| 502.5 in an App Service response body | The platform, about your process | Process failed to start or crashed — startup command, port binding, missing runtime |
| 502 from Application Gateway | Gateway, about the backend | Probe failing, host-name mismatch, backend NSG, or backend TLS certificate |
| 503 from Application Gateway or Load Balancer | No healthy backends | Backend health blade first |
| 504 from Front Door | Origin slower than the origin timeout | Fix the slow path before raising the timeout |
| 403 from Front Door or App Gateway with a WAF reference | A managed rule matched | Find the rule ID in the WAF logs; tune, do not disable the ruleset |
| 403 from a storage or Key Vault endpoint | The service firewall or a missing data role | The message distinguishes them: network messages name the rule set |
| 409 on a create | Name in use, soft-deleted, or a concurrent operation | See deployment errors above |

## Throttling and 429

Azure throttles on two axes: resource capacity, and control-plane API rate.

- **Cosmos DB 429** — the request cost exceeded provisioned RU/s for that partition. Read the `x-ms-request-charge` on the expensive query and `x-ms-retry-after-ms`. Fixing the query or the indexing policy is cheaper than raising RU/s (`databases.md`).
- **Storage 503 / `ServerBusy`** — the account-level request-rate ceiling, not the container's. Spread across accounts or partitions; the SDK's retry policy handles bursts.
- **ARM control-plane throttling** — a script polling `az` in a loop hits per-subscription read limits. Use Resource Graph for inventory reads instead of iterating resources (`commands.md`).
- **Entra ID throttling** on Graph calls during bulk operations — batch and respect `Retry-After`.
- Universal shape: exponential backoff with jitter, and honour the header the service returned. A retry loop with a fixed delay converts throttling into an outage.

## Resource Vanished or Restarted

| Symptom | Cause | Where it is recorded |
|---|---|---|
| VM rebooted, no deployment | Platform maintenance or host failure | Resource Health; Scheduled Events via IMDS gives advance notice (`vms.md`) |
| VM disappeared ~30 seconds after a notice | Spot eviction | Eviction policy: deallocate keeps the disk, delete does not |
| Resource deleted, nobody admits it | Activity Log, `Delete` operations, last 90 days | Add a `CanNotDelete` lock afterwards |
| App restarted at 3am | App Service platform update, or an idle unload with Always On off | App Service diagnostics |
| Function stopped firing silently | Its storage account became unreachable, or keys rotated | The function host state lives there (`functions.md`) |
| AKS nodes replaced | Node image upgrade or autoscaler | Cluster upgrade history |

## It Works in the Portal but Not in Code

| Difference | Why |
|---|---|
| Different identity | The portal uses your user; the code uses a managed identity or service principal with different roles |
| Different plane | The portal often reads keys on your behalf; code without the data role cannot |
| Different network path | Your laptop is on an allowed IP; the workload is not, or vice versa with a private endpoint |
| Different subscription | The portal remembers a filter; the SDK reads its own configuration |
| Different API version | The portal uses the newest; an old SDK sends an older version that lacks the property |
| Different tenant | Guest access in the portal, home tenant in the token |

## When You Are Truly Stuck

Cut the problem in half from the same network position and the same identity: deploy a throwaway VM or container **in the same subnet, with the same managed identity**, and make the single failing call. Works there → the difference is your application's configuration. Fails there → the difference is identity or network, and you have halved the search space.

**When a non-obvious cause is finally found, write it down**: one line in `## Pain Points` in `~/Clawic/data/azure/memory.md` if it is a tendency worth remembering, or `~/Clawic/data/azure/artifacts/runbook-<symptom>.md` with its `## Boxes` line if it took steps someone will need again (`memory-template.md`). The second occurrence of the same outage should cost minutes.
