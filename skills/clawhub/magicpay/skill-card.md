## Description:

Helps agents handle MagicPay payments, funding, saved information, email, account readiness, and payment recovery through a remote service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers using an agent can check balances, initiate authorized purchases and transfers, manage saved information and agent email, and follow up on payment status through MagicPay.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Purchases and transfers may spend funds through a connected payment account.

Mitigation: Require explicit spending intent and review MagicPay approval screens before authorizing payment.

Risk: Saved information and email workflows can expose or persist sensitive personal data.

Mitigation: Save information only on an explicit request; avoid storing passwords, API keys, or identity documents unless intentionally authorized.

Risk: A pending or ambiguous payment could be mistaken for completion or retried unnecessarily.

Mitigation: Check and reconcile the original payment operation before reporting settlement or starting a replacement.

## Reference(s):

- [MagicPay on ClawHub](https://clawhub.ai/xor777/skills/magicpay)
- [MagicPay homepage listed in release metadata](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [OpenClaw marketplace documentation listed in package metadata](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [Payment operations](references/payment-operations.md)
- [Memory handling](references/memory.md)
- [Guardrails](references/guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with status updates and approval links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment completion requires confirmation from the original operation; an approval screen or receipt link alone does not establish settlement.]

## Skill Version(s):

0.4.72 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
