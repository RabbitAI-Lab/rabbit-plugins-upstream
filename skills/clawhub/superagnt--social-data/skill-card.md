## Description:

Unified data API for AI agents. One API key for LinkedIn, YouTube, TikTok, X, Instagram, Reddit, and Facebook, plus web scraping, SEO data, and hosted webhook receiving. Structured JSON, no infra to run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI agents use this skill to retrieve structured data across social platforms, web search and scraping, and SEO APIs. They can also configure hosted webhook endpoints to receive and process third-party events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webhook deliveries are accepted without signature verification, so an event may be processed without independent confirmation of its source.

Mitigation: Independently verify webhook events with their source before consequential actions, and treat each receive URL as a credential.

## Reference(s):

- [Social Data documentation](https://superagnt.com/r/ch-social-data-docs)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/social-data)
- [Scoped MCP server](https://mcp.superagnt.com/mcp/social-data)
- [MCP installation instructions](https://www.superagnt.com/install?facet=social-data)
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

**Output Type(s):** [JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON API responses and Markdown instructions with curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API requests use SUPERAGNT_API_KEY and may consume account credits.]

## Skill Version(s):

2.0.18 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
