## Description:

Query booli.se from a shell with the fpx CLI to resolve areas, search for-sale and sold listings, and read property details through one-shot GraphQL calls via a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real estate data users use this skill to run anonymous Booli property-data GraphQL queries from shell scripts without running booli-mcp. It supports area lookup, for-sale searches, sold-listing comparisons, and property detail retrieval after configuring FetchProxy and the Transporter extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests are routed through a user-approved browser bridge and FetchProxy profile for booli.se.

Mitigation: Keep the fpx profile scoped to booli.se, confirm browser site access before pairing, and use the bridge only for the documented anonymous property-data queries.

Risk: GraphQL calls can return an errors array even when the HTTP request succeeds.

Mitigation: Check response bodies for GraphQL errors before using returned listing, sold-price, or property-detail data.

Risk: The skill accesses public Booli property data through booli.se.

Mitigation: Stay within booli.se terms and avoid account or non-public data workflows.

## Reference(s):

- [Booli GraphQL queries for fpx](references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [booli-fpx ClawHub skill page](https://clawhub.ai/chrischall/skills/booli-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON GraphQL request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command-oriented guidance for anonymous Booli GraphQL reads; outputs from executed examples are JSON from the upstream endpoint.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
