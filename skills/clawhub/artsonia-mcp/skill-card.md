## Description:

Helps agents access student artwork portfolios, comments, fans, and account notifications on Artsonia through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, fans, and their agents can view linked students' artwork and activity, manage comments and fans, adjust notifications, and download artwork with account authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Artsonia credentials and saved sessions could expose a parent or fan account.

Mitigation: Keep passwords, MCP configuration, .env files, and session caches private and out of source control.

Risk: Comments, fan invitations, notification changes, and artwork downloads can affect others or expose student artwork.

Mitigation: Review confirmation previews before approving actions and handle downloaded artwork, especially private pieces, carefully.

## Reference(s):

- [ClawHub artsonia-mcp release](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration, Files]

**Output Format:** [Markdown guidance, structured tool responses, and downloaded artwork images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account-changing actions and downloads require confirmation previews by default.]

## Skill Version(s):

1.2.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
