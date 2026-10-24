## Description:

Provides agents with TikTok video, creator, sound, and trend data for content and creator research as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and research agents retrieve TikTok video and creator details or search accounts and videos for social listening, analysis, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok queries, usernames, video IDs, and the bearer credential are sent to superagnt.

Mitigation: Review the data shared with superagnt and keep the credential private before making requests.

Risk: The optional MCP setup requests OAuth authorization.

Mitigation: Review the requested access before approving the MCP connection.

Risk: API usage consumes account-backed credits and may incur charges.

Mitigation: Monitor the credit balance and billing when using the API.

## Reference(s):

- [TikTok Data documentation](https://superagnt.com/r/ch-tiktok-data-docs)
- [TikTok Data ClawHub listing](https://clawhub.ai/superagnt/skills/tiktok-data)
- [MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)

## Skill Output:

**Output Type(s):** [JSON data, Shell commands, Guidance]

**Output Format:** [Structured JSON API responses and Markdown setup instructions with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API requests require a superagnt credential; an optional scoped MCP integration supports OAuth.]

## Skill Version(s):

2.0.7 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
