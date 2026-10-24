## Description:

Helps agents find Redfin listings, property details, market reports, climate risk, and a user's saved homes and searches through a browser-connected MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate researchers, and other external users can ask an agent to compare Redfin listings, review property and market information, estimate mortgage costs, and inspect their saved activity when they choose to sign in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved-home and saved-search requests expose account activity from the signed-in Redfin browser session to the agent.

Mitigation: Use saved-activity tools only when the user intends to share that activity with the agent.

Risk: Using the skill requires installing an external MCP package and browser extension.

Mitigation: Install the package and extension only if you are comfortable running both.

## Reference(s):

- [Redfin skill on ClawHub](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp package](https://www.npmjs.com/package/redfin-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or structured text with property, market, and saved-activity details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; saved homes and searches require a signed-in Redfin browser session.]

## Skill Version(s):

1.2.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
