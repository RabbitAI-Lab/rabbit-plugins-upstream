## Description:

Use this skill to manage and diagnose Proxmox VE virtual machines, containers, storage, backups, snapshots, cluster health, HA, pools, firewall status, and async tasks through governed CLI and MCP operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect, operate, and troubleshoot Proxmox VE environments with audited read and write workflows. It is intended for explicit Proxmox VE tasks such as VM lifecycle changes, snapshots, backups, migration, storage inspection, and read-only cluster diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release installs a community package that can receive operational access to Proxmox infrastructure.

Mitigation: Install only a pinned and verified package version, and review the package before granting access to production systems.

Risk: The skill handles powerful Proxmox credentials and can perform destructive operations.

Mitigation: Use a dedicated least-privilege API token, keep TLS verification enabled, protect the local Proxmox configuration directory, and start with dry runs or read-only credentials.

Risk: Write operations can change VM, container, disk, backup, snapshot, and migration state.

Mitigation: Confirm the target VMID, node, storage, and task status before action; prefer dry-run previews and use recorded undo identifiers where available.

## Reference(s):

- [Proxmox AIops project homepage](https://github.com/AIops-tools/Proxmox-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/proxmox-aiops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with inline shell commands and structured MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Proxmox task UPIDs, audit references, dry-run previews, ranked diagnostic findings, and undo identifiers for reversible writes.]

## Skill Version(s):

0.13.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
