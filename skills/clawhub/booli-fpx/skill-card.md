## Description:

Query booli.se from a shell with the fpx CLI to resolve areas, search active and sold property listings, and read property detail through browser-mediated GraphQL calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to query public Booli Swedish property data from scripts or agent workflows without running the booli MCP server. It helps produce area lookup, active listing search, sold listing comparison, and property detail requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup requires installing @fetchproxy/cli and pairing the Transporter browser extension for domain-scoped requests to booli.se.

Mitigation: Review or pin the CLI package before installation, avoid elevated shells, and pair only the booli.se profile needed for this skill.

Risk: Pairing persists after setup, so later fpx calls can continue using the approved browser-mediated connection.

Mitigation: Remove the fpx profile or revoke extension site access when the skill is no longer needed.

Risk: GraphQL errors can be returned inside an HTTP 200 response.

Mitigation: Check the response errors field, for example with jq '.errors // empty', before relying on returned data.

## Reference(s):

- [Booli GraphQL queries for fpx](references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli-fpx)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON GraphQL request bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for anonymous Booli GraphQL reads and may require checking GraphQL errors in HTTP 200 responses.]

## Skill Version(s):

1.3.2 (source: ClawHub server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
