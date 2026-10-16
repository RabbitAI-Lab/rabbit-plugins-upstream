## Description:

Helps Ceph operators diagnose cluster health and capacity and carry out audited maintenance through the Ceph Dashboard API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Ceph administrators and infrastructure engineers use this skill to investigate cluster alerts, inspect storage health and capacity, and plan or execute Ceph maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP writes can delete storage resources or change replica size without an enforced approval gate.

Mitigation: Start with a dedicated read-only Ceph Dashboard account; grant write access only for controlled maintenance and require external human approval before destructive MCP writes.

## Reference(s):

- [Ceph AIops project homepage](https://github.com/AIops-tools/Ceph-AIops)
- [Ceph AIops on ClawHub](https://clawhub.ai/zw008/skills/ceph-aiops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides diagnostic findings and suggested actions; maintenance operations can change cluster state.]

## Skill Version(s):

0.13.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
