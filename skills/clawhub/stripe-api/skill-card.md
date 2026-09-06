## Description:

Stripe API integration with managed OAuth for administering customers, subscriptions, invoices, products, prices, payments, charges, coupons, refunds, and related Stripe account data through Maton CLI commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and finance-support teams use this skill to inspect and administer Stripe billing resources through guided Maton CLI and API commands. It is intended for Stripe administration workflows that start with read-only checks and require explicit approval for writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable Stripe operations can affect live billing, payments, subscriptions, invoices, refunds, and customer records.

Mitigation: Prefer read-only checks first and require explicit confirmation that includes the endpoint, target resource, object IDs, amounts, and test or live mode before any write.

Risk: Using the wrong Stripe connection or mode can apply an action to an unintended account or environment.

Mitigation: Verify the connection ID and live/test mode before each request, and use the least-privileged Stripe and Maton account available.

Risk: Connection deletion is irreversible and can break automation that depends on the connection.

Mitigation: List and match the exact connection ID with the user before deletion, and do not rely on a skipped confirmation unless the specific connection was already confirmed.

Risk: Stripe responses can include sensitive financial, cardholder, or customer personal data.

Mitigation: Return only the fields needed for the task and avoid printing, logging, or storing raw responses unless the user explicitly asks for them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/stripe-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Stripe API Reference](https://docs.stripe.com/api)
- [Stripe Testing](https://docs.stripe.com/testing)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request paths, command flags, resource identifiers, and safety confirmations for Stripe operations.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
