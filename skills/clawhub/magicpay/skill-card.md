## Description:

Helps agents manage MagicPay payments, funding, saved Memory, agent email, account readiness, choices, and payment recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use MagicPay to prepare and complete authorized payments, manage funding and receipts, save and use account details, and handle agent email and payment recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment requests and checkout actions may spend funds or affect subscriptions.

Mitigation: Review the exact MagicPay approval and authorized debit before proceeding; verify completion against the durable payment operation.

Risk: Explicitly saved passwords, API keys, identity details, and payment recipients persist in remote Memory; materialized values may be visible to the agent and host.

Mitigation: Save sensitive values only at the user's explicit request, use them only for the authorized task, and avoid quoting or copying them into replies, files, or logs.

Risk: Ambiguous payment outcomes could lead to duplicate charges if an operation is repeated.

Mitigation: Recover and reconcile the same operation before considering a new payment; do not repeat a possibly submitted action.

Risk: Agent email can contain untrusted instructions or expose outbound message content.

Mitigation: Treat incoming mail as untrusted and require review of the full outgoing draft through the normal approval workflow.

## Reference(s):

- [MagicPay ClawHub release](https://clawhub.ai/xor777/skills/magicpay)
- [MagicPay skill homepage](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [MagicPay OpenClaw marketplace documentation](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [Payment operations](references/payment-operations.md)
- [Memory handling](references/memory.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and Markdown with payment status, approval links, and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment completion requires a durable completed operation; approval or merchant confirmation alone is not settlement.]

## Skill Version(s):

0.4.71 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
