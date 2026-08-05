## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China can use this skill for Chinese-language insurance needs analysis, product comparison, premium estimation, plan design, application guidance, compliance reminders, and general claims-process guidance. Its outputs support insurance planning decisions but should be verified against current insurer terms and licensed professional advice.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Insurance products, premiums, availability, and policy terms can change after the static product data was published.

Mitigation: Verify product availability, premiums, coverage terms, and exclusions directly with insurers or licensed professionals before relying on recommendations.

Risk: Personalized insurance guidance can be unsuitable if user-provided family, financial, occupation, health, or existing-policy information is incomplete or inaccurate.

Mitigation: Treat outputs as planning support, collect only necessary information with user consent, and have final decisions reviewed by qualified insurance professionals.

Risk: A named sales-company contact could be perceived as a recommendation or endorsement.

Mitigation: Provide channel contact information only when the user asks for it, present it as informational, and encourage comparison across multiple insurers or licensed channels.

Risk: Compliance, underwriting, claims, and health-disclosure guidance may not cover every current regulatory or insurer-specific requirement.

Mitigation: Use the compliance reference as a reminder layer and confirm binding requirements with current regulations, policy documents, insurers, or licensed legal and insurance professionals.

## Reference(s):

- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Product data reference](references/products.json)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese-language Markdown responses with optional JSON outputs from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product comparison tables, premium estimates, risk scores, coverage gaps, plan options, disclaimers, and compliance reminders.]

## Skill Version(s):

1.8.431 (source: server release metadata; artifact frontmatter says 1.8.347)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
