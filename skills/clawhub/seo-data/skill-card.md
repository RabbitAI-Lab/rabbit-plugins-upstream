## Description:

SEO and search intelligence for agents: live Google results, keyword research, competitor and backlink gaps, page audits and AI answer visibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to connect to Superagnt SEO data through MCP or curl, then retrieve search results, keyword metrics, competitor gaps, backlink data, page audits, AI visibility metrics, and technology-stack lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends SEO targets, keywords, URLs, and the Superagnt API key to Superagnt services.

Mitigation: Use it only with data approved for Superagnt processing, protect SUPERAGNT_API_KEY as a secret, and rotate the key if it is exposed.

Risk: The skill points agents toward broader Superagnt platform discovery and enablement beyond the stated SEO endpoints.

Mitigation: Keep use scoped to the SEO MCP server and documented SEO API paths unless a human intentionally approves broader Superagnt tool-family enablement.

Risk: Some calls are priced per call or by returned row count.

Mitigation: Start with default limits and increase depth, limit, or broad query settings only after reviewing expected cost.

## Reference(s):

- [Superagnt SEO Data Documentation](https://superagnt.com/r/ch-seo-data-docs)
- [Superagnt SEO MCP Server](https://mcp.superagnt.com/mcp/seo)
- [Superagnt Agent Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub SEO Data Listing](https://clawhub.ai/jaencarrodine/skills/seo-data)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with JSON schemas and inline curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY; API call cost scales with endpoint and returned rows.]

## Skill Version(s):

2.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
