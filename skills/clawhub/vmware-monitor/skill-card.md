## Description:

VMware Monitor helps agents run read-only VMware vCenter and ESXi inventory, health, alarm, event, performance, capacity, and investigation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, infrastructure operators, and support engineers use this skill to inspect VMware environments, triage active issues, and prepare read-only investigation summaries before any operational change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Daemon and webhook features may expose VMware alarms, events, host-log snippets, or infrastructure names through local logs or configured endpoints.

Mitigation: Keep daemon and webhook features disabled unless needed, review the configured endpoint, and use a least-privilege read-only VMware account.

Risk: Stored VMware passwords are obfuscated with base64 rather than encrypted at rest.

Mitigation: Treat the password store as sensitive, restrict file permissions, and avoid storing passwords in the environment file when stronger secret storage is required.

Risk: The security summary flags Review-level risk because the skill's risk-free framing understates daemon and webhook data-handling concerns.

Mitigation: Review the package and source before production use, especially scheduled scanning, webhook delivery, and local logging behavior.

Risk: Some vSphere 9.1 REST response parsing is documented as best-effort pending replay against a live vSphere 9.1 vCenter.

Mitigation: Validate vSphere 9.1 memory tiering, vLCM compliance, last-apply, and deployment-size outputs against the target vCenter before relying on them for operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [VMware Monitor homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Capabilities](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [Investigation Protocol](artifact/references/investigation-protocol.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)
- [Cluster Health Summary Display Template](artifact/references/health-summary-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with VMware CLI commands, structured summaries, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include offline HTML snapshot file paths when users request saved health or investigation reports.]

## Skill Version(s):

1.8.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
