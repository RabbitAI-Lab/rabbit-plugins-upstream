## Description:

Provides read-only VMware vCenter and ESXi inventory, health summaries, alarms, events, and infrastructure investigation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to assess VMware health, investigate VMs, hosts, and datastores, and review alarms and events without changing vSphere resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infrastructure access can expose sensitive inventory and operational details.

Mitigation: Use a dedicated, least-privilege VMware account.

Risk: Locally stored credentials and audit data require protection.

Mitigation: Inject production passwords from a secret manager where possible and protect local configuration and logs.

Risk: Webhook alerts can send operational details to external destinations.

Mitigation: Enable webhooks only for trusted destinations.

Risk: A running monitoring daemon continues collecting operational data.

Mitigation: Start the daemon only when continuous monitoring is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Project homepage listed in metadata](https://github.com/vmware-skills/VMware-Monitor)
- [Setup guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [Investigation protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown health summaries, investigation findings, and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports read-only VMware observations; does not perform vSphere changes.]

## Skill Version(s):

2.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
