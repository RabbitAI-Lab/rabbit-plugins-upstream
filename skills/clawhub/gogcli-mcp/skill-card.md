## Description:

Gogcli-mcp helps agents route Google Workspace automation requests through gogcli-based MCP servers for Docs, Sheets, Slides, Drive, and Classroom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to configure agents for Google Workspace automation through a locally authenticated gogcli account. It is intended for document, spreadsheet, presentation, Drive, and Classroom workflows where the user can confirm the target account and resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to operate through a locally authenticated Google Workspace account.

Mitigation: Install it only when that account should be available to agents, and set or verify the intended account before use.

Risk: Workspace actions such as edits, uploads, downloads, permission changes, grading, or roster updates can affect real user data.

Mitigation: Confirm the target document, sheet, Drive item, class, account, and requested action before executing those operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp)
- [gogcli project reference](https://github.com/chrischall/gogcli)

## Skill Output:

**Output Type(s):** [Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed against the authenticated Google account and target Workspace resource before execution.]

## Skill Version(s):

2.25.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
