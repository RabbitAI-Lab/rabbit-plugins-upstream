## Description:

根据房间类型、建筑与装修资料生成装饰概算和物资计划，并将 CAD 测量候选保留为待核对输入。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

施工员、技术员和造价人员可按房间或逐项尺寸编制装饰工程初步概算、物资需求计划及待复核清单；输出不替代正式报价或结算。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default setup may download, install and run an external CAD skill despite documentation claiming no network use.

Mitigation: Review the dependency and its setup before installing; in restricted or offline environments, set SKILL_NO_BASE=1 and install the reviewed CAD dependency manually if needed.

Risk: Reference prices and unverified CAD measurements may produce inaccurate estimates or material orders.

Mitigation: Check flagged items, drawings, project rules and current contract prices before using results for purchasing or decisions.

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)

## Skill Output:

**Output Type(s):** [Files, Analysis, Guidance]

**Output Format:** [Excel workbook, CSV tables and Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates estimate quantities from purchasing quantities and flags missing or uncertain inputs.]

## Skill Version(s):

0.9.17 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
