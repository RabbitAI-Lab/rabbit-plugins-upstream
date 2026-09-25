## Description:

Query booli.se from a shell with the fpx CLI to resolve areas, search for-sale and sold listings, and read property detail through one-shot GraphQL calls using a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve public Booli property data from shell workflows without running the booli-mcp server. It supports area lookup, active listing search, sold listing search, and property detail queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on browser-tab routing and persistent fpx pairing to fetch Booli data.

Mitigation: Install the fpx CLI and Transporter extension only if this routing model is acceptable, keep the profile scoped to booli.se, and review pairing before use.

Risk: Booli GraphQL responses may include errors even when the HTTP request succeeds.

Mitigation: Check the response for a GraphQL errors array before relying on returned property data.

Risk: Use of public Booli data may be subject to Booli's terms of use.

Mitigation: Use the skill only for permitted public-data workflows and follow Booli's terms of use.

## Reference(s):

- [Booli GraphQL queries for fpx](references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON GraphQL request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce fpx commands and jq recipes for public Booli property data.]

## Skill Version(s):

2.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
