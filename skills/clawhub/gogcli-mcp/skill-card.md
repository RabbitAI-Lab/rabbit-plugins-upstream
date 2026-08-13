## Description:

This skill helps agents route Google Workspace automation requests through gogcli MCP servers for Docs, Sheets, Slides, Drive, and Classroom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure and invoke gogcli-based MCP servers for Google Workspace document, spreadsheet, presentation, file, and classroom workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route broad Google Workspace requests to tools that may edit files, change permissions, or affect Classroom data.

Mitigation: Install only the specific subpackage needed and require explicit confirmation before edits, permission changes, grading, uploads, downloads, or bulk operations.

Risk: The skill relies on an authenticated Google account available to gogcli on the local machine.

Mitigation: Use a least-privilege Google account where possible and set GOG_ACCOUNT when multiple accounts are configured.

## Reference(s):

- [gogcli tool](https://github.com/chrischall/gogcli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to perform Google Workspace operations through authenticated local gogcli MCP servers.]

## Skill Version(s):

2.23.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
