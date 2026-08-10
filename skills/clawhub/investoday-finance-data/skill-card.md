## Description:

InvestToday Finance Data helps agents fetch Chinese financial-market data and investment-research information across A-shares, Hong Kong stocks, funds, ETFs, indices, financial statements, announcements, research reports, news, and macroeconomic datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and financial analysts use this skill to locate InvestToday endpoints and call the investoday-api CLI for market quotes, fundamentals, announcements, research, macro data, and structured exports. It is not intended for trading advice, order execution, or inventing conclusions when data is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Initialization examples include --auto-update and --skip-verify, and security evidence warns that this can enable an under-disclosed background updater that modifies the CLI and installed skills.

Mitigation: Prefer running initialization without --auto-update and without --skip-verify unless scheduled updates are explicitly intended; review update behavior before installation.

Risk: The skill uses an API key for InvestToday service access.

Mitigation: Treat API keys as sensitive secrets and avoid pasting real keys into shared logs, prompts, transcripts, or generated examples.

Risk: Financial query parameters are sent to InvestToday's external service.

Mitigation: Avoid sending confidential portfolio, strategy, or customer information unless external service use is approved for that data.

Risk: Market and financial data can be incomplete, unavailable, stale, or misinterpreted as investment advice.

Mitigation: State data limitations, avoid direct buy or sell recommendations, and do not infer conclusions from missing results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [API Reference Index (English)](docs/references-index.en.md)
- [API Reference Index (Chinese)](docs/references-index.md)
- [A-share, Shenzhen, Shanghai, and Beijing Data References](references/沪深京数据/基础信息/证券资料.md)
- [Fund Overview References](references/基金/基金资料/基金概况.md)
- [Macroeconomic Data References](references/宏观经济/国内宏观.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured CLI/API output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ and the @investoday/investoday-api package; network access and InvestToday API credentials may be required.]

## Skill Version(s):

1.8.63 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
