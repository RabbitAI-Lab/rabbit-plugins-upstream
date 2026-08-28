## Description:

Tracks SEC Form 4 insider buying and selling by ticker, market-wide insider activity, cluster-buy signals, and 10b5-1 plan indicators through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and interpret public insider-trading disclosures for market research, including ticker-level Form 4 activity, market-wide buying and selling, cluster buys, and planned-sale context. The skill is informational and read-only; it does not place trades, manage portfolios, or provide personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SentiSense API key and may optionally persist CLI credentials locally.

Mitigation: Use environment-based credentials when possible, restrict local credential storage to trusted machines, and remove stored CLI credentials when no longer needed.

Risk: Insider-trading data can be misread as investment advice or personalized trading guidance.

Mitigation: Present results as market research context only, separate open-market activity from awards and other corporate mechanics, and avoid buy or sell recommendations.

Risk: Free-tier and rate-limited responses may be truncated or delayed.

Mitigation: Disclose preview slices when present, respect Retry-After headers, and avoid overstating incomplete result windows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/insider-trading-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense Pricing](https://app.sentisense.ai/pricing?coupon=AGENTS26)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require SENTISENSE_API_KEY and network access to SentiSense; results should be treated as market research context, not investment advice.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
