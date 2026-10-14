## Description:

Helps agents handle MagicPay payments, funding, saved Memory values, agent email, account readiness, user choices, and payment recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent to make purchases or manage a MagicPay account can check balances, fund payments, complete approved checkouts, manage subscriptions and receipts, use saved details, and recover uncertain transactions. The agent guides the workflow while consequential payment decisions remain subject to MagicPay approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payments or funding actions can spend money or be duplicated after an uncertain response.

Mitigation: Use the exact MagicPay approval for consequential actions and reconcile the same operation before any replacement; report settlement only when the completed operation confirms it.

Risk: Saved sensitive values and browser checkout details may be visible to the agent and host.

Mitigation: Use them only for the authorized task and supported input flow; do not repeat them in responses or copy them into files, logs, or exported evidence.

## Reference(s):

- [MagicPay skill on ClawHub](https://clawhub.ai/xor777/skills/magicpay)
- [MagicPay skill homepage](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [OpenClaw marketplace guide](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [Payment operations](references/payment-operations.md)
- [Browser payments](references/host-browser-payments.md)
- [Saved Memory and sensitive values](references/memory.md)
- [Payment status and recovery](references/statuses.md)
- [Value-handling guardrails](references/guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with payment status, choices, and relevant links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sensitive saved values should not be repeated in replies.]

## Skill Version(s):

0.4.91 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
