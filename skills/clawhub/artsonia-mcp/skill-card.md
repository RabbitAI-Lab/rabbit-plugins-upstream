## Description:

Connects an agent to Artsonia student-art portfolios, artwork, comments, fans, and notifications through an authenticated MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and fans with an Artsonia account use an agent to view student artwork and activity, manage comments or fan invitations, and adjust notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to an Artsonia login exposes children's artwork and account information to the MCP server.

Mitigation: Use only with an account authorized to access the students' data and protect the login credentials.

Risk: Comments and fan invitations can change an account or contact others if confirmation is bypassed; some other actions run without confirmation.

Mitigation: Keep confirmation mode at ask-user or refuse, never auto, and review each write before calling the tool.

Risk: Downloaded artwork, including private pieces and associated metadata, can persist on disk.

Mitigation: Set a constrained output directory, exclude private pieces when unnecessary, and review or delete downloaded files after use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package](https://www.npmjs.com/package/artsonia-mcp)
- [Project repository linked in skill documentation](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Image files]

**Output Format:** [MCP tool responses and optional downloaded artwork images or metadata files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Artwork downloads may include private images and persistent metadata; some account changes run without a confirmation step.]

## Skill Version(s):

1.3.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
