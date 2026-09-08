## Description:

China-focused insurance advisory skill that helps users analyze coverage needs, compare products, estimate premiums, design insurance plans, answer insurance questions, and surface compliance reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to get preliminary insurance needs analysis, product comparisons, premium estimates, plan options, insurance knowledge answers, and compliance reminders. Outputs should be treated as advisory drafts that require independent verification before purchase or sales use.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill can steer users toward specific insurance intermediaries.

Mitigation: Disclose the channel recommendation, compare alternatives, and independently verify any intermediary before sharing contact details or taking action.

Risk: Recommendations may rely on stale, inactive, or unreliable product records.

Mitigation: Verify product availability, premiums, coverage terms, benefits, and sales eligibility with official insurer or regulator sources before purchase or sales use.

Risk: Insurance advice may be mistaken for professional financial, legal, underwriting, or claims guidance.

Mitigation: Treat outputs as preliminary advisory drafts and escalate underwriting, claims, legal, or final purchase decisions to qualified professionals.

## Reference(s):

- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Insurance product data](references/products.json)
- [National Financial Regulatory Administration intermediary information disclosure platform](https://www.nfra.gov.cn/)
- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese Markdown responses with optional JSON results from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes preliminary recommendations, comparison tables, disclaimers, and compliance reminders; product and premium details require independent verification.]

## Skill Version(s):

2.0.86 (source: server release evidence and target metadata; artifact frontmatter reports 2.0.90)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
