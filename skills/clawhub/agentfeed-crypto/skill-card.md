## Description:

Guides agents in retrieving live crypto liquidation, funding, options, and market-regime data through free and paid AgentFeed API routes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seekdaseek](https://clawhub.ai/user/seekdaseek)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, analysts, and developers use this skill to examine current liquidation activity, funding extremes, options positioning, and market conditions before making their own decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid live API calls can spend USDC from the user's wallet.

Mitigation: Get user approval before paid calls, check the live price, and cap each payment at the approved per-call amount.

Risk: Payment-address lookalikes could misdirect a payment.

Mitigation: Use payment details only from a fresh API payment challenge and stop if the recipient differs from the documented address.

Risk: Market data, forecasts, and modeled positioning can be stale or mistaken for trading advice.

Mitigation: Check freshness and evidence, disclose model limits, and present findings as information rather than trading recommendations.

## Reference(s):

- [AgentFeed API documentation](https://x402.ochinimus.app/openapi.json)
- [AgentFeed homepage](https://x402.ochinimus.app)
- [AgentFeed source and issues](https://github.com/seekdaseek/agentfeed)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with market-data summaries and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid API responses are JSON; agent summaries should note data freshness and uncertainty.]

## Skill Version(s):

1.1.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
