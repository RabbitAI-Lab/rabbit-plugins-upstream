## Description:

Manage LinkedIn outreach campaigns, leads, lists, inbox conversations, and analytics via HeyReach through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to connect agents to HeyReach outreach workflows, including campaign management, lead and list operations, inbox synchronization, and analytics through superagnt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration exposes outreach, inbox, webhook, workspace administration, and API-key creation capabilities through a single superagnt credential.

Mitigation: Use a narrowly scoped superagnt key where possible and avoid organization-scoped credentials unless admin actions are explicitly required.

Risk: Agent actions can send messages, start or change campaigns, delete leads, create webhooks, invite users, or create API keys.

Mitigation: Require manual confirmation before executing high-impact outreach, deletion, webhook, user-management, or API-key operations.

## Reference(s):

- [Superagnt HeyReach documentation](https://superagnt.com/r/ch-heyreach-outreach-docs)
- [Superagnt API key dashboard](https://superagnt.com/r/ch-heyreach-outreach-key)
- [Superagnt connections dashboard](https://app.superagnt.com/dashboard/connections)
- [Superagnt MCP endpoint](https://mcp.superagnt.com/mcp)
- [MCP client setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub skill listing](https://clawhub.ai/jaencarrodine/skills/heyreach-outreach)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls, JSON]

**Output Format:** [Markdown guidance with curl commands and JSON tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for direct API examples; MCP-capable clients can connect to the Superagnt MCP endpoint.]

## Skill Version(s):

2.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
