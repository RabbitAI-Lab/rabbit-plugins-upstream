## Description:

基于 cad-file-reader 园林识图候选，按中英文图例分类统计苗木、解析苗木表设计基线、按闭合区域计算铺装面积，可选展开 DXF 块内铺装，输出带使用边界、置信分层（P0–P3）和证据坐标的园林概算底稿与物资计划草稿；不替代设计复核、放线、点树、竣工计量、对量、结算与正式报价。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Landscape estimators and CAD practitioners use the skill to turn plant and paving candidates from landscape drawings into reviewable quantity takeoff and material planning drafts. Review confidence tiers, evidence coordinates, and flagged items before relying on any quantity.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Optional project sharing may execute unverified local code.

Mitigation: Prefer standalone calculation; if sharing is needed, choose a trusted client and verify the retrieved revision.

Risk: Draft estimates may have misleading approval labels or uncertain quantities.

Mitigation: Manually review uncertain quantities and treat results as budget and material planning drafts, not final measurements, settlement figures, or quotations.

Risk: Shared project records persist locally, and the workflow depends on a separate CAD reader.

Mitigation: Account for local persistence and review the cad-file-reader dependency before installation.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/yuanlin-suanliang)

## Skill Output:

**Output Type(s):** [Analysis, Files, Markdown]

**Output Format:** [Excel workbook, CSV files, and a Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Budget and material planning drafts with confidence tiers, evidence coordinates, and review flags; not final measurement or quotation.]

## Skill Version(s):

0.4.30 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
