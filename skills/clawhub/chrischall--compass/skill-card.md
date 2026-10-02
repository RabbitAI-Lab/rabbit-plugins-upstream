## Description:

Find and compare Compass real-estate listings, property details, photos, and price history, and estimate mortgage payments and affordability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and other users can search and compare Compass properties, inspect listing histories and photos, and calculate estimated housing costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP package and browser extension can fetch Compass pages using the user's signed-in browser session.

Mitigation: Verify the npm package and ContextMint Bridge release or source before installing, and use a browser session appropriate for that access.

Risk: Listing searches can fail when the browser session is signed out or challenged by Compass.

Mitigation: Confirm the signed-in tab and bridge connection before relying on listing results.

## Reference(s):

- [Compass skill on ClawHub](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language summaries and structured property details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only property lookups; saved homes and saved searches are not supported.]

## Skill Version(s):

1.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
