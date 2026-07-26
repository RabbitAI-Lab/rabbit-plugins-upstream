## Description: <br>
Use this skill when an agent needs VMware Aria Operations data for performance metrics, alerts, capacity planning, anomaly detection, and automated reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operations teams use this skill to inspect VMware Aria Operations environments, investigate alerts, analyze capacity and anomalies, and generate reports. It is read-heavy, with audited write actions limited to alert state changes, alert definition management, and report generation or deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access VMware Aria Operations data and includes limited administrative write actions. <br>
Mitigation: Install it only for agents that should access VMware Aria Operations, use least-privilege or read-only service accounts unless writes are required, and review the audit log for acknowledged, canceled, generated, or deleted objects. <br>
Risk: Credentials may be stored in local VMware Aria configuration files. <br>
Mitigation: Keep ~/.vmware-aria/.env locked down and prefer external secret injection when stronger protection is required. <br>
Risk: Disabling TLS verification can weaken protection for production connections. <br>
Mitigation: Keep SSL verification enabled in production. <br>


## Reference(s): <br>
- [VMware Aria source homepage](https://github.com/zw008/VMware-Aria) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>
- [Investigation Protocol](references/investigation-protocol.md) <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aria) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured operational summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include VMware Aria metric summaries, alert and capacity analysis, report workflow steps, and configuration guidance.] <br>

## Skill Version(s): <br>
1.8.8 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
