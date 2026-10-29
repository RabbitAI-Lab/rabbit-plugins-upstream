## Description:

Scrapes and searches public web pages and maps site URLs for agents, returning readable content and structured results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public web content, search results, and site URLs for research, monitoring, and data extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested URLs and search targets are sent to a third-party service.

Mitigation: Do not submit secrets, private or internal URLs, regulated data, or confidential investigation targets without authorization.

Risk: API requests and search-result scraping can consume paid credits.

Mitigation: Monitor API key usage and credit consumption before running broad searches or site maps.

## Reference(s):

- [Web Scraping documentation](https://superagnt.com/r/ch-web-scraping-docs)
- [MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub skill listing](https://clawhub.ai/superagnt/skills/web-scraping)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, URL lists]

**Output Format:** [JSON responses containing page content, extracted data, search results, or site URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional HTML and page screenshots; output varies with requested formats.]

## Skill Version(s):

2.0.7 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
