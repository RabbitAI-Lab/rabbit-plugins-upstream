## Description:

TikTok videos, creators, sounds, and trend data for agents - content and creator research as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and data teams use this skill to look up TikTok video, creator, account search, and trend data through Superagnt for social listening, creator research, alerts, dashboards, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok lookup queries and the user's Superagnt credential to Superagnt services.

Mitigation: Use the scoped TikTok MCP endpoint or documented TikTok API endpoints, keep SUPERAGNT_API_KEY secret, and enable broader Superagnt platform families only when those capabilities are intentionally needed.

Risk: The skill depends on live network requests, Superagnt account credits, and a valid API key.

Mitigation: Verify the install with the documented credits endpoint before use and handle 401 or 402 responses as credential or credit issues.

## Reference(s):

- [Superagnt TikTok documentation](https://superagnt.com/r/ch-tiktok-data-docs)
- [Scoped TikTok MCP server](https://mcp.superagnt.com/mcp/tiktok)
- [Agent setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Superagnt API keys dashboard](https://superagnt.com/r/ch-tiktok-data-key)
- [ClawHub listing](https://clawhub.ai/jaencarrodine/skills/tiktok-data)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, JSON]

**Output Format:** [Markdown guidance with curl examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and network access to Superagnt API or the scoped TikTok MCP server.]

## Skill Version(s):

2.0.5 (source: frontmatter and server release metadata, released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
