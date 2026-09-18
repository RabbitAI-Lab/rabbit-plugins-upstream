## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to connect HeyReach outreach workflows to agents, including campaign management, lead and list updates, inbox handling, and analytics through the superagnt API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes organization administration, API-key creation, user invitations, and broad webhook controls beyond ordinary outreach automation.

Mitigation: Install only when those capabilities are needed, use the least-privileged Superagnt and HeyReach credentials available, and avoid organization-scoped keys unless intentionally delegating administrative access.

Risk: Campaign, inbox, lead deletion, webhook, API-key, and user-invitation actions can materially affect outreach operations and connected accounts.

Mitigation: Require explicit human approval before sending messages, starting or resuming campaigns, deleting leads, creating webhooks, creating API keys, or inviting users.

## Reference(s):

- [HeyReach Integration documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [ClawHub listing](https://clawhub.ai/jaencarrodine/skills/heyreach-outreach)
- [Superagnt MCP server](https://mcp.superagnt.com/mcp)
- [Superagnt MCP setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Superagnt connections dashboard](https://app.superagnt.com/dashboard/connections)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON schemas and bash curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for command-based use; MCP-capable clients may connect to the Superagnt MCP server.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
