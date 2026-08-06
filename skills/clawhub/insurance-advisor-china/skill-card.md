## Description:

中国大陆AI保险顾问。为个人和家庭提供全方位的保险咨询、产品对比、方案设计、投保指导。当用户询问保险配置、保险方案、产品对比、重疾险/医疗险/寿险/意外险/储蓄险推荐、保费计算、保障缺口分析、需求分析、核保合规、理赔等问题时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill to evaluate personal and family insurance needs, compare insurance products, estimate premiums, design coverage plans, and get general underwriting, compliance, and claims guidance.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may ask users for personal, family, financial, and health-related insurance details.

Mitigation: Collect only information needed for the insurance task and avoid retaining or sharing sensitive details outside the active conversation.

Risk: Product recommendations and premium calculations may become inaccurate because insurance products and rates change.

Mitigation: Treat bundled product data and calculator outputs as informational, and verify current terms, eligibility, and premiums with insurers or licensed professionals before purchase.

Risk: Insurance advice, underwriting, compliance, and claims guidance may be mistaken for professional advice.

Mitigation: Present guidance as general information, preserve the skill's disclaimers, and direct users to licensed insurance or legal professionals for binding decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Insurance products data](references/products.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with JSON outputs from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled reference data and local calculators; product details and premium estimates are informational and should be verified against current insurer terms.]

## Skill Version(s):

1.8.433 (source: server release evidence; artifact frontmatter says 1.8.347)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
