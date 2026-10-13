## Description:

Helps agents manage VMware VMs and infrastructure through lifecycle, deployment, guest operations, alarm management, and health investigation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and developers use this skill to provision and manage VMware VMs, investigate VM and cluster issues, and handle vCenter alarms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-initiated writes can change or delete VMware infrastructure, including operations that act on the first call.

Mitigation: Use a dedicated least-privilege vCenter/ESXi account, configure deny rules before production use, and require human approval for infrastructure writes.

Risk: Guest command execution and uploads can affect VMs and expose privileged guest credentials to the agent.

Mitigation: Avoid passing privileged guest credentials through MCP; use least-privilege guest accounts and approve guest operations explicitly.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project homepage (declared in skill metadata)](https://github.com/vmware-skills/VMware-AIops)
- [Setup guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Analysis]

**Output Format:** [Text and Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents in performing VMware infrastructure operations.]

## Skill Version(s):

1.12.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
