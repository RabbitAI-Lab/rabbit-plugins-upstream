## Description:

Guides front-line deployment engineers through enterprise AI discovery, delivery, auditing, and ongoing improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Front-line deployment engineers and enterprise teams use this skill to assess AI workflows, plan and deliver agent-based processes, audit changes, and document operational handoff and maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can change local agent configuration and give the harness persistent control over agent behavior.

Mitigation: Inspect the actual installer and MCP registry before installation; approve configuration changes and grant only necessary roles and tools.

Risk: Background maintenance and high-impact tools can perform actions beyond the intended deployment workflow.

Mitigation: Disable daemon, sustain, model-training, publishing, and device tools unless expressly required.

Risk: Task logs, knowledge records, audit reports, and device heartbeats may contain sensitive enterprise data.

Mitigation: Confirm where these records are stored or sent and apply appropriate access and retention controls.

## Reference(s):

- [FDE Skill on ClawHub](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Core rules](artifact/rules/core-rules.md)
- [Delivery workflow](artifact/skills/04-deliver.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown with checklists and configuration or command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include audit reports, deployment plans, enterprise-specific skill documents, and improvement recommendations.]

## Skill Version(s):

1.5.9 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
