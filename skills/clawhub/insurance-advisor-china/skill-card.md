## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use this skill for Chinese-language insurance needs analysis, product comparison, premium estimates, coverage planning, compliance guidance, and general claims process guidance. The skill uses bundled product data and reference material to produce advisory outputs that should be verified against insurers or licensed professionals before purchase decisions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The security scan verdict is suspicious because the release includes under-disclosed maintenance scripts that can alter bundled product data and patch recommendation code.

Mitigation: Install only if comfortable with a local insurance-advice skill that runs Python scripts; do not run scripts/datafix utilities unless intentionally maintaining the product database or skill code.

Risk: Insurance recommendations and premium estimates rely on bundled product data that may be stale, incomplete, or different from insurer pricing and underwriting decisions.

Mitigation: Verify recommendations, product availability, premiums, underwriting requirements, and purchase decisions with official insurers or licensed professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Skill definition](artifact/SKILL.md)
- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Compliance reference](artifact/references/compliance.md)
- [Product database](artifact/references/products.json)
- [Product database analysis](artifact/references/_repo_analysis_2026-08-21.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with optional JSON outputs from local Python scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include insurance needs reports, product comparison tables, premium calculations, plan designs, compliance notes, disclaimers, and general claims guidance.]

## Skill Version(s):

2.0.45 (source: server release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
