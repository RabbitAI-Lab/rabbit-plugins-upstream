## Description:

Helps agents look up Redfin property listings, property details, housing market reports, and a user's saved homes and searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate professionals, and other users can ask an agent to find Redfin listings, review property and market information, estimate mortgage payments, and inspect their saved homes or searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and browser bridge can access Redfin requests and private saved activity through a signed-in tab.

Mitigation: Install only if comfortable with that access; use project-scoped MCP configuration where possible and avoid connecting sessions with saved activity you do not want available to the agent.

Risk: Using an external MCP package and browser extension requires trusting their source.

Mitigation: Verify the package and extension source before installing or using them.

## Reference(s):

- [Redfin skill release](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp package](https://www.npmjs.com/package/redfin-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses with listing details, market metrics, saved activity, or mortgage calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; saved homes and searches require a signed-in Redfin browser tab.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
