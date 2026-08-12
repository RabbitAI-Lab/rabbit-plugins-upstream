## Description:

Helps agents use gogcli-backed MCP servers for Google Workspace automation across Docs, Sheets, Slides, Drive, and Classroom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to configure and operate gogcli MCP servers for Google Workspace document, spreadsheet, presentation, Drive, and Classroom workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent act through a locally authenticated Google Workspace account for high-impact Docs, Drive, Sheets, Slides, or Classroom operations.

Mitigation: Use a dedicated or least-privileged Google account where possible, set GOG_ACCOUNT explicitly, and confirm before edits, uploads, downloads, permission changes, grading, or Classroom actions.

Risk: Shared gogcli authentication can make it unclear which Google account an MCP server will use.

Mitigation: List authenticated gogcli accounts before use and configure the intended account in the MCP server environment.

## Reference(s):

- [gogcli GitHub repository](https://github.com/chrischall/gogcli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP server configuration snippets and gogcli authentication guidance.]

## Skill Version(s):

2.23.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
