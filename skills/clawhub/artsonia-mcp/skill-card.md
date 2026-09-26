## Description:

Helps agents access Artsonia student-art portfolios, activity, comments, and fans, and manage artwork downloads and account interactions through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized caregivers use an agent to view a student's Artsonia artwork and activity, review comments and fans, download artwork, and request confirmed changes to comments, invitations, or notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MCP server receives Artsonia login credentials and may cache a session locally.

Mitigation: Use only an authorized account, protect credentials and local session files, and disable the session cache if needed.

Risk: Artwork downloads may include private student images and metadata written to disk.

Mitigation: Check the destination and optional metadata settings before confirming; exclude private artwork when it is not needed.

Risk: Comments, fan invitations, notification changes, and downloads can affect an account or create local files.

Mitigation: Keep confirmation mode at its default, review the preview, and approve only the intended action.

## Reference(s):

- [Artsonia MCP skill on ClawHub](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration instructions]

**Output Format:** [Agent responses and optional downloaded images or JSON metadata files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Artwork downloads and account changes require confirmation by default.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
