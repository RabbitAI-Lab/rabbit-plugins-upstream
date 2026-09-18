## Description:

TikTok videos, creators, sounds, and trend data for agents — content and creator research as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketing and research teams, and data teams use this skill to retrieve TikTok video details, creator profiles, account search, video search, and related structured JSON for social listening, creator intelligence, alerts, digests, dashboards, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The preferred MCP setup can expand into broader Superagnt workspace tools beyond TikTok research.

Mitigation: Review the MCP connection before installing; prefer a TikTok-only scope or curl/API use when only TikTok research is needed, and avoid enabling broader Superagnt tool families unless their access is understood.

## Reference(s):

- [TikTok Data documentation](https://superagnt.com/r/ch-tiktok-data-docs)
- [TikTok MCP server](https://mcp.superagnt.com/mcp/tiktok)
- [Agent setup instructions](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Dashboard and API keys](https://superagnt.com/r/ch-tiktok-data-key)
- [ClawHub listing](https://clawhub.ai/jaencarrodine/skills/tiktok-data)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with curl examples and JSON API schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY; curl-only usage and MCP connection are documented.]

## Skill Version(s):

2.0.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
