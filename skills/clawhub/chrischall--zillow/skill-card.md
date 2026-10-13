## Description:

Helps agents look up Zillow listings, property details, Zestimates, saved homes and searches, and market reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People researching homes and real-estate markets can ask an agent to find listings, inspect properties, compare prices, and review their saved Zillow activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server and browser extension can use a signed-in Zillow session to read saved homes and searches.

Mitigation: Use only if comfortable sharing this session access; remove the MCP configuration or extension when no longer needed.

Risk: Installing the server and browser extension introduces third-party software into the browsing workflow.

Mitigation: Review the npm package and extension source or release checksums before installation.

## Reference(s):

- [Zillow skill on ClawHub](https://clawhub.ai/chrischall/skills/zillow)
- [zillow-mcp npm package](https://www.npmjs.com/package/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property and market information is read-only; saved activity requires a signed-in Zillow browser session.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
