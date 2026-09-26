## Description:

Helps agents find and compare Compass real-estate listings, retrieve property details and price history, and resolve addresses through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Homebuyers, real-estate researchers, and their agents can search Compass listings, inspect property records and photos, compare homes, and estimate mortgage costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external MCP package and browser extension use a signed-in Compass session.

Mitigation: Review both upstream projects and extension permissions before installing; use project-level MCP configuration to limit scope.

## Reference(s):

- [Compass skill release](https://clawhub.ai/chrischall/skills/compass)
- [Compass MCP package](https://www.npmjs.com/package/compass-mcp)
- [Compass MCP source linked in skill](https://github.com/chrischall/compass-mcp)
- [Fetchproxy browser extension source linked in skill](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Natural-language responses and structured property data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing links, photo links, comparisons, and mortgage estimates.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
