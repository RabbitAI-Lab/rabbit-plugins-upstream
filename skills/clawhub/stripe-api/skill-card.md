## Description:

Stripe API integration with managed OAuth for agent-assisted administration of customers, subscriptions, invoices, products, prices, payments, and related Stripe resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to inspect and administer Stripe accounts through Maton-managed OAuth. It supports read/list workflows and carefully approved write operations for customers, subscriptions, invoices, products, prices, payments, charges, payment methods, coupons, and refunds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad raw Stripe API access can reach high-impact financial actions beyond the documented safe area.

Mitigation: Use documented endpoints by default, review the exact endpoint and effect before raw API use, and require explicit user confirmation before every write.

Risk: Stripe administration can affect live billing, payment, and customer data.

Mitigation: Use OAuth with the least-privileged or test-mode account possible, pin the intended connection, retrieve target resources first, and revoke unused connections.

## Reference(s):

- [ClawHub Stripe Skill](https://clawhub.ai/byungkyu/skills/stripe-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [Stripe API Reference](https://docs.stripe.com/api)
- [Stripe Testing](https://docs.stripe.com/testing)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active Stripe connection.]

## Skill Version(s):

1.2.0 (source: server release evidence; skill frontmatter metadata reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
