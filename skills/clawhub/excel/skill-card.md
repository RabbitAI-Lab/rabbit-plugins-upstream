## Description:

Excel 表格去重清洗。自动去除多余空格、全角字符转半角、标准化手机号和身份证号、按关键列（姓名/手机号/编号）去重，并生成清洗报告 sheet。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dont4getme-2](https://clawhub.ai/user/dont4getme-2)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and agents use this skill to clean uploaded Excel workbooks that contain duplicate rows, inconsistent whitespace, full-width characters, phone numbers, or ID-card text. It guides the agent to produce a cleaned workbook and a concise cleaning report while preserving the original file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rows may be removed when the deduplication key columns do not match the user's intent.

Mitigation: Confirm the intended key columns before running the cleanup and review the generated 清洗报告 sheet afterward.

Risk: Contact or identity-like fields may be normalized in the output workbook.

Mitigation: Review the cleaned workbook before using it for customer, roster, registration, or other sensitive records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dont4getme-2/skills/excel)
- [Publisher profile](https://clawhub.ai/user/dont4getme-2)

## Skill Output:

**Output Type(s):** [shell commands, files, markdown, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated Excel workbook files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a cleaned workbook with a 清洗结果 sheet and a 清洗报告 sheet; the original input file is retained.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
