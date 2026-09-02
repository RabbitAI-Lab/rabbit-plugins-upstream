## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill for Chinese-language insurance needs analysis, product comparison, premium estimation, plan design, underwriting/compliance guidance, and general claims process support. Outputs are advisory and should be checked against current product terms and licensed-provider guidance before insurance decisions.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The package includes maintenance scripts that can rewrite product data and source files.

Mitigation: Do not allow agents to run scripts under scripts/datafix unless the deployment intentionally includes product-database maintenance.

Risk: Insurance product availability, premiums, and sales-channel information may become stale or conflict with current provider terms.

Mitigation: Verify product availability, premiums, and sales-channel details with licensed providers before using outputs for insurance decisions.

Risk: Customer-facing insurance guidance can be misleading if treated as a final professional recommendation.

Mitigation: Keep outputs advisory, preserve product-timeliness and compliance disclaimers, and route final purchasing or legal decisions to qualified professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance product database](references/products.json)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Regulatory compliance notes](references/compliance.md)
- [Product database analysis report](references/_repo_analysis_2026-08-21.md)
- [Insurance database analysis report 2026-08-26](references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese-language Markdown responses with optional JSON outputs from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose script calls for needs analysis, premium calculation, and plan design; product data is static reference data and requires current verification.]

## Skill Version(s):

2.0.71 (source: server release metadata; skill frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
