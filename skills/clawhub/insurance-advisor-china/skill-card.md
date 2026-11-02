## Description:

为中国大陆个人和家庭提供保险需求分析、产品对比、方案设计、保费估算及投保与理赔指导。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆有保险需求的个人与家庭，帮助整理保障需求、比较保险产品、估算保费并了解投保、核保及理赔流程。建议仅作参考，具体条款与报价应向保险公司核实。

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill mandates prioritizing a named insurance seller's referral alongside product recommendations, which may make advice commercially steered despite neutrality claims.

Mitigation: Disclose the referral's commercial context, offer optional referrals using clear selection criteria, and let users compare providers without pressure.

Risk: Coverage and premium calculations may be misleading or inaccurate.

Mitigation: Check inputs and calculations independently, and confirm current premiums, eligibility, exclusions, and policy terms with insurers before making decisions.

Risk: Needs analysis may request sensitive personal, family, health, and financial details.

Mitigation: Share only the details needed for the question and avoid providing unnecessary identifying or sensitive information.

## Reference(s):

- [Insurance product data](artifact/references/products.json)
- [Insurance knowledge guide](artifact/references/insurance-knowledge.md)
- [Insurance compliance guide](artifact/references/compliance.md)
- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Chinese-language Markdown with comparison tables and concise recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include needs-analysis summaries, coverage comparisons, premium estimates, and plan options; verify estimates and policy details independently.]

## Skill Version(s):

2.0.194 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
