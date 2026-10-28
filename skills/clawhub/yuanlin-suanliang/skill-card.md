## Description:

基于 cad-file-reader 园林识图候选，按中英文图例分类统计苗木、解析苗木表设计基线、按闭合区域计算铺装面积，可选展开 DXF 块内铺装，输出带使用边界、置信分层（P0–P3）和证据坐标的园林概算底稿与物资计划草稿；不替代设计复核、放线、点树、竣工计量、对量、结算与正式报价。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

园林设计与工程造价人员可用它将 CAD 识图候选整理为可复核的苗木数量与铺装面积概算底稿，并生成物资计划草稿。使用者应在采购、定价或结算前人工核对结果。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Optional sharing can execute unverified local code and can make cached or unreviewed results appear trustworthy.

Mitigation: Use the standalone calculation workflow until sharing restricts execution to a verified client and corrects its review and cache checks.

Risk: Estimated quantities may be unsuitable for purchasing, pricing, or settlement without review.

Mitigation: Manually verify quantities before using them for purchasing, pricing, or settlement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisong2003-lgtm/skills/yuanlin-suanliang)

## Skill Output:

**Output Type(s):** [Analysis, Files, Markdown, CSV, JSON]

**Output Format:** [Excel workbook, CSV files, Markdown report, and JSON data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quantity and area estimates include confidence levels, evidence coordinates, and review flags.]

## Skill Version(s):

0.4.28 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
