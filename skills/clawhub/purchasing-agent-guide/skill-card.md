## Description:

Guides users through MCP-based purchasing workflows, including login, store browsing, category selection, USDT checkout, order lookup, payment verification, refunds, and customer messages while keeping the assistant within the shopping flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yohyow](https://clawhub.ai/user/yohyow)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to connect to a purchasing MCP service and guide shopping sessions step by step. It helps an agent present disclaimers, collect required user confirmations, browse stores, place USDT orders, check order status, verify payment, request refunds, and leave messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service asks users to provide login passwords in chat.

Mitigation: Use a unique password for this service, do not reuse credentials, and avoid sharing unrelated secrets in the conversation.

Risk: The skill supports order placement and USDT payment verification.

Mitigation: Review each order before payment, verify the network and exact USDT amount, and confirm no-refund terms before sending funds.

Risk: The release security summary says the skill needs review before use.

Mitigation: Install only when the MCP operator is trusted and the shopping workflow has been reviewed for the intended use case.

Risk: The purchasing flow concerns procured accounts and could be misused.

Mitigation: Keep use within lawful, authorized educational or testing purposes and stop workflows that indicate illegal or unauthorized activity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yohyow/skills/purchasing-agent-guide)
- [Publisher profile](https://clawhub.ai/user/yohyow)
- [MCP setup guide](artifact/mcp-setup.md)
- [Conversation examples](artifact/examples.md)
- [Public MCP endpoint](https://mcp.137449244.xyz/mcp)
- [MCP health check](https://mcp.137449244.xyz/health)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration, shell commands]

**Output Format:** [Markdown guidance with MCP client configuration snippets and user-facing response patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes required disclaimer language, confirmation phrases, payment-transfer handling rules, and MCP setup instructions.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
