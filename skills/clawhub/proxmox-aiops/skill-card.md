## Description: <br>
proxmox-aiops helps agents inspect, diagnose, and administer Proxmox VE VMs, containers, storage, backups, snapshots, HA, firewall state, and cluster health through governed CLI and MCP workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, infrastructure operators, and automation agents use this skill to manage Proxmox VE environments, including VM/container lifecycle operations, snapshots, backup/restore, storage checks, cluster diagnostics, and read-only root-cause analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact Proxmox VM and container write operations, including deletes, rollbacks, restores, migrations, stops, and reconfiguration. <br>
Mitigation: Use a dedicated least-privilege Proxmox API token, prefer read-only permissions unless writes are required, and require an external approval process for destructive or high-impact actions. <br>
Risk: Credential setup exposes Proxmox API tokens or passwords if configuration files are mishandled. <br>
Mitigation: Store secrets only in the configured secret file or environment variables, restrict file permissions on ~/.proxmox-aiops, and verify audit redaction before use. <br>
Risk: Repeated or premature write retries can compound operational impact while Proxmox asynchronous tasks are still running. <br>
Mitigation: Poll returned task UPIDs and review task logs instead of re-issuing operations. <br>
Risk: Agent output may propose actions beyond the user's intended operational scope. <br>
Mitigation: Constrain the connected Proxmox account to the intended pools, nodes, and permissions, and review dry-run previews before writes. <br>


## Reference(s): <br>
- [Proxmox AIops homepage](https://github.com/AIops-tools/Proxmox-AIops) <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/proxmox-aiops) <br>
- [capabilities.md](references/capabilities.md) <br>
- [cli-reference.md](references/cli-reference.md) <br>
- [setup-guide.md](references/setup-guide.md) <br>
- [agent-guardrails.md](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, MCP tool calls, and structured command results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task UPIDs, audit-oriented status summaries, dry-run previews, diagnostic findings, and configuration paths.] <br>

## Skill Version(s): <br>
0.11.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
