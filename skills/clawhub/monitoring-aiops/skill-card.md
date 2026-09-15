## Description:

Monitoring AIops helps agents operate SolarWinds Orion, PRTG, and Zabbix monitoring environments with read workflows, alert rollups, health checks, guarded maintenance actions, auditing, and undo support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure, NOC, and SRE teams use this skill to inspect and operate SolarWinds Orion, PRTG, and Zabbix monitoring estates through an agent. It is intended for alert triage, read-only monitoring questions, health checks, and guarded maintenance workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can suppress or remove monitoring coverage through maintenance, unmanage, pause, and deletion workflows.

Mitigation: Start with a read-only monitoring account, require external approval for write-capable credentials, prefer time-boxed maintenance, and use dry-run and double confirmation for high-risk operations.

Risk: Credential and local state handling can expose sensitive monitoring access if the runtime environment is weakly controlled.

Mitigation: Pin a known package version, protect MONITORING_AIOPS_HOME, tightly control MONITORING_AIOPS_MASTER_PASSWORD, and migrate away from legacy plaintext secret environment variables.

Risk: Weak TLS defaults can make production monitoring connections vulnerable to untrusted certificates.

Mitigation: Enable verify_ssl with a trusted CA for production targets.

Risk: Live-environment behavior may differ from mocked SWIS, PRTG, or Zabbix responses.

Mitigation: Run doctor and staged read-only checks against the intended monitoring platform before allowing write-capable operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/monitoring-aiops)
- [Project homepage](https://github.com/AIops-tools/Monitoring-AIops)
- [Capabilities reference](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with inline shell commands, configuration snippets, and monitoring-operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform-specific monitoring identifiers, truncated-result notices, audit guidance, and guarded write or undo recommendations.]

## Skill Version(s):

0.10.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
