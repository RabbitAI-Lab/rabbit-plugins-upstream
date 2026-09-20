## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate workflow users use this skill to search Compass listings, resolve addresses, retrieve property details and photos, compare listings, review price history, and calculate mortgage or affordability scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Compass requests through a signed-in browser session and a third-party browser extension.

Mitigation: Use a dedicated browser profile for Compass work, review the npm package and extension source before installation, and avoid profiles that contain unrelated sensitive sessions.

Risk: Compass data access relies on server-rendered page state and signed-in session behavior that may change or fail.

Mitigation: Treat lookup results as current Compass page observations, verify important property details against Compass directly, and expect clear failures when authentication or WAF challenges interrupt access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp source repository](https://github.com/chrischall/compass-mcp)
- [fetchproxy extension source repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown and structured text with property data, URLs, comparison summaries, calculator results, and setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Compass lookup behavior depends on compass-mcp, the fetchproxy browser extension, and an active signed-in Compass browser session.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
