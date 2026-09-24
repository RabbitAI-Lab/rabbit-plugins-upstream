## Description:

Look up real-estate listings, property details, photos, price history, and resolve addresses on Compass via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate researchers use this skill to query Compass listings, retrieve property details and media, compare properties, inspect price history, and run local mortgage or affordability calculations through an MCP integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party MCP package and browser extension that use a signed-in Compass browser tab to fetch listing data.

Mitigation: Install only if comfortable with that access pattern, review the npm package and fetchproxy extension source separately, and keep the MCP entry scoped to projects where it is needed.

Risk: The integration relies on the user's authenticated browser session and Compass page behavior, which can fail when the session is unavailable or site restrictions change.

Mitigation: Confirm the browser extension and signed-in Compass tab are active before use, remove the extension and MCP configuration when no longer needed, and verify important listing data against Compass directly.

## Reference(s):

- [Compass Skill on ClawHub](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp source](https://github.com/chrischall/compass-mcp)
- [fetchproxy extension source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only Compass listing data, property details, photo URLs, price history, comparisons, diagnostics, and local mortgage or affordability calculations.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
