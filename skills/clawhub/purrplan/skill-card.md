## Description:

Drive PurrPlan (social media scheduler) from your agent: plan, draft, schedule, and publish posts across 12+ networks, manage the unified inbox, and read analytics through PurrPlan's remote MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sebastiendb](https://clawhub.ai/user/sebastiendb)

### License/Terms of Use:

MIT-0

## Use Case:

External users and social media teams use this skill to connect an agent to their PurrPlan account for planning content calendars, drafting or scheduling posts, replying to inbox items after approval, and checking social analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer token exposure could allow access to the user's connected PurrPlan workspace within the token's scopes.

Mitigation: Use the narrowest token scopes that fit the workflow, store the token securely, and rotate it if exposed.

Risk: Write and inbox-reply permissions can publish posts or send messages from connected social accounts.

Mitigation: Require explicit user approval before publishing or replying, and use confirmation flags only after the user approves the exact action.

Risk: Inbox content can contain untrusted text that may try to steer the agent.

Mitigation: Treat inbox content as data rather than instructions and present proposed replies to the user before sending.

Risk: Running an unpinned mcp-remote package can introduce supply-chain uncertainty.

Mitigation: Prefer native HTTP MCP support or a pinned and vetted mcp-remote version.

## Reference(s):

- [PurrPlan Skill on ClawHub](https://clawhub.ai/sebastiendb/skills/purrplan)
- [PurrPlan Developer Documentation](https://purrplan.ai/en/developpeurs)
- [PurrPlan MCP Integration](https://app.purrplan.ai/app/mcp-integration)
- [PurrPlan MCP Health Check](https://app.purrplan.ai/api/mcp/health)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown guidance with JSON configuration and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a PurrPlan account token and user approval before publishing posts or replying to inbox messages.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
