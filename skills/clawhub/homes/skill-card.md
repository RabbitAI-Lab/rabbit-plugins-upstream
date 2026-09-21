## Description:

homes helps agents look up homes.com real-estate listings, property details, price and tax history, market reports, saved homes, and photo galleries through a configured homes-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search homes.com listings, resolve addresses, inspect property records and histories, compare properties, fetch saved homes or searches, and run local mortgage or affordability calculators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the external homes-mcp package and fetchproxy browser extension.

Mitigation: Install it only in environments where running those external components is acceptable, and review the package and extension before use.

Risk: Saved homes and saved searches use the active homes.com login and may return account-scoped data.

Mitigation: Use a deliberate browser session, avoid shared accounts or machines, and treat returned saved-item data as user-account data.

Risk: Listing and market results are scraped page data rather than official homes.com API responses.

Mitigation: Verify important price, tax, listing, and market information against authoritative sources before making decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes)
- [homes-mcp npm package](https://www.npmjs.com/package/homes-mcp)
- [fetchproxy extension setup](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Markdown or structured tool results with setup configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scraped homes.com listing, history, market, saved-search, and photo data depending on the selected MCP tool.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
