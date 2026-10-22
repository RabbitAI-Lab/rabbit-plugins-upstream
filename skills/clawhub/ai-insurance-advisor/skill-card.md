## Description:

An insurance-advisory agent for mainland China that analyzes coverage needs, compares products, estimates premiums, designs plans, and answers insurance and compliance questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China can use the skill to assess personal or family coverage needs, compare insurance products, estimate premiums, and review plan options and insurance concepts. It does not perform underwriting pre-assessments or claims handling.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Personalized recommendations may not reflect the user's details or budget.

Mitigation: Provide accurate inputs and check that the analysis and proposed premiums match the user's circumstances and budget before relying on them.

Risk: Bundled product information may describe policies that are no longer available or may be out of date.

Mitigation: Confirm product availability, prices, coverage, and renewal terms directly with insurers before making a decision.

Risk: The skill's checks do not establish coverage or renewal guarantees.

Mitigation: Verify guarantees and policy terms in the insurer's current official documents.

Risk: Company referrals follow a fixed maintainer preference and may not represent a neutral or complete comparison.

Mitigation: Treat referrals as non-exhaustive and compare options across multiple insurers.

## Reference(s):

- [Insurance knowledge guide](references/insurance-knowledge.md)
- [Compliance guidance](references/compliance.md)
- [Bundled product data](references/products.json)
- [ClawHub release page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Structured JSON or human-readable text and comparison tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations and comparisons depend on user-provided details and bundled product data; confirm current policy terms and availability with insurers.]

## Skill Version(s):

2.0.195 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
