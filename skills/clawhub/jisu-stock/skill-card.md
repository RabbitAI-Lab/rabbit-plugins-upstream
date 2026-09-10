## Description:

按股票代码查当日行情与详情（分钟级趋势），按分类拉取股票列表，查询交易日历及财务报表。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer stock-market questions by retrieving current quotes, minute-level trends, stock lists, trading-calendar status, and financial-statement data from JisuAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stock query parameters and the JISU_API_KEY are sent to JisuAPI.

Mitigation: Install only if that data flow is acceptable, and constrain runtime access to python3, JISU_API_KEY, and api.jisuapi.com where the host supports it.

Risk: Returned market and financial data is third-party data and should not be treated as financial advice.

Mitigation: Use the results as informational context and verify important trading or business decisions against authoritative sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jisuapi/skills/jisu-stock)
- [JisuAPI stock API documentation](https://www.jisuapi.com/api/stock/)
- [JisuAPI homepage](https://www.jisuapi.com/)
- [Related ClawHub stock history skill](https://clawhub.ai/jisuapi/stockhistory)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Configuration]

**Output Format:** [JSON responses from a Python CLI, with Markdown usage guidance in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, a JISU_API_KEY environment variable, and network access to api.jisuapi.com.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
