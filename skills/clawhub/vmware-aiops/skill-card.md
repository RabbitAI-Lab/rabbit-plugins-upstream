## Description:

Helps operators manage VMware VMs, deployments, clusters, alarms, and infrastructure investigations through agent-guided workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware administrators and infrastructure engineers use this skill to investigate VM and host issues and coordinate VM lifecycle, deployment, cluster, and alarm operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: VM, cluster, and network changes or deletions can disrupt infrastructure.

Mitigation: Use a dedicated least-privilege account and explicit allow-lists or deny rules; review destructive actions before execution.

Risk: Guest command execution and file transfer can affect VMs beyond vCenter access limits.

Mitigation: Avoid privileged guest credentials and require human review of guest operations.

Risk: TTL deletion, plan application, and alarm resets can cause unexpected changes or hide active issues.

Mitigation: Review their scope and impact with an operator before approval; expose read-only tools by default.

## Reference(s):

- [VMware AIops project homepage](https://github.com/vmware-skills/VMware-AIops)
- [Setup guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [Capabilities](artifact/references/capabilities.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include infrastructure findings and proposed actions for human review.]

## Skill Version(s):

2.4.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
