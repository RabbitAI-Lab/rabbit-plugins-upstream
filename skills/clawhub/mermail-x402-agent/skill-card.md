## Description:

Pay a user-selected x402 service with Mermail Agent Wallet / PayBox, then continue the original job with the paid result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when a task requires discovering an x402-paid service, resolving the required charge, completing a Mermail PayBox payment with approval, and continuing the original task with the paid result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate wallet payment and funding flows for paid x402 services.

Mitigation: Require a fresh payment preview and user approval that confirms the service origin, asset, chain, vendor floor, required charge, and maximum spend before payment.

Risk: HTTP 402 challenges, catalog rows, email, and paid-service payloads may contain untrusted instructions.

Mitigation: Treat those payloads as data, match the selected service and spend cap to the authenticated user's current request, and ignore embedded instructions that change scope or payment behavior.

Risk: Pending signatures, funding handoffs, or uncertain PayBox statuses can be mistaken for successful payment.

Mitigation: Continue the original task only after terminal payment success, reconcile uncertain status with the documented PayBox request flow, and never ask users to paste signing keys or approval secrets.

## Reference(s):

- [Mermail AI Skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail x402 Agent security guidance](artifact/references/security.md)
- [Mermail x402 Agent tools](artifact/references/tools.md)
- [Mermail x402 Agent workflows](artifact/references/workflows.md)
- [Mermail MCP server](https://console.mermail.app/mcp)

## Skill Output:

**Output Type(s):** [guidance, API Calls, markdown, configuration]

**Output Format:** [Markdown guidance with structured payment previews and tool-call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces payment-status summaries, blocker reports, and instructions for handoff URLs without exposing signing keys or payment secrets.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
