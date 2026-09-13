## Description:

Fetches date-, freshness-, and completeness-checked raw market and quantitative data for A-share, Hong Kong, and U.S. equities, including quotes, K-lines, technical indicators, limit-up and limit-down pools, fund flows, block trades, chip distribution, financial statements, and news.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent builders use this skill to retrieve normalized market data and raw audit records for market state checks, stock research workflows, watchlist tracking, and financial data retrieval. The skill provides data and validation boundaries rather than trading, position sizing, or investment conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An automatic quote fallback uses unencrypted HTTP and can cache market data that could be observed or tampered with.

Mitigation: Review the skill before installation, prefer configuring IWENCAI_API_KEY so the primary HTTPS provider is used, restrict file writes to the skill data directory, and avoid relying on fallback Sina quote data for high-stakes decisions unless the fallback is removed, made opt-in, or clearly labeled untrusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fize/skills/market)
- [Market Data Scenarios](references/scenarios.md)
- [iWenCai SkillHub](https://www.iwencai.com/skillhub)
- [iWenCai query2data API](https://openapi.iwencai.com/v1/query2data)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON document on stdout, with optional JSON output files and raw data paths for large market datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may write normalized market data, cache records, and raw observations under the skill data directory.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
