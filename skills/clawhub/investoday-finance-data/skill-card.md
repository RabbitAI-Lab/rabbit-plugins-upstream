## Description:

Fetch Chinese financial-market data and investment-research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, macroeconomics, and more than 200 related interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find Chinese market data, inspect securities and funds, gather announcements and research views, and export structured datasets for investment research or comparison. It should not be used for direct buy/sell advice, automated trading, or inventing conclusions when data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends a persistent background updater and package update channel.

Mitigation: Install only if the InvestToday npm package and update channel are trusted; prefer initialization without `--auto-update` and review or disable any scheduled updater.

Risk: Trading-signal and investment-analysis outputs may be mistaken for personalized financial advice.

Mitigation: Treat all signal and analysis outputs as informational data only, and avoid using the skill for direct buy/sell advice or automated trading.

Risk: Free-text API fields may transmit sensitive user-provided content to the data service.

Mitigation: Do not submit confidential notes, credentials, account details, or personal data to free-text API fields.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [API reference index](artifact/docs/references-index.en.md)
- [A-share company and market data references](artifact/references/沪深京数据/公司行为/基本信息.md)
- [A-share real-time quotes reference](artifact/references/沪深京数据/股票行情/实时行情.md)
- [Fund overview reference](artifact/references/基金/基金资料/基金概况.md)
- [Macro economy reference](artifact/references/宏观经济/国内宏观.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or text with inline CLI commands and structured financial-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require Node.js 18+, the @investoday/investoday-api package, network access, local initialization, and endpoint-specific query or JSON body parameters.]

## Skill Version(s):

1.8.73 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
