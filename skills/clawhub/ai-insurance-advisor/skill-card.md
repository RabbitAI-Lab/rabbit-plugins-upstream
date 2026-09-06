## Description:

AI Insurance Advisor supports Mainland China insurance needs analysis, product comparison, premium calculation, plan design, insurance knowledge Q&A, and compliance reminders using local reference data and Python tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China use this skill to assess personal or family insurance needs, compare products, estimate premiums, design coverage plans, and receive insurance knowledge or compliance reminders.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance recommendations may be non-neutral because the security evidence flags a hard-coded sales referral.

Mitigation: Remove the referral or clearly disclose it before consumer use, and review recommendation language for neutrality.

Risk: Product recommendations, policy terms, and premiums may be outdated or inaccurate because the skill relies on static local product data and the security evidence notes possible delisted products.

Mitigation: Verify product availability, policy terms, and premiums with insurers or licensed distribution channels before relying on outputs.

Risk: The skill provides financial and insurance guidance that may be mistaken for regulated professional advice.

Mitigation: Use outputs as reference material only and route underwriting, claims, legal, and final purchase decisions to qualified professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Product dataset](references/products.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese prose and Markdown tables, with JSON returned by local calculation scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product recommendations and premiums are based on static local data and require independent verification before use.]

## Skill Version(s):

2.0.80 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
