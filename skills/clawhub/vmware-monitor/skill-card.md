## Description:

This skill provides read-only VMware/vSphere/ESXi inventory, health, alarm, event, and VM/host/datastore investigations, including cross-cluster and cross-vCenter triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and VMware administrators use the skill to inspect vSphere inventory, review alarms and events, and triage health or capacity issues across hosts, clusters, datastores, and vCenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was benign but had medium confidence and partial coverage; the supplied security guidance also calls out installation and credential setup.

Mitigation: Review the installation and credential steps before use, and connect with a dedicated vSphere Read-Only account while keeping TLS verification enabled.

Risk: When enabled, webhook alerts can disclose entity names and sanitized alarm, event, or log text that may include hostnames, IP addresses, and usernames.

Mitigation: Leave webhooks disabled unless needed, and only configure destinations approved to receive operational data.

## Reference(s):

- [Setup guide](references/setup-guide.md)
- [Capabilities reference](references/capabilities.md)
- [Investigation protocol](references/investigation-protocol.md)
- [Project homepage](https://github.com/vmware-skills/VMware-Monitor)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-monitor)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Configuration guidance, Shell commands]

**Output Format:** [Readable Markdown summaries and operational guidance; optional self-contained HTML health snapshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only VMware findings may include inventory names, health details, alarms, and events. Optional HTML snapshots are written locally.]

## Skill Version(s):

2.6.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
