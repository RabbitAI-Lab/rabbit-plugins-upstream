## Description:

Unified data API for AI agents. One API key for LinkedIn, YouTube, TikTok, X, Instagram, Reddit, and Facebook, plus web scraping, SEO data, and hosted webhook receiving. Structured JSON, no infra to run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to retrieve structured social, web, and SEO data through one API and to receive and process hosted webhook events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webhook deliveries may be forged or replayed because the receive URL is the only credential and requests are not signature-verified.

Mitigation: Independently verify event authenticity before taking consequential actions based on a delivery.

Risk: The security review covered 10 of 11 components and one static analyzer was degraded.

Mitigation: Treat the scan as incomplete and review the remaining component and degraded analyzer results before deployment.

## Reference(s):

- [Social Data documentation](https://superagnt.com/r/ch-social-data-docs)
- [Scoped social-data MCP server](https://mcp.superagnt.com/mcp/social-data)
- [Facebook API reference](references/facebook/README.md)
- [Instagram API reference](references/instagram/README.md)
- [LinkedIn API reference](references/linkedin/README.md)
- [Reddit API reference](references/reddit/README.md)
- [SEO API reference](references/seo/README.md)
- [TikTok API reference](references/tiktok/README.md)
- [Web API reference](references/web/README.md)
- [X API reference](references/x/README.md)
- [YouTube API reference](references/youtube/README.md)

## Skill Output:

**Output Type(s):** [JSON data, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with curl examples, JSON schemas, and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a superagnt API key for authenticated data and webhook operations.]

## Skill Version(s):

2.0.17 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
