## Description:

Track and cap x402 spend across providers with per-endpoint hard and soft caps, pre-authorized override budgets, cumulative spend tracking, and monthly ceilings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marketingkioldenburg](https://clawhub.ai/user/marketingkioldenburg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to gate x402 pay-per-request API calls against a budget.json policy before payment. It helps agents enforce per-call, session, provider, and monthly spend ceilings while keeping an audit-oriented spend log.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect price-unit conversion can cause an agent to compare micro-denominated x402 prices against USDC budget caps incorrectly.

Mitigation: Convert atomic USDC units using the documented 1e6 divisor before enforcing hard caps, soft caps, override budgets, and cumulative ceilings.

Risk: Unbounded retries or self-approved escalations can create unexpected paid x402 calls.

Mitigation: Use pre-authorized override budgets only, fail hard above configured caps, and retry only within the idempotency rules of the payment client.

Risk: Spend logs may contain transaction hashes or payment-signature metadata.

Mitigation: Protect append-only spend logs with access controls appropriate for payment-related metadata.

## Reference(s):

- [x402 homepage](https://www.x402.org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on budget.json policy checks, x402 price discovery, and append-only spend-log records.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
