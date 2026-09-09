## Description:

Look up real-estate listings, property details, price/tax history, market reports, saved homes, and photo galleries on homes.com via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for homes.com listing search, property detail, price and tax history, market report, saved-home, saved-search, gallery, and local mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external homes-mcp package and fetchproxy browser extension.

Mitigation: Install only after reviewing those components and confirming you are comfortable with the external package and extension.

Risk: Some features read homes.com through a signed-in browser session, including saved homes and saved searches when requested.

Mitigation: Use an appropriate homes.com account session and avoid invoking account-specific tools unless that session data should be available to the agent.

Risk: homes.com may present an AWS WAF challenge or require an authenticated tab for account-specific features.

Mitigation: Keep the browser extension active, open homes.com in Chrome, sign in when needed, and resolve browser challenges before relying on tool output.

Risk: homes.com does not publish a public consumer API, so page structure changes can affect extraction quality.

Mitigation: Review important listing, history, tax, and market outputs against homes.com before making high-value decisions.

## Reference(s):

- [homes ClawHub page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [homes-mcp source](https://github.com/chrischall/homes-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some tools support compact or full views; compact output omits image URLs for supported listing, property, comparison, bulk, and market-report responses.]

## Skill Version(s):

1.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
