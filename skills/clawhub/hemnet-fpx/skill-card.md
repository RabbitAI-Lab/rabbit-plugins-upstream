## Description:

Helps agents query public Hemnet property listings from a shell using fpx and a paired browser tab, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can resolve Swedish locations, search for-sale and sold properties, and retrieve listing details through read-only Hemnet GraphQL queries from scripts or a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external fpx CLI and ContextMint Bridge extension operate through the user's browser context.

Mitigation: Verify and trust both tools before installing; restrict extension site access to hemnet.se and use a fetch-only profile. Avoid logged-in or private account data unless the tools have been independently verified.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON query bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries return public Hemnet GraphQL JSON; prices are in SEK and areas in square meters.]

## Skill Version(s):

1.1.13 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
