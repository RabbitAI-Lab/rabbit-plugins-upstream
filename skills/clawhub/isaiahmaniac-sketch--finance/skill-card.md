## Description:

Use this skill when the user asks about stock prices, options, dividends, splits, ticker details, cryptocurrency prices, market caps, or any financial market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[isaiahmaniac-sketch](https://clawhub.ai/user/isaiahmaniac-sketch)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to query US equities, options, dividends, splits, ticker metadata, and cryptocurrency market data through Polygon.io and CoinGecko examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Finance queries may be sent to Polygon or CoinGecko, which can expose requested tickers, coins, dates, or other market-data interests.

Mitigation: Avoid including private portfolio details unless they are intentionally part of the market-data request.

Risk: Market data is time-sensitive and may be gated to a specific date by the environment.

Mitigation: Include the query date or time context in outputs and verify current values before using results for decisions.

## Reference(s):

- [CoinGecko API](https://api.coingecko.com/api/v3)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with Python code blocks and tabular quick references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include API request examples, market-data summaries, ticker details, options contract details, dividend and split information, and cryptocurrency price or metadata results.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
