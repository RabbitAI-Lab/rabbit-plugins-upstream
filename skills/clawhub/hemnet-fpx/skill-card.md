## Description:

Query hemnet.se from a shell with the fpx CLI to resolve locations, search for-sale and sold listings, and read listing detail through one-shot GraphQL calls via a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data users use this skill to query public Hemnet property listing data from scripts or shells without running the Hemnet MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a browser-mediated CLI and extension pairing to make Hemnet requests.

Mitigation: Install only trusted versions of @fetchproxy/cli and the Transporter extension, and approve only the hemnet.se-scoped pairing.

Risk: GraphQL responses may include errors even when the HTTP request succeeds.

Mitigation: Check the GraphQL errors field before using returned listing data.

Risk: The skill accesses Hemnet through public anonymous reads subject to Hemnet's terms.

Mitigation: Use the queries only for permitted public-read workflows and stay within hemnet.se's terms.

## Reference(s):

- [Hemnet GraphQL query examples](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON GraphQL request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-oriented Hemnet query guidance and examples; command output is expected to be GraphQL JSON from fpx.]

## Skill Version(s):

0.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
