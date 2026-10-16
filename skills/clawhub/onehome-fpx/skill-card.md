## Description:

Guides agents in using fpx and an authorized OneHome browser session to search shared real-estate listings and retrieve listing details without the OneHome MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents with authorized access to a OneHome share use this skill to find saved searches, inspect listings and photos, and retrieve property details through a paired browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Capturing and replaying a OneHome bearer token can expose an authorized user's private session.

Mitigation: Use only your own authorized session, limit access to the paired browser extension, and unpair or disable the profile when finished.

Risk: Magic links, session tokens, temporary files, command output, and returned contact or listing data may disclose sensitive information.

Mitigation: Avoid sharing or logging credentials and private results; remove temporary files after use.

## Reference(s):

- [OneHome fpx release](https://clawhub.ai/chrischall/skills/onehome-fpx)
- [GraphQL and REST operation examples](references/graphql-operations.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [fetchproxy CLI and extension documentation](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands, GraphQL queries, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include saved-search scope and private listing or contact data.]

## Skill Version(s):

1.1.9 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
