## Description:

Use for MagicPay payments, funding, Memory, agent email, account readiness, optional choices and human input, or payment recovery through remote MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent coordinate MagicPay account setup, payment approvals, funding, Memory-backed form fill, agent email, subscriptions, invoices, and same-operation payment recovery through MagicPay workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags a high-impact payment setup that relies on remote instructions and an unpinned plugin.

Mitigation: Review the skill before installation, install only through the trusted OpenClaw plugin manager, and verify the publisher before enabling payment workflows.

Risk: The skill can handle payment approvals, OAuth links, Memory values, email drafts, browser form filling, and purchased deliverables.

Mitigation: Use private conversations for payment and OAuth links, keep sensitive values out of chat and logs, and follow MagicPay approval and same-operation recovery boundaries.

Risk: Development-mode diagnostics may expose read-only logs, database projections, and source context.

Mitigation: Avoid development-mode connections unless that diagnostic visibility is acceptable for the environment.

## Reference(s):

- [ClawHub MagicPay Skill](https://clawhub.ai/xor777/skills/magicpay)
- [MagicPay ClawHub Homepage](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [MagicPay OpenClaw Marketplace README](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [MagicPay Agent Guide](https://magiccard.ai/agents)
- [MagicPay Account Settings](https://app.magiccard.ai/settings)
- [Setup](references/setup.md)
- [Runtime Setup: OpenClaw](references/runtime-setup.md)
- [MCP Routing Map](references/commands.md)
- [Remote Workflow](references/workflow.md)
- [Guardrails](references/guardrails.md)
- [Status Meanings](references/statuses.md)
- [Payment Operations](references/payment-operations.md)
- [Host Browser Payments](references/host-browser-payments.md)
- [Memory](references/memory.md)
- [Normalized Choices](references/choices.md)
- [Requests](references/requests.md)
- [Invoices](references/invoices.md)
- [Agent Email](references/email.md)
- [Subscriptions](references/subscriptions.md)
- [Development Session Review](references/development-session-review.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with tool names, workflow steps, links, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to use MagicPay-controlled approval, Memory, email, browser form, invoice, subscription, and payment recovery workflows.]

## Skill Version(s):

0.4.43 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
