## Description:

Fetches Chinese financial-market data and investment research information across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, macroeconomics, and related market datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find InvestToday CLI endpoints, fetch structured Chinese financial-market datasets, compare securities or funds, and summarize informational market research. It is not intended for direct trading advice, automated order execution, or invented conclusions when data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes a non-interactive initialization example that passes an API key on the command line and combines auto-update with verification bypass flags.

Mitigation: Prefer interactive initialization, avoid passing API keys directly on the command line, and avoid --auto-update or --skip-verify unless the package and update source have been independently verified.

Risk: Financial-market outputs can be incomplete, unavailable, delayed, or unsuitable as a basis for trading decisions.

Mitigation: Treat outputs as informational research data, state data availability limits clearly, and avoid direct buy/sell advice or automated trade execution.

## Reference(s):

- [InvestToday Finance Data Skill](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English API Reference Index](docs/references-index.en.md)
- [Chinese API Reference Index](docs/references-index.md)
- [Basic Data](references/基础数据.md)
- [Market Data](references/市场数据.md)
- [A-share and Beijing/Shenzhen/Shanghai Stock Quotes](references/沪深京数据/股票行情/实时行情.md)
- [A-share Financial Statements](references/沪深京数据/财务数据/三大报表当期数据.md)
- [Hong Kong Stock Data](references/港股/基础数据.md)
- [Fund Overview](references/基金/基金资料/基金概况.md)
- [Fund Net Asset Value Data](references/基金/基金业绩表现/净值数据.md)
- [Index Quotes](references/指数/基础行情.md)
- [Research Reports](references/研报/基础数据.md)
- [Announcements](references/公告.md)
- [Domestic Macroeconomics](references/宏观经济/国内宏观.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API calls, Guidance]

**Output Format:** [Markdown with inline shell commands and structured finance-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on Node.js 18+, the @investoday/investoday-api package, initialized CLI configuration, network access, and API permissions; returned market data should be treated as informational research data, not financial advice.]

## Skill Version(s):

1.8.81 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
