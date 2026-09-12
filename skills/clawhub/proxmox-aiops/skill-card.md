## Description:

Proxmox AIops helps agents manage and diagnose Proxmox VE virtual machines, containers, cluster resources, storage, backups, snapshots, firewall state, HA resources, and common lifecycle operations with audit, undo, and risk-tier guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and infrastructure operators use this skill to inspect, troubleshoot, and perform governed VM and container operations in explicitly Proxmox VE environments. It is suited for agent-assisted operations where read/write actions should be auditable and destructive actions require extra care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make destructive infrastructure changes such as stopping, deleting, rolling back, restoring, migrating, or reconfiguring Proxmox guests.

Mitigation: Use dry-run previews where available, require human review for destructive actions, and connect with a dedicated least-privilege Proxmox API token so unauthorized writes fail at the server.

Risk: Credential handling, TLS configuration, and package provenance are left under user control.

Mitigation: Pin a reviewed package version, keep TLS verification enabled in production, avoid plaintext passwords where possible, and restrict permissions on Proxmox AIops configuration, audit, and undo files.

Risk: Audit and undo data can reveal sensitive infrastructure details.

Mitigation: Treat local audit and undo files as sensitive operational records and store them with restricted filesystem permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/proxmox-aiops)
- [Project homepage](https://github.com/AIops-tools/Proxmox-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, analysis, API calls]

**Output Format:** [Markdown with inline shell commands and structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Proxmox task UPIDs for asynchronous write operations; operational outputs can include audit and undo identifiers.]

## Skill Version(s):

0.13.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
