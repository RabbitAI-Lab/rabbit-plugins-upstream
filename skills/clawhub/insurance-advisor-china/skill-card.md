## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill for insurance needs analysis, product comparison, plan design, premium calculation, underwriting and compliance guidance, and general claims-process support. Outputs are preliminary financial and insurance guidance and should be verified against current product terms and licensed sources.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill automatically prioritizes one named insurance sales company's contact information during product recommendations, creating a commercial-steering concern.

Mitigation: Disclose that the contact is informational, compare multiple channels, and require users to verify options with licensed sources before purchase.

Risk: Insurance, health-disclosure, and premium outputs may be incomplete or outdated for an individual user's situation.

Mitigation: Treat outputs as preliminary, confirm current product terms with insurers or licensed professionals, and avoid sharing more personal health or financial detail than needed.

Risk: The local product database contains active and discontinued products, so recommendations may depend on data freshness and filtering behavior.

Mitigation: Use active-product and quality filters, include product-timeliness disclaimers, and verify availability before acting on any recommendation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance Knowledge Base](artifact/references/insurance-knowledge.md)
- [Compliance Reference](artifact/references/compliance.md)
- [Insurance Product Database](artifact/references/products.json)
- [Product Database Analysis 2026-08-21](artifact/references/_repo_analysis_2026-08-21.md)
- [Insurance Database Analysis 2026-08-26](artifact/references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Chinese Markdown prose and tables, with JSON from helper scripts when run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static product, knowledge, and compliance files; insurance, health-disclosure, and premium outputs should be treated as preliminary.]

## Skill Version(s):

2.0.126 (source: server release evidence; artifact frontmatter says 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
