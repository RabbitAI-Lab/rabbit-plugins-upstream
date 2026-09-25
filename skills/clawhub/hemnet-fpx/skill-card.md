## Description:

Query Hemnet property data from a shell with the fpx CLI, including location lookup, active listing search, sold listing search, and listing detail requests through browser-backed GraphQL calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare shell commands and GraphQL request bodies for retrieving public Hemnet property listings without running the Hemnet MCP server. It is suited for scripted property searches, listing inspection, and sold-price comparisons where the user controls the browser-backed fetch proxy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent fpx pairing can allow later commands to use the user's browser-backed access to hemnet.se.

Mitigation: Install and pair only trusted @fetchproxy/cli and Transporter extension instances, and run only Hemnet queries the user intends to make.

Risk: Automated access to Hemnet may be subject to Hemnet terms or upstream limits.

Mitigation: Use the skill for anonymous public reads, keep requests proportionate, and follow Hemnet's terms.

Risk: GraphQL responses can include errors even when the HTTP request succeeds.

Mitigation: Check the response for a GraphQL errors array before relying on returned listing data.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON GraphQL request bodies, and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions and request examples; commands run only when the user or agent executes them.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
