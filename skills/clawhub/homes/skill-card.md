## Description:

Look up real-estate listings, property details, price and tax history, market reports, saved homes, saved searches, and photo galleries on homes.com via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for homes.com real-estate searches, property details, market history, saved-home information, and local mortgage or affordability calculations through a read-only MCP integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration reads homes.com pages through an active browser session, including account-scoped saved homes and saved searches when requested.

Mitigation: Use it only with a browser profile whose homes.com account data you are comfortable exposing to the agent.

Risk: homes.com may serve AWS WAF challenges or page variants that prevent extraction or cause incomplete results.

Mitigation: Confirm critical property details on homes.com directly before making real-estate decisions.

Risk: Mortgage, affordability, and rent-versus-buy calculations depend on user-supplied assumptions and may not reflect current financing, tax, insurance, or listing conditions.

Mitigation: Treat calculator outputs as decision support and verify financial, tax, and listing details with authoritative sources or qualified professionals.

## Reference(s):

- [homes ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [homes-mcp source repository](https://github.com/chrischall/homes-mcp)
- [fetchproxy extension source repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown summaries with structured real-estate facts and setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only homes.com access; saved homes and saved searches require an authenticated browser session.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
