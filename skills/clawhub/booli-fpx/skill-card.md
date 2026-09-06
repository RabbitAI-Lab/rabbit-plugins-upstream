## Description:

Query booli.se from a shell with the fpx CLI to resolve areas, search for-sale and sold listings, and read property detail through one-shot GraphQL calls via a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Booli property data from scripts or shell workflows without running the Booli MCP server. It supports area resolution, active listing search, sold listing comparisons, and property-detail lookups through documented GraphQL request bodies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a browser-assisted CLI and extension that can send requests through an open Booli tab.

Mitigation: Review and trust @fetchproxy/cli and the Transporter extension before installation, and keep browser site access limited to booli.se.

Risk: Booli GraphQL responses can include an errors array even when the HTTP request succeeds.

Mitigation: Check `.errors` before using returned listing, sold-property, or property-detail data.

## Reference(s):

- [Booli GraphQL queries for fpx](references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON GraphQL request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The commands return GraphQL JSON from Booli; users should check GraphQL errors before relying on results.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
