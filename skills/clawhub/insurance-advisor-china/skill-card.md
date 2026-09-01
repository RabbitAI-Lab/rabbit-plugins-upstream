## Description:

中国大陆 AI 保险顾问，帮助个人和家庭进行保险咨询、产品对比、保费计算、保障缺口分析、方案设计、投保合规和理赔流程问答。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to compare insurance products, estimate premiums, analyze coverage gaps, design personal or family insurance plans, and get general underwriting, compliance, and claims-process guidance.

### Deployment Geography for Use:

China (Mainland)

## Known Risks and Mitigations:

Risk: Insurance product details and premiums may be stale or incomplete because the skill uses a local static product database.

Mitigation: Verify product availability, terms, premiums, and underwriting requirements with official insurer or licensed-channel sources before making decisions.

Risk: Users may mistake generated insurance guidance for advice from a licensed professional.

Mitigation: Treat outputs as general planning assistance and consult qualified insurance or legal professionals for binding recommendations or compliance questions.

Risk: Maintenance scripts under scripts/datafix can modify local skill data or code.

Mitigation: Use the documented advisor scripts for normal operation and run datafix scripts only after review and with intent to update local package data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance product database](references/products.json)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Regulatory compliance notes](references/compliance.md)
- [Product database analysis, 2026-08-21](references/_repo_analysis_2026-08-21.md)
- [Product database analysis, 2026-08-26](references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese markdown responses with optional JSON outputs from local Python helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal advisor scripts read local static reference data and return structured analysis, premium calculations, product comparisons, or plan options.]

## Skill Version(s):

2.0.69 (source: server release evidence; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
