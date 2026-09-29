## Description:

Guides agents to search private OneHome saved searches and property listings through an authenticated browser session using command-line requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized OneHome users use this skill to retrieve shared saved searches, property details, photos, and neighborhood information without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Magic-link tokens and bearer credentials can grant access to private account and listing data.

Mitigation: Use only authorized sessions; keep tokens out of shared terminal output, screenshots, and shell history.

Risk: Temporary request and response files may retain sensitive session information.

Mitigation: Prefer ephemeral variables, restrict access to temporary files, and remove them after use.

## Reference(s):

- [OneHome GraphQL and REST operations](references/graphql-operations.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/onehome-fpx)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.1.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
