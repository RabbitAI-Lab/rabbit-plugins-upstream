## Description:

Access Artsonia student-art portfolios, comments, and fans via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure and operate an Artsonia MCP server for viewing student artwork portfolios, checking comments and fans, downloading artwork, posting comments, inviting fans, and managing Artsonia notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles children's artwork and related metadata, which can be sensitive if copied into shared folders, synced storage, or broad agent context.

Mitigation: Use explicit prompts before downloads, choose private local destinations, and avoid shared or synced folders for children's artwork and metadata.

Risk: The MCP server uses Artsonia credentials and can persist session data locally.

Mitigation: Install only from a trusted package source, protect Artsonia credentials, and disable or redirect the session cache when local session persistence is not acceptable.

Risk: Social actions such as posting comments, inviting fans, and changing notifications can affect an Artsonia account.

Mitigation: Require explicit user confirmation before social or notification-changing actions and review generated comments before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [npm package: artsonia-mcp](https://www.npmjs.com/package/artsonia-mcp)
- [Project repository](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Artsonia account summaries, artwork metadata, comment and fan information, local download paths, and notification-setting guidance when the MCP server is configured.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
