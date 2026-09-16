## Description:

Fetches Chinese financial-market data and investment-research information across A-shares, Hong Kong stocks, funds, indices, financials, announcements, research reports, macroeconomics, and related datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up Chinese market quotes, company financials, fund and index data, announcements, research reports, macro indicators, and structured datasets for investment research or downstream analysis. It should not be used for direct buy or sell advice, automated trading, or invented conclusions when data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external InvestToday CLI handles API credentials and includes documented options for automatic updates and verification bypass.

Mitigation: Use interactive `investoday-api init`, avoid `--skip-verify`, and avoid automatic updates unless the publisher documents signed or integrity-checked updates.

Risk: Passing an API key directly on the command line can expose it through shell history or process metadata.

Mitigation: Prefer interactive credential entry or a secure local secret mechanism, and avoid placing API keys in command-line arguments.

Risk: Financial analysis, valuation, and trading-signal fields can be mistaken for personalized investment advice.

Mitigation: Treat returned data as research material, verify important figures against authoritative sources, and do not use the skill for direct buy or sell recommendations or automated trading.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English Skill Instructions](SKILL_EN.md)
- [API Reference Index](docs/references-index.en.md)
- [Chinese API Reference Index](docs/references-index.md)
- [A-Share Securities Reference](references/沪深京数据/基础信息/证券资料.md)
- [A-Share Real-Time Quotes Reference](references/沪深京数据/股票行情/实时行情.md)
- [A-Share Financial Statements Reference](references/沪深京数据/财务数据/三大报表当期数据.md)
- [Fund NAV Reference](references/基金/基金业绩表现/净值数据.md)
- [Index Quotes Reference](references/指数/基础行情.md)
- [Announcements Reference](references/公告.md)
- [Research Reports Reference](references/研报/基础数据.md)
- [Macroeconomics Reference](references/宏观经济/国内宏观.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and structured financial-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require Node.js 18+, the @investoday/investoday-api package, network access, API credentials, and endpoint-specific query or JSON body parameters.]

## Skill Version(s):

1.8.84 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
