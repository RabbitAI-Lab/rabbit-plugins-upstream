## Description:

Send email and SMS and manage a Pingram account via hosted MCP in OpenClaw.

This skill is ready for commercial/non-commercial use.

## Publisher:

[millerm30](https://clawhub.ai/user/millerm30)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to connect Pingram's hosted MCP server, send email or SMS notifications, inspect delivery logs, and manage Pingram account resources such as phone numbers and sender domains.

### Deployment Geography for Use:

Global, with Pingram regional MCP endpoints available for US, Canada, and EU accounts.

## Known Risks and Mitigations:

Risk: Email and SMS content, recipient addresses, phone numbers, and delivery logs are handled by Pingram's hosted service.

Mitigation: Use Pingram only when it is the intended external notification provider, choose the regional endpoint that matches the account, and review sensitive message content and recipients before authorizing sends.

Risk: The skill can guide account-management actions for phone numbers, sender domains, inboxes, accounts, and A2P-related tools exposed by Pingram MCP.

Mitigation: Inspect proposed account changes before execution and prefer MCP tool listing or probe output over guessed tool names.

## Reference(s):

- [Pingram OpenClaw integration documentation](https://www.pingram.io/docs/integrations/openclaw)
- [Pingram MCP endpoint](https://mcp.pingram.io)
- [Pingram Canada MCP endpoint](https://mcp.ca.pingram.io)
- [Pingram EU MCP endpoint](https://mcp.eu.pingram.io)
- [ClawHub Pingram skill page](https://clawhub.ai/millerm30/skills/pingram)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to use Pingram MCP tools for notification, delivery-log, and account-management tasks.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
