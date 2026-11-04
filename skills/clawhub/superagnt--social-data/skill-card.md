## Description:

Unified data API for AI agents. One API key for LinkedIn, YouTube, TikTok, X, Instagram, Reddit, and Facebook, plus web scraping, SEO data, and hosted webhook receiving. Structured JSON, no infra to run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use the service to retrieve structured data from social platforms, web search and scraping, and SEO APIs. They can also configure hosted webhook endpoints and review incoming event deliveries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key and webhook receive URLs act as credentials; webhook deliveries can contain raw payloads, headers, and source IP addresses.

Mitigation: Store keys and receive URLs as secrets, limit access, avoid logging or unnecessary sharing, and review what data will be collected before enabling delivery.

Risk: Webhook deliveries are not verified by a signature in the documented flow, so notifications may be untrusted.

Mitigation: Verify events using the provider's signing mechanism and validate their contents before acting; do not let notifications alone trigger financial or account changes.

Risk: API use may incur service charges, provider retention applies, and the hosted backend and optional MCP implementation were not audited.

Mitigation: Review billing and retention terms before sending sensitive queries or events, and assess the provider's security before relying on it for sensitive workflows.

## Reference(s):

- [Facebook API reference](references/facebook/README.md)
- [Instagram API reference](references/instagram/README.md)
- [LinkedIn API reference](references/linkedin/README.md)
- [Reddit API reference](references/reddit/README.md)
- [SEO API reference](references/seo/README.md)
- [TikTok API reference](references/tiktok/README.md)
- [Web API reference](references/web/README.md)
- [X API reference](references/x/README.md)
- [YouTube API reference](references/youtube/README.md)
- [Superagnt social-data documentation](https://superagnt.com/r/ch-social-data-docs)
- [Scoped social-data MCP server](https://mcp.superagnt.com/mcp/social-data)
- [Superagnt API key and account](https://superagnt.com/r/ch-social-data-key)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured JSON API results, Markdown web content, and setup guidance with curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated endpoints require SUPERAGNT_API_KEY; API usage may consume credits.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
