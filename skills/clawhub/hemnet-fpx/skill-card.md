## Description:

Query hemnet.se from a shell with the fpx CLI to resolve locations, search for-sale and sold listings, and read listing details through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query public Hemnet property data from shell workflows without running the Hemnet MCP server. It is useful for scripted real-estate lookups, listing detail retrieval, and sold-listing comparisons through fpx.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes requests through the user's browser session via fpx and the Transporter extension.

Mitigation: Keep Transporter site access limited to hemnet.se, use the skill only for anonymous read-only property lookups, and stay within Hemnet's terms.

Risk: GraphQL errors can appear in an HTTP-200 response and may be mistaken for valid data.

Mitigation: Check the response for an errors array before using results, and verify sold-listing counts before trusting derived medians or averages.

Risk: Requests can fail if the extension is unpaired, the browser tab is closed, or Hemnet's challenge has not been cleared.

Mitigation: Use fpx health and the documented exit codes to confirm bridge status, then refresh or open a www.hemnet.se tab before retrying.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce fpx commands, GraphQL request bodies, jq post-processing, and troubleshooting guidance.]

## Skill Version(s):

0.3.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
