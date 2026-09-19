## Description:

Query booli.se from a shell with the fpx CLI to resolve areas, search for-sale and sold listings, and read property detail through one-shot GraphQL calls via a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query public Booli property data from scripts or shell sessions without running the Booli MCP server. It helps resolve Booli area IDs, search active and sold Swedish property listings, and fetch property details as GraphQL JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on installing the external @fetchproxy/cli package globally and pairing it with the Transporter browser extension.

Mitigation: Confirm the package and extension are acceptable for the target environment before installation, and keep the browser bridge scoped to booli.se.

Risk: Browser-bridge pairing persists after setup.

Mitigation: Use a dedicated browser profile or limited site access for Booli workflows, and remove or rotate the pairing when it is no longer needed.

Risk: Booli requests must stay within the service's terms and rely on the user's browser session clearing site challenges.

Mitigation: Use the skill only for anonymous public reads within Booli's terms, and check GraphQL errors before relying on returned data.

## Reference(s):

- [Booli GraphQL queries for fpx](references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli-fpx)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands, GraphQL request bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces commands and query bodies for anonymous Booli GraphQL reads through fpx; command output is GraphQL JSON.]

## Skill Version(s):

2.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
