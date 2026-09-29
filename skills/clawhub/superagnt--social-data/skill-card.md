## Description:

Unified social data API for AI agents. One API key for LinkedIn, YouTube, TikTok, X, Instagram, Reddit, and Facebook - structured JSON, no scraping infrastructure. Also includes hosted webhook receiving for inbound events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call Superagnt APIs for structured social, web, SEO, and hosted webhook data without managing separate scraping infrastructure or upstream vendor accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends social, web, SEO, and webhook data to Superagnt.

Mitigation: Use it only with authorized data and apply retention and privacy controls before sending sensitive profile, business, or third-party data.

Risk: Hosted webhook receive URLs act like credentials and do not prove that an event is genuine.

Mitigation: Treat receive URLs as secrets, avoid logging or redisplaying them, and validate vendor payloads before acting on deliveries.

Risk: Webhook endpoints are persistent infrastructure and deletion immediately stops third-party POST delivery.

Mitigation: List and reuse existing endpoints where appropriate, acknowledge processed deliveries, and confirm with the user before deleting endpoints.

Risk: The security scan reports that the skill exposes broader web, SEO, and persistent webhook handling than the social-data framing clearly suggests.

Mitigation: Review the installed surface and restrict use to the documented APIs and workflows needed for the user's task.

## Reference(s):

- [Social Data Documentation](https://superagnt.com/r/ch-social-data-docs)
- [Social Data MCP Server](https://mcp.superagnt.com/mcp/social-data)
- [MCP Agent Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [LinkedIn API Reference](references/linkedin/README.md)
- [YouTube API Reference](references/youtube/README.md)
- [TikTok API Reference](references/tiktok/README.md)
- [X (Twitter) API Reference](references/x/README.md)
- [Instagram API Reference](references/instagram/README.md)
- [Reddit API Reference](references/reddit/README.md)
- [Facebook API Reference](references/facebook/README.md)
- [Web API Reference](references/web/README.md)
- [SEO API Reference](references/seo/README.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with curl commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for documented API calls.]

## Skill Version(s):

2.0.6 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
