## Description:

Look up Compass real-estate listings, property details, photos, price history, and address resolutions through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Compass listings, retrieve property records, view photos and price history, compare listings, resolve addresses, and run local mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can run mutable third-party package and browser-extension code.

Mitigation: Review compass-mcp and fetchproxy before installing, and prefer pinned versions or a reviewed commit.

Risk: The MCP bridge connects tool requests to a signed-in Compass browser session.

Mitigation: Use a dedicated browser profile signed into only Compass, and remove the MCP entry or extension when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp source](https://github.com/chrischall/compass-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured listing, property, photo, price-history, comparison, diagnostic, and local mortgage-calculation results.]

## Skill Version(s):

0.14.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
