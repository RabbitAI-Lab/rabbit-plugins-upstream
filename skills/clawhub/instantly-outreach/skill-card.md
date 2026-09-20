## Description:

Manage cold email campaigns, leads, and outreach analytics via Instantly AI through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to connect Instantly AI through Superagnt so agents can manage outreach campaigns, leads, accounts, analytics, webhooks, and related workspace settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes workspace administration, credential, billing, and destructive account operations beyond ordinary outreach workflows.

Mitigation: Install it only in workspaces where the agent is allowed to administer Instantly, and require explicit human approval for administrative or destructive actions.

Risk: API key creation/deletion, workspace membership changes, ownership transfer, webhook setup, mailbox password handling, email actions, and bulk delete operations can materially change or expose account state.

Mitigation: Gate these operations behind user confirmation, least-privilege access, and review of the exact request before execution.

## Reference(s):

- [Superagnt Instantly AI Integration documentation](https://superagnt.com/r/ch-instantly-outreach-docs)
- [Superagnt MCP server](https://mcp.superagnt.com/mcp)
- [MCP agent setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Superagnt dashboard API keys](https://superagnt.com/r/ch-instantly-outreach-key)
- [Superagnt connections dashboard](https://app.superagnt.com/dashboard/connections)
- [ClawHub listing](https://clawhub.ai/jaencarrodine/skills/instantly-outreach)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl commands, endpoint tables, and JSON tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl; MCP-capable clients can connect through the Superagnt MCP server.]

## Skill Version(s):

2.0.5 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
