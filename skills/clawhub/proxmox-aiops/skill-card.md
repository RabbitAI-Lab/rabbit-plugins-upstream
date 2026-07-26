## Description: <br>
Proxmox Aiops helps agents manage and diagnose Proxmox VE VMs, containers, clusters, storage, backups, snapshots, and related operations through governed CLI and MCP workflows with audit, budget, undo, and risk-tier controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to inspect, administer, and troubleshoot Proxmox VE environments, including VM/container lifecycle actions, snapshots, backups, storage, HA, firewall inspection, and read-only RCA for node or guest pressure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform destructive Proxmox administration actions such as stopping, deleting, rolling back, restoring, or migrating guests. <br>
Mitigation: Install only for intended Proxmox administration workflows, use least-privilege Proxmox API tokens, prefer read-only roles unless writes are required, and use the documented dry-run and confirmation paths before write actions. <br>
Risk: Credentials and audit or undo state are stored under ~/.proxmox-aiops/ and could expose sensitive operational data if file permissions are weak. <br>
Mitigation: Protect ~/.proxmox-aiops/ with restrictive permissions, keep secrets in the per-target .env file, avoid password authentication where possible, and review local audit and undo storage practices before enabling MCP write workflows. <br>
Risk: Agent mistakes could repeat operations or act on the wrong Proxmox object if tool results are ignored or inferred. <br>
Mitigation: Require agents to call the actual tool, report real errors, treat null or truncated data explicitly, poll asynchronous task UPIDs instead of reissuing writes, and cite returned IDs and measured values when diagnosing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/proxmox-aiops) <br>
- [Project Homepage](https://github.com/AIops-tools/Proxmox-AIops) <br>
- [Capabilities Reference](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to call proxmox-aiops CLI or MCP tools and to report task UPIDs, audit details, diagnostics, and tool results.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
