## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate workflow users use this skill to query Compass listing pages for property searches, listing details, photos, price history, comparisons, address resolution, and local mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external MCP package and browser extension with a signed-in Compass tab to read listing pages.

Mitigation: Install only after reviewing the package and extension sources, and use it in a browser session appropriate for this workflow.

Risk: Network-backed tools can fail or return limited data when the Compass session is not authenticated, site access changes, or AWS WAF challenges are present.

Mitigation: Keep the Compass tab signed in, expect clear failures for unavailable pages, and verify important listing data before relying on it.

Risk: The integration reads Compass page-rendered data rather than a public consumer API.

Mitigation: Use at your discretion, respect applicable site access rules, and review outputs before making business or financial decisions.

## Reference(s):

- [Compass skill release](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp repository](https://github.com/chrischall/compass-mcp)
- [fetchproxy repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration and inline shell commands; MCP tools return structured real-estate lookup and calculation results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Network-backed tools depend on an installed compass-mcp package, the fetchproxy browser extension, and a signed-in Compass browser session; local mortgage and affordability calculators do not require network access.]

## Skill Version(s):

0.13.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
