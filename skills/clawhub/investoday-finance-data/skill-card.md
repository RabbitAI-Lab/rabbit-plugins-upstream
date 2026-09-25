## Description:

Fetches Chinese financial-market data and investment-research information across A-shares, Hong Kong stocks, funds, indices, quotes, financials, announcements, research reports, news, and macroeconomic datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to locate InvestToday API references and run investoday-api calls for Chinese market research, data export, comparison, and financial analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can be exposed if placed directly in shell history or shared command logs.

Mitigation: Prefer interactive or otherwise protected API-key setup, and avoid pasting secrets into reusable shell commands.

Risk: Financial data can be incomplete, unavailable, delayed, or unsuitable as a sole basis for high-stakes decisions.

Mitigation: Verify high-stakes financial conclusions against authoritative sources and clearly state data scope, time range, permission, or network limitations.

Risk: Some endpoints may expose personnel, contact, or submitted free-text fields.

Mitigation: Handle those fields as potentially sensitive and avoid unnecessary disclosure or retention.

Risk: The skill depends on the third-party InvestToday API package and service.

Mitigation: Use it only when the package and service are trusted for the intended environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [Reference index](docs/references-index.en.md)
- [Basic data](references/基础数据.md)
- [Market data](references/市场数据.md)
- [A-share realtime quotes](references/沪深京数据/股票行情/实时行情.md)
- [A-share financial indicators](references/沪深京数据/财务数据/财务衍生指标数据.md)
- [Hong Kong stock basics](references/港股/基础数据.md)
- [Fund overview](references/基金/基金资料/基金概况.md)
- [Index data](references/指数/指数资料.md)
- [Research reports](references/研报/基础数据.md)
- [Announcements](references/公告.md)
- [Domestic macroeconomics](references/宏观经济/国内宏观.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with inline investoday-api shell commands and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference structured finance API outputs from the InvestToday CLI when credentials, network access, and endpoint permissions are available.]

## Skill Version(s):

1.8.90 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
