## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to compare insurance products, estimate premiums, analyze coverage gaps, design personal or family insurance plans, and get general underwriting, compliance, and claims guidance.

### Deployment Geography for Use:

China (Mainland China)

## Known Risks and Mitigations:

Risk: Insurance recommendations may rely on defaults, incomplete product records, or stale static data.

Mitigation: Treat outputs as rough reference only and verify product status, eligibility, benefits, and premiums with licensed sources before acting.

Risk: Script calls can ignore user input or fail, which can make personalized recommendations unreliable.

Mitigation: Check script inputs, error responses, and assumptions before using generated analysis or plan outputs.

Risk: Personalized insurance analysis may involve financial, family, health, or underwriting details.

Mitigation: Share only the minimum necessary details and avoid unnecessary personal or health information until input handling and data practices are reviewed.

## Reference(s):

- [Insurance Advisor China Skill Definition](artifact/SKILL.md)
- [Insurance Knowledge Base](artifact/references/insurance-knowledge.md)
- [Regulatory Compliance Notes](artifact/references/compliance.md)
- [Insurance Product Data](artifact/references/products.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown guidance with comparison tables and JSON outputs from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static product data and local Python scripts for needs analysis, premium calculation, and plan design.]

## Skill Version(s):

1.8.443 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
