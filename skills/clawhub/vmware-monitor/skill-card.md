## Description:

Helps agents inspect VMware vCenter and ESXi inventory, health, alarms, events, and performance without changing infrastructure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to triage VMware environments, investigate VMs, hosts, and datastores, and review read-only health and activity reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infrastructure credentials may be exposed if stored insecurely or granted excessive privileges.

Mitigation: Use a dedicated least-privilege VMware account, preferably with the Read-Only role; inject credentials or use a secrets manager rather than storing production passwords in .env.

Risk: Optional webhook alerts may disclose hostnames, IP addresses, usernames, alarm or event text, and connection errors.

Mitigation: Enable webhooks only for trusted destinations authorized to receive operational data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Project homepage](https://github.com/vmware-skills/VMware-Monitor)
- [Setup guide](artifact/references/setup-guide.md)
- [Investigation protocol](artifact/references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown summaries with optional structured query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local HTML health snapshots and opt-in webhook alerts.]

## Skill Version(s):

2.4.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
