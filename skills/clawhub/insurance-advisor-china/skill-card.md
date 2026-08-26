## Description:

中国大陆AI保险顾问，为个人和家庭提供保险咨询、产品对比、方案设计、投保指导、保费计算、保障缺口分析、核保合规和理赔支持。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill to analyze personal or family insurance needs, compare products, estimate premiums, design coverage plans, and receive Chinese-language insurance knowledge, compliance, and claims guidance.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The workflow can collect sensitive financial, family, and health context for insurance needs analysis.

Mitigation: Share only the minimum information needed, avoid unnecessary identifiers or detailed health records, and keep any collected user context under appropriate privacy controls.

Risk: The bundled product and compliance data may be stale, polluted, or inconsistent.

Mitigation: Verify product availability, premiums, policy status, and compliance claims with insurers or licensed professionals before making insurance decisions.

Risk: The skill provides non-authoritative insurance guidance that may be mistaken for licensed professional advice.

Mitigation: Present outputs as reference material only and preserve the skill's stated disclaimers when recommending or comparing products.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance product database](references/products.json)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Compliance guidance](references/compliance.md)
- [Product database analysis](references/_repo_analysis_2026-08-21.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese-language Markdown or JSON reports, depending on the workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Script-backed workflows can return structured JSON for needs analysis, premium calculation, and plan design; user-facing answers should include the skill's stated disclaimers when giving product recommendations.]

## Skill Version(s):

2.0.53 (source: server release evidence; artifact frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
