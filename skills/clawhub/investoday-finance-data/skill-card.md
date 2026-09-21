## Description:

Fetches Chinese financial-market data across A-shares, Hong Kong stocks, funds, indices, financial statements, announcements, research reports, real-time quotes, and macroeconomic datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to locate InvestToday endpoints and call the InvestToday CLI for Chinese market research, financial data lookup, and structured data export. It supports research workflows for quotes, fundamentals, filings, reports, macro data, sectors, funds, indices, and related comparisons without providing trading advice or executing orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can handle API credentials and includes a non-interactive example with an API key and --skip-verify.

Mitigation: Prefer interactive initialization or environment-based secret entry, avoid placing API keys directly in shell commands, and avoid --skip-verify unless the operator understands the consequence.

Risk: Financial outputs may be mistaken for investment advice or treated as conclusive when data is incomplete.

Mitigation: Treat outputs as research data, verify important conclusions against authoritative sources, and do not use the skill for direct buy/sell advice or order execution.

Risk: Security evidence reports contaminated or inconsistent finance examples in included references.

Mitigation: Review examples before relying on them, and validate material financial conclusions against the live API or another authoritative data source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English reference index](docs/references-index.en.md)
- [Chinese reference index](docs/references-index.md)
- [Base data references](references/基础数据.md)
- [Market data references](references/市场数据.md)
- [A-share stock quote references](references/沪深京数据/股票行情/实时行情.md)
- [A-share financial data references](references/沪深京数据/财务数据/三大报表当期数据.md)
- [Fund data references](references/基金/基金资料.md)
- [Index quote references](references/指数/基础行情.md)
- [Announcement references](references/公告.md)
- [Research report references](references/研报/基础数据.md)
- [Macroeconomic references](references/宏观经济/国内宏观.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, markdown]

**Output Format:** [Markdown guidance with inline CLI commands and references to structured API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, the @investoday/investoday-api package, network access, and initialized InvestToday API credentials.]

## Skill Version(s):

1.8.89 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
