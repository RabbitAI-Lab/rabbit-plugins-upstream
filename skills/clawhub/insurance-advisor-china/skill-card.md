## Description:

Provides insurance consultation, product comparisons, coverage planning, and purchase guidance for individuals and families in mainland China.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use the skill to review insurance needs, compare products, estimate premiums, and plan coverage. It also provides general guidance about policy terms, underwriting, and claims.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Some plan claims may describe multiple critical-illness payouts or lifetime coverage without verified policy terms; the security scan was partial.

Mitigation: Review the skill before relying on its recommendations, and confirm payout conditions and coverage duration against the insurer's policy wording.

Risk: The skill instructs itself to prioritize one insurance sales channel's contact details, which may influence how users perceive its recommendations.

Mitigation: Compare products and sales channels independently before making a purchase decision.

## Reference(s):

- [Insurance product catalog](references/products.json)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Insurance compliance reference](references/compliance.md)
- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Conversational text, comparison tables, and structured JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized using user-provided insurance and household details and the bundled product and reference files.]

## Skill Version(s):

2.4.2 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
