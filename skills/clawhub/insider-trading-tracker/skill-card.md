## Description:

Track insider trading from SEC Form 4 filings: insider buying and selling by ticker, market-wide insider activity, cluster buy signals where 3 or more insiders buy the same stock, and 10b5-1 plan detection for officer, director, and 10% owner trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to retrieve read-only SentiSense insider trading data from SEC Form 4 filings, summarize ticker-level or market-wide insider activity, and distinguish open-market transactions from awards, exercises, gifts, tax withholding, and 10b5-1 planned sales. Outputs are informational context and not personalized trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests include a SentiSense API key and are sent to SentiSense services.

Mitigation: Install only if that data flow is acceptable, and prefer the documented environment variable flow for API key handling.

Risk: The optional CLI auth command stores a local credential file.

Mitigation: Use SENTISENSE_API_KEY from the environment when local credential storage is not desired; remove stored CLI credentials if no longer needed.

Risk: Financial outputs could be mistaken for trading advice.

Mitigation: Treat all results as research context only, separate open-market trades from mechanical transactions, and avoid personalized buy or sell recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/insider-trading-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API Key Signup](https://app.sentisense.ai/get-api-key)
- [SentiSense Application](https://app.sentisense.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional CLI commands, REST request examples, and JSON response interpretation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for full API access; free-tier responses may be preview slices.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
