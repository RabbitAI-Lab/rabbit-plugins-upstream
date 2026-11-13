## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。发布产物仅含 SKILL.md + 3 个只读参考文件（references/products.json、insurance-knowledge.md、compliance.md）+ 3 个运行时脚本（needs_analyzer / premium_calculator / plan_designer）；数据清洗脚本与回归测试脚本是本地维护工具，不随发布产物分发。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use this skill for insurance needs analysis, product comparisons, premium estimates, plan design, and explanations of insurance coverage and claims.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The security scan had medium confidence and was partial because part of the product dataset was not fully inspected.

Mitigation: Review the uninspected product data before installing or relying on the skill's comparisons and recommendations.

## Reference(s):

- [Insurance Product Dataset](references/products.json)
- [Insurance Knowledge Reference](references/insurance-knowledge.md)
- [Insurance Compliance Reference](references/compliance.md)
- [ClawHub Skill Release](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language text and Markdown reports, including comparison tables and structured recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis and recommendations are based on the supplied local product data and include relevant limitations and disclaimers.]

## Skill Version(s):

2.4.6 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
