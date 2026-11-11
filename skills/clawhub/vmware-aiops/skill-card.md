## Description:

Use VMware AIops to manage VMware VM lifecycle, deployment, guest operations, alarms, clusters, and read-only infrastructure triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and VMware administrators use this skill to inspect VMware environments and manage VM, deployment, guest, alarm, and cluster workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks this release suspicious because reported host-network capabilities exceed the stated scope and part of the capability documentation could not be fully inspected.

Mitigation: Review the host-network capabilities and complete capability documentation before use; enable only necessary network changes and use a least-privilege VMware account.

## Reference(s):

- [Capabilities and permission boundaries](artifact/references/capabilities.md)
- [Setup guide](artifact/references/setup-guide.md)
- [Investigation protocol](artifact/references/investigation-protocol.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [CLI reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, VM operation plans]

**Output Format:** [Markdown responses with text guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe state-changing VMware operations; available actions depend on the configured account's permissions.]

## Skill Version(s):

2.5.0 (source: server-resolved release metadata, references/setup-guide.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
