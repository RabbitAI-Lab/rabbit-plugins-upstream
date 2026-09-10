## Description:

Query hemnet.se from a shell with the fpx CLI to resolve locations, search for-sale and sold listings, and read listing detail through one-shot GraphQL calls using a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Hemnet property data from shell workflows without running the Hemnet MCP server. It is suited for location lookup, active listing search, sold listing comparison, and listing detail retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing @fetchproxy/cli globally without a pinned version can introduce supply-chain exposure if the package changes.

Mitigation: Pin @fetchproxy/cli to a reviewed version and avoid running npm install as an administrator.

Risk: A browser-paired Transporter extension can proxy browser-cleared requests if granted broad site access.

Mitigation: Pair only the hemnet profile and keep the extension's site access limited to hemnet.se.

Risk: Using the skill outside public, read-only Hemnet queries could exceed the intended access pattern.

Mitigation: Use the skill only for anonymous read-only Hemnet queries and stay within Hemnet's terms.

Risk: GraphQL errors can appear in a successful HTTP response body and be missed by callers.

Mitigation: Check the response for an errors array before relying on returned listing data.

## Reference(s):

- [Hemnet GraphQL queries for fpx](references/graphql-queries.md)
- [Hemnet GraphQL endpoint](https://www.hemnet.se/graphql)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with shell commands, JSON request bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only query guidance for public Hemnet GraphQL data; callers should check GraphQL errors in successful HTTP responses.]

## Skill Version(s):

0.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
