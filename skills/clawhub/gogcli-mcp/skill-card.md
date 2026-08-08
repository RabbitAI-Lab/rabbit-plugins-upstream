## Description:

This skill helps agents support Google Workspace automation through gogcli-backed MCP servers for Docs, Sheets, Slides, Drive, and Classroom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to configure agents that can help create, read, edit, search, and manage Google Workspace resources through gogcli MCP packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on a user's Google Workspace account and may affect Docs, Sheets, Slides, Drive, or Classroom data.

Mitigation: Use a dedicated or least-privilege Google account and require explicit confirmation before edits, uploads, downloads, Classroom changes, or Drive permission updates.

Risk: The all-in-one umbrella package can expose broad Workspace capabilities through shared gogcli authentication.

Mitigation: Install only the specific subpackages needed and review the npm package source before using the umbrella package with important Workspace data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp)
- [gogcli repository](https://github.com/chrischall/gogcli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may involve authenticated Google Workspace operations through locally configured gogcli credentials.]

## Skill Version(s):

2.19.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
