## Description:

This skill helps agents configure and use gogcli MCP servers for Google Workspace automation across Docs, Sheets, Slides, Drive, and Classroom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect agents to gogcli-based MCP servers for Google Workspace document, spreadsheet, presentation, file, and classroom workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install target can use a local Google account more broadly than the artifact clearly describes.

Mitigation: Review the actual gogcli-mcp package capabilities before installing, prefer the narrow subpackage needed for the task, and set GOG_ACCOUNT explicitly.

Risk: Google Workspace actions can affect documents, files, permissions, grades, or raw API behavior.

Mitigation: Require confirmation before delete, share, send, grade, permission, or raw API actions.

## Reference(s):

- [gogcli](https://github.com/chrischall/gogcli)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP server configuration snippets, package-selection guidance, and Google account environment variables.]

## Skill Version(s):

2.21.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
