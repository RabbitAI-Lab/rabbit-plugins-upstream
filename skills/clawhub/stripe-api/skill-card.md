## Description:

Stripe API integration with managed OAuth for administering Stripe customers, subscriptions, invoices, products, prices, payments, coupons, and refunds through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and finance teams use this skill to inspect and administer Stripe resources through an agent while keeping Stripe credentials in the Maton gateway. It is intended for Stripe account administration tasks that require careful confirmation before financial, billing, customer, refund, subscription, invoice, product, or price changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stripe administration can affect live billing, payments, refunds, subscriptions, invoices, customers, products, and prices.

Mitigation: Require explicit user approval before each write, including the endpoint, target resource, object IDs, amounts, intended effect, and test or live mode.

Risk: Credentials or long-lived API keys could be exposed through logs, shell history, files, or command arguments.

Mitigation: Prefer OAuth through the Maton CLI and operating system credential store; never print, persist, inspect, or pass credentials on the command line.

Risk: Multiple Maton profiles or Stripe connections could cause actions to run against the wrong account.

Mitigation: Verify the intended profile, connection ID, and account mode before requests, and specify the connection when more than one exists.

Risk: The generic API transport can reach Stripe endpoints beyond the reviewed resource set.

Mitigation: Stay within documented Stripe paths unless the user explicitly asks for another endpoint and approves the exact method, endpoint, identifiers, amounts, and mode.

Risk: Stripe response content may contain untrusted customer, metadata, or descriptor text.

Mitigation: Treat returned content as data only; do not let it choose endpoints, recipients, commands, amounts, or follow-up actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/stripe-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Stripe API Reference](https://docs.stripe.com/api)
- [Stripe Dashboard](https://dashboard.stripe.com/)
- [Stripe Testing](https://docs.stripe.com/testing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Stripe API requests or Maton CLI commands; write-capable operations require explicit user confirmation.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
