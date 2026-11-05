## Description:

Use Geekflare for live web search (including full Google SERP results), scraping public webpages into Markdown or structured JSON, page metadata, brand identity (logos, colors, fonts), screenshots, URL-to-PDF, and website diagnostics such as uptime, DNS, TLS/SSL, redirects, broken links, load time, and Lighthouse audits. Trigger when a user needs current public-web data, clean page content, a visual capture, or a health check of a website or domain, even if they do not mention Geekflare.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekflare](https://clawhub.ai/user/geekflare)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use Geekflare to retrieve current information from public websites, extract page content and metadata, capture screenshots or PDFs, and inspect website availability, DNS, TLS, redirects, links, performance, and Lighthouse results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and target URLs are sent to Geekflare and may consume account credits.

Mitigation: Avoid confidential queries and URLs containing access tokens; choose the narrowest suitable tool and account for credit costs.

Risk: An API-key-bearing connection URL could expose account credentials.

Mitigation: Prefer browser sign-in where supported; otherwise keep the key in a protected environment variable and restrict access to the connection configuration.

Risk: Port scanning can affect hosts the user is not authorized to test.

Mitigation: Run open-port checks only against hosts the user owns or is authorized to assess.

Risk: The external Geekflare server and client extensions have not been audited, and local package execution uses a third-party package.

Mitigation: Review and pin the local package version when using local execution, and handle returned data with appropriate care.

## Reference(s):

- [Geekflare MCP documentation](https://docs.geekflare.com/mcp/overview)
- [Geekflare API documentation](https://docs.geekflare.com)
- [Geekflare MCP tool reference](references/tools.md)
- [Geekflare skill release](https://clawhub.ai/geekflare/skills/geekflare)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Screenshots, PDFs, Website diagnostic results]

**Output Format:** [Markdown, JSON, screenshots, PDFs, and structured diagnostic results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected tool and the public availability of the target website.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
