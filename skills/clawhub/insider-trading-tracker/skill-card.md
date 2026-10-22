## Description:

Provides read-only analysis of SEC Form 4 insider transactions by ticker, market-wide activity, cluster buying, and confirmed 10b5-1 plans through SentiSense.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use the skill to review public insider-trading disclosures, distinguish open-market trades from compensation events, and identify potential cluster buying without placing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests go to SentiSense and may use a SENTISENSE_API_KEY from the environment.

Mitigation: Review the destination before use and provide the key only to the intended service.

Risk: Financial data may be incomplete in free preview responses or misleading when compensation transactions are treated as open-market trades.

Mitigation: Label preview results, separate open-market purchases and sales from awards and tax withholding, and treat findings as information rather than investment advice.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thesentitrader/skills/insider-trading-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Natural-language summaries with cited filing dates, transaction details, and preview status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only informational output; no trades or account changes.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
