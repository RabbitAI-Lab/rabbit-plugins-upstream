## Description:

Unified data API for AI agents. One API key for LinkedIn, YouTube, TikTok, X, Instagram, Reddit, and Facebook, plus web scraping, SEO data, and hosted webhook receiving. Structured JSON, no infra to run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI agents use this skill to retrieve structured data from social platforms, web search and scraping, and SEO APIs, or to receive and process hosted webhook events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and webhook contents are sent to superagnt, which retains delivery history after acknowledgement or endpoint deactivation.

Mitigation: Use a dedicated provider key, monitor credit usage, and account for retained delivery history when sending data.

Risk: Webhook receive URLs act as credentials, and incoming events may require validation before use.

Mitigation: Keep receive URLs secret, poll only the intended endpoint, and independently verify events before taking sensitive actions.

## Reference(s):

- [Social Data documentation](https://superagnt.com/r/ch-social-data-docs)
- [Social Data listing](https://clawhub.ai/superagnt/skills/social-data)
- [Scoped social-data MCP server](https://mcp.superagnt.com/mcp/social-data)
- [Facebook API Reference](artifact/references/facebook/README.md)
- [Instagram API Reference](artifact/references/instagram/README.md)
- [LinkedIn API Reference](artifact/references/linkedin/README.md)
- [Reddit API Reference](artifact/references/reddit/README.md)
- [SEO API Reference](artifact/references/seo/README.md)
- [TikTok API Reference](artifact/references/tiktok/README.md)
- [Web API Reference](artifact/references/web/README.md)
- [X (Twitter) API Reference](artifact/references/x/README.md)
- [YouTube API Reference](artifact/references/youtube/README.md)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured JSON data and Markdown guidance with curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses vary by platform; webhook deliveries include the sender's JSON payload.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
