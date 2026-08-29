## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill for Chinese-language insurance needs analysis, product comparison, premium calculation, plan design, compliance reminders, and claims-process guidance. The skill supports personal and family insurance planning with local reference files and Python helper scripts.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The package includes maintenance scripts that can rewrite product data or patch skill scripts.

Mitigation: Use the documented advisor scripts for normal use and run datafix scripts only when intentionally maintaining the local product data or code.

Risk: Insurance product data may be stale, incomplete, or different from official insurer terms.

Mitigation: Verify product details, availability, premiums, and policy terms with official insurer or licensed-channel sources before making decisions.

Risk: Insurance and compliance outputs may be mistaken for professional legal, financial, or underwriting advice.

Mitigation: Treat outputs as planning guidance and use qualified professional review for final insurance, compliance, underwriting, or claims decisions.

## Reference(s):

- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Regulatory Compliance Notes](references/compliance.md)
- [Insurance Product Database](references/products.json)
- [Product Library Analysis Report (2026-08-21)](references/_repo_analysis_2026-08-21.md)
- [Insurance Database Analysis Report (2026-08-26)](references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands]

**Output Format:** [Chinese Markdown guidance with JSON outputs from local Python scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static product and compliance reference data; product details should be verified with official sources before acting.]

## Skill Version(s):

2.0.63 (source: server release metadata; SKILL.md frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
