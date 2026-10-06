## Description:

Helps agents find Zillow listings, property details, Zestimates, market reports, and a user's saved homes and searches through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and other users can ask an agent to research Zillow properties and market trends or review their saved Zillow activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in Zillow activity, including saved homes and searches, can be exposed to the agent when requested.

Mitigation: Use saved-data tools only when you intend to share that account-specific activity with the agent.

Risk: The MCP server queries Zillow through a signed-in browser session and requires an npm package and browser extension.

Mitigation: Confirm you are comfortable with session-based access and verify the package and extension sources before installing.

## Reference(s):

- [Zillow skill listing](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Natural-language summaries and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved-home and saved-search data require a signed-in Zillow session.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
