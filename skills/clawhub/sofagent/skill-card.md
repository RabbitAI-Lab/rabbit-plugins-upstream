## Description:

sofagent is an FDE governance skill that helps front-line deployment engineers structure enterprise AI rollouts, constrain agent behavior, audit changes, and preserve operational knowledge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, front-line deployment engineers, and enterprise IT teams use this skill to map business workflows, identify AI-ready nodes, define knowledge and constraint layers, guide deployment, and run ongoing audit-oriented maintenance. It is intended for enterprise AI implementation and governance workflows rather than simple chat, one-step lookup, or standalone application coding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad operational authority and can guide persistent local memory, logs, knowledge bases, orchestrators, agents, and deployment state.

Mitigation: Use it only in a controlled enterprise workspace, scope retention and redaction before use, and review generated deployment state before activation.

Risk: The skill may guide shell-orchestrated actions such as install, activation, snapshots, market operations, USB deployment, or daemon-backed workflows.

Mitigation: Require human confirmation for operational commands and run them with least-privilege access in the intended target environment.

Risk: Enterprise workflow discovery can involve sensitive business, personal, or regulated data.

Mitigation: Avoid providing secrets or regulated data unless redaction, local storage boundaries, access controls, and retention policies are configured and verified.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Publisher Profile](https://clawhub.ai/user/kongfangxun)
- [Main Skill Definition](artifact/SKILL.md)
- [Agent Index](artifact/AGENTS.md)
- [Delivery Phase Guide](artifact/skills/04-deliver.md)
- [Exit and Sustain Phase Guide](artifact/skills/05-exit.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, structured checklists, deployment instructions, and audit summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include enterprise workflow descriptions, node-level deployment artifacts, skill instructions, audit summaries, reflection records, and maintenance guidance.]

## Skill Version(s):

1.3.5 (source: evidence.release.version and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
