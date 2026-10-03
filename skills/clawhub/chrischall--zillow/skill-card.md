## Description:

Helps agents look up Zillow listings, property details, valuations, market reports, mortgage estimates, and a user's saved homes and searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home shoppers and real-estate researchers use this skill to explore listings, property values, market trends, mortgage estimates, and their saved Zillow activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in browser session can expose personal saved homes and searches to the skill's tools.

Mitigation: Only connect a Zillow account when needed and treat saved activity as personal data.

Risk: The required package and browser extension handle requests through a signed-in Zillow tab.

Mitigation: Verify the package and extension release before installation, and use only trusted copies.

## Reference(s):

- [zillow-mcp package](https://www.npmjs.com/package/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown text with property details, market metrics, and calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved homes and searches require a signed-in Zillow session.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
