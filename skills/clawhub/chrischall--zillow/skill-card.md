## Description:

Look up Zillow listings, property details and Zestimates, saved searches and homes, and market reports using natural-language requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People comparing homes or monitoring Zillow activity can use this skill to find listings, review property and market data, check saved searches and homes, and estimate mortgage payments through a conversational agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review scanned the Markdown component only; referenced paths and external links were outside its coverage.

Mitigation: Review the setup instructions and external downloads or links before installing.

Risk: Signed-in tools can return saved searches and homes from the user's Zillow account.

Mitigation: Use signed-in activity only when needed and handle its results as private account information.

Risk: The skill relies on Zillow web behavior and an active browser bridge, so authentication issues, captchas, or endpoint changes can interrupt results.

Mitigation: Keep the signed-in browser and extension active, and verify important details directly on Zillow.

## Reference(s):

- [zillow-mcp on npm](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp project page](https://github.com/chrischall/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge project page](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [Natural-language answers with structured listing, property, market, saved-activity, and mortgage data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups and calculations; saved activity requires a signed-in Zillow browser session.]

## Skill Version(s):

1.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
