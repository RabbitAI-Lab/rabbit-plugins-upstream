## Description:

Helps agents find Redfin listings, inspect property details and market reports, estimate mortgage payments, and retrieve saved homes and searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and other users can ask an agent to research Redfin listings and market data, review their saved activity, and estimate housing costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party server and browser extension can access the user's signed-in Redfin session and saved activity.

Mitigation: Install them only if trusted, treat saved homes and searches as personal data, and prefer project-level configuration to limit scope.

Risk: Redfin's private endpoints or browser challenges may interrupt lookups or change returned data.

Mitigation: Confirm important property and market details on Redfin before relying on them.

## Reference(s):

- [redfin on ClawHub](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp package](https://www.npmjs.com/package/redfin-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language answers with property, market, saved-search, or mortgage details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property and saved-activity details depend on the available Redfin browser session; compact responses omit some image URLs.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
