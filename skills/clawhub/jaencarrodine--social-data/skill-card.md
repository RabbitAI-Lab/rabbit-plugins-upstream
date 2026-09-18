## Description:

Unified social data API for AI agents. One API key for LinkedIn, YouTube, TikTok, X, Instagram, Reddit, and Facebook; structured JSON, no scraping infrastructure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve structured social, web, SEO, and webhook data through Superagnt APIs without maintaining separate scraping infrastructure or upstream vendor integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects agents to a broad remote data platform that includes social APIs, web scraping, SEO queries, and hosted webhooks.

Mitigation: Install it only when those capabilities are intended, and review enabled MCP tools and OAuth scopes before use.

Risk: The Superagnt API key and webhook receive URLs act as credentials.

Mitigation: Store them as secrets, avoid logging or sharing them, and rotate keys or webhook endpoints if exposure is suspected.

Risk: Hosted webhook deliveries can contain raw third-party payloads, headers, and source IPs.

Mitigation: Avoid sending sensitive internal URLs or secrets, validate each payload before acting on it, and acknowledge deliveries only after successful processing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jaencarrodine/skills/social-data)
- [Superagnt Social Data Documentation](https://superagnt.com/r/ch-social-data-docs)
- [Superagnt MCP Server](https://mcp.superagnt.com/mcp/social-data)
- [Superagnt Agent Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [LinkedIn API Reference](artifact/references/linkedin/README.md)
- [YouTube API Reference](artifact/references/youtube/README.md)
- [TikTok API Reference](artifact/references/tiktok/README.md)
- [X API Reference](artifact/references/x/README.md)
- [Instagram API Reference](artifact/references/instagram/README.md)
- [Reddit API Reference](artifact/references/reddit/README.md)
- [Facebook API Reference](artifact/references/facebook/README.md)
- [Web API Reference](artifact/references/web/README.md)
- [SEO API Reference](artifact/references/seo/README.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, API calls]

**Output Format:** [Markdown with curl examples, configuration guidance, and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for direct API use; MCP-capable clients can connect to the Superagnt MCP server.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
