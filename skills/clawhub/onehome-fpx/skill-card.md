## Description:

Helps agents query authorized OneHome saved searches and property listings from the shell using fpx instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate professionals use this skill to retrieve shared OneHome searches and listing details from sessions they are authorized to access without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Captured session bearer values and magic-link tokens can expose private OneHome access if logged, saved, or shared.

Mitigation: Treat these credentials like passwords; avoid logging or storing them in shell history or /tmp.

Risk: Reusing a live browser session or magic link can access OneHome data outside the user's authorization.

Mitigation: Use only sessions and links you are explicitly authorized to access, and prefer an official or scoped integration when available.

## Reference(s):

- [OneHome GraphQL and REST operations](references/graphql-operations.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Fetchproxy extension documentation](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with shell and GraphQL examples; queries return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the authorized OneHome session and its saved-search scope.]

## Skill Version(s):

1.1.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
