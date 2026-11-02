## Description:

从 Excel/CSV 任务清单识别字段并计算可追溯的任务评分，输出带质检说明的 Excel、Markdown 和 JSON 结果；数据不足时会降级或报告失败，不编造分数。

This skill is ready for commercial/non-commercial use.

## Publisher:

[weikion](https://clawhub.ai/user/weikion)

### License/Terms of Use:

MIT-0

## Use Case:

需要汇总和比较任务工作量的团队可用它从 Excel/CSV 清单生成逐任务评分及可复核的批次报告。结果针对任务，不用于个人绩效定级或惩罚。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task names imported from spreadsheets may become active Excel formulas in generated reports.

Mitigation: Until imported text is kept as text by the exporter, process only trusted spreadsheets; keep reports private and review and calibrate scores before allocation decisions.

Risk: Reports may contain business data, and output can overwrite earlier results if paths are reused.

Mitigation: Keep reports private and use a dedicated output directory.

## Reference(s):

- [Source repository (server-resolved provenance)](https://github.com/weikion/gongfen-calc)
- [Scoring anchors and algorithm guidance](artifact/references/scoring_anchors.md)
- [Field dictionary and data quality rules](artifact/references/field_dictionary.md)
- [ClawHub skill page](https://clawhub.ai/weikion/skills/gongfen-calc)

## Skill Output:

**Output Type(s):** [Files, Spreadsheets, Markdown, JSON]

**Output Format:** [Excel workbook (.xlsx), Markdown report (.md), and structured JSON (.json)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-level scores with source-row traceability; insufficient input data is reported or causes a lower-confidence result.]

## Skill Version(s):

0.1.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
