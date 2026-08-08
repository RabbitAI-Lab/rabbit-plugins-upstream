## Description: <br>
Monitoring AIops helps agents operate SolarWinds Orion, Paessler PRTG, and Zabbix monitoring environments with read workflows, alert triage, audited writes, and maintenance operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, SREs, and NOC operators use this skill to inspect monitoring state, answer SWQL questions, triage active alerts, and perform guarded maintenance actions across SolarWinds Orion, PRTG, and Zabbix environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make real monitoring-system changes without a built-in read-only or approval gate. <br>
Mitigation: Start with least-privilege or read-only monitoring accounts, require external human approval and change-control for writes, and use dry-run and double confirmation for high-risk operations. <br>
Risk: Reusable monitoring credentials are stored locally. <br>
Mitigation: Protect the monitoring-aiops home directory, avoid long-lived exported master passwords, and use the encrypted secret store and rotation or migration commands described by the setup guide. <br>
Risk: Production use can be weakened if TLS verification remains disabled for self-signed lab environments. <br>
Mitigation: Enable TLS verification for production targets and review target configuration before connecting to live monitoring systems. <br>


## Reference(s): <br>
- [Capabilities Reference](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Setup and Security Guide](references/setup-guide.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>
- [Project homepage](https://github.com/AIops-tools/Monitoring-AIops) <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/monitoring-aiops) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured monitoring results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can surface monitoring status, alert rollups, SWQL answers, maintenance guidance, and audited write outcomes for configured monitoring targets.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
