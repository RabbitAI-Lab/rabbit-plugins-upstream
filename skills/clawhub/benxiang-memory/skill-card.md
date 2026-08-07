## Description:

Shadow Memory is a local stdio MCP server workflow that persists project state in a .origin package so agents can recover context, commit semantic state changes, and inspect why facts, tasks, decisions, risks, and modules have their current values.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to preserve auditable project state across chat sessions and multi-agent work. It is suited for projects where facts, decisions, tasks, risks, and workspace modules need persistent history, evidence, and accountability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on locally cloned MCP server code and a local .origin package.

Mitigation: Use a trusted source for the protocol repository, inspect the MCP server before installation, and keep the .origin package in a project-specific location.

Risk: Committed state may contain persistent project facts, decisions, task history, or other sensitive material.

Mitigation: Avoid storing secrets or private material unless intentional, and review committed memory data as durable project records.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dongsheng123132/skills/benxiang-memory)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist project facts, decisions, tasks, risks, modules, and history in a local .origin package through MCP tools.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
