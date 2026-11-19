## Description:

为中国大陆个人与家庭提供保险需求分析、产品比较、保费估算、方案设计、保险知识与合规提示，并支持生成营销和培训文案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆有保险需求的个人、家庭及提供保险咨询的智能体，用于梳理保障需求、比较本地产品数据、估算保费和设计方案，并回答保险知识与合规问题。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: The security review reports a medium confidence risk that an explicitly excluded insurance benefit may be presented as covered; the overall scan was partial.

Mitigation: Verify coverage against current policy wording, preserve exclusions and conditions, and treat uncertain cases as unverified pending confirmation from the insurer or a qualified insurance professional.

Risk: Some referenced paths were missing during the scan, so its overall analysis is incomplete.

Mitigation: Review the complete release contents and resolve missing referenced files before relying on the scan as a full security assessment.

## Reference(s):

- [保险知识库](artifact/references/insurance-knowledge.md)
- [监管合规要点](artifact/references/compliance.md)
- [本地保险产品数据](artifact/references/products.json)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text, Markdown, JSON]

**Output Format:** [中文文本、Markdown 对比表格与结构化 JSON 分析结果]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [结果依赖随技能提供的静态产品、知识与合规资料；营销文案和培训话术由智能体生成。]

## Skill Version(s):

2.4.22 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
