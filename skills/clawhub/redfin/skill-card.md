## Description:

Look up Redfin listings, property details, market reports, and your saved homes and searches through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home seekers and property researchers can ask an agent to search Redfin listings, examine properties and market trends, estimate mortgage payments, or review their saved homes and searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected agent can read saved homes and searches from your signed-in Redfin session.

Mitigation: Use saved-data tools only when you intend to share that account data with the agent session.

Risk: Using the skill requires installing an MCP package and a browser extension with access to the Redfin session.

Mitigation: Review the package and extension source or verify the extension release checksums before installation.

## Reference(s):

- [Redfin skill on ClawHub](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp package](https://www.npmjs.com/package/redfin-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes listing details, market metrics, mortgage calculations, and, when authorized, saved homes and searches. Compact responses omit some photo URLs.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
