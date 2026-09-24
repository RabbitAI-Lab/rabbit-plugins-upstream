## Description:

Use for MagicPay payments, funding, Memory, agent email, account readiness, optional choices and human input, or payment recovery through remote MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use MagicPay to prepare and recover payment workflows, funding, Memory-backed form fills, agent email, and human-in-the-loop choices through MagicPay's remote MCP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended for high-impact payment and personal-data workflows involving amounts, recipients, checkout URLs, Auto-Approve settings, and saved Memory use.

Mitigation: Review the payment target, amount, recipient, saved details, and approval settings before execution, and rely on MagicPay's scoped approval and recovery workflows.

Risk: Materialized payment or Memory values could be exposed if copied into replies, helper files, logs, telemetry, or exported evidence.

Mitigation: Use sensitive values only through the authorized host input path and avoid quoting, logging, storing, or exporting them.

Risk: Ambiguous payment dispatch or settlement can create duplicate-payment risk if an agent retries or replaces an operation too early.

Mitigation: Preserve exact operation, run, request, and idempotency identifiers; reconcile only the same operation and treat only a durable completed payment operation as settlement.

## Reference(s):

- [MagicPay ClawHub Skill](https://clawhub.ai/xor777/skills/magicpay)
- [MagicPay Skill Source](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [MagicPay Marketplace README](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [Payment Operations](references/payment-operations.md)
- [Host Browser Payments](references/host-browser-payments.md)
- [Memory](references/memory.md)
- [Guardrails](references/guardrails.md)
- [Runtime Setup](references/runtime-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline tool names and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated MagicPay remote MCP connection for payment, Memory, approval, and email operations.]

## Skill Version(s):

0.4.65 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
