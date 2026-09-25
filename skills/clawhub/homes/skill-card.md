## Description:

Look up real-estate listings, property details, price/tax history, market reports, saved homes, and photo galleries on homes.com via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate researchers use this skill to query homes.com listings, property details, price and tax history, market reports, saved homes, and photo galleries through the homes-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external homes-mcp npm package and a separate fetchproxy browser extension.

Mitigation: Install only if you trust those components and review their behavior before use.

Risk: A signed-in browser session can expose saved homes and saved searches from the user's homes.com account.

Mitigation: Use an account and browser session appropriate for the task, and request saved-home or saved-search data only when that access is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [homes-mcp source linked by artifact](https://github.com/chrischall/homes-mcp)
- [fetchproxy source linked by artifact](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and MCP tool usage descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents toward read-only MCP tools and local calculator outputs; compact views strip media URLs by default.]

## Skill Version(s):

2.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
