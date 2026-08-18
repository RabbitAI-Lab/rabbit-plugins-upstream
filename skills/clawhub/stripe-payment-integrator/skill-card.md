## Description:

Helps developers plan and generate payment integration guidance and example code for Stripe payment intents, subscriptions, webhooks, refunds, Connect-style payouts, and WeChat Pay or Alipay alternatives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design and implement online payment flows for ecommerce, SaaS subscriptions, refunds, platform payouts, invoices, webhook processing, and domestic China payment alternatives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated payment, refund, subscription, or payout code can affect financial state if used against production accounts without review.

Mitigation: Run first in test or sandbox mode, review all generated code, and confirm financial state changes are scoped to the application logic.

Risk: Payment-provider API keys, webhook secrets, and merchant credentials are sensitive and may be exposed if hardcoded or committed.

Mitigation: Store secrets in environment variables or a secrets manager, keep webhook secrets separate from API keys, and avoid committing local credential files.

Risk: Webhook handling can be spoofed or duplicated if endpoints do not verify signatures and enforce idempotency.

Mitigation: Use HTTPS endpoints, verify provider signatures, deduplicate events by event ID, and route only application-approved event types.

Risk: The skill can suggest SDK installation or test commands through agent exec workflows.

Mitigation: Review shell commands before execution and run them only in approved development environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/stripe-payment-integrator)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with code blocks, API examples, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include payment, refund, subscription, webhook, and payment-provider SDK examples that require review before production use.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and changelog mention 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
