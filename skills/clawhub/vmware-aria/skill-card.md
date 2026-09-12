## Description:

vmware-aria helps agents use VMware Aria Operations and VCF Operations data for performance metrics, alerts, capacity planning, anomaly detection, and automated reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect VMware Aria Operations environments, investigate alerts, plan capacity, detect anomalies, and generate operational reports. It is primarily read-oriented, with limited audited write actions for alert state, alert definitions, and report management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and invokes an external Python package that connects to VMware Aria Operations using environment-provided credentials.

Mitigation: Review the exact package/source before deployment, restrict outbound access to approved Aria endpoints, and prefer a secret manager over a local .env file for production credentials.

Risk: The skill can perform write actions for alert acknowledgement or cancellation, alert definition management, and report management.

Mitigation: Use a read-only Aria service account by default, grant write permissions only when those workflows are required, and require explicit approval for write actions.

Risk: Local credential storage can expose Aria passwords if workstation or file permissions are weak.

Mitigation: Keep local credential files owner-readable only and avoid storing production passwords in local files when a managed secret store is available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aria)
- [VMware Aria homepage](https://github.com/vmware-skills/VMware-Aria)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational recommendations derived from VMware Aria Operations data; list results should be checked for truncation before summarizing.]

## Skill Version(s):

1.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
