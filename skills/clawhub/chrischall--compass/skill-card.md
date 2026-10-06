## Description:

Helps agents look up and compare Compass property listings, photos, price histories, and addresses through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research and compare Compass property listings, retrieve listing details and price history, resolve addresses, and estimate mortgage payments or affordability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MCP package and browser extension interact with a signed-in Compass session.

Mitigation: Review both components before installing and use them only if comfortable with their access to the browser session.

Risk: Read-only listing data scraped from Compass may be incomplete or outdated.

Mitigation: Verify consequential property details and prices against current listings or authoritative sources.

## Reference(s):

- [ClawHub compass skill release](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses with structured listing details and calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property results depend on Compass site availability and an active signed-in browser session; mortgage and affordability calculations work locally.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
