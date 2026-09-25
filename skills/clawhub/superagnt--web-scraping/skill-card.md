## Description:

Scrape, search, and map the web for agents - clean markdown, structured JSON, and site URL discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to fetch public web pages as clean markdown or structured JSON, run web searches with scraped results, and map site URLs for research, RAG ingestion, monitoring, enrichment, and extraction workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs, search terms, scrape options, and resulting web-content processing requests are sent to superagnt.

Mitigation: Use public, non-sensitive targets unless there is approval to share the target information with the provider.

Risk: SUPERAGNT_API_KEY is a paid API credential.

Mitigation: Store it in the environment, limit exposure in logs or shared prompts, and rotate it if disclosure is suspected.

## Reference(s):

- [superagnt Web Scraping documentation](https://superagnt.com/r/ch-web-scraping-docs)
- [Dashboard and API keys](https://superagnt.com/r/ch-web-scraping-key)
- [Scoped MCP server](https://mcp.superagnt.com/mcp/web-scraping)
- [MCP agent setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/web-scraping)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with inline bash commands, API request examples, and JSON tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl; API responses can include markdown, structured JSON, links, images, screenshots, search results, and site URL maps depending on endpoint options.]

## Skill Version(s):

2.0.6 (source: frontmatter, release metadata, artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
