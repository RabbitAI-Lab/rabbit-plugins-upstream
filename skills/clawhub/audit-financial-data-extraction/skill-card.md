## Description:

Extracts and calculates key financial indicators from audit report text and helps produce an Excel result file for tender-related financial data entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[longtel-skill](https://clawhub.ai/user/longtel-skill)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and financial operations users can use this skill to locate, extract, calculate, and verify consolidated and parent-company financial metrics from audit report text. It supports manual question-answer workflows and a Python-assisted workflow that writes extracted values and calculated indicators to Excel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic extraction may produce incomplete or inaccurate financial values when audit report text formatting does not match the expected patterns.

Mitigation: Review the generated Excel output, verify calculations against the source audit report, and manually supplement missing values before using the data.

Risk: Generated Excel files may contain confidential financial data.

Mitigation: Choose an appropriate local output location, avoid shared folders for confidential reports, and delete or protect generated files according to organizational data-handling rules.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/longtel-skill/skills/audit-financial-data-extraction)
- [Publisher Profile](https://clawhub.ai/user/longtel-skill)
- [2025 Annual Audit Report Key Financial Data Extraction Q&A](references/2025年度审计报告重点财务数据提取问答.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, files, guidance]

**Output Format:** [Markdown guidance with command examples and optional local Excel output from the bundled Python script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Automatic mode reads a user-provided text file and writes a local .xlsx file; users should review extracted values and manually fill any missing fields.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
