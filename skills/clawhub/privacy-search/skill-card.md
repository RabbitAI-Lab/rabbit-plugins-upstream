## Description:

Privacy Search provides privacy-oriented multi-engine search, optional local SearXNG routing, result ranking, content fetching, synthesized answers with citations, fact checking, vertical search modes, and MCP tools for agent integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use Privacy Search to add privacy-aware web search, result export, content fetching, citation-backed synthesis, fact checking, and MCP-accessible search tools to local or agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and fetched URLs may be sent to external search engines or web services.

Mitigation: Use strict privacy mode, prefer local SearXNG where appropriate, and configure a proxy or VPN when IP hiding matters.

Risk: Local cache and search history can retain sensitive query data on shared devices.

Mitigation: Use --no-cache for sensitive searches, disable cache/history in configuration, or clear cache and history after use.

Risk: MCP tools can let connected agents search, synthesize, or fetch arbitrary web content.

Mitigation: Expose MCP tools only to trusted agents and restrict tool availability when arbitrary URL fetches or external queries are not acceptable.

Risk: Automated search can encounter engine rate limits, parsing failures, or service-term constraints.

Mitigation: Keep default rate limits, respect robots.txt and search engine terms, and run self-tests before relying on specific engines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/privacy-search)
- [Quick Start](references/QUICK_START.md)
- [Search engine adapter documentation](references/engines.md)
- [MCP Server tool schema](references/mcp_schema.md)
- [Configuration example](references/config.yaml.example)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON responses, with CLI command examples and MCP JSON-RPC tool payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include web URLs, citations, search result metadata, fetched page text, cache/history notices, and privacy-mode diagnostics.]

## Skill Version(s):

1.8.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
