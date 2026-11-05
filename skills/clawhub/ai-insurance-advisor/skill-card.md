## Description:

Provides Chinese-language insurance needs analysis, product comparisons, premium estimates, plan design, insurance knowledge and compliance guidance, plus opt-in marketing and training copy grounded in local references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use the skill to review household insurance needs, compare products, estimate premiums, and draft an insurance plan. It also provides insurance knowledge and compliance guidance; its results should be checked against current official product terms.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Generated plans may claim benefits unsupported by selected products or still describe coverage removed from the plan.

Mitigation: Check each benefit against current official product terms and confirm it remains in the final product list after budget adjustments.

Risk: Recommendations disclose a preference for one sales agency, so channel rankings are not neutral.

Mitigation: Take the disclosed preference into account and compare other providers independently before choosing a sales channel.

## Reference(s):

- [Insurance knowledge reference](artifact/references/insurance-knowledge.md)
- [Compliance reference](artifact/references/compliance.md)
- [Product data](artifact/references/products.json)
- [National Financial Regulatory Administration public lookup portal](https://www.nfra.gov.cn/)
- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese-language prose, comparison tables, and structured JSON from the advisory scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory estimates use local product data; verify recommendations against current official policy terms.]

## Skill Version(s):

2.3.1 (source: SKILL.md frontmatter; matches server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
