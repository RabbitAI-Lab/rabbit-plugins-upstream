## Description: <br>
Provides read-only VMware vCenter/ESXi monitoring, inventory, health triage, alarm and event review, performance and capacity checks, and object-centered investigation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, infrastructure engineers, and operations teams use this skill to query VMware vCenter/ESXi inventory, health, alarms, events, capacity, and object-centered investigations without write operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: VMware inventory, sessions, events, and host logs can expose sensitive operational information. <br>
Mitigation: Run the skill with a least-privilege read-only VMware account and restrict local configuration and audit files to authorized users. <br>
Risk: Continuous monitoring and webhook notifications can send aggregated alert metadata outside the local agent environment when enabled. <br>
Mitigation: Start the daemon only when continuous monitoring is required and configure Slack, Discord, or webhook URLs only for approved destinations. <br>
Risk: Per-target VMware credentials are configured through local environment files. <br>
Mitigation: Keep the environment file access-restricted, avoid plaintext secrets for production deployments where possible, and review configuration before installation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-monitor) <br>
- [VMware Monitor Repository](https://github.com/zw008/VMware-Monitor) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Investigation Protocol](references/investigation-protocol.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>
- [Cluster Health Summary Display Template](references/health-summary-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance, CLI commands, structured JSON-style tool results, rendered tables, and optional self-contained HTML snapshot files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only VMware monitoring output may include inventory, alarms, events, performance samples, capacity checks, suggested actions, and audit-aware command guidance.] <br>

## Skill Version(s): <br>
1.8.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
