## Description:

Monitoring AIops lets agents operate SolarWinds Orion, Paessler PRTG, and Zabbix monitoring environments for NOC overviews, alert rollups, read-only SWQL queries, health checks, and governed write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and NOC operators use this skill to inspect and triage infrastructure monitoring data across SolarWinds, PRTG, and Zabbix, then perform audited maintenance or alert actions when explicitly authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes high-impact monitoring write actions without an enforced MCP approval or read-only gate.

Mitigation: Start with read-only SolarWinds, PRTG, or Zabbix credentials and require explicit human approval before MCP writes such as mute, unmanage, remove node, pause sensor, or delete maintenance.

Risk: Production monitoring access can expose sensitive credentials and operational state.

Mitigation: Use the encrypted credential setup, set the master password only through controlled environment configuration, and enable SSL verification for production targets.

Risk: Some behavior is documented as exercised against mocked monitoring responses rather than live NOC systems.

Mitigation: Run connectivity and behavior checks with `monitoring-aiops doctor` and validate workflows against low-impact PRTG or Zabbix environments before using production SolarWinds workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/monitoring-aiops)
- [Monitoring AIops homepage](https://github.com/AIops-tools/Monitoring-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to call MCP tools or CLI commands against configured SolarWinds, PRTG, or Zabbix targets; read results may be truncated and should be reported as such.]

## Skill Version(s):

0.10.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
