## Description:

Proxmox AIops helps agents manage and diagnose Proxmox VE virtual machines, containers, storage, backups, snapshots, HA, firewall, and cluster health with governed CLI and MCP operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure operators, and external agents use this skill to inspect, operate, and troubleshoot Proxmox VE environments. It is suited for VM and container lifecycle work, storage and backup workflows, cluster status checks, and read-only root-cause analysis when the target is explicitly Proxmox VE.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform destructive Proxmox infrastructure actions.

Mitigation: Use a dedicated least-privilege Proxmox API token, prefer read-only roles unless writes are required, preview supported destructive operations with dry-run, and rely on audited write paths and undo records where available.

Risk: Credential-storage guidance is inconsistent across the release evidence and artifact text.

Mitigation: Verify how the installed version stores secrets, keep ~/.proxmox-aiops out of backups and sync tools, keep config files free of secrets, and restrict secret files to the local user.

Risk: Disabling TLS verification can expose Proxmox API credentials or operations outside isolated labs.

Mitigation: Keep TLS verification enabled in normal environments and disable it only for isolated self-signed lab deployments.

Risk: Repeated asynchronous writes or polling can amplify operational mistakes.

Mitigation: Poll returned task identifiers instead of reissuing operations, pin package versions in sensitive environments, and use the documented call and wall-time budget controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/proxmox-aiops)
- [Project homepage](https://github.com/AIops-tools/Proxmox-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or invoke Proxmox CLI or MCP operations; write operations can return asynchronous task identifiers that require polling.]

## Skill Version(s):

0.13.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
