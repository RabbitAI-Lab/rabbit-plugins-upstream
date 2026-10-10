## Description:

Looks up Zillow listings, property details, Zestimates, saved homes and searches, and housing market reports through a browser-connected MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home buyers, renters, and real-estate researchers use the skill to explore Zillow listings, property estimates, saved activity, and local market trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved homes and searches expose private Zillow account activity through a signed-in browser session.

Mitigation: Use the integration only for authorized accounts and treat saved activity as private data.

Risk: Requests depend on an installed MCP package and browser extension connected to the Zillow session.

Mitigation: Verify the npm package and ContextMint Bridge release before installation and enable the extension only when comfortable with this access.

## Reference(s):

- [Zillow skill on ClawHub](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Text and structured property or market data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only results; saved homes and searches require a signed-in Zillow browser session.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
