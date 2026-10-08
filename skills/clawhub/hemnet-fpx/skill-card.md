## Description:

Guides agents to resolve Swedish locations and query Hemnet's public for-sale, sold, and property-detail data using the fpx CLI and a paired browser extension instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up Swedish property listings and sale comparisons from a shell or script without running the Hemnet MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a CLI and browser extension introduces third-party software with persistent bridge access.

Mitigation: Verify the @fetchproxy/cli package and ContextMint Bridge release, limit Chrome site access to hemnet.se, and remove the profile or extension when no longer needed.

Risk: Querying Hemnet may conflict with the site's usage terms.

Mitigation: Confirm the intended use complies with Hemnet's terms before querying.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and GraphQL JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hemnet query results are JSON; property prices are in SEK and areas in m².]

## Skill Version(s):

1.1.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
