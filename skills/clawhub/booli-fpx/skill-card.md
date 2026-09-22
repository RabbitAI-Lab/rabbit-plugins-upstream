## Description:

Query booli.se from a shell with the fpx CLI to resolve areas, search for-sale and sold listings, and read property detail through browser-backed GraphQL calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to obtain public Booli real estate data from a shell when the booli MCP server is unavailable or unnecessary. It provides setup guidance, GraphQL request bodies, and jq recipes for area lookup, active listings, sold listings, and property detail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the Transporter extension and a globally installed fpx CLI to send booli.se requests through the user's browser context.

Mitigation: Install only when that browser-backed workflow is acceptable, keep Chrome site access limited to booli.se, and use the dedicated booli fpx profile described by the skill.

Risk: Automated querying of Booli data may be subject to Booli's terms and operational limits.

Mitigation: Review Booli's terms before automated querying and keep request volume appropriate for the intended use.

Risk: GraphQL errors can appear in an HTTP-200 response body, and thin result sets can make derived market statistics unreliable.

Mitigation: Check the GraphQL errors field before using results and review result counts before trusting derived summaries.

## Reference(s):

- [Booli GraphQL queries for fpx](artifact/references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with shell and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces textual instructions and request bodies; executed commands return GraphQL JSON suitable for jq processing.]

## Skill Version(s):

2.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
