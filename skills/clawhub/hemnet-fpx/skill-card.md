## Description:

Query hemnet.se from a shell with the fpx CLI to resolve locations, search for-sale and sold listings, and retrieve listing details through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to produce fpx shell commands, GraphQL request bodies, and jq checks for retrieving public Hemnet listing data without running the hemnet-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the fpx CLI and Transporter browser extension to query Hemnet through a signed-in browser tab.

Mitigation: Confirm the fpx CLI and Transporter extension are trusted before use, and keep Chrome site access limited to hemnet.se.

Risk: The skill queries public Hemnet data through Hemnet's GraphQL endpoint.

Mitigation: Use the skill only for public Hemnet data and follow Hemnet's terms.

Risk: Hemnet GraphQL responses can include an errors array even when the HTTP request succeeds.

Mitigation: Check GraphQL errors with jq before relying on listing, sold-listing, or market-stat results.

## Reference(s):

- [Hemnet GraphQL queries for fpx](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes fpx commands, GraphQL request bodies, jq filters, setup notes, and exit-code interpretation.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
