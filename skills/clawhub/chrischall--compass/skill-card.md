## Description:

Enables agents to look up Compass real-estate listings, property details, photos, price history, address resolutions, comparisons, and mortgage or affordability calculations through the Compass MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can ask an agent to search, inspect, compare, and summarize Compass property data, or run local mortgage and affordability calculations. Network-backed lookups require compass-mcp plus the fetchproxy browser extension connected to a signed-in Compass session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup asks users to run mutable third-party MCP and browser-extension code.

Mitigation: Review and pin the compass-mcp package version and fetchproxy commit before installing or running the skill.

Risk: The skill operates against a signed-in browser session through the fetchproxy extension.

Mitigation: Use a dedicated browser profile for Compass, keep the extension disabled except when needed, and avoid exposing unrelated local files or credentials to the MCP host.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp source](https://github.com/chrischall/compass-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown text with JSON configuration and shell command snippets; MCP tools may return structured listing, property, photo, price-history, comparison, session, and calculator data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Network tools are read-only and require an active signed-in Compass browser session through fetchproxy; local mortgage and affordability calculations do not require network access.]

## Skill Version(s):

0.14.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
