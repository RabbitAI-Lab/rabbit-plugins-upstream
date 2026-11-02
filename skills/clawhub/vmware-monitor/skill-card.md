## Description:

Provides read-only monitoring, health triage, inventory, and object investigations for VMware vCenter and ESXi environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware administrators and infrastructure engineers use this skill to review vCenter and ESXi health, inventory, alarms, events, capacity, and performance, and to investigate a VM, host, or datastore. Its queries are read-only toward VMware infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: VMware credentials and local audit records can expose sensitive infrastructure access or activity.

Mitigation: Use a dedicated Read-Only VMware account, protect credential and audit files, and keep certificate verification enabled.

Risk: Optional alerts can send infrastructure details to configured Slack or Discord destinations.

Mitigation: Enable webhooks only for destinations approved to receive infrastructure details.

Risk: Saved health reports contain local infrastructure details.

Mitigation: Store and share generated reports only in locations with appropriate access controls.

## Reference(s):

- [Project repository](https://github.com/vmware-skills/VMware-Monitor)
- [Setup guide](references/setup-guide.md)
- [Capabilities reference](references/capabilities.md)
- [Investigation protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Structured VMware query results, concise Markdown summaries, and optional standalone HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on configured targets, available account privileges, and returned VMware data; optional reports are local snapshots.]

## Skill Version(s):

2.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
