## Description:

Uses StockToday’s Tushare-compatible gateway to retrieve, clean, compare, and export financial and macroeconomic data for Chinese, Hong Kong, and U.S. markets and other asset classes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[usa2046](https://clawhub.ai/user/usa2046)

### License/Terms of Use:

MIT

## Use Case:

External users can request market, financial statement, fund flow, sector, news, or macroeconomic research and receive a sourced data summary, comparisons, or an export. Developers can also use the Tushare-compatible interface for repeatable data retrieval workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional HTTP mode bypasses the promised server restrictions and could expose the API token.

Mitigation: Use a StockToday-issued token with the default HTTPS gateway, leave TUSHARE_GATEWAY_ALLOW_INSECURE unset, and restrict activation to financial requests. Have hostname validation corrected before using HTTP backups.

## Reference(s):

- [StockToday API gateway](https://tushare.citydata.club/)
- [StockToday](https://stocktoday.cn)
- [StockToday API interface reference](references/数据接口.md)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, CSV, Parquet, Code]

**Output Format:** [Markdown summaries and tables; CSV or Parquet exports; Python scripts when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include query scope, source, fields, row counts, and missing-data notes.]

## Skill Version(s):

2.1.9 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
