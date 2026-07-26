# Infrastructure as Code — Bicep, ARM, Terraform and Policy

Everything that survives the session is code. This file covers the two toolchains, the deployment semantics that delete things unexpectedly, and Azure Policy — which is not IaC but blocks it constantly.

**Contents:** [Bicep vs Terraform](#bicep-vs-terraform) · [Deployment Modes and Scopes](#deployment-modes-and-scopes) · [Deployment Stacks](#deployment-stacks) · [Preview Before Every Change](#preview-before-every-change) · [Bicep Practice](#bicep-practice) · [Terraform on Azure](#terraform-on-azure) · [Locks](#locks) · [Azure Policy](#azure-policy) · [Provider Registration and Naming](#provider-registration-and-naming) · [Structuring the Estate](#structuring-the-estate)

Generated artifacts follow `iac_tool` (config). Where this file shows both, produce only the configured one.

## Bicep vs Terraform

| | Bicep | Terraform (`azurerm`) |
|---|---|---|
| State | None — ARM is the state | A state file you must host, lock and protect |
| New resource types | Available as soon as the ARM API is | Waits for provider support (`azapi` closes the gap) |
| Preview | `what-if`, evaluated by ARM against live resources | `plan`, evaluated against state |
| Multi-cloud | No | Yes |
| Deleting a resource you removed from the file | Only in Complete mode | Yes, by default |
| Modules | Registry or local paths, ARM-native | Rich ecosystem, versioned |

Decision shape: single-cloud Azure estate with a platform team that dislikes state files → Bicep. Multi-cloud, heavy module reuse, existing Terraform discipline → Terraform. Both beat portal clicking by a distance; neither survives someone hotfixing in the portal.

## Deployment Modes and Scopes

- **Incremental (default)**: resources in the template are created or updated; resources *not* in the template are left alone. Drift accumulates invisibly — an incremental deployment can never tell you what it did not touch.
- **Complete**: everything in the target scope that is not in the template is **deleted**. It is the only way ARM converges to the template, and it is how people delete production. Never run it at a scope containing resources the template does not own, and never run it without `what-if` output that a human read.
- **Scopes**: resource group, subscription, management group, tenant. Subscription-scope templates create resource groups; management-group scope deploys policy and role assignments. Choosing the scope wrong is why a template "cannot find" a resource type.
- **Deployment history is capped** at 800 records per resource group; past that, deployments fail until older records are purged. On a busy CI pipeline this arrives without warning.
- Deployment names should be deterministic and meaningful (`workload-env-<run-id>`), because the history is the audit trail.

## Deployment Stacks

A stack is a managed collection of resources with an explicit lifecycle: resources it owns are tracked, and removing one from the template can delete or detach it deliberately rather than by mode.

- Deny settings on a stack prevent changes to managed resources from outside the stack — the supported answer to portal hotfixes.
- Correct for platform-owned foundations (networking, policy, shared services) that application teams must not edit.
- Adopting stacks on an existing estate means importing what already exists; plan it as a change with a rollback, not as a switch.

## Preview Before Every Change

- `what-if` (Bicep/ARM) compares the template against live resources and prints creates, deletes, modifies and no-ops. It has known blind spots for properties the provider does not return — treat a clean `what-if` on a resource with secrets or lists as "probably fine", not "proven".
- `plan` (Terraform) compares against state. A plan that shows a surprise **replacement** is the one to stop and read: `ForceNew` on a property means destroy-and-create, and for a database or a public IP that is an outage.
- Rule: no apply without a preview that someone read, and no preview run against a different subscription than the apply (SKILL.md Rule 7).
- A significant change earns its row in `~/Clawic/data/azure/deploys/<year>.md` (template version, rollback target). When the preview itself is the evidence — a replacement, a delete, a first apply to production — save the output as `~/Clawic/data/azure/artifacts/plan-<change>.md`, point the deploy row at it, and add its `## Boxes` line in the same turn (`memory-template.md`). The diff is the best postmortem evidence there is.

## Bicep Practice

- Modules per lifecycle, not per resource type: `network`, `data`, `app`. Cross-module wiring via outputs, not by hard-coded names.
- **`uniqueString()` for globally-unique names**, seeded on the resource group id so it is stable across deployments. Random suffixes generated at deploy time produce a new resource on every run.
- Parameters get types, allowed values and defaults; `@secure()` for anything sensitive — and even then, prefer a Key Vault reference in the parameter file over a value that travels through a pipeline log.
- Existing resources referenced with `existing` rather than re-declared; re-declaring a resource you do not own is how a template overwrites someone else's settings.
- Loops (`for`) and conditions (`if`) keep environments in one template; a per-environment parameter file beats a per-environment copy of the template.
- Bicep compiles to ARM JSON: when an error mentions a property you never wrote, read the compiled JSON.
- Test with `what-if` against a scratch resource group before the first apply to production.

## Terraform on Azure

- **State contains secrets in plaintext** — connection strings, generated passwords, keys. Remote backend in a storage account with encryption, restricted network access, versioning and soft delete; access via managed identity or OIDC, never a stored key. State is a credential store, and it belongs nowhere near `~/Clawic/data/`.
- State locking is provided by the storage backend's lease. A killed pipeline leaves a lease behind; break it deliberately, after confirming nothing is running.
- Pin the provider version and the Terraform version. `azurerm` majors change resource behaviour, and an unpinned provider upgrade mid-sprint is an unplanned migration.
- **`azapi` provider** covers resources and properties `azurerm` has not implemented yet — the standard escape hatch for preview features, and better than clicking.
- Authenticate CI with **workload identity federation** (OIDC), not a client secret (`identity.md`).
- `prevent_destroy` on data resources; `ignore_changes` for properties another system owns (tags applied by Policy, autoscale-managed capacity) — otherwise every plan shows the same phantom diff.
- Importing an existing estate is a project: import blocks or `terraform import`, one resource at a time, verifying an empty plan after each.

## Locks

- `CanNotDelete` prevents deletion but allows changes. `ReadOnly` prevents changes — including operations that look like reads but issue POST, such as listing keys or restarting a resource, which breaks more than people expect.
- Locks inherit downward from subscription and resource group.
- Locks block Terraform destroy and Complete-mode deployments, which is the point, and they also block legitimate CI runs, which is the cost. Apply them to data resources and platform foundations, not to everything.
- Removing a lock is an auditable action; requiring it before a destructive operation is a cheap, effective guardrail.

## Azure Policy

Policy is the reason a valid template gets rejected, and the best available tool for making an estate consistent.

| Effect | Does | Applies to existing resources |
|---|---|---|
| `Audit` | Marks non-compliance, changes nothing | Yes, at evaluation |
| `Deny` | Blocks the create/update | No — existing resources stay |
| `Modify` | Adds or changes properties (typically tags) | Only through a remediation task |
| `DeployIfNotExists` | Deploys a companion resource (diagnostic settings, agents) | Only through a remediation task |
| `AuditIfNotExists` | Flags resources missing a companion resource | Yes |

- `Modify` and `DeployIfNotExists` need a **managed identity** on the assignment with rights at the target scope, and they do nothing to what already exists until a **remediation task** runs. This is the number one reason "the tag policy is not working".
- Evaluation is not instantaneous: assignment takes effect within roughly half an hour, and the full compliance scan runs on a cycle of hours. Do not conclude a policy is broken from an immediate check.
- Initiatives (policy sets) group related definitions with shared parameters — the unit that maps onto a compliance regime.
- Exemptions with an expiry date are better than removing the assignment; an exemption without a date is a permanent hole with a friendly name.
- Deploy policy as code, at management-group scope, alongside the landing zone (`governance.md`).
- **When a definition finally does what it should**, save it: `~/Clawic/data/azure/artifacts/policy-<name>.md` with the JSON, the scope, the effect, and what it prevents — plus its `## Boxes` line in `memory.md`. Policy definitions are derived through trial and error and lost the same way (`memory-template.md`).

## Provider Registration and Naming

- Resource providers register **per subscription**. A template that works in one subscription and fails with `MissingSubscriptionRegistration` in another has found an unregistered provider; registration takes minutes and belongs in subscription bootstrap.
- Globally unique names: storage accounts, Key Vaults, ACR, App Service, Cosmos, Front Door. Validate availability before deploying, and remember soft-deleted resources hold their names.
- Naming comes from `naming_pattern` (config). Consistency matters more than the specific scheme: it is what makes cost reports, Resource Graph queries and access reviews possible.
- Length and character limits differ per resource type (storage accounts are the harshest: short, lowercase, alphanumeric). A naming function that works for every type has to account for that.

## Structuring the Estate

- One resource group per lifecycle, not per resource type: things that are created, updated and deleted together. A shared "everything" group is what makes deletions terrifying.
- Separate the platform (networking, DNS, Key Vault, policy) from the applications; different owners, different change cadence, different locks.
- Environments separate by subscription where `tenancy_model` is `management-group`, by resource group otherwise (`governance.md`).
- Pipelines deploy with a federated identity scoped to exactly what they own; a pipeline with subscription Owner is a lateral-movement path (`identity.md`).

**When the IaC tool, state backend, or repository layout is decided, record it** in `## Current Infrastructure` in `~/Clawic/data/azure/memory.md`: tool, where state lives, which scopes it deploys at, and which resources are deliberately not managed by it. That last item is the one that saves the next incident.
