## Description: <br>
vmware-aria helps agents query and administer VMware Aria Operations data for performance metrics, alerts, capacity planning, anomaly detection, reports, and platform health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to monitor VMware Aria Operations environments, investigate alerts and anomalies, plan capacity, generate reports, and perform approved alert, alert-definition, and report writes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query and administer VMware Aria Operations, including alert, report, and alert-definition writes. <br>
Mitigation: Install only for agents intended to work with Aria Operations, use a read-only Aria account for monitoring-only workflows, and require explicit approval for write actions. <br>
Risk: The skill uses local configuration, credential environment files, and audit logs for Aria Operations access. <br>
Mitigation: Keep ~/.vmware-aria/.env and ~/.vmware/audit.db tightly permissioned, avoid storing passwords in config.yaml, and prefer managed secret injection for production deployments. <br>
Risk: Incorrect or incomplete operational conclusions could mislead capacity, alert, or anomaly response. <br>
Mitigation: Review list-result truncation, preserve Aria criticality and status values, and use the investigation protocol before presenting root-cause conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aria) <br>
- [VMware Aria homepage](https://github.com/vmware-skills/VMware-Aria) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Investigation Protocol](references/investigation-protocol.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, tables, and JSON-style summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include operational findings, capacity forecasts, alert or report status, and setup or approval guidance.] <br>

## Skill Version(s): <br>
1.8.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
