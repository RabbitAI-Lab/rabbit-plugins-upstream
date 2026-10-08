## Description:

Connects agents to personal Outlook mail, calendars, contacts, and tasks through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users connect a personal Outlook account to read and organize mail, calendars, contacts, and tasks, with optional user-approved write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent access to personal Outlook data and optional write actions may expose or alter sensitive content.

Mitigation: Start in read-only mode, use separate read-only consent when needed, and enable only necessary write categories.

Risk: Downloaded attachments may contain sensitive data.

Mitigation: Keep the permitted attachment directory narrow and grant access only when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [outlook-graph-mcp package](https://pypi.org/project/outlook-graph-mcp/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured MCP tool results and text prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected mailbox and enabled permissions.]

## Skill Version(s):

1.25.1 (source: ClawHub release, CHANGELOG.md, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
