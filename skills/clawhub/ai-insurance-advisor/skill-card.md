## Description:

面向中国大陆个人和家庭，提供保险需求分析、产品对比、保费估算、方案设计，以及保险知识和合规提示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆有保险需求的个人和家庭，用于梳理保障需求、比较产品、估算保费并准备保险方案。知识问答和合规提示供参考；营销文案及培训话术须按技能说明经合规审核。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: A confirmed coverage-unit issue could allow recommendations above a product’s actual coverage limit.

Mitigation: Avoid relying on coverage amounts until the unit issue is resolved and calculations are checked against the product data.

Risk: The security scan was partial and does not establish that the artifact is safe.

Mitigation: Review the unresolved local references and complete a full security review before installation.

## Reference(s):

- [Insurance Knowledge](references/insurance-knowledge.md)
- [Compliance Guide](references/compliance.md)
- [Product Dataset](references/products.json)
- [ClawHub Security Audit](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor/security-audit)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [中文 JSON 数据及面向用户的中文说明和对比表]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [产品和知识参考来自随技能发布的本地文件；营销和培训内容应在合规审核后使用。]

## Skill Version(s):

2.3.6 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
