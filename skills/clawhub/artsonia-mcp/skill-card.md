## Description:

Accesses Artsonia student-art portfolios, comments, fans, notifications, and artwork downloads through an installed artsonia-mcp MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers configure this skill for agents that assist Artsonia parent or fan account holders with viewing student artwork, managing comments, fans, and notifications, and downloading portfolio data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an external MCP package with Artsonia account credentials.

Mitigation: Review the MCP package before use, pin a trusted package version, and provide credentials through a protected secret store or tightly permissioned environment injection.

Risk: Session data and child-related artwork data can be stored locally.

Mitigation: Avoid committed project .env files or shared configuration, consider disabling session caching on shared systems, and choose protected local download locations.

Risk: Some tools can post comments, invite fans, change notifications, or download child-related data.

Mitigation: Require explicit user confirmation before state-changing or bulk-download actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Files, Configuration]

**Output Format:** [Markdown or JSON-like tool results, with downloaded image and metadata files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write artwork images, sidecar metadata, and index manifests to user-selected local folders.]

## Skill Version(s):

0.12.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
