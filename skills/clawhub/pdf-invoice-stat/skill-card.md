## Description:

基于 pdfplumber、PaddleOCR 和 PP-StructureV3 在本地提取增值税电子发票、火车票和通行费 PDF 信息，并输出格式化 Excel。

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

财务、报销和运营人员可使用该技能将本地 PDF 发票、铁路电子客票和通行费票据提取为结构化 Excel，便于汇总、核对和报销整理。开发者也可直接运行随附 Python 脚本处理本地票据文件。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source PDFs and generated Excel files can contain sensitive financial and tax records.

Mitigation: Run the skill on a trusted local machine, restrict access to input and output files, and handle generated workbooks according to the user's financial-record retention policy.

Risk: Optional OCR paths may download model files locally and temporarily render PDF pages under /tmp.

Mitigation: Use OCR dependencies only when needed for scanned or complex PDFs, keep the machine single-user or otherwise trusted during processing, and clear temporary or cached OCR artifacts according to local policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seairteng/skills/pdf-invoice-stat)
- [Publisher profile](https://clawhub.ai/user/seairteng)
- [artifact/SKILL.md](artifact/SKILL.md)
- [artifact/CHANGELOG.md](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Excel workbook with console summary and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes user-provided local PDFs and writes a formatted .xlsx file; optional OCR dependencies may download model files locally on first use.]

## Skill Version(s):

2.4.1 (source: server release metadata and artifact changelog, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
