## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to get Chinese-language insurance needs analysis, product comparisons, premium estimates, plan design, underwriting guidance, compliance reminders, and general claims-process guidance. The skill supports personal and family insurance planning using local reference files and helper calculators.

### Deployment Geography for Use:

China (Mainland)

## Known Risks and Mitigations:

Risk: The skill may process personal, family, financial, and health-related details supplied in chat.

Mitigation: Use only the information needed for the insurance task, avoid sharing unnecessary sensitive details, and follow the security guidance from the release evidence.

Risk: Insurance product availability, pricing, and compliance requirements may differ from static reference data or generated calculations.

Mitigation: Verify product availability, pricing, and compliance with licensed professionals before purchasing or relying on a recommendation.

Risk: Sales contact information or channel suggestions may be incomplete or unsuitable for a user's circumstances.

Mitigation: Independently evaluate any sales contact and compare multiple channels before engaging or buying.

## Reference(s):

- [Insurance Knowledge](artifact/references/insurance-knowledge.md)
- [Compliance Reference](artifact/references/compliance.md)
- [Insurance Product Data](artifact/references/products.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese Markdown responses with structured JSON from helper scripts when calculations are used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product comparison tables, risk scores, coverage-gap calculations, premium estimates, plan options, disclaimers, and compliance guidance.]

## Skill Version(s):

1.8.437 (source: server release evidence; artifact frontmatter says 1.8.347)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
