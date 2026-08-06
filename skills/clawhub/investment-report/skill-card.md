## Description:

生成A股个股深度投资报告，支持按公司名称单个或批量撰写股票分析、估值分析、交易计划和综合评分。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiu-chuan](https://clawhub.ai/user/jiu-chuan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to generate Chinese-language A-share company investment research reports from company names, including business breakdown, financial forecasts, valuation, risk notes, and a required disclaimer. Outputs should be treated as informational and independently verified before any investment decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill generates financial analysis and trading plans that may contain incomplete, stale, or incorrect market data.

Mitigation: Treat the output as informational, verify financial data and sources independently, and do not rely on the report as investment advice.

Risk: The skill writes markdown report files and may use the workspace root when no output folder is specified.

Mitigation: Specify an output folder before generation to avoid unexpected files in the workspace root.

## Reference(s):

- [Report Template](references/template.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown reports written as .md files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report filenames follow the documented business-and-company naming convention, and reports include a disclaimer that they are for learning and reference only.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
