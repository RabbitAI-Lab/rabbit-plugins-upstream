## Description:

Access Artsonia student-art portfolios, comments, and fans via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to an Artsonia MCP server for student portfolios, artwork details, comments, fans, downloads, and notification preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses Artsonia account credentials and maintains a session cookie, so account access and the session cache are sensitive.

Mitigation: Install only from a trusted package source, provide credentials only in a trusted local environment, and disable or relocate the session cache on shared machines.

Risk: Student artwork, comments, downloaded images, metadata sidecars, embedded image metadata, and manifests can contain sensitive student or family information.

Mitigation: Use a private local download destination, avoid embedding or writing metadata unless needed, and review whether private artwork should be excluded before downloading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package](https://www.npmjs.com/package/artsonia-mcp)
- [artsonia-mcp source link from artifact](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agent use of an MCP server that can return portfolio data, comments, fan information, downloaded files, image metadata, and local manifests.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
