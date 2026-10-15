## Description:

Helps an agent handle MagicPay payments, funding, saved details, agent email, account readiness, user choices, and payment recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent to shop or manage payments can use MagicPay to check account readiness and balances, arrange funding, obtain payment approval, complete checkout, and reconcile uncertain outcomes. It also guides optional saved-detail and agent-email workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Purchases or transfers may exceed the user's intended spend or proceed without appropriate payment approval.

Mitigation: Review MagicPay approval settings and spend limits before use; require the exact operation's approval for consequential payments.

Risk: Saved personal details or credentials may be reused or exposed during checkout and agent-email workflows.

Mitigation: Save secrets only when reuse is intended, and keep materialized values out of replies, logs, files, and exported evidence.

Risk: An uncertain checkout outcome may lead to a duplicate charge if the payment is repeated.

Mitigation: Reconcile the same operation and verify durable completion before treating it as settled; never repeat a possibly dispatched payment.

## Reference(s):

- [MagicPay ClawHub release](https://clawhub.ai/xor777/skills/magicpay)
- [Skill homepage listed in release metadata](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [OpenClaw marketplace documentation listed in skill metadata](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [Payment operations](artifact/references/payment-operations.md)
- [Guardrails](artifact/references/guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with links and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include payment status, approval links, funding instructions, and receipt details.]

## Skill Version(s):

0.4.94 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
