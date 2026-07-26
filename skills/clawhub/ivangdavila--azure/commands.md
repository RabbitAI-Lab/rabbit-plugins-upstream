# The az Toolkit

Reference for the invocations that come up constantly. Every example assumes `default_subscription` and `default_location` from config; where neither is set, name the assumed values before running anything (SKILL.md Rule 7).

**Contents:** [Context and Login](#context-and-login) · [Output and Filtering](#output-and-filtering) · [Resource Graph](#resource-graph) · [Inventory Recipes](#inventory-recipes) · [Cost](#cost) · [Deployment](#deployment) · [Identity](#identity) · [Diagnostics](#diagnostics) · [Long Operations and Scripting](#long-operations-and-scripting) · [Extensions and Versions](#extensions-and-versions)

## Context and Login

```bash
az login                                  # device code: az login --use-device-code
az account show --output table            # who and where — run this before believing anything
az account list --output table
az account set --subscription "prod-platform"
az configure --defaults location=westeurope group=rg-app-prod
```

- Context is machine-wide and persists across sessions. The most expensive Azure mistake is a correct command in the wrong subscription.
- Multiple tenants: `az login --tenant <tenant-id>`, and `az account list --all` to see subscriptions across them.
- Service principal login for automation prefers federated credentials in CI over `--password` (`identity.md`).
- Sovereign clouds: `az cloud set --name AzureUSGovernment` before login, matching `cloud_environment`.

## Output and Filtering

```bash
az vm list --output table
az vm list --query "[?powerState=='VM running'].{name:name, size:hardwareProfile.vmSize, rg:resourceGroup}" -o table
az vm list --query "[].name" -o tsv | while read -r name; do echo "$name"; done
```

- `--query` is JMESPath, applied client-side after the response. It filters output, not the API call.
- `-o table` for humans, `-o tsv` for shell loops, `-o json` for anything parsed by a program.
- `--only-show-errors` quiets deprecation warnings in scripts; `--verbose` and `--debug` show the actual REST calls, which is how you learn the API version being used.
- For anything that would iterate many resources, use Resource Graph instead: it is one query rather than N calls, and it does not trip control-plane throttling.

## Resource Graph

The inventory tool (SKILL.md Rule 1). KQL over ARM metadata across every subscription you can read.

```bash
az graph query -q "
Resources
| summarize count() by type, location
| order by count_ desc" -o table
```

- Add `--subscriptions <id> <id>` to scope, or omit to query everything visible.
- Paging: results are capped per page; `--first` and `--skip` walk them, and a `summarize` usually removes the need.
- `ResourceContainers` holds subscriptions and resource groups; `Resources` holds everything else. Joining the two gives resource-group tags alongside resources.
- Save anything you will ask twice to `## Saved Queries` in `memory.md` (`monitoring.md`).

## Inventory Recipes

```bash
# Unattached managed disks — the most common waste
az graph query -q "
Resources
| where type =~ 'microsoft.compute/disks' and properties.diskState == 'Unattached'
| project name, resourceGroup, location, sizeGb = properties.diskSizeGB" -o table

# Public IPs and what they are attached to
az graph query -q "
Resources
| where type =~ 'microsoft.network/publicipaddresses'
| project name, resourceGroup, attachedTo = tostring(properties.ipConfiguration.id)" -o table

# Storage accounts allowing public network access
az graph query -q "
Resources
| where type =~ 'microsoft.storage/storageaccounts'
| where properties.publicNetworkAccess != 'Disabled'
| project name, resourceGroup, sharedKey = properties.allowSharedKeyAccess" -o table

# Resources missing a required tag
az graph query -q "
Resources
| where isnull(tags['Owner'])
| summarize count() by type, resourceGroup" -o table
```

Quota and capacity:

```bash
az vm list-usage --location westeurope -o table              # vCPU quota per family
az vm list-skus --location westeurope --size Standard_D --all -o table   # restrictions and why
```

## Cost

```bash
az consumption usage list --start-date 2026-07-01 --end-date 2026-07-08 -o table
az consumption budget list -o table
```

- The CLI's cost surface is thinner than the portal's Cost Analysis; for a real bill investigation, drive Cost Analysis and read the grouping (`costs.md`).
- Cost data lags by a day or more, and the current month is always incomplete. Record every figure with the date it was read (`memory-template.md`).
- With `billing_model` of `ea` or `csp`, subscription-scope numbers may not reflect the invoice at all.

## Deployment

```bash
# Bicep — always preview first
az deployment group what-if --resource-group rg-app-prod --template-file main.bicep --parameters prod.bicepparam
az deployment group create  --resource-group rg-app-prod --template-file main.bicep --parameters prod.bicepparam --name app-2026-07-26

az deployment sub what-if --location westeurope --template-file platform.bicep    # subscription scope
az bicep build --file main.bicep      # see the compiled ARM when an error names an unfamiliar property
az deployment group list --resource-group rg-app-prod --query "length(@)"   # watch the 800 history cap
```

- Complete mode deletes everything in scope that is not in the template. It is never a default and never runs without a read `what-if` (`iac.md`).
- Deployment names should be deterministic and meaningful — the history is the audit trail.
- Terraform users: same discipline, `plan` then `apply`, with the state backend and provider version pinned.

## Identity

```bash
az ad signed-in-user show --query "{name:displayName, id:id}"
az role assignment list --assignee <principal-id> --all -o table
az role assignment create --assignee <principal-id> --role "Storage Blob Data Reader" --scope <resource-id>
az identity create --name id-app-prod --resource-group rg-app-prod       # user-assigned managed identity
az ad app federated-credential create --id <app-id> --parameters ./federated.json
```

- Always assign at the narrowest scope that works, and prefer groups as the target (SKILL.md Rule 4).
- Data-plane roles are separate from Contributor and are the fix for most 403s from code (`identity.md`).
- Propagation is documented at up to 30 minutes; re-authenticating is a faster test than assigning again.

## Diagnostics

```bash
az monitor activity-log list --resource-group rg-app-prod --start-time 2026-07-25T00:00:00Z --query "[?status.value=='Failed']" -o table
az monitor diagnostic-settings create --name to-law --resource <resource-id> --workspace <workspace-id> --logs '[{"category":"AuditEvent","enabled":true}]'
az network nic list-effective-nsg --name <nic> --resource-group <rg>
az network nic show-effective-route-table --name <nic> --resource-group <rg>
az network watcher test-ip-flow --vm <vm> --direction Outbound --protocol TCP --local <ip>:0 --remote <ip>:443
az webapp log tail --name <app> --resource-group <rg>
az aks get-credentials --name <cluster> --resource-group <rg>    # prefer --admin never; use Entra auth
```

The correlation ID from a failed Activity Log entry links the deployment, the provider error and any Policy denial into one story (`debug.md`).

## Long Operations and Scripting

- `--no-wait` returns immediately for long creates; poll with `az resource wait` or the resource's own `wait` subcommand.
- `az group delete --yes --no-wait` is the most destructive command in daily use. It never belongs in a copy-paste block alongside read-only commands (SKILL.md Output Gates).
- In scripts: `set -euo pipefail`, explicit `--subscription` on every command rather than relying on ambient context, and `-o tsv` for values consumed by the shell.
- Idempotency: most `az ... create` commands are create-or-update, but not all. Check before assuming a re-run is safe.
- Rate limits: loops over hundreds of resources will throttle. Resource Graph for reads; batch for writes.

## Extensions and Versions

- Extensions (`az extension add --name <name>`) ship commands outside the core CLI, and some remain in preview with breaking changes between releases. Pin the extension version in CI.
- `az version` in a bug report; `az upgrade` deliberately, not mid-incident.
- Commands marked preview change without notice. For anything in a pipeline, prefer a GA command, an ARM/Bicep deployment, or the `azapi` Terraform provider (`iac.md`).
- The Az PowerShell module is a full alternative; teams standardize on one. Record which in `config.yaml` under the Tooling preference area (`memory-template.md`).
