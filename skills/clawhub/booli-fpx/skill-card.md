## Description:

Query booli.se Swedish property data from a shell with the fpx CLI, including area resolution, for-sale listings, sold listings, and property detail through one-shot GraphQL calls from a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data users use this skill to query public Booli property listings and sold-property data from scripts or shell sessions without running the Booli MCP server. It is suited for one-off lookups, lightweight analysis, and reproducing MCP-style Booli queries with fpx and jq.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on fpx and the Transporter browser extension with site access to booli.se.

Mitigation: Use a dedicated fpx profile for Booli, keep the browser extension site access limited to booli.se, and install only when this bridge behavior is acceptable.

Risk: Temporary JSON request files may contain query details or parameters that users did not intend to keep.

Mitigation: Review temporary request files before execution and remove them when they are no longer needed.

Risk: GraphQL responses can include an errors array even when the HTTP request succeeds.

Mitigation: Check jq '.errors // empty' and validate result counts before relying on listing or market-stat outputs.

## Reference(s):

- [Booli GraphQL queries for fpx](references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces executable fpx and jq examples for public Booli GraphQL queries; users should review temporary request files and GraphQL errors before relying on results.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
