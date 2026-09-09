## Description:

gogcli-mcp helps agents set up and use gogcli-backed MCP servers for Google Workspace automation across Docs, Sheets, Slides, Drive, and Classroom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Google Workspace users use this skill to configure MCP servers that let an agent work with Docs, Sheets, Slides, Drive, and Classroom through an authenticated gogcli account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configured MCP servers act through an authenticated Google account and can affect Google Workspace content.

Mitigation: Install only for intended accounts and prefer a dedicated or least-privilege Google account where practical.

Risk: If multiple gogcli accounts are available, actions may run against the wrong account.

Mitigation: Set GOG_ACCOUNT explicitly in the MCP server environment.

Risk: npm package updates may change the behavior of the installed MCP server packages.

Mitigation: Review the package source and version before use, especially before allowing broad access.

Risk: Document edits, grading actions, or Drive permission changes may be destructive or expose data.

Mitigation: Require confirmation before destructive changes, grading updates, or sharing-permission changes.

## Reference(s):

- [gogcli GitHub project](https://github.com/chrischall/gogcli)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs setup guidance for MCP server configuration and gogcli authentication.]

## Skill Version(s):

2.28.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
