## Description:

Use for MagicPay payments, funding, Memory, agent email, account readiness, optional choices and human input, or payment recovery through remote MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use MagicPay to coordinate payments, funding, payment recovery, saved Memory, optional choices, account readiness, invoices, and agent email through MagicPay/OpenClaw flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment, funding, and saved form data actions can affect money movement or expose sensitive values if used outside the intended approval flow.

Mitigation: Review MagicPay approval and top-up pages carefully, use private conversations for payment or email work, and rely on MagicPay/OpenClaw scoped controls for high-impact actions.

Risk: Choosing Save can persist sensitive values for later reuse.

Mitigation: Save values only when the user explicitly chooses Save, and avoid quoting or exporting protected values in replies, helper files, logs, or evidence.

Risk: Payment submission, merchant pages, or opened funding links may be mistaken for settlement.

Mitigation: Treat only a durable completed payment operation as settlement evidence, and use same-operation status or reconciliation for ambiguous outcomes.

## Reference(s):

- [ClawHub MagicPay skill page](https://clawhub.ai/xor777/skills/magicpay)
- [MagicPay source homepage](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [MagicPay marketplace README](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [Connection Setup](references/setup.md)
- [Runtime Setup: OpenClaw](references/runtime-setup.md)
- [MCP Routing Map](references/commands.md)
- [Remote Payment Operations](references/payment-operations.md)
- [Direct Browser Payments](references/host-browser-payments.md)
- [Memory](references/memory.md)
- [Exact Runtime Requests](references/requests.md)
- [Guardrails](references/guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown]

**Output Format:** [Markdown guidance with tool names, exact continuation rules, and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May route sensitive payment, Memory, email, invoice, and approval workflows through MagicPay/OpenClaw controls.]

## Skill Version(s):

0.4.55 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
