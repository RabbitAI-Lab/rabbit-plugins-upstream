## Description:

Access Artsonia student-art portfolios, comments, fans, artwork downloads, and notification settings through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with Artsonia parent or fan accounts use this skill to view linked students' portfolios, inspect activity and artwork details, download artwork, manage fans, post comments, and update notifications through a registered Artsonia MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses unpinned external code and Artsonia credentials.

Mitigation: Install only a trusted package version or commit and provide credentials through protected environment configuration rather than checked-in project files.

Risk: The skill can access child portfolio data, including private artwork and downloads.

Mitigation: Confirm the account scope before use, restrict downloads to intended content, and review private-artwork options before saving files locally.

Risk: The skill can perform account-changing actions such as posting comments, inviting fans, and changing notifications.

Mitigation: Require explicit user confirmation before invoking write-capable tools.

Risk: Session caching can preserve authenticated access on disk.

Mitigation: Disable session caching when possible or protect the session cache path with appropriate local file permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [npm package](https://www.npmjs.com/package/artsonia-mcp)
- [Source repository](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return portfolio data, comments, fan lists, downloaded image files, metadata sidecars, and local index manifests depending on the invoked MCP tool.]

## Skill Version(s):

0.12.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
