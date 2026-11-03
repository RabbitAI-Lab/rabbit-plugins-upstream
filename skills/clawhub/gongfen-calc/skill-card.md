## Description:

从格式不固定的 Excel/CSV 任务清单中识别字段、归一单位并评分，生成逐任务评级表和 Markdown 报告；不用于个人绩效评级、淘汰或扣罚。

This skill is ready for commercial/non-commercial use.

## Publisher:

[weikion](https://clawhub.ai/user/weikion)

### License/Terms of Use:

Apache 2.0

## Use Case:

团队和分析人员可用它把格式不一的 Excel/CSV 任务清单整理成可复核的任务评分表和报告，并查看数据质量提示。结果是任务分，不应用于个人绩效评级、淘汰或扣罚。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that output safeguards can allow source-file overwrites; existing reports and baseline.json can also be replaced.

Mitigation: Work on spreadsheet copies, choose a fresh output directory, and ensure output paths cannot resolve to the input file.

Risk: Imported text may be turned into spreadsheet formulas.

Mitigation: Treat input text as untrusted and use the skill only when exported text is forced to remain plain text.

Risk: Complete export behavior was not tested because dependencies were unavailable.

Mitigation: Prefer a reviewed installer version and check results using copies before relying on them.

## Reference(s):

- [Scoring anchors](artifact/references/scoring_anchors.md)
- [Field dictionary and data-quality checks](artifact/references/field_dictionary.md)
- [ClawHub skill page](https://clawhub.ai/weikion/skills/gongfen-calc)

## Skill Output:

**Output Type(s):** [Spreadsheet files, Markdown, JSON]

**Output Format:** [Excel workbook (.xlsx), Markdown report (.md), and JSON data (.json)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces task-level scores with data-quality notes; insufficient data may result in descriptive output without official points. Not an individual performance rating.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
