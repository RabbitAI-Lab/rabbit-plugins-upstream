## Description:

Query booli.se property data from a shell with the fpx CLI by resolving areas, searching for-sale and sold listings, and reading property details through one-shot GraphQL calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve public Booli property listings and sale data from shell workflows without running the booli-mcp server. It helps agents prepare fpx setup commands, GraphQL request bodies, and jq checks for area lookup, listing search, sold-comparable search, and property detail reads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and pairing @fetchproxy/cli and the Transporter extension creates normal local setup risk.

Mitigation: Pin @fetchproxy/cli to a reviewed version, limit the Transporter extension's site access to booli.se, and revoke the fpx pairing when it is no longer needed.

Risk: The skill accesses Booli through the user's browser-backed session and should remain limited to public property data.

Mitigation: Use the skill only for public Booli data and within Booli's terms.

Risk: GraphQL errors can appear in a successful HTTP response body.

Mitigation: Check jq '.errors // empty' before relying on returned data.

## Reference(s):

- [Booli GraphQL queries for fpx](artifact/references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with shell commands and JSON GraphQL request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include jq filters, fpx exit-code handling, and notes to check GraphQL errors in successful HTTP responses.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
