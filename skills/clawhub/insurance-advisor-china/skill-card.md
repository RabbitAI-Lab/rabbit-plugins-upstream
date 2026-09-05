## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill for Chinese-language insurance education, needs analysis, product comparison, premium estimates, plan design, underwriting and compliance reminders, and general claims guidance. Agents may call bundled local scripts to produce structured JSON analyses and then present concise Chinese guidance or comparison tables.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Product recommendations and premium estimates may be stale or incomplete because they are based on a static product database.

Mitigation: Treat outputs as reference material and verify current terms, pricing, eligibility, and availability with licensed insurance sources before purchase.

Risk: Bundled maintenance scripts under scripts/datafix can rewrite product data or patch skill source files when run.

Mitigation: Do not run datafix scripts during normal advisor use; run them only intentionally, prefer dry-run mode first, and review backups and reports before accepting changes.

Risk: Insurance, underwriting, compliance, and claims guidance may be incomplete for a user's specific circumstances.

Mitigation: Use the skill's compliance and disclaimer guidance, and route final legal, underwriting, claims, or purchase decisions to qualified professionals or official insurer materials.

## Reference(s):

- [Insurance Knowledge Base](artifact/references/insurance-knowledge.md)
- [Regulatory Compliance Notes](artifact/references/compliance.md)
- [Insurance Product Database](artifact/references/products.json)
- [Product Database Analysis 2026-08-26](artifact/references/保险资料库分析报告_2026-08-26.md)
- [Product Database Analysis 2026-08-21](artifact/references/_repo_analysis_2026-08-21.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese Markdown responses and structured JSON from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static product data and includes freshness, multi-provider, and professional verification disclaimers for insurance recommendations.]

## Skill Version(s):

2.0.77 (source: server release evidence; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
