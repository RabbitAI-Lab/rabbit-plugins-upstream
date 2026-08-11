## Description:

Monitoring AIops helps agents operate SolarWinds Orion, Paessler PRTG, and Zabbix monitoring environments with status queries, alert rollups, and audited guarded write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

NOC engineers, SREs, and monitoring operators use this skill to inspect SolarWinds Orion, PRTG, and Zabbix health, summarize active alerts, answer common SWQL questions, and run audited maintenance or suppression workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make high-impact monitoring changes without a built-in read-only or approval gate.

Mitigation: Use least-privilege monitoring accounts, start with read-only permissions where possible, and treat acknowledge, mute, unmanage, pause, delete-maintenance, and remove-node actions as change-controlled operations.

Risk: Credentials and the master password protect access to monitoring systems.

Mitigation: Store platform secrets in the encrypted secret store, avoid exporting the master password except through a controlled secret manager or ephemeral process environment, and enable SSL verification for production targets.

Risk: The artifact states that behavior has been exercised against mocked responses but not yet validated against a live NOC.

Mitigation: Run connectivity and live-platform checks such as doctor before operational use, and verify behavior on PRTG Freeware or a Zabbix test appliance before using the SolarWinds workflows in production.

## Reference(s):

- [Project homepage](https://github.com/AIops-tools/Monitoring-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/monitoring-aiops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured monitoring summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded monitoring tables, audit-oriented guidance, and dry-run or undo instructions for higher-risk operations.]

## Skill Version(s):

0.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
