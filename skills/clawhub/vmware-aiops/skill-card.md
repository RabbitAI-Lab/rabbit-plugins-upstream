## Description:

Helps operators investigate and manage VMware virtual machines, clusters, deployments, guest operations, and vCenter alarms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to triage VMware environments and carry out VM lifecycle, deployment, guest, cluster, and alarm-management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact infrastructure changes can disrupt or delete virtual machines and clusters.

Mitigation: Use a dedicated least-privilege vCenter/ESXi account, configure deny rules before connecting production targets, and review change previews before confirming.

Risk: Guest commands run with supplied credentials, and guest passwords passed to MCP tools are visible to the agent.

Mitigation: Avoid root or administrator guest accounts; use limited guest credentials and do not pass secrets unless guest operations are necessary.

Risk: Granting write access when only monitoring is needed creates unnecessary exposure.

Mitigation: Use a read-only companion skill for monitoring-only tasks.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project homepage listed in skill metadata](https://github.com/vmware-skills/VMware-AIops)
- [Setup and security guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown explanations and command examples; structured tool results where supported]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include environment triage, change previews, and operation outcomes.]

## Skill Version(s):

2.0.0 (source: ClawHub release metadata and skill installation instructions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
