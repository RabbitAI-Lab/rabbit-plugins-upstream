## Description:

Provides VMware Aria Operations and VCF Operations monitoring assistance for metrics, alerts, capacity, anomalies, reports, resource maintenance, platform health, and related operational lookup tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site reliability engineers, and infrastructure operators use this skill to inspect VMware Aria Operations data, triage alerts, review capacity and anomaly signals, generate reports, and manage limited Aria-side operational states. It is read-heavy, with write actions limited to alert state, alert notes, alert definitions, report generation/deletion, and resource maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release installs external code that will handle VMware Aria credentials.

Mitigation: Verify the package source and release integrity, pin version 1.15.0, and use a secret manager or injected environment variables for production credentials.

Risk: Some tools can perform infrastructure-affecting write actions such as alert changes, report changes, and resource maintenance.

Mitigation: Use a read-only Aria service account unless write actions are required, require explicit approval for write workflows, and rely on the documented audit logging for write activity.

Risk: Network access to unintended endpoints could expose operational credentials or data.

Mitigation: Restrict tool network access to the intended VMware Aria endpoint and verify TLS configuration during setup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aria)
- [Project homepage](https://github.com/vmware-skills/VMware-Aria)
- [Setup Guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [CLI Reference](references/cli-reference.md)
- [Ops Playbooks](references/ops-playbooks.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured operational summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI commands, MCP tool suggestions, JSON-like result interpretation, and operational caveats for VMware Aria data.]

## Skill Version(s):

1.15.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
