## Description:

Guides agents in querying public Booli property listings and sales through the fpx CLI and a connected browser tab without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents can resolve Swedish areas, search homes for sale and sold prices, and retrieve property details from Booli using one-shot shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI and browser extension are third-party components, and pairing grants access through a browser profile.

Mitigation: Verify their sources before installation and approve only the intended booli.se profile.

Risk: Query variables or temporary JSON files could expose sensitive personal notes.

Mitigation: Keep sensitive notes out of queries and temporary files.

## Reference(s):

- [Booli GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge extension source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries can return public listing data as JSON; prices are in SEK and areas are in m².]

## Skill Version(s):

2.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
