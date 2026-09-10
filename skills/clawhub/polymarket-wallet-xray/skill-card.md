## Description:

X-ray any Polymarket wallet for skill level, entry quality, bot detection, and edge analysis using public Polymarket trade data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze Polymarket wallet trade history, compare trader behavior, identify bots or anomalies, and study entry quality and risk profile. It supports research and strategy evaluation, not automated copy-trading or financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package asks for a Simmer API key and includes account-status functionality that can query private account balances and positions.

Mitigation: Use the public wallet analysis without a Simmer API key when account-status checks are not needed; only set SIMMER_API_KEY when intentionally querying a Simmer account, and rotate or remove the key after use.

Risk: Wallet metrics and recommendation text could be mistaken for financial advice or used for blind copy-trading.

Mitigation: Treat results as research signals only; independently validate conclusions, avoid automated copy-trading, and use conservative paper testing before any live strategy.

Risk: Public trade-history APIs may be incomplete, rate-limited, or unavailable, which can produce partial wallet analysis.

Mitigation: Check for warnings in the output, limit analysis size when rate-limited, and avoid making decisions from incomplete or stale data.

## Reference(s):

- [Simmer API Reference](https://docs.simmer.markets/api/overview)
- [Original Polymarket wallet analysis framework](https://x.com/thejayden/status/2020891572389224878)
- [Polymarket CLOB API](https://clob.polymarket.com)
- [Polymarket Data API](https://data-api.polymarket.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON analysis with wallet metrics, plus setup and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include profitability, entry quality, bot-detection, edge-detection, risk-profile, and recommendation fields.]

## Skill Version(s):

1.1.5 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
