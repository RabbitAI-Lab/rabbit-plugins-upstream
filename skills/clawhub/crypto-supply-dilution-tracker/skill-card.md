## Description:

Analyzes crypto token supply dilution risk by comparing circulating supply against max or total supply using CoinGecko market data and returns dilution scores, remaining supply percentages, and risk labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

External crypto researchers, traders, DeFi analysts, portfolio reviewers, and developers use this skill for quick supply-side due diligence on how much token supply may still enter circulation. It is a screening proxy for dilution risk, not investment advice or a vesting unlock calendar.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes live requests to CoinGecko when run.

Mitigation: Use it only in environments where outbound requests to CoinGecko are acceptable.

Risk: The results are a supply-side proxy and do not include vesting cliffs, lockup schedules, or investment suitability analysis.

Mitigation: Treat the output as one due-diligence signal and confirm tokenomics, unlock schedules, and financial decisions with independent sources.

## Reference(s):

- [CoinGecko coins markets API](https://api.coingecko.com/api/v3/coins/markets)
- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/crypto-supply-dilution-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Plain text table or JSON, with usage guidance and shell command examples in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live CoinGecko data when executed; no API key is required.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
