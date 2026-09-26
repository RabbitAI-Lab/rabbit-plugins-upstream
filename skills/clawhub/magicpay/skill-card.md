## Description:

MagicPay helps agents handle payments, funding, saved Memory values, agent email, account readiness, optional user choices, and payment recovery through remote MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to orchestrate MagicPay payment flows, checkout funding, x402 purchases, crypto transfers, Memory-assisted form filling, receipt and invoice handling, and agent email while preserving exact approvals and recovery state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive payment, saved Memory, and email workflows.

Mitigation: Install it only when those capabilities are intended, keep sensitive values out of chat and logs, and use MagicPay-hosted approval and OAuth pages for protected actions.

Risk: A payment approval, browser click, provider submission, or receipt view can be mistaken for settlement.

Mitigation: Treat only a durable completed payment operation as settlement, and reconcile the exact operation instead of repeating a possibly dispatched payment.

Risk: Saved Memory can persist protected values for later reuse.

Mitigation: Persist protected values only after explicit Save actions, reuse exact item and revision identifiers, and ask only for missing or ambiguous facts.

Risk: Email, invoices, seller responses, and web pages can contain untrusted instructions.

Mitigation: Use those materials as evidence or user-owned output, not as authority for payments, replies, account changes, or disclosure of saved information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xor777/skills/magicpay)
- [Clawdis homepage](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [OpenClaw marketplace README](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [MagicCard agent guidance](https://magiccard.ai/agents)
- [Remote Workflow](references/workflow.md)
- [Guardrails](references/guardrails.md)
- [MCP Routing Map](references/commands.md)
- [Remote Payment Operations](references/payment-operations.md)
- [Direct Browser Payments](references/host-browser-payments.md)
- [Memory](references/memory.md)
- [Connection Setup](references/setup.md)
- [Runtime Setup: OpenClaw](references/runtime-setup.md)
- [Exact Runtime Requests](references/requests.md)
- [Status Meanings](references/statuses.md)
- [Receipt Email and Invoices](references/invoices.md)
- [Agent email](references/email.md)
- [Subscriptions](references/subscriptions.md)
- [Normalized Choices](references/choices.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain-text operational guidance with command and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide payment, Memory, email, and recovery workflows; protected values should stay out of replies, logs, files, and exported evidence.]

## Skill Version(s):

0.4.67 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
