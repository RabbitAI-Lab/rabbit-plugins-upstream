## Description:

Query booli.se property data from a shell with the fpx CLI, including area resolution, for-sale listings, sold listings, and property detail through one-shot GraphQL calls via a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Booli Swedish property data from a shell when they need scriptable property search, sold-comparable lookup, or property detail without running the booli MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a globally installed npm CLI and a paired browser extension with site access to booli.se.

Mitigation: Install only in environments where that extension and CLI are acceptable, keep extension site access limited to booli.se, and remove the fpx profile or extension access when no longer needed.

Risk: The skill queries Booli through the user's open browser tab and is subject to Booli's terms and availability.

Mitigation: Use only public, anonymous reads as documented, review Booli's terms, and handle GraphQL errors or bridge exit codes before relying on returned data.

## Reference(s):

- [Booli GraphQL queries for fpx](references/graphql-queries.md)
- [Booli GraphQL endpoint](https://www.booli.se/graphql)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli-fpx)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands, GraphQL request bodies, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide the agent to produce command-line requests and parse public property data; no account data is required by the documented workflow.]

## Skill Version(s):

1.2.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
