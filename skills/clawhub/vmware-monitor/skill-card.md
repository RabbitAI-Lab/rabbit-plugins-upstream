## Description:

Provides read-only VMware vCenter and ESXi inventory, health monitoring, and incident investigation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to inspect VMware inventory, triage alarms and events, assess cluster health, and investigate VMs, hosts, and datastores without changing vSphere resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monitoring access may expose sensitive infrastructure data and locally stored credentials.

Mitigation: Use a dedicated read-only VMware service account rather than administrator credentials, and prefer a secret manager over a local .env file in production.

Risk: Optional webhook notifications may disclose hostnames, IPs, usernames, alarms, events, or log excerpts.

Mitigation: Enable webhooks only for destinations approved to receive that infrastructure information.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Project homepage (listed in metadata)](https://github.com/vmware-skills/VMware-Monitor)
- [Setup guide](artifact/references/setup-guide.md)
- [Capabilities](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Investigation protocol](artifact/references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries and tables with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide generation of local HTML health snapshots; infrastructure data may be sensitive.]

## Skill Version(s):

2.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
