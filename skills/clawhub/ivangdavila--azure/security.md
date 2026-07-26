# Security — Exposure, Key Vault, Detection and the Leak Runbook

Identity is the perimeter, and the permissions half of the subject — role systems, evaluation order, managed identities, PIM — is a separate route from the Quick Reference (`identity.md`). This file covers exposure, secrets, encryption, detection, and what to do when a credential leaks.

**Contents:** [Threat Model in Three Lines](#threat-model-in-three-lines) · [The Exposure Sweep](#the-exposure-sweep) · [Key Vault](#key-vault) · [Encryption](#encryption) · [Network Exposure](#network-exposure) · [Detection Stack, in Cost Order](#detection-stack-in-cost-order) · [Leaked Credential Runbook](#leaked-credential-runbook) · [Compliance Regimes](#compliance-regimes) · [Audit Checklist](#audit-checklist)

## Threat Model in Three Lines

1. **Credentials leak** — from a repository, a laptop, a pipeline log, a Terraform state file, or a request forged against the instance metadata endpoint. This is the overwhelming majority of real incidents.
2. **Something is public that should not be** — a storage account, a database firewall rule that admits all of Azure, a management port open to the internet, a Key Vault on "all networks".
3. **Cost is the payload** — a stolen credential's first act is usually to deploy GPU capacity for mining, which is why the anomaly alert from `costs.md` doubles as a security control.

## The Exposure Sweep

Run these as Resource Graph queries across every subscription; each returns a list, not an opinion (`commands.md`).

| Question | Why it matters |
|---|---|
| Storage accounts with public network access enabled, or public blob access allowed | The classic data leak, and the easiest to fix |
| Storage accounts with shared-key access enabled | Every control-plane Contributor is silently a data owner |
| SQL servers with the "Allow Azure services" (0.0.0.0) rule | Admits resources from **other tenants**, not just yours |
| Databases and Key Vaults with public network access and no firewall rules | An internet-reachable data plane behind one credential |
| NSG rules with source `Internet`/`*` on 22, 3389, 1433, 3306, 5432 | Management and database ports facing the world |
| Public IPs, and which resource each is attached to | Every one is an attack surface and a line item |
| VMs without disk encryption or with unmanaged disks | Legacy configurations that policy never caught |
| App registrations with client secrets, and their expiry dates | Credentials with a calendar deadline (`identity.md`) |
| Resources without a diagnostic setting | You cannot investigate what was never recorded |
| AKS clusters with local accounts enabled or a public API server | Kubernetes RBAC bypass |

Everything found goes into `## Current Infrastructure` with the date of the sweep — the next audit should start from the gaps, not from the beginning.

## Key Vault

- **RBAC data plane, not legacy access policies.** Access policies have no inheritance, no PIM, and no consistent audit story. Existing vaults should be migrated deliberately, not left in mixed mode.
- **Soft delete is mandatory** (90 days): a deleted vault's name is unusable until purged, which is a deployment failure people meet at the worst time. **Purge protection**, once enabled, cannot be disabled — correct for production, painful in ephemeral test environments, so decide per environment.
- Separate vaults by blast radius and lifecycle: platform secrets, per-application secrets, certificates. One vault for everything means one role assignment for everything.
- Network: private endpoint or firewall with explicit rules. The "trusted Microsoft services" exception is broader than it sounds; pair it with resource-instance rules where the service supports them.
- Rotation: secrets have versions, and applications must read by name rather than pinning a version. Near-expiry events can drive automated rotation; without that, the expiry date belongs in `## Due`.
- **Audit logging must be enabled with a diagnostic setting** — vault access is exactly what you need after an incident, and it is off by default.
- Managed HSM is a separate product for key-ownership regimes, with its own access model and a higher cost floor.

## Encryption

| Layer | Default | When to change it |
|---|---|---|
| Storage, SQL, Cosmos at rest | Platform-managed keys, always on | Customer-managed keys when a regime requires key ownership or revocation |
| VM disks | Platform-managed keys | **Encryption at host** covers OS, data and temp disks with the least operational cost; in-guest encryption only for specific requirements |
| Data in transit | TLS, and services enforce minimum versions | Enforce TLS 1.2 or higher explicitly; older clients fail loudly, which is correct |
| Backups | Inherit the vault's encryption | Customer-managed keys where the regime says so |
| In use | — | Confidential computing SKUs for regulated workloads that need memory encryption |

Customer-managed keys are a commitment: the Key Vault becomes a hard dependency of the data. Losing key access loses the data, so the key vault needs its own protection, its own backup, and purge protection on.

## Network Exposure

- Data services get private endpoints and public access disabled — in that order, verifying resolution first (`networking.md`).
- Management access to VMs through Bastion or just-in-time access, never a permanent open port. Just-in-time opens the rule for a bounded window on request and closes it automatically.
- Front Door or Application Gateway in front of public web workloads, with the origin locked to the service tag plus an identifying header — otherwise the WAF is optional for an attacker who found the origin.
- WAF in prevention mode, tuned with the logs from a period in detection mode. A WAF in detection mode forever is a dashboard, not a control.
- DDoS protection: the platform provides basic mitigation; the paid tier adds tuned policies, telemetry and cost protection. Justify it by the value of the endpoint, not by anxiety.

## Detection Stack, in Cost Order

1. **Free**: Defender for Cloud's secure score and recommendations, Activity Log alerts on deletions and role assignments, cost anomaly alerts, Entra sign-in and audit logs.
2. **Cheap and high-yield**: Defender for Cloud plans on the resource types that hold data — servers, storage, SQL, Key Vault, containers. Pricing is per resource per month, so the bill is predictable and it scales with the estate.
3. **Considered**: Microsoft Sentinel for correlation across sources. Its cost follows ingestion, so it magnifies every decision in `monitoring.md` — turn it on after ingestion is under control, not before.
4. **Always**: a defined owner and channel for each alert. Detection with no recipient is a log file.

Enabling every plan on a small estate can outspend the workloads it protects. Start with the free tier and the data-bearing resources.

## Leaked Credential Runbook

A key, secret, connection string or token has been exposed. Order matters — revoke before investigating, because the attacker is not waiting.

1. **Revoke the credential.** Storage: rotate the key (pairs exist so consumers can move first). Service principal: delete the secret or certificate. SAS: rotate the signing key, or revoke the user delegation key. Function keys: renew. If it is a user, revoke sign-in sessions and reset.
2. **Rotate what the credential could reach**, not just the credential. A leaked storage key implies every SAS derived from it.
3. **Establish the window**: when was it exposed, and what does the log show in that window? Storage and Key Vault diagnostic logs, SQL audit, Entra sign-in logs, Activity Log for control-plane use.
4. **Look for persistence.** The standard moves: a new secret or certificate added to an existing app registration, a new federated credential, a new role assignment, a new user with a directory role, a new automation account or runbook. Check the Entra audit log for `Update application` and `Add member to role` events across the exposure window.
5. **Check cost.** A spike in GPU or compute in an unusual region is the fastest confirmation of exploitation.
6. **Close the path.** How did it leak — a repository, a log, a state file, a screenshot in a ticket? The path is the finding; the credential is the symptom.
7. **Write the runbook down**: `~/Clawic/data/azure/artifacts/runbook-credential-leak.md`, with what was rotated, what the logs showed, and what was changed to prevent it — plus its `## Boxes` line in `memory.md`. Second time, this costs minutes (`memory-template.md`).

Prevention that actually works: managed identity and federated credentials so there is nothing to leak; secret scanning on repositories; short SAS lifetimes with an account-level expiry policy; state files in a locked backend; and never writing a secret value into any note, ticket or memory file — pointer only.

## Compliance Regimes

`compliance_regime` (config) changes defaults rather than adding a checklist at the end.

| Regime | What it forces early |
|---|---|
| `pci` | Network segmentation, no public data plane, logging retention, restricted key access, documented scope boundaries |
| `hipaa` | Encryption with documented key management, audit logging on data access, a signed agreement covering the services in scope |
| `soc2` | Change management evidence, access reviews on a cadence, monitoring with alerting, documented incident response |
| `fedramp` | A sovereign or government cloud environment, restricted service catalogue, stricter identity requirements |
| `none` | The baseline in this file |

Two rules regardless of regime: service eligibility is checked **before** the design (not every service is in scope for every regime, and sovereign clouds lag features), and the compliance dashboard in Defender for Cloud is evidence, not achievement — it reports on what is configured, not on what is practised.

## Audit Checklist

| Check | How |
|---|---|
| No standing privileged access; break-glass accounts tested | `identity.md` access review |
| MFA enforced, legacy authentication blocked | Conditional Access, sign-in logs |
| Shared-key access disabled on storage; public blob access off | Resource Graph query across subscriptions |
| No 0.0.0.0 "Allow Azure services" rules on SQL or other data services | Resource Graph query |
| No management or database ports open to the internet | NSG rules query |
| Key Vaults in RBAC mode, purge protection on for production, diagnostics enabled | Per-vault properties |
| Diagnostic settings deployed by Policy, not by hand | Policy compliance |
| Defender plans enabled on data-bearing resource types | Defender for Cloud settings |
| Budget and anomaly alerts exist (they are a security control) | `costs.md` |
| Client secrets and certificates expiring within 90 days | Entra app registrations, cross-checked with `## Due` |
| Backups exist, are immutable where it matters, and a restore has been timed | `production.md` |

Write the sweep result into `## Current Infrastructure` in `~/Clawic/data/azure/memory.md`, any expiry date found into `## Due`, and any hardening decision that took work into `artifacts/` with its `## Boxes` line. The next session should start from the gaps.
