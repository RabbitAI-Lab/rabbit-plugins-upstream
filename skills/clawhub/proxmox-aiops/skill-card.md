## Description:

Provides governed Proxmox VE VM and container operations and diagnostics through CLI and MCP tools with audit logging, budget controls, undo records, and risk-tier labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and infrastructure operators use this skill to inspect, diagnose, and manage Proxmox VE VMs, containers, snapshots, backups, storage, HA status, firewall status, and cluster health. It is intended for explicitly Proxmox or Proxmox VE environments, not other hypervisors, Kubernetes, or cloud providers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make destructive infrastructure changes in Proxmox.

Mitigation: Use a dedicated least-privilege API token, prefer read-only permissions unless writes are required, and review write actions before execution.

Risk: Credential setup can expose high-impact Proxmox secrets if broad tokens or passwords are used.

Mitigation: Avoid passwords and broad root or admin tokens, prefer the encrypted secret store, and keep TLS verification enabled.

Risk: The local audit and undo database may contain sensitive infrastructure details.

Mitigation: Treat audit and undo data as sensitive operational records and protect the configured Proxmox AIops home directory accordingly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/proxmox-aiops)
- [Project homepage](https://github.com/AIops-tools/Proxmox-AIops)
- [proxmox-aiops capabilities](references/capabilities.md)
- [proxmox-aiops CLI reference](references/cli-reference.md)
- [proxmox-aiops setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Proxmox task UPIDs, dry-run guidance, audit or undo identifiers, and configuration snippets.]

## Skill Version(s):

0.13.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
