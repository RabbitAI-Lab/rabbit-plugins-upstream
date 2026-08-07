## Description:

生成A股个股深度投资报告；用户提供公司名称后，生成包含公司概况、业务构成、财务预测、SOTP估值、投资逻辑、六维分析、交易计划和综合评分的报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiu-chuan](https://clawhub.ai/user/jiu-chuan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to draft A-share company investment research reports from one or more company names. It supports single-company and batch report generation with web-researched financial data, valuation assumptions, risk notes, trading plans, ratings, and a required disclaimer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated ratings, target prices, valuation assumptions, and trading plans may be mistaken for financial advice.

Mitigation: Treat reports as research drafts, verify source data and assumptions independently, and keep the required disclaimer in the generated Markdown.

Risk: Batch use can create multiple Markdown files in the workspace.

Mitigation: Specify the target folder and ask the agent to confirm filenames before writing report files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jiu-chuan/skills/investment-report)
- [Investment report template](references/template.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Analysis, Guidance]

**Output Format:** [Markdown investment report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate one or more reports named by business segment and company; each report should include cited financial data and a disclaimer.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
