## Description:

在本地解析宏业 .SGCFX 计价工程文件，导出清单、工料机及费用汇总，并对送审与审核版本进行核减对比和勾稽校验。

This skill is ready for commercial/non-commercial use.

## Publisher:

[kormendierijon681-oss](https://clawhub.ai/user/kormendierijon681-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Cost estimators and reviewers use the skill to extract bill-of-quantities, labor/material/machinery, and fee summaries from Hongye SGCFX files, compare versions, and reconcile exported totals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reusing extraction or output directories can overwrite or mix project results.

Mitigation: Use a fresh extraction and output directory for each project, and keep original files backed up.

Risk: Submitted/reviewed labels may not match the actual source versions.

Mitigation: Verify each version against its source file before interpreting a comparison, then reconcile the exported totals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kormendierijon681-oss/skills/sgcfx-hongye-parse)

## Skill Output:

**Output Type(s):** [Files, Spreadsheets, Analysis]

**Output Format:** [Excel .xlsx workbooks and CSV comparison reports]

**Output Parameters:** [Input: Hongye .SGCFX project files and optional versions to compare; output: selected directory.]

**Other Properties Related to Output:** [Local file processing with reconciliation checks; verify exported totals before relying on them.]

## Skill Version(s):

2.0.0 (source: package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
