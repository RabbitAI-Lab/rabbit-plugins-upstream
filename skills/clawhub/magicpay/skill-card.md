## Description:

Helps agents handle MagicPay payments, funding, saved details, agent email, account readiness, choices, and payment recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with MagicPay use this skill to prepare and track purchases, funding, checkout, subscriptions, saved details, and approved email while recovering interrupted payment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payments, crypto transfers, and x402 purchases can incur real charges, especially when Auto-Approve is enabled.

Mitigation: Review approval, Auto-Approve, spending limits, and top-up settings before use; reconcile the existing operation rather than retrying an uncertain charge.

Risk: Saved details and payment-scoped card values may be visible to the agent and host during form filling.

Mitigation: Review Memory permissions, use sensitive values only for the authorized task, and avoid copying them into replies, logs, or files.

Risk: Managed agent email can send messages on a user's behalf.

Mitigation: Review the recipient and exact draft through MagicPay's approval flow before sending.

## Reference(s):

- [MagicPay ClawHub release](https://clawhub.ai/xor777/skills/magicpay)
- [Skill homepage (author-provided)](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [OpenClaw marketplace documentation](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [Payment operations](references/payment-operations.md)
- [Safety guardrails](references/guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with payment status, instructions, and links when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment approval and settlement are distinct; report the status of the exact operation.]

## Skill Version(s):

0.4.85 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
