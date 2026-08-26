## Description:

Stripe API integration with managed OAuth for administering customers, subscriptions, invoices, products, prices, payments, and related Stripe resources through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and finance administrators use this skill for agent-assisted Stripe administration, including reading account data and preparing customer, subscription, invoice, product, price, and payment changes. The skill should be installed only where Stripe administration is needed and write actions can be reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic Stripe API passthrough can reach high-impact financial endpoints beyond the short scope statement.

Mitigation: Verify the exact `maton api` endpoint, target Stripe account, resource IDs, amounts, and test or live mode before any request, and require explicit user confirmation for every write.

Risk: Stripe administration actions can modify billing, payments, subscriptions, invoices, customers, products, or prices.

Mitigation: Prefer test mode and read-only checks first, use the least-privileged Stripe connection available, and summarize financial consequences before executing a write.

Risk: Long-lived API keys or provider-issued tokens may be exposed if printed, stored, passed on command lines, or sent to the wrong host.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting credentials, and send raw HTTP fallback credentials only to `api.maton.ai` when the CLI cannot be used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/stripe-api)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Stripe API Reference](https://docs.stripe.com/api)
- [Stripe Testing](https://docs.stripe.com/testing)
- [Stripe Dashboard](https://dashboard.stripe.com/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue read or write Stripe API calls through Maton when the user has authenticated and approved high-impact operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
