## Description:

Connects an agent to Artsonia to view student artwork, comments, and fans and manage account interactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and fans use an agent to browse linked students' artwork and activity, read comments and feedback, download images, and manage comments, fan invitations, or notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Artsonia credentials and cached sessions grant access to a user's account.

Mitigation: Install only if you trust the Artsonia MCP package, protect credentials in the MCP configuration, and review or disable session caching as appropriate.

Risk: Comments, fan invitations, notification changes, and artwork downloads can affect the account or children's artwork privacy.

Mitigation: Keep write confirmations enabled and review the preview and destination before approving these actions.

## Reference(s):

- [Artsonia MCP package](https://www.npmjs.com/package/artsonia-mcp)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Text and Markdown with MCP configuration examples and tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Artwork downloads can produce image files and optional JSON indexes or metadata sidecars.]

## Skill Version(s):

1.2.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
