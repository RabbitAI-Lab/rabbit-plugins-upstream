## Description:

Guides agents using the fpx CLI to look up US Redfin listings, property details, market data, climate risk, and, when authorized, saved homes and searches without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to retrieve US real-estate listings, property histories, trends, rentals, and climate data from Redfin through a browser-connected CLI; signed-in users may also request their saved homes and searches.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Saved homes and saved searches expose private Redfin account data when the browser tab is signed in.

Mitigation: Read saved items only at the user's explicit request; use a signed-out tab or separate browser profile for public lookups.

Risk: Setup requires installing the fpx CLI and ContextMint Bridge browser extension.

Mitigation: Install only if comfortable with both components, and verify extension releases before installation.

Risk: Fuzzy address matching and substituted search regions can return a different property or area.

Mitigation: Confirm the resolved address and returned region before relying on listing results.

## Reference(s):

- [Redfin fpx endpoint guide](artifact/references/stingray-endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [ContextMint Bridge installation and releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell examples and instructions for interpreting Redfin responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires fpx and ContextMint Bridge with a Redfin tab; saved items require a signed-in session.]

## Skill Version(s):

1.1.4 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
