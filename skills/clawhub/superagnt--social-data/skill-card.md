## Description:

Unified data API for AI agents. One API key for LinkedIn, YouTube, TikTok, X, Instagram, Reddit, and Facebook, plus web scraping, SEO data, and hosted webhook receiving. Structured JSON, no infra to run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to retrieve structured data across social platforms, web search and scraping, and SEO APIs, and to receive and process third-party webhook deliveries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webhook requests are not signature-verified, so forged events could be trusted; the receive URL also acts as a secret.

Mitigation: Keep receive URLs secret and independently verify events with the sending service before trusting or acting on them.

## Reference(s):

- [Social Data documentation](https://superagnt.com/r/ch-social-data-docs)
- [Scoped Social Data MCP server](https://mcp.superagnt.com/mcp/social-data)
- [Social Data ClawHub listing](https://clawhub.ai/superagnt/skills/social-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured JSON API responses with Markdown documentation and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY for authenticated data and webhook operations.]

## Skill Version(s):

2.0.15 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
