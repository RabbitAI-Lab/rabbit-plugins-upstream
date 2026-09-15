## Description:

Look up Compass real-estate listings, property details, photos, price history, address matches, comparisons, and mortgage or affordability calculations through the compass-mcp MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer real-estate questions from Compass listings, compare properties, inspect photos and price history, resolve addresses, and calculate mortgage or affordability scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup relies on mutable external code through the compass-mcp npm package and fetchproxy Chrome extension.

Mitigation: Use project-local MCP configuration, pin reviewed package and repository versions where possible, and inspect the extension permissions before loading it in Chrome.

Risk: The browser bridge uses the user's signed-in Compass session, so installation grants the bridge access to session-scoped Compass pages.

Mitigation: Install only when this access is acceptable, keep the bridged browser session scoped to the intended account, and review fetchproxy permissions before use.

Risk: Compass access depends on a signed-in browser tab and may fail when authentication, WAF challenges, or unsupported saved-home workflows block retrieval.

Mitigation: Run the health check, resolve browser challenges in Chrome, and verify important real-estate facts against Compass or other authoritative records before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass)
- [compass-mcp npm package](https://www.npmjs.com/package/compass-mcp)
- [compass-mcp GitHub project](https://github.com/chrischall/compass-mcp)
- [fetchproxy GitHub project](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured property data, comparison summaries, JSON snippets, and setup commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Network listing tools require compass-mcp, the fetchproxy Chrome extension, and a signed-in Compass browser session; local mortgage and affordability calculations can run without sign-in.]

## Skill Version(s):

0.14.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
