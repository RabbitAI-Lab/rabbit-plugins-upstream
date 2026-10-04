## Description:

Helps agents look up Zillow listings, property details, Zestimates, market reports, and a user's saved homes and searches through an MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home buyers, real-estate researchers, and other users can ask an agent to find listings, inspect property and market data, estimate mortgage costs, or check their saved Zillow activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser extension can access a signed-in Zillow tab, including personal saved homes and searches.

Mitigation: Install only if comfortable with that access; request saved activity deliberately and use project-level MCP configuration when possible.

Risk: Installing an MCP package and manually loaded browser extension introduces software supply-chain exposure.

Mitigation: Verify the npm package and extension release before installation.

## Reference(s):

- [zillow-mcp package](https://www.npmjs.com/package/zillow-mcp)
- [zillow-mcp project documentation](https://github.com/chrischall/zillow-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses with Zillow listing, property, market, or calculation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only access; saved homes and searches require a signed-in Zillow browser session.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
