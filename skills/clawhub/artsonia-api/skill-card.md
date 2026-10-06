## Description:

Guides agents in accessing Artsonia student portfolios, comments, fans, feedback, and artwork through authenticated shell requests without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized parents and developers use this skill to retrieve student artwork and account information or perform approved account actions using shell commands instead of an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated access exposes private student and family content, credentials, session cookies, and downloaded artwork.

Mitigation: Use only accounts and content you are authorized to access; protect credentials, session cookies, downloaded pages, profile data, and artwork as sensitive.

Risk: Write commands can send real fan invitations or change live account and feedback state.

Mitigation: Require explicit approval of the exact action, recipient, artist or artwork ID, and expected effect before running any write command; re-read affected pages to check results.

## Reference(s):

- [Artsonia API skill release](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Artsonia endpoint recipes](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may retrieve account pages, student artwork, and profile data or submit account changes.]

## Skill Version(s):

1.2.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
