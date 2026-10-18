## Description:

将 CAD 园林识图结果整理为可复核的苗木统计、铺装面积概算和物资计划草稿，并标注证据、置信分层及待核对项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

景观设计与工程计量人员可将 CAD 识图候选整理成苗木数量、铺装面积和物资计划草稿，逐项复核证据与缺项；结果不用于竣工计量、结算或正式报价。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text from untrusted CAD drawings may appear as executable spreadsheet formulas in generated CSV/XLSX reports.

Mitigation: Use only trusted drawings and treat generated spreadsheets as unsafe until formula sanitization is added; review before opening them in spreadsheet software.

Risk: Incomplete drawing geometry or missing scale and layer information can produce misleading quantity estimates.

Mitigation: Verify drawing scale and units, inspect low-confidence items and evidence coordinates, and have a qualified reviewer confirm results before relying on them.

## Reference(s):

- [ClawHub 技能发布页](https://clawhub.ai/lisong2003-lgtm/skills/yuanlin-suanliang)
- [使用说明](README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown report, CSV tables and optional XLSX workbook]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confidence levels, evidence coordinates and items requiring review; quantities are preliminary estimates.]

## Skill Version(s):

0.4.19 (source: ClawHub release metadata; bundled skill files list older versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
