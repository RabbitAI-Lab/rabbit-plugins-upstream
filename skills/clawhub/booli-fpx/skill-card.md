## Description:

Helps agents query public Swedish property listings, sold prices, and property details on Booli through a browser-connected command-line tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up Swedish areas, search active and sold property listings, and inspect property details without running a separate MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unverified CLI or browser extension can expose the browser environment.

Mitigation: Verify the @fetchproxy/cli package and ContextMint Bridge source or release before installing; limit extension site access to booli.se.

Risk: Sensitive personal data in a GraphQL request is sent to Booli.

Mitigation: Avoid including sensitive personal data in request bodies unless you intend to send it to Booli.

Risk: A successful command can still contain GraphQL errors or too few sold listings for reliable comparisons.

Mitigation: Check the response errors and sample count before relying on property results or market summaries.

## Reference(s):

- [Booli GraphQL query examples](references/graphql-queries.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/booli-fpx)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON data]

**Output Format:** [Markdown guidance with shell commands and GraphQL JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property prices are in SEK and areas in m².]

## Skill Version(s):

2.1.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
