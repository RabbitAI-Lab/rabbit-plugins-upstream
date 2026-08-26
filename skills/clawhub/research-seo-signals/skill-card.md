## Description:

Retrieve traceable keyword, search result, trend, GEO, competitor, and backlink data for SEO research and analysis via SignalDig.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and growth teams use this skill to turn SEO research goals into scoped SignalDig MCP requests and receive concise, evidence-linked reports for keywords, domains, markets, and languages. It supports metric lookup, related-keyword discovery, SERP observations, Google Trends evidence, competitor analysis, GEO visibility, and backlink analysis without making the final growth decision for the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends SEO queries, target domains, market, and language to SignalDig through its MCP server.

Mitigation: Use the skill only when that data transfer is acceptable for the user and workspace, and avoid submitting confidential keywords or domains unless authorized.

Risk: The SignalDig API key is required for live research and could be exposed if copied into shared files or messages.

Mitigation: Store the key only in the client MCP configuration or approved secret store, and treat it as a password.

Risk: The artifact contains wording about X/social output, while security guidance says to question full-report output that claims X/social results without separate authorization.

Mitigation: Keep SEO results scoped to SignalDig SEO evidence, and require a separately authorized social-data skill or tool before treating social results as covered.

Risk: The skill can produce misleading reports if live MCP tools are unavailable or terminal results are partial.

Mitigation: Stop when the MCP server or tools are unavailable, never fabricate metrics, and clearly label partial coverage and limitations from the terminal result.

## Reference(s):

- [SignalDig Homepage](https://signaldig.com/)
- [SignalDig SEO MCP Endpoint](https://mcp.signaldig.com/data/seo/mcp)
- [Setup Guide](references/setup-guide.md)
- [SEO Research Functional Contract](references/mcp-contract.md)
- [ClawHub Skill Page](https://clawhub.ai/jerrykik/skills/research-seo-signals)
- [Publisher Profile](https://clawhub.ai/user/jerrykik)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance, configuration]

**Output Format:** [Markdown reports with evidence identifiers, exact observed values, limitations, source job identifiers, and setup guidance when the SignalDig MCP server is unavailable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the daily-growth-signals MCP server and a SignalDig API key; defaults to concise reports and reuses prior request IDs when available.]

## Skill Version(s):

1.4.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
