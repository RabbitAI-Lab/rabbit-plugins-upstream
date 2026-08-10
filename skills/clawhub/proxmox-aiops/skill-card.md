## Description:

Provides governed Proxmox VE VM and container operations and diagnostics through CLI and MCP tools with audit logging, budget guards, undo recording, and risk-tier labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and infrastructure operators use this skill to inspect, diagnose, and manage Proxmox VE VMs, containers, storage, backups, snapshots, HA, pools, firewall state, and cluster health from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact Proxmox write access can stop, delete, roll back, restore, or migrate VMs according to the permissions of the connected Proxmox account.

Mitigation: Review before production installation, use a dedicated least-privilege API token, prefer read-only roles when writes are not required, and dry-run or explicitly confirm destructive operations.

Risk: Credential-storage guidance is inconsistent across the evidence, so users may need to confirm whether their installed version uses an encrypted secret store or plaintext environment files.

Mitigation: Verify the installed proxmox-aiops version's credential behavior, avoid password auth when possible, and protect any ~/.proxmox-aiops/.env file with restrictive permissions.

Risk: Audit logs, budget guards, and risk-tier labels help with traceability but do not replace authorization or policy enforcement.

Mitigation: Enforce access through Proxmox permissions and operator review, and treat risk labels as decision support rather than an approval gate.

## Reference(s):

- [Proxmox AIops GitHub Repository](https://github.com/AIops-tools/Proxmox-AIops)
- [Agent guardrails](references/agent-guardrails.md)
- [proxmox-aiops capabilities](references/capabilities.md)
- [proxmox-aiops CLI reference](references/cli-reference.md)
- [proxmox-aiops setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI and MCP command examples, configuration snippets, and operational summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Proxmox task identifiers, audit context, risk labels, and dry-run or undo guidance for write operations.]

## Skill Version(s):

0.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
