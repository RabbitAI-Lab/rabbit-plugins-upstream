# Identity — Entra ID, RBAC, and Why the Role You Assigned Did Nothing

Azure has two identity systems that share a portal and almost nothing else: **Entra ID directory roles** govern the directory (users, groups, app registrations), **Azure RBAC** governs resources (subscriptions, resource groups, resources). Most "permissions bugs" are a correct assignment in the wrong system, at the wrong scope, or on the wrong plane.

**Contents:** [The Two Role Systems](#the-two-role-systems) · [Evaluation Order](#evaluation-order) · [Diagnosing a Denial](#diagnosing-a-denial) · [Control Plane vs Data Plane](#control-plane-vs-data-plane) · [Managed Identity](#managed-identity) · [Service Principals and Federated Credentials](#service-principals-and-federated-credentials) · [PIM and Privileged Access](#pim-and-privileged-access) · [Custom Roles](#custom-roles) · [Guests, Tenants and B2B](#guests-tenants-and-b2b) · [Access Review Checklist](#access-review-checklist)

## The Two Role Systems

| | Entra ID directory roles | Azure RBAC |
|---|---|---|
| Governs | Users, groups, applications, the directory itself | Subscriptions, resource groups, resources |
| Examples | Global Administrator, Application Administrator, User Administrator | Owner, Contributor, Reader, Storage Blob Data Contributor |
| Scope | Tenant (or administrative unit) | Management group → subscription → resource group → resource, inherited downward |
| Assigned in | Entra ID blade | The resource's Access control (IAM) blade |

A Global Administrator has **no** access to Azure resources by default. The "elevate access" toggle grants them User Access Administrator at the root management group — a deliberate, audited action, and the way you recover a tenant whose subscriptions have no owners. Turn it back off afterwards.

## Evaluation Order

A request succeeds only if it survives every gate:

1. **Deny assignment** — created by the platform (managed applications, some deployment stacks and blueprints), not by users. It beats every allow, and it is the reason a subscription Owner can be told no. Visible on the resource's IAM blade under Deny assignments.
2. **Azure Policy `Deny` effect** — blocks the *write*, not the read, and returns a policy-shaped error naming the assignment. It is not RBAC, and widening a role never fixes it (`iac.md`).
3. **Role assignment at this scope or any parent** — union of everything inherited. There is no user-authored deny to subtract from it; the only way to remove access is to remove assignments.
4. **ABAC condition** on the assignment, where present — most commonly on storage data roles, keyed on blob path or tag.
5. **Resource-level firewall or private endpoint policy** — a perfect role still fails if the service refuses the network path. `AuthorizationFailed` says role; `Forbidden`/`403` from a data endpoint with a network message says firewall (`networking.md`).

Propagation is documented at up to 30 minutes and tokens cache role claims until refreshed. Two consequences: pipelines that assign a role and immediately use it fail intermittently, and re-authenticating is a faster test than assigning the role a second time.

## Diagnosing a Denial

Ask these in order; each one is cheap and eliminates a class.

| Question | How to check | If wrong |
|---|---|---|
| Am I in the right subscription? | `az account show` | `az account set --subscription <name>` — this is the single most common cause |
| Am I the identity I think I am? | `az ad signed-in-user show`, or the identity the code runs as | A CI pipeline is a service principal, not you |
| Is the assignment at a scope that covers this resource? | `az role assignment list --assignee <id> --all` | Assignments do not inherit *upward*; a resource-group role never covers a sibling group |
| Is this a data-plane operation? | Does the call touch blobs, secrets, queues, Cosmos items? | Assign the matching data role (below) |
| Is there a deny assignment or a Policy denial? | IAM blade → Deny assignments; the error text names a policy assignment | Neither is fixed by more RBAC |
| Was it assigned in the last half hour? | Assignment timestamp | Wait or refresh the token before doing anything else |
| Is the network path allowed? | Service firewall, private endpoint DNS | `networking.md` |

Activity Log holds the failed operation with a correlation ID; for data-plane calls the resource's own diagnostic logs (for example storage `StorageRead`) hold the reason. Never widen a role because a denial is unexplained — an unexplained denial that goes away is a security finding you deleted.

## Control Plane vs Data Plane

This distinction has no equivalent in most other clouds and it produces the majority of confusing 403s.

| Resource | Control-plane role (manage it) | Data-plane role (use its contents) |
|---|---|---|
| Storage account | Contributor — can read the *keys*, therefore the data, which is why key access should be disabled | Storage Blob Data Reader/Contributor, Queue Data, File Data |
| Key Vault (RBAC mode) | Contributor — can change the access model, an escalation path worth auditing | Key Vault Secrets User / Certificates Officer / Crypto User |
| Cosmos DB | Contributor — can read keys unless disabled | Cosmos DB Built-in Data Reader/Contributor (assigned via the data-plane API, not the IAM blade) |
| Service Bus / Event Hubs | Contributor | Data Sender / Data Receiver |
| AKS | Contributor — can pull admin credentials, which bypasses Kubernetes RBAC | Azure Kubernetes Service RBAC roles, with local accounts disabled |

The hardening rule that follows: disable shared-key and local-admin paths (`allowSharedKeyAccess=false`, `disableLocalAccounts` on AKS, RBAC mode on Key Vault). Otherwise every control-plane Contributor is silently a data-plane Owner, and no data role assignment tells you the truth.

## Managed Identity

Default for anything Azure-to-Azure. No secret, no expiry, no rotation.

- **System-assigned** — lifecycle bound to the resource: created with it, deleted with it, unique to it. Correct when one resource needs its own identity. Deleting and recreating the resource orphans every role assignment it had, which then have to be reassigned.
- **User-assigned** — a standalone resource you assign to one or many workloads. Correct when identity must survive redeploys, be shared by a scale set, or be created ahead of the workload by a platform team. Its role assignments are made once.
- Tokens come from the instance metadata endpoint inside the resource; nothing is stored on disk. A VM with a managed identity is a credential — SSRF against the metadata endpoint is the corresponding threat (`security.md`).
- Managed identities are tenant-bound: they cannot authenticate to a resource in another tenant. Cross-tenant access needs a multi-tenant app registration with federated or certificate credentials.
- Not every service accepts a managed identity for every connection yet. When one does not, the fallback is a Key Vault reference, never a secret in configuration.

## Service Principals and Federated Credentials

An app registration is the application object; the service principal is its instance in a tenant.

- **Federated credentials are the right answer for CI.** GitHub Actions, Azure DevOps, GitLab and Kubernetes workloads can exchange their own OIDC token for an Azure token, keyed on issuer plus subject. No secret exists, so nothing expires and nothing leaks. This is the single highest-value change on most estates.
- **Certificates beat client secrets** where federation is impossible: longer life, and a compromise leaves an artifact you can trace.
- **Client secrets expire on a date.** The portal caps their lifetime and defaults to a short window; whatever the value, it is a scheduled outage unless it is written down. The moment one is created, its expiry goes into `## Due` in `memory.md` with the app name.
- **Attackers add credentials to existing app registrations** rather than creating new ones — it survives password resets and looks like configuration. Audit `Update application – Certificates and secrets management` events in the Entra audit log (`security.md`).
- Conditional Access does not apply to service principals without the workload-identities licence; treat their network restrictions as a separate control.
- One service principal per workload per environment. A shared "deploy" principal with Owner on everything is the credential that turns one leaked pipeline variable into a tenant compromise.

## PIM and Privileged Access

- **Eligible instead of active**: nobody holds Owner or Global Administrator standing. Activation is time-boxed, justified, optionally approved, and logged. This converts a permanent credential into an auditable event.
- Activation adds latency measured in minutes — design pipelines around it rather than granting a standing role to work around it.
- **Approval workflows and role management do not mix well**: an Owner cannot always grant a role that requires approval. Use User Access Administrator, PIM-eligible, for access administration.
- **Break-glass accounts**: two cloud-only accounts, excluded from Conditional Access, long random passwords stored offline (never in `~/Clawic/data/`), with sign-in alerts. Test them on the same cadence as the DR drill, and record the test in `## Due`.
- Access reviews on eligible roles and guest accounts, quarterly, recorded in `## Due`.

## Custom Roles

Build one when a built-in role is too wide and the gap is structural, not a one-off.

- Definition is `Actions`, `NotActions`, `DataActions`, `NotDataActions`, plus `AssignableScopes`. `NotActions` subtracts from `Actions`; it is not a deny and does nothing about permissions granted by another assignment.
- Data operations must go in `DataActions` — putting them in `Actions` silently grants nothing.
- Start from the built-in role JSON that is closest, subtract, and test with `az role assignment list` plus an actual call. Deriving a working custom role costs a full business cycle.
- **When one finally works, save it**: `~/Clawic/data/azure/artifacts/role-<name>.md` with the JSON, the date, what it unblocked, and which built-in role it replaced — then add its `## Boxes` line to `memory.md`. Nobody should pay that cost twice.
- Prefer groups as the assignment target: a subscription accepts 4,000 role assignments, and per-user assignments exhaust it while making review impossible.

## Guests, Tenants and B2B

- Guest (B2B) users authenticate against their home tenant; disabling their account there does not remove their access here. Access reviews, not termination emails, are the control.
- Guests default to being able to enumerate parts of the directory. Restrict external user permissions in External Identities settings unless there is a reason not to.
- **Moving a subscription to another tenant deletes every role assignment and every system-assigned managed identity in it.** The subscription arrives empty of access, with workloads authenticating as identities that no longer exist. Plan it as a migration with an access inventory taken first (`governance.md`).
- Customer-facing identity (sign-up, social login) is a different product line from workforce identity. Entra External ID is the current path for new tenants; treat Azure AD B2C as an existing-estate technology and verify availability before designing anything new on it.

## Access Review Checklist

| Check | How |
|---|---|
| No standing Owner or Global Administrator on humans | Entra roles + `az role assignment list --all --role Owner` |
| Break-glass accounts exist, are excluded from CA, and were tested | Entra ID sign-in logs |
| MFA enforced for every human, no legacy auth allowed | Conditional Access policies, sign-in logs filtered on legacy clients |
| Service principals: none with subscription Owner; all with an owner recorded | `az ad sp list`, cross-checked against `## Subscription Context` |
| Client secrets and certificates expiring in the next 90 days | Entra app registrations, then confirm each against `## Due` |
| Credentials added to existing app registrations in the last 90 days | Entra audit log, `Update application` events |
| Guests still needed | Access review, quarterly |
| Data-plane roles assigned deliberately, shared-key access disabled | `az storage account show --query allowSharedKeyAccess`, Key Vault in RBAC mode, AKS local accounts disabled |
| Role assignments count against the 4,000 subscription ceiling | Assign to groups, not users |

Write the review date to `## Due`, any expiry date found to `## Due` as its own one-off row, and any custom role or working policy to `artifacts/` with its `## Boxes` line. An access review whose findings live only in a chat message gets rediscovered next quarter.
