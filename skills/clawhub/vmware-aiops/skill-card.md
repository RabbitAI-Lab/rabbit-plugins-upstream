## Description: <br>
vmware-aiops helps agents manage VMware/vSphere/ESXi VMs, deployments, guest operations, clusters, alarms, and triage workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
VMware operators and infrastructure engineers use this skill to automate VM lifecycle tasks, deployment workflows, guest operations, cluster administration, alarm handling, and investigation-driven remediation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify VMware infrastructure, including VM lifecycle, guest operation, cluster, alarm, and limited underlay-network actions. <br>
Mitigation: Install it only for trusted VMware operators, use a dedicated least-privilege vCenter account, and require operator review before state-changing actions. <br>
Risk: Production changes may affect live workloads or shared infrastructure. <br>
Mitigation: Configure policy deny rules or maintenance windows for production targets and prefer dry-runs or plan review where supported. <br>
Risk: Guest execution and file transfer can run commands inside managed VMs. <br>
Mitigation: Avoid root guest credentials unless strictly necessary and review each guest exec or file transfer request carefully. <br>
Risk: TLS verification bypass is available for isolated lab environments. <br>
Mitigation: Keep TLS verification enabled in production and use CA-signed certificates for production vCenter or ESXi endpoints. <br>
Risk: Read-only VMware questions do not require the write surface exposed by this skill. <br>
Mitigation: Use vmware-monitor for inventory, health, events, and other read-only questions. <br>


## Reference(s): <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Capabilities Reference](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Investigation Protocol](references/investigation-protocol.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>
- [VMware-AIops source homepage](https://github.com/zw008/VMware-AIops) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI and MCP tool names, shell command examples, operational plans, and risk notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include confirmations, dry-run recommendations, and follow-up checks before VMware state changes.] <br>

## Skill Version(s): <br>
1.8.10 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
