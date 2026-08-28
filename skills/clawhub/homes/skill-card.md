## Description:

Look up real-estate listings, property details, price/tax history, market reports, saved homes, and photo galleries on homes.com via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate workflows use this skill to search homes.com listings, resolve property addresses, review property records, compare homes, inspect price and tax history, retrieve photo galleries, and run local mortgage or affordability calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route homes.com requests through a signed-in Chrome session and may expose saved homes or saved searches to the agent when those tools are used.

Mitigation: Use the saved-items tools only when account-derived homes.com data is appropriate for the agent context.

Risk: The skill depends on a separately installed fetchproxy browser extension.

Mitigation: Install the fetchproxy extension only from the referenced source and review it before use.

## Reference(s):

- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [homes-mcp source referenced by the skill](https://github.com/chrischall/homes-mcp)
- [fetchproxy extension source referenced by setup](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or structured text with MCP setup configuration and real-estate lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include homes.com listing details, property records, price and tax history, market statistics, saved-items summaries, photo URLs, and local calculator outputs.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
