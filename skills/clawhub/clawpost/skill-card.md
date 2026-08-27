## Description:

Post to X (Twitter), LinkedIn, Facebook, TikTok, and Instagram via Claw Post API; comment on Reddit threads through the user's browser; and search for, join, and post to Facebook groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daydreamnationtechlabs](https://clawhub.ai/user/daydreamnationtechlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to publish social content, upload media for posts, reply on Reddit, and manage Facebook group discovery, joins, membership checks, and posts through Claw Post.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish posts, create Reddit comments, join Facebook groups, and request memberships through the user's logged-in browser session.

Mitigation: Require the agent to show the platform, account context, destination URL or group, media, and final text, then wait for explicit approval before each account-affecting action.

Risk: A leaked or over-shared CLAWPOST_API_KEY could allow actions through the connected Claw Post account.

Mitigation: Store the key only in the agent environment or secret store and rotate it from the dashboard when access should be revoked.

Risk: The paired Chrome extension operates on supported social sites and the Claw Post API.

Mitigation: Review the extension permissions before installation and use only when the operator accepts that browser-session access model.

## Reference(s):

- [Claw Post API documentation](https://clawpost.net/api-docs)
- [Claw Post MCP endpoint](https://mcp.clawpost.net/mcp)
- [ClawHub skill listing](https://clawhub.ai/daydreamnationtechlabs/skills/clawpost)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown instructions with HTTP examples and JSON request or response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CLAWPOST_API_KEY for REST API use, or MCP OAuth for compatible MCP clients.]

## Skill Version(s):

2.1.0 (source: server release evidence and CHANGELOG, released 2026-08-27)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
