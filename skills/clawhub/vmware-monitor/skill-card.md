## Description: <br>
Provides read-only VMware vCenter and ESXi monitoring for inventory, alarms, events, health summaries, and object investigations without exposing destructive operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Infrastructure operators, SREs, and VMware administrators use this skill to ask agents for read-only vSphere inventory, health triage, alarm and event review, and object-centered investigations before deciding on manual or companion-skill remediation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose sensitive VMware inventory, alarms, sessions, host logs, VM details, and local credential references. <br>
Mitigation: Install only where the agent is authorized to read VMware infrastructure data, use least-privilege read-only vCenter accounts, protect ~/.vmware-monitor/.env, and prefer a real secret manager for production credentials. <br>
Risk: Continuous monitoring and webhook delivery can send operational alert metadata outside the local agent workflow when enabled. <br>
Mitigation: Start the daemon and configure Slack, Discord, or other webhook URLs only when ongoing monitoring and external alert delivery are intended. <br>
Risk: Read-only monitoring data can still be incomplete, point-in-time, or truncated in large environments. <br>
Mitigation: Check returned, total, truncated, and hint fields before summarizing list results, and treat performance or capacity readings as current observations rather than historical trends. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-monitor) <br>
- [Project homepage from ClawHub metadata](https://github.com/vmware-skills/VMware-Monitor) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Investigation Protocol](references/investigation-protocol.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>
- [Cluster Health Summary Template](references/health-summary-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, CLI tables, JSON-like MCP responses, and optional self-contained HTML snapshots.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only outputs; MCP list responses include returned, limit, total, truncated, and hint metadata.] <br>

## Skill Version(s): <br>
1.8.9 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
