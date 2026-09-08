## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill for insurance consultation, needs analysis, product comparison, premium calculation, plan design, underwriting and compliance guidance, and general claims-process guidance. The outputs are informational and should be checked against current product terms and qualified professional advice before purchase decisions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Insurance recommendations and product comparisons may present a named insurance agency phone number prominently.

Mitigation: Treat the contact information as informational only; compare multiple channels and independently verify agency status and suitability before acting.

Risk: Product details, premiums, availability, and regulatory requirements may be stale because the skill uses local static data.

Mitigation: Verify current product terms, premiums, availability, and compliance requirements with the insurer or a qualified professional before purchase or claims decisions.

Risk: Maintenance scripts can modify local product data or runtime scripts when manually run.

Mitigation: Do not run maintenance scripts unless the user explicitly intends to modify local skill data or scripts; review changes and backups before deploying updated data.

## Reference(s):

- [Skill source](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Insurance products data](references/products.json)
- [Repository analysis report](references/_repo_analysis_2026-08-21.md)
- [Insurance data analysis report](references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown responses with optional JSON from local helper scripts and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static insurance product, knowledge, and compliance files; normal runtime has no network access and no file writes.]

## Skill Version(s):

2.0.86 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
