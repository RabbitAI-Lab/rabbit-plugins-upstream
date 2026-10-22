## Description:

根据房间类型、建筑说明、建筑图、结构图、房间装修表、做法表和节点详图，快速出装饰概算和物资计划；可导入 cad-file-reader 的长度/面积测量候选作为待核对输入，做法映射、洞口扣减、损耗、材料台账和清单量仍由本技能计算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

External construction estimators, site engineers, and quantity surveyors use this skill to prepare preliminary interior-finishing cost estimates and material plans from project drawings, room schedules, and finish details. It retains calculation bases, missing inputs, and review prompts for project-specific verification.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Setup and optional shared-state features may execute dependency or discovered scripts despite offline controls.

Mitigation: Review the dependency bootstrap before setup; for table-only estimates, run scripts/decor_qty.py directly. Enable shared state only with a trusted client and verify cached project inputs before reuse.

Risk: Estimates may be misleading if default rules, drawing measurements, or reference prices are treated as project-authoritative.

Mitigation: Verify project drawings, node details, current applicable requirements, and contract or local-market prices; treat outputs as preliminary rather than final measurement, settlement, or formal quotation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)
- [Publisher profile](https://clawhub.ai/user/lisong2003-lgtm)

## Skill Output:

**Output Type(s):** [spreadsheet, CSV, Markdown, guidance]

**Output Format:** [An XLSX workbook with six worksheets, CSV tables, and a Markdown report, including calculation bases, assumptions, missing items, and review prompts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preliminary estimating and material-planning outputs; values require project-specific review and are not for final measurement, settlement, or formal quotation.]

## Skill Version(s):

0.9.22 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
