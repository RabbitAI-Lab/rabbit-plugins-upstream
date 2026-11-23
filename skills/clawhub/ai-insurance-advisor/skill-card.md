## Description:

为中国大陆个人与家庭提供保险需求分析、产品与保费对比、方案设计及保险知识和合规提示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆有保险需求的个人与家庭，用于梳理保障需求、比较产品与保费、生成初步保险方案并解答基础保险知识问题。结果应结合现行保险条款核实；核保与理赔事项需转交专业服务。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: ClawScan 标记该技能为可疑（中等置信度）：方案设计脚本的两项发现称，明确列为除外的治疗可能被呈现为承保范围，从而误导保险比较或决策。

Mitigation: 依赖生成方案前，逐项对照保险公司的现行条款和除外责任核实保障范围，并请持牌保险专业人士复核。

Risk: 安全分析覆盖不完整：Skillspector 扫描了列出的七个组件，但因部分本地引用无法解析而标记为部分分析，仍存在不确定性。

Mitigation: 使用建议前检查随附的产品、知识和合规参考文件，并独立核实关键保障结论。

## Reference(s):

- [产品数据](references/products.json)
- [保险知识](references/insurance-knowledge.md)
- [合规提示](references/compliance.md)
- [ClawHub 技能页面](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [ClawHub 安全审计页面](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor/security-audit)
- [国家金融监督管理总局保险中介机构信息披露平台（公开查询入口）](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [中文文本、Markdown 对比表和结构化 JSON 报告]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [根据用户提供的个人、家庭、预算和现有保障信息生成；不写入文件。]

## Skill Version(s):

2.4.36 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
