## Description:

Looks up Compass real-estate listings, property details, photos, price histories, and addresses through an MCP server connected to a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Real-estate shoppers and agents use this skill to find and compare Compass listings, inspect property records and price histories, and estimate mortgage costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and browser extension can access a signed-in Compass session and may expose account-visible information to the agent.

Mitigation: Use a project-local MCP configuration and a browser profile without information you do not want the agent to see.

Risk: Installing external MCP and browser-extension releases introduces software supply-chain exposure.

Mitigation: Verify the package and extension source and release before installation.

## Reference(s):

- [Compass skill listing](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp package](https://www.npmjs.com/package/compass-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown with property summaries, comparisons, and setup instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only property lookups require a signed-in Compass browser session; mortgage and affordability estimates run locally.]

## Skill Version(s):

1.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
