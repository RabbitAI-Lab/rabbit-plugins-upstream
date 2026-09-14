## Description:

Stripe API integration with managed OAuth for administering customers, subscriptions, invoices, products, prices, payments, and related Stripe workflows through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and finance-adjacent teams use this skill to inspect and administer Stripe resources through an agent while keeping Stripe credentials managed by the Maton gateway. It is suited for customer, subscription, invoice, product, price, payment, refund, and approved automation tasks that require explicit confirmation before writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stripe writes can change payments, refunds, invoices, subscriptions, and other customer-facing financial records.

Mitigation: Require explicit user confirmation with the exact endpoint, method, target resource, object IDs, amount, and test or live mode before every write.

Risk: The wrong Stripe connection or overly broad OAuth access could affect an unintended account.

Mitigation: Use OAuth with the least-privileged Stripe account available, verify the connection ID before each request, and revoke unused connections promptly.

Risk: Command-line examples involving API keys or webhook signing keys can expose secrets in shell history or logs.

Mitigation: Prefer OAuth and the operating system credential store; when a key is unavoidable, use a prompt or secret manager and rotate any secret exposed in history or logs.

Risk: Hosted functions and triggers can turn an approved one-off Stripe action into recurring automation.

Mitigation: Deploy only user-authored or user-reviewed handlers, prefer DENY_ALL network policy, and require separate approval for function creation, updates, invocation, and trigger routing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/stripe-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Stripe API Reference](https://docs.stripe.com/api)
- [Stripe Testing](https://docs.stripe.com/testing)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code examples, JSON examples, and procedural guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Stripe API calls, Maton CLI commands, hosted function snippets, trigger setup steps, and confirmation checklists for sensitive actions.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
