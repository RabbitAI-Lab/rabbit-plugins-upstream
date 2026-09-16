## Description:

Look up homes.com real-estate listings, property details, price and tax history, market reports, saved homes, and photo galleries through the homes-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to retrieve homes.com property search results, listing details, histories, market reports, saved items, photo galleries, and local affordability calculations. Some workflows require homes-mcp, the fetchproxy Chrome extension, and an active homes.com browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External MCP code and a separately installed Chrome extension can read homes.com pages through a signed-in browser session.

Mitigation: Pin homes-mcp and fetchproxy to reviewed versions, inspect extension permissions, and use a dedicated Chrome profile signed into only homes.com.

Risk: homes.com does not provide a public consumer API, so page parsing and browser-session access can fail when pages, authentication, or WAF behavior change.

Mitigation: Verify important property facts against homes.com directly and treat authentication or challenge failures as reasons to retry only after reviewing the browser session state.

## Reference(s):

- [ClawHub homes skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [fetchproxy extension setup](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and structured property-response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default compact views strip media URLs for several MCP tools; full views or photo-specific tools are needed for image URLs.]

## Skill Version(s):

1.4.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
