## Description:

Guides agents through querying public Booli property listings, sold prices, and property details using the fpx CLI and a paired browser tab instead of a running MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to resolve Swedish areas and retrieve public for-sale listings, sold-property comparisons, and property details from Booli through a browser-assisted CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI and browser extension run requests through the user's browser context.

Mitigation: Trust the CLI and extension before installation, verify the extension source or release hash where possible, restrict the profile and site access to booli.se, and avoid sensitive logged-in sites.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/booli-fpx)
- [Booli GraphQL query examples](references/graphql-queries.md)
- [ContextMint Bridge source and releases](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booli results are returned as JSON; prices are in SEK and area measurements are in square meters.]

## Skill Version(s):

2.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
