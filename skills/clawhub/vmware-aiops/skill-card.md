## Description:

VMware AIops helps agents manage VMware vSphere and ESXi VM lifecycle operations, deployments, guest operations, cluster changes, alarm handling, and infrastructure triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure administrators, developers, and operations engineers use this skill to let an agent perform VMware VM lifecycle, deployment, guest operation, alarm, and cluster-management workflows. It is intended for environments where the operator can provide least-privilege VMware credentials and review state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent high-impact VMware administration authority.

Mitigation: Install only for agents that are expected to administer VMware infrastructure, and use a dedicated least-privilege vCenter account.

Risk: MCP write calls can change infrastructure state without a built-in confirmation gate.

Mitigation: Require human review in the agent workflow before any MCP write call and configure policy deny rules for production targets.

Risk: Guest operations can run commands inside virtual machines with the supplied guest credentials.

Mitigation: Avoid root guest credentials unless necessary, omit guest credentials when guest operations are not needed, and scope guest accounts narrowly.

Risk: Webhook integrations may expose operational alerts outside the VMware environment.

Mitigation: Keep webhook destinations controlled and use only approved Slack or Discord endpoints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aiops)
- [Project homepage](https://github.com/vmware-skills/VMware-AIops)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Investigation protocol](references/investigation-protocol.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct an agent to call VMware CLI or MCP tools; outputs should preserve human review before write operations.]

## Skill Version(s):

1.8.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
