## Description:

Provides China-focused insurance needs assessments, product comparisons, premium estimates, coverage plans, and application and claims guidance for individuals and families.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use this skill to assess coverage gaps, compare insurance products, estimate premiums, and plan coverage. Its outputs are general guidance, not a substitute for independent suitability and policy checks.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Product comparisons and coverage plans proactively surface one insurance sales company's phone number, which may steer users toward that provider.

Mitigation: Treat the contact as optional, compare independent sales channels, and do not interpret its inclusion as an endorsement.

Risk: Insurance planning can solicit sensitive health and financial details without strong upfront privacy guardrails.

Mitigation: Share only details needed for the task and avoid disclosing identifying or unnecessary health and financial information.

Risk: Static product data and estimated premiums may be outdated or unsuitable for a particular applicant.

Mitigation: Independently confirm current availability, pricing, licensing, policy terms, and suitability before purchasing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Insurance product data](references/products.json)
- [Compliance guidance](references/compliance.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Chinese-language text and Markdown tables; structured JSON reports from calculation tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes product comparisons, estimated premiums, coverage-gap assessments, plan options, and policy-timing caveats.]

## Skill Version(s):

2.0.151 (source: ClawHub server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
