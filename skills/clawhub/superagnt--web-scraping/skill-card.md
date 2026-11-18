## Description:

Scrape, search, and map the web for agents — clean markdown, structured JSON, and site URL discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the skill to retrieve live web content, search results, structured data, and site URL lists for research, RAG, monitoring, and enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install verification step performs an account-credit lookup through the external service.

Mitigation: Review whether this lookup fits your workflow and use the skill only with a service you trust.

Risk: Requests authenticate to the external service with SUPERAGNT_API_KEY.

Mitigation: Keep the key in the configured environment variable and avoid exposing it in prompts or logs.

## Reference(s):

- [Web Scraping documentation](https://superagnt.com/r/ch-web-scraping-docs)
- [Scoped Web Scraping MCP server](https://mcp.superagnt.com/mcp/web-scraping)
- [MCP client setup](https://www.superagnt.com/install?facet=web-scraping)

## Skill Output:

**Output Type(s):** [Markdown, Structured JSON, HTML, Links, Images, Site URL lists]

**Output Format:** [Web content and search results in the requested format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Format and content options can be selected per request.]

## Skill Version(s):

2.0.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
