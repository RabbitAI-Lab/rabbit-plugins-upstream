## Description:

Track insider trading from SEC Form 4 filings: insider buying and selling by ticker, market-wide insider activity, cluster buy signals where 3 or more insiders buy the same stock, and 10b5-1 plan detection for officer, director, and 10% owner trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve and interpret read-only SEC Form 4 insider trading data for single tickers, market-wide activity, cluster buying, and 10b5-1 plan context. Outputs are informational market data and should not be treated as personalized buy or sell recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional CLI path executes a third-party npm package.

Mitigation: Prefer REST or curl when avoiding package execution; if using the CLI, run the pinned command with only SENTISENSE_API_KEY exposed and remove any stored credential when no longer needed.

Risk: Insider trading outputs can be misread as financial advice.

Mitigation: Present results as informational market data only, avoid personalized buy or sell recommendations, and report only what the API returns.

Risk: Form 4 rows can overstate directional trading if awards, exercises, gifts, tax withholding, 10b5-1 planned sales, or foreign-security rows are mixed into open-market totals.

Mitigation: Separate open-market P and S codes from corporate mechanics, exclude code-F tax withholding from sell tallies, flag confirmed 10b5-1 sales, and explain securityBasis rows without deriving implied prices.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/insider-trading-tracker)
- [SentiSense Homepage](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense API](https://app.sentisense.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with REST endpoint examples, shell command snippets, and optional JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output; requires SENTISENSE_API_KEY for full API access and may show preview-limited data on the free tier.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
