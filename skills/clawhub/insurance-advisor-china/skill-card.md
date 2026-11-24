## Description:

为中国大陆个人与家庭提供保险需求分析、产品对比、保费测算、方案设计以及投保和理赔指导。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆有保险需求的个人与家庭，用于分析保障缺口、比较保险产品、测算保费并获取投保合规与理赔流程指导。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: ClawScan reports a possible coverage-claim flaw that could lead the skill to say an excluded mild illness is covered; the partial scan leaves the evidence incomplete.

Mitigation: Before relying on a recommendation, verify coverage details with the insurer or against the applicable policy documents.

## Reference(s):

- [Product data](references/products.json)
- [Insurance knowledge](references/insurance-knowledge.md)
- [Compliance guidance](references/compliance.md)
- [National Financial Regulatory Administration information portal](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Chinese-language guidance and reports, Markdown comparison tables, and JSON calculation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product information is static; confirm current product details and premiums with insurers. Chinese is the default output language.]

## Skill Version(s):

2.4.39 (source: SKILL.md frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
