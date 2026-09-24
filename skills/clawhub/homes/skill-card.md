## Description:

Look up real-estate listings, property details, price/tax history, market reports, saved homes, and photo galleries on homes.com via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search homes.com listings, inspect property details, compare homes, retrieve history and market data, and work with saved homes or searches through a signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external npm package and a separate Chrome extension that are not bundled in the artifact.

Mitigation: Review the homes-mcp package and fetchproxy extension before installation, and install them only from sources you trust.

Risk: Some tools can use a signed-in homes.com browser session to read saved homes or saved searches.

Mitigation: Use the skill only in browser sessions where this account-level access is intended, and avoid invoking saved-home or saved-search tools when that data should remain private.

Risk: homes.com may present AWS WAF challenges or session-authentication failures that interrupt data retrieval.

Mitigation: Confirm the homes.com tab is signed in and has cleared any browser challenge before relying on returned listing or history data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [fetchproxy extension setup](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or text responses with structured property data and setup snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing URLs, property records, history rows, market summaries, saved-home data, photo URLs, or local calculator results depending on the invoked MCP tool.]

## Skill Version(s):

2.1.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
