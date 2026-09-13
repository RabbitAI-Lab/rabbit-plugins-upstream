## Description:

monitoring-aiops helps operations teams inspect and operate SolarWinds Orion, PRTG, and Zabbix monitoring environments with NOC overviews, read-only SWQL, alert rollups, health checks, and guarded maintenance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site reliability engineers, and NOC operators use this skill to triage monitoring state, answer SolarWinds SWQL questions, review PRTG and Zabbix health data, and perform audited maintenance actions across supported monitoring platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable monitoring actions can acknowledge alerts, suppress monitoring, alter maintenance windows, unmanage nodes, or remove nodes without an enforced skill-side approval gate.

Mitigation: Use read-only monitoring accounts by default, require external change approval before write-capable credentials are enabled, and rely on dry-run, double confirmation, time-boxing, audit logs, and undo where available.

Risk: Credential, TLS, and install hardening gaps could expose monitoring secrets or run an unreviewed release.

Mitigation: Enable TLS certificate verification in production, avoid secrets in command-line arguments or shell history, protect ~/.monitoring-aiops, and pin the package or plugin to a reviewed version.

Risk: Behavior is documented as tested against mocked SolarWinds, PRTG, and Zabbix responses and still needing live NOC verification.

Mitigation: Run doctor and limited live checks against non-production or low-impact targets before relying on the skill for operational changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/monitoring-aiops)
- [Project homepage](https://github.com/AIops-tools/Monitoring-AIops)
- [Capabilities reference](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and monitoring-operation recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include monitoring observations, triage steps, bounded query results, setup instructions, and proposed guarded write actions.]

## Skill Version(s):

0.10.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
