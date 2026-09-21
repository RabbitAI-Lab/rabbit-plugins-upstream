## Description:

Access Artsonia student-art portfolios, comments, fans, notifications, and artwork downloads through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an Artsonia parent or fan account use this skill to connect an agent to Artsonia, retrieve student portfolios and artwork details, post comments, manage fans and notifications, and download artwork files when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses Artsonia account credentials and can access student portfolio data.

Mitigation: Install only when comfortable providing Artsonia credentials, keep credentials private, and limit use to authorized accounts and devices.

Risk: Artwork downloads, metadata embeds, indexes, sidecar files, and session data may persist child artwork, comments, teacher feedback, and account data locally.

Mitigation: Use private destination folders, enable metadata or sidecar options only when needed, and review locally stored files before sharing or retaining them.

Risk: Comment posting, fan invitations, and notification updates can change account-visible Artsonia state.

Mitigation: Review those actions before execution and use them only for intended students, artworks, recipients, and notification settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [npm package](https://www.npmjs.com/package/artsonia-mcp)
- [Source repository](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration, Shell commands, Files]

**Output Format:** [Markdown with JSON and bash code blocks; MCP tool responses may include text, structured records, and downloaded files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write downloaded artwork images, optional metadata sidecars, indexes, embedded image metadata, and session-cache files depending on configuration.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
