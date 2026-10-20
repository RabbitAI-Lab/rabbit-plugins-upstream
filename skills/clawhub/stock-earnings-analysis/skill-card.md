## Description:

Organizes US stock earnings into dated fiscal-quarter readouts with KPI changes, management guidance, call summaries, filing risk-factor changes, and market context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and researchers use this skill to review US company earnings by fiscal quarter, compare reported performance and guidance, and contextualize recent and upcoming reports. It provides research, not investment advice or trading automation.

### Deployment Geography for Use:

Global (US stocks)

## Known Risks and Mitigations:

Risk: Stock tickers and earnings-analysis queries are sent to SentiSense, with an API key when configured.

Mitigation: Use only if comfortable sharing those queries; keep the optional SENTISENSE_API_KEY private and use it only for read-only access.

Risk: Financial summaries or delayed market data could be mistaken for personalized advice or live prices.

Mitigation: Check report dates and data freshness, label delayed prices, and retain the not-investment-advice disclaimer.

## Reference(s):

- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key information](https://app.sentisense.ai/get-api-key)
- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown with dated quarter summaries and KPI tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [States coverage gaps and data freshness; includes a not-investment-advice disclaimer.]

## Skill Version(s):

1.4.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
