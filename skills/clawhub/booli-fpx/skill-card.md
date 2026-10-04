## Description:

Guides agents in querying public Booli property listings, sold prices, and property details through a browser-connected command-line tool without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve Swedish areas, search Booli listings and sold properties, and inspect property details from a shell or script without a running MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge can send requests through an open Booli tab after pairing.

Mitigation: Verify the @fetchproxy/cli package and ContextMint Bridge release, scope the profile to booli.se, and approve pairing only if comfortable with requests through that tab.

Risk: GraphQL errors can appear in a successful HTTP response.

Mitigation: Check the response's errors array before using listing or property data.

## Reference(s):

- [Booli GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands, GraphQL JSON examples, and jq recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booli responses are JSON; prices are in SEK and areas are in square meters.]

## Skill Version(s):

2.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
