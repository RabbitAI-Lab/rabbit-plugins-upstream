## Description:

Look up real-estate listings, property details, market reports, and saved Redfin homes or searches via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate workflows use this skill to search Redfin listings, inspect property details, review market reports, calculate mortgage payments, and retrieve saved homes or searches when signed in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access private saved-home and saved-search data through a signed-in Redfin browser session.

Mitigation: Use the saved-home and saved-search tools only when that account data is intended to be shared with the agent.

Risk: The integration depends on an MCP server and browser extension operating in an authenticated browser context.

Mitigation: Prefer project-scoped MCP configuration and review the external npm package and browser extension source before installation.

Risk: Fresh Redfin sessions may encounter AWS WAF challenges before requests succeed.

Mitigation: Resolve the challenge in the active Chrome tab before relying on the skill for repeated lookups.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/redfin)
- [redfin-mcp npm package](https://www.npmjs.com/package/redfin-mcp)
- [redfin-mcp source](https://github.com/chrischall/redfin-mcp)
- [fetchproxy source](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing data, property details, market metrics, saved-home summaries, saved-search summaries, and mortgage calculations returned through MCP tools.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
