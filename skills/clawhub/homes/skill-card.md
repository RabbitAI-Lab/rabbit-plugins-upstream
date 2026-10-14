## Description:

Looks up homes.com listings, property details, price and tax history, market reports, saved homes, and photos through a browser-connected MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Home buyers, real-estate professionals, and other agents use this skill to research US property listings, compare homes, inspect price and tax history, and access their saved homes and searches.

### Deployment Geography for Use:

Global (US property data)

## Known Risks and Mitigations:

Risk: Installation runs the homes-mcp npm package and requires the ContextMint Bridge browser extension.

Mitigation: Review the package and extension before installation.

Risk: The bridge uses the active homes.com browser session, including access to signed-in saved homes and searches.

Mitigation: Use only when comfortable granting read-only access to listing data and account-gated saved items through that session.

## Reference(s):

- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub homes release](https://clawhub.ai/chrischall/skills/homes)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses with property data and comparisons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listing and photo details depend on homes.com page data; saved items require a signed-in browser session.]

## Skill Version(s):

2.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
