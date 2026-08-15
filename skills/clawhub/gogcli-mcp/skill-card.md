## Description:

This skill helps agents use gogcli-backed MCP servers for Google Workspace automation across Docs, Sheets, Slides, Drive, and Classroom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users install this skill when they want an agent to configure or operate gogcli MCP packages for Google Workspace tasks such as editing documents, updating spreadsheets, finding slides, managing Drive files, or working with Classroom data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated use can access or modify sensitive Google account data, including Drive permissions, Classroom roster or submission data, and document content.

Mitigation: Install only the narrowest gogcli MCP package needed, authenticate only the intended Google account, and review sensitive Drive, Classroom, and document-edit actions before execution.

## Reference(s):

- [gogcli](https://github.com/chrischall/gogcli)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP server configuration snippets and authentication guidance.]

## Skill Version(s):

2.24.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
