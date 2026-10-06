## Description:

Provides Chinese-language insurance needs analysis, product comparisons, premium estimates, coverage planning, and claims guidance for individuals and families in mainland China.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use this skill to assess insurance needs, compare local products, estimate premiums, plan coverage, and learn about applications and claims.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Product recommendations proactively surface a named insurance sales contact, which may influence purchasing decisions.

Mitigation: Treat the contact as a lead, not an endorsement; compare independent channels before deciding.

Risk: Static product details and premium estimates may be outdated or inaccurate.

Mitigation: Confirm current product availability, policy terms, eligibility, and quoted premiums with the insurer before purchase.

Risk: Offline maintenance scripts can change local product data or runtime scripts.

Mitigation: Do not run datafix or runtime patch scripts unless you intend and authorize those changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge reference](artifact/references/insurance-knowledge.md)
- [Compliance reference](artifact/references/compliance.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Text]

**Output Format:** [Chinese-language text and Markdown tables; structured JSON from calculation scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local, static product and premium reference data; verify current offerings and prices independently.]

## Skill Version(s):

2.0.155 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
