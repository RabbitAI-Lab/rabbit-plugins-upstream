## Description:

将多个 Excel、PDF 或图片来源的企业报表合并为统一结果，支持 Word 模板填充，并可在明确要求时生成含财务比率、风险评估和建议的分析报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[merlinbeard000](https://clawhub.ai/user/merlinbeard000)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, finance teams, and business analysts use this skill to merge enterprise reports, reconcile group consolidation data, fill Word templates, and generate reviewable financial analysis reports when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive enterprise and financial report data.

Mitigation: Use it only with reports and templates the agent is intended to read, and direct outputs to new filenames for review before sharing.

Risk: PDF extraction, image-based recognition, financial ratios, elimination entries, and generated narrative can be wrong or incomplete.

Mitigation: Review extracted data, ratio calculations, consolidation adjustments, and final report text before relying on the output.

## Reference(s):

- [Merge Modes](references/merge_modes.md)
- [PDF Extraction](references/pdf_extraction.md)
- [Image PDF Guide](references/image_pdf_guide.md)
- [Standard Report Template](references/standard_report_template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Files, Guidance]

**Output Format:** [Markdown guidance with command examples, JSON mapping/configuration snippets, and generated Excel or Word document outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include merged .xlsx files, filled .docx reports, extracted PDF tables, elimination-entry logs, and generated financial-analysis narratives for user review.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
