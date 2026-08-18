## Description:

Drive Databar MCP: leads, marketing intel, tables, flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, sales, marketing, recruiting, and research teams use this skill to run Databar MCP enrichment, scraping, table, flow, and export workflows with cost checks before paid operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Databar workflows can spend account credits on enrichment, scraping, table, source, and export operations.

Mitigation: Check balance and provider pricing before paid runs, price the full chain, and get explicit approval for large exports, schedules, and delete operations.

Risk: Contact discovery, social scraping, employment data, and CRM exports may involve personal data, provider terms, and regional privacy or outreach laws.

Mitigation: Confirm permission and a lawful basis before collection or outreach, review provider and platform terms, and avoid redistributing restricted raw provider data.

Risk: Some Databar operations are asynchronous, cached, position-aligned, or destructive, which can lead to incomplete results, stale data, mismatched joins, or permanent deletion.

Mitigation: Poll task status before reporting results, preserve input order for bulk joins, request fresh data only when needed, and require explicit user instruction before destructive calls.

## Reference(s):

- [Databar MCP skill page](https://clawhub.ai/dennisrongo/skills/databar-mcp)
- [Databar](https://databar.ai/)
- [Databar MCP documentation](https://docs.databar.ai/mcp-server)
- [Databar MCP endpoint](https://mcp.databar.ai/mcp)
- [Databar Recipes](references/recipes.md)
- [Databar Recipes - Marketing, SEO & Social](references/recipes-marketing-social.md)
- [Databar Recipes - Job Search, Recruiting & Research](references/recipes-people-research.md)
- [Databar Recipes - Finance, Apps & Web Traffic](references/recipes-finance-app.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and MCP tool-call patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents through Databar discovery, pricing, async polling, table persistence, scheduled sources, exports, and verification steps.]

## Skill Version(s):

0.2.2 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
