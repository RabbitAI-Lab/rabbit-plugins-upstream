## Description:

Use this skill when an agent needs VMware Aria Operations or VCF Operations data for performance metrics, alerts, capacity planning, anomaly detection, and automated reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to query VMware Aria Operations data, investigate alerts, check capacity forecasts, identify anomalies, and generate operational reports from Aria data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform limited write actions, including alert cancellation, alert definition changes, report generation, and deletion.

Mitigation: Require explicit confirmation before those actions and use least-privilege or read-only Aria accounts when possible.

Risk: Aria Operations credentials are needed for configured targets.

Mitigation: Protect the .env credential file and avoid storing passwords in config files.

Risk: Disabling TLS verification can reduce connection assurance outside isolated labs.

Mitigation: Keep verify_ssl:true for normal deployments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-aria)
- [VMware Aria GitHub Repository](https://github.com/vmware-skills/VMware-Aria)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Text]

**Output Format:** [Markdown and text with inline shell commands and operational findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Aria Operations metrics, alert summaries, capacity forecasts, anomaly findings, report links, and setup guidance.]

## Skill Version(s):

1.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
