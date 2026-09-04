## Description:

Looks up homes.com real-estate listings, property details, price and tax history, market reports, saved homes, and photo galleries through the homes-mcp MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for homes.com property search, listing details, history, market, saved-home, photo, and local mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party MCP server and browser extension that fetch homes.com pages through the user's signed-in Chrome session.

Mitigation: Review the homes-mcp and fetchproxy sources before installation, prefer project-level MCP configuration, and enable the integration only for workspaces where that browser-session access is acceptable.

Risk: Saved homes and saved searches can expose account-specific homes.com data to the agent.

Mitigation: Use saved-home and saved-search tools only when the user intends to share that account data in the active agent session.

Risk: homes.com may present AWS WAF challenges or session-authentication failures that interrupt page extraction.

Mitigation: Use the documented healthcheck and session diagnostics, resolve browser challenges in Chrome, and treat failed or partial extraction results as incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [homes-mcp source](https://github.com/chrischall/homes-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured real-estate records, comparison tables, history summaries, photo URLs, diagnostics, and local calculator results.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
