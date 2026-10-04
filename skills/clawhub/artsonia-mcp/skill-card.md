## Description:

Connects an agent to Artsonia to view linked students' artwork, comments, fans, and activity and to manage comments, invitations, and notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and fans with linked Artsonia accounts use this skill to browse student portfolios and feedback, download artwork, post comments, invite fans, and adjust notifications through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Artsonia account credentials and linked student artwork, comments, fans, and notifications are accessible to the MCP server.

Mitigation: Install only if you trust the server with the account and its linked student data; keep credentials private.

Risk: Artwork downloads and session data may remain on a shared device.

Mitigation: Choose a private download location and disable or relocate the session cache on shared machines.

Risk: Comments, invitations, notification changes, and downloads can have unintended effects.

Mitigation: Keep the default confirmation mode and approve previews before writes or downloads.

## Reference(s):

- [Artsonia MCP skill release](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package (linked in skill)](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Files, Configuration instructions]

**Output Format:** [Structured tool results; optionally downloaded artwork images and JSON metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a registered Artsonia MCP server and account credentials; write actions request confirmation by default.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
