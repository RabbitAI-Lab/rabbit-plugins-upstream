## Description:

Stripe API integration with managed OAuth for customers, subscriptions, invoices, products, prices, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer Stripe resources through Maton-managed OAuth while keeping credentials out of the local agent workflow. It is intended for Stripe account administration tasks such as reading customer, subscription, invoice, product, price, payment, and refund data, with explicit confirmation before writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic Stripe API path can reach broader Stripe endpoints than the reviewed scope technically enforces.

Mitigation: Stay within the documented Stripe resources unless the user explicitly requests an exact undocumented endpoint, then confirm the method, object IDs, amounts, and test or live mode before calling it.

Risk: Write-capable Stripe actions can affect live billing, payments, refunds, subscriptions, prices, or deletions.

Mitigation: Default to read-only calls, verify the connection and target resource first, prefer test mode or least-privileged access, and require explicit user confirmation for every write.

Risk: Ambiguous failures during money-moving calls can lead to duplicate charges or refunds if retried blindly.

Mitigation: After a timeout or server error, retrieve the relevant object or recent activity to determine the result before retrying; use the same Idempotency-Key when a retry is necessary.

Risk: Local Maton API keys can leak through logs, shell history, child processes, or persisted files when the CLI fallback is used.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist credentials, pass keys only through the active process environment when necessary, and rotate any key that may have been exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/stripe-api)
- [Maton](https://maton.ai)
- [Stripe API Reference](https://docs.stripe.com/api)
- [Stripe Testing](https://docs.stripe.com/testing)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Stripe API calls through Maton CLI or SDK workflows; write-capable actions require explicit user confirmation.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
