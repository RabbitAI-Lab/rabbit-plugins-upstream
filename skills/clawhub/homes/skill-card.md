## Description:

Looks up Homes.com real-estate listings, property details, price and tax history, market reports, saved homes, and photo galleries through the homes-mcp MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, real-estate analysts, and end users use this skill to query Homes.com listings, property records, histories, photos, saved items, and local mortgage or affordability calculations through an MCP-backed browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external homes-mcp package and fetchproxy browser extension that operate through the user's browser session and can access Homes.com pages available to the signed-in account.

Mitigation: Review and trust the external package and extension before installation, keep them scoped to Homes.com use, and avoid using accounts or sessions that expose unnecessary saved data.

Risk: Homes.com does not publish a public consumer API, so page access can depend on an active browser session and may be affected by authentication or WAF challenges.

Mitigation: Keep a signed-in Homes.com tab active when needed, handle session and challenge errors explicitly, and verify important listing or history details against Homes.com before relying on them.

## Reference(s):

- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [homes-mcp source repository](https://github.com/chrischall/homes-mcp)
- [fetchproxy extension repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool-use instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return compact or full property data; compact responses strip selected media URLs, while photo-gallery output preserves image URLs.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
