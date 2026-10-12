## Description:

Helps an agent manage MagicPay payments, funding, checkout, saved details, email, subscriptions, and payment recovery with user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

People and their agents use MagicPay to prepare and complete authorized purchases, manage funding and subscriptions, handle invoices and agent email, and reuse saved details when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real payments, transfers, and checkout can incur charges.

Mitigation: Review the exact purchase and spending limit; rely on MagicPay approval or an applicable policy before payment.

Risk: Explicit Memory saves can retain sensitive personal or payment information.

Mitigation: Review what will be saved and authorize saves only when later reuse is wanted.

Risk: Invoice and managed-email workflows may expose private correspondence or trigger account actions.

Mitigation: Confirm intended mailbox access and review replies and actions separately from reading messages.

## Reference(s):

- [MagicPay ClawHub listing](https://clawhub.ai/xor777/skills/magicpay)
- [Listed skill homepage](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [Listed OpenClaw marketplace documentation](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [Payment operations guidance](artifact/references/payment-operations.md)
- [Memory and saved-details guidance](artifact/references/memory.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Conversational text or Markdown with payment status, choices, and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment and fulfillment outcomes should be distinguished; sensitive saved values should not be echoed.]

## Skill Version(s):

0.4.89 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
