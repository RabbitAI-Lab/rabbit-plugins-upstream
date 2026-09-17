## Description:

Instagram profiles, posts, reels, and audience data for agents - influencer and brand research without a headless browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketing researchers, and creator-intelligence teams use this skill to access Superagnt Instagram profile, post, reel, location, hashtag, and audience data from agents without running a headless browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Instagram research targets to Superagnt as an external data provider.

Mitigation: Install only when Superagnt is an approved provider for the intended use, and prefer an Instagram-only API key or OAuth scope when available.

Risk: The referenced MCP platform can expose dynamically expandable tools beyond Instagram, including non-Instagram workspace capabilities.

Mitigation: Review MCP permissions before approval and avoid enabling non-Instagram tool families unless they are explicitly needed.

## Reference(s):

- [Superagnt Instagram Data Documentation](https://superagnt.com/r/ch-instagram-data-docs)
- [Superagnt Instagram MCP Server](https://mcp.superagnt.com/mcp/instagram)
- [Superagnt Agent Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Superagnt API Keys Dashboard](https://superagnt.com/r/ch-instagram-data-key)
- [ClawHub Skill Listing](https://clawhub.ai/jaencarrodine/skills/instagram-data)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Text]

**Output Format:** [Markdown with JSON schemas and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY; API responses are structured JSON from Superagnt endpoints.]

## Skill Version(s):

2.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
