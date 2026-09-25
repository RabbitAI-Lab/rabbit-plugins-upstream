## Description:

Access Artsonia student-art portfolios, comments, and fans via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an MCP client to Artsonia so they can inspect student artwork portfolios, comments, fans, notifications, and related account activity through natural-language requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Artsonia credentials and cached session data.

Mitigation: Install only from a trusted package source, provide credentials only in an appropriate local MCP configuration, and review or disable the session cache path when needed.

Risk: The skill can access or export student artwork, comments, feedback, and private portfolio data.

Mitigation: Treat exported files and metadata as private data, choose download destinations deliberately, and use options that exclude private pieces when sharing or archiving output.

Risk: Write-capable tools can post comments, invite fans, change notification settings, mark feedback read, or download artwork.

Mitigation: Keep confirmation mode at the default user-approval flow or refuse writes; avoid automatic confirmation unless the deployment explicitly accepts that risk.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [npm package](https://www.npmjs.com/package/artsonia-mcp)
- [Project source link from artifact](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Files, Markdown]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Artsonia account data, confirmation previews, downloaded artwork files, metadata sidecars, and index manifests depending on the invoked MCP tool.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
