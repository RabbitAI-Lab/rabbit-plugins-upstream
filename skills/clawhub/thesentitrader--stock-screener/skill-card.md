## Description:

Screens tracked US stocks and ETFs using SentiSense sentiment, analyst, technical, momentum, and price signals through curated or custom filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research agents use this read-only skill to find stocks or ETFs matching sentiment, analyst, price, and technical criteria, including within a watchlist. Results are research context, not personalized trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screener queries, optional watchlist tickers, and the API key are sent to SentiSense.

Mitigation: Use the skill only if comfortable sharing these with app.sentisense.ai; keep the API key out of shared outputs.

Risk: Screener results may be mistaken for personalized investment advice or current price quotes.

Mitigation: Treat results as research context, not trading instructions; verify time-sensitive market data independently.

## Reference(s):

- [Stock Screener on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-screener)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with screening results and filter plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes matched counts and the executed plan; results reflect a periodically refreshed screener snapshot.]

## Skill Version(s):

1.3.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
