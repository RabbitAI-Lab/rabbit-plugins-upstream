## Description:

Use Geekflare for live web search (including full Google SERP results), scraping public webpages into Markdown or structured JSON, page metadata, brand identity (logos, colors, fonts), screenshots, URL-to-PDF, and website diagnostics such as uptime, DNS, DNSSEC, TLS/SSL, redirects, broken links, load time, and Lighthouse audits. Trigger when a user needs current public-web data, clean page content, a visual capture, or a health check of a website or domain, even if they do not mention Geekflare.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scorpiock](https://clawhub.ai/user/scorpiock)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Geekflare to research current public-web information, extract page content, capture web pages, and assess website or domain health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, URLs, and extraction prompts are sent to Geekflare and could expose confidential information or sensitive URL parameters.

Mitigation: Exclude confidential details and sensitive URL parameters from requests.

Risk: The API key and key-bearing remote MCP URL could be exposed, and calls consume account credits.

Mitigation: Protect the key and MCP URL, keep credentials out of chat and committed configuration, and consider credit usage before making calls.

Risk: Hosted captures may be accessible to others, and local package installation introduces supply-chain risk.

Mitigation: Consider who can access hosted captures; for local installation, pin a reviewed package version and install only the integration needed for the client.

## Reference(s):

- [Geekflare MCP documentation](https://docs.geekflare.com/mcp/overview)
- [Geekflare API documentation](https://docs.geekflare.com)
- [Geekflare MCP tool reference](references/tools.md)
- [ClawHub skill release](https://clawhub.ai/scorpiock/skills/geekflare)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Configuration instructions, Shell commands]

**Output Format:** [Text, Markdown, JSON, screenshots, or PDF captures depending on the requested tool]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool-specific results may include hosted captures or downloadable files.]

## Skill Version(s):

1.1.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
