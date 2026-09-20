## Description:

Unified social data API for AI agents with one API key for LinkedIn, YouTube, TikTok, X, Instagram, Reddit, Facebook, web, and SEO data as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to connect agents to Superagnt APIs for social media, web, SEO, and webhook workflows without maintaining separate scraping infrastructure or platform-specific API integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives Superagnt an API key-backed role in fetching social, web, and SEO data, which can transmit sensitive URLs or data to an external service.

Mitigation: Use only organization-approved data, avoid private/internal URLs and regulated data unless Superagnt is approved as a processor, and rotate the API key if exposure is suspected.

Risk: Hosted webhook endpoints can receive and retain raw incoming events, headers, and source IP information.

Mitigation: Reuse existing endpoints when appropriate, treat receive URLs as credentials, rotate exposed webhook URLs, and avoid sending unrelated customer data.

Risk: Deleting a webhook endpoint immediately stops third-party senders from posting events.

Mitigation: Confirm with the user before deleting endpoints and verify that the sender configuration has been updated or disabled.

## Reference(s):

- [Superagnt Social Data Documentation](https://superagnt.com/r/ch-social-data-docs)
- [Superagnt MCP Social Data Server](https://mcp.superagnt.com/mcp/social-data)
- [Superagnt API Key Dashboard](https://superagnt.com/r/ch-social-data-key)
- [LinkedIn API Reference](references/linkedin/README.md)
- [YouTube API Reference](references/youtube/README.md)
- [TikTok API Reference](references/tiktok/README.md)
- [X API Reference](references/x/README.md)
- [Instagram API Reference](references/instagram/README.md)
- [Reddit API Reference](references/reddit/README.md)
- [Facebook API Reference](references/facebook/README.md)
- [Web API Reference](references/web/README.md)
- [SEO API Reference](references/seo/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration, JSON]

**Output Format:** [Markdown guidance with curl examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY for authenticated requests; webhook receive URLs should be treated as secrets.]

## Skill Version(s):

2.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
