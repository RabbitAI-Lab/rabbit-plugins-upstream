## Description:

Use for MagicPay payments, funding, Memory, agent email, account readiness, optional choices and human input, or payment recovery through remote MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use MagicPay to route payment, funding, checkout, Memory, invoice, choice, and agent email workflows through the MagicPay remote MCP while preserving exact approval and reconciliation state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate payment, checkout, funding, invoice, and email workflows that may have financial or account impact.

Mitigation: Install it only when MagicPay should handle those workflows, and review MagicPay approvals, checkout details, and email drafts before accepting them.

Risk: Saved Memory can include sensitive details that may later be reused in agent tasks.

Mitigation: Save secrets only when persistence is intended, and use protected values only for the authorized task through host-supported input paths.

Risk: Payment state can be ambiguous when approval, browser submission, merchant confirmation, or settlement are confused.

Mitigation: Treat durable MagicPay operation state as authoritative and use same-operation status or reconciliation rather than replaying uncertain work.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xor777/skills/magicpay)
- [Publisher Profile](https://clawhub.ai/user/xor777)
- [Clawdis Homepage](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [OpenClaw Metadata Homepage](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [Connection Setup](references/setup.md)
- [Runtime Setup: OpenClaw](references/runtime-setup.md)
- [MCP Routing Map](references/commands.md)
- [Remote Payment Operations](references/payment-operations.md)
- [Direct Browser Payments](references/host-browser-payments.md)
- [Memory](references/memory.md)
- [Exact Runtime Requests](references/requests.md)
- [Normalized Choices](references/choices.md)
- [Receipt Email and Invoices](references/invoices.md)
- [Agent email](references/email.md)
- [Subscriptions](references/subscriptions.md)
- [Remote Workflow](references/workflow.md)
- [Status Meanings](references/statuses.md)
- [Guardrails](references/guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration]

**Output Format:** [Natural-language guidance with exact tool-routing instructions, links, and occasional inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve backend-returned identifiers and avoid exposing sensitive Memory, payment, or email values.]

## Skill Version(s):

0.4.64 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
