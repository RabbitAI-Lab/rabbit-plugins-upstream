## Description:

Configure, verify, repair, or minimize Dataify MCP for Claude Desktop, Codex, Cursor, Windsurf, or another MCP client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to configure Dataify MCP connections, select the smallest useful tool preset, inspect existing MCP configuration with credential redaction, and verify the MCP server connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataify API tokens can be stored in selected MCP client configuration URLs and backup files on the local machine.

Mitigation: Use a scoped or revocable token, avoid sharing configuration files or support bundles, and rotate the token if those files may have been exposed.

## Reference(s):

- [Dataify Documentation](https://doc.dataify.com)
- [Dataify Support](https://www.dataify.com/)
- [Tool presets](references/tool-presets.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include redacted inspection output, backup-file paths, and protocol verification status.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
