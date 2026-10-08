## Description:

Screens US stocks and ETFs using sentiment, analyst ratings, technical indicators, momentum, price, and market cap, with custom filters or curated screens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research agents use this read-only skill to find US stocks and ETFs matching sentiment, analyst, technical, and market criteria, and to review the screen plan alongside results. It does not provide personalized trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The hosted service receives the SentiSense API key when a screen runs.

Mitigation: Use this skill only if comfortable sending the key to SentiSense; keep the key in the environment rather than displaying it in output.

Risk: Optional watchlist tickers and User-Agent details are sent to SentiSense.

Mitigation: Avoid sending sensitive watchlists or identifying agent details unless needed.

Risk: Screening data can be mistaken for live prices or financial advice.

Mitigation: Treat results as research data, identify their snapshot timing, and verify current market information before decisions.

## Reference(s):

- [Stock Screener on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-screener)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries of screening results and executed filter plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research data from periodic snapshots; results are not live quotes or personalized recommendations.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
