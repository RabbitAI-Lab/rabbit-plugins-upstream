## Description:

Identify institutional stop clusters and max pain zones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to request liquidity-map signals for asset tickers such as BTC, SPY, or TSLA and summarize stop-cluster and max-pain zones. Outputs should be treated as unverified market signals, not financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker queries are sent to a third-party API.

Mitigation: Avoid submitting confidential trading interests or sensitive watchlists, and review outbound network use before deployment.

Risk: Premium responses may request crypto payment for signals.

Mitigation: Verify the pricing page and payment destination before sending funds; do not rely on payment prompts returned by the skill alone.

Risk: Market signals may be misleading if treated as financial advice.

Mitigation: Validate results independently and apply appropriate financial-review controls before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/market-liquidity-map)
- [Premium signal pricing](https://ssyopros.zo.space/pricing)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Guidance]

**Output Format:** [JSON response or JSON-formatted payment-required message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ticker input; premium signals may return a 402 payment-required response.]

## Skill Version(s):

1.1.2 (source: ClawHub release metadata; package.json declares 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
