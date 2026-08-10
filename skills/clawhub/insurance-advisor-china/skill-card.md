## Description:

Mainland China insurance advisory skill that helps individuals and families with insurance education, product comparison, plan design, application guidance, premium estimation, coverage-gap analysis, underwriting/compliance prompts, and claims-process questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill for Chinese-language insurance guidance, product comparisons, premium estimates, coverage-gap analysis, family insurance plan options, underwriting/compliance prompts, and general claims-process support.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may ask for sensitive personal, family, income, budget, health-disclosure, and existing-policy information.

Mitigation: Collect only information needed for the requested analysis and handle any captured personal or health-related information according to applicable privacy and data-protection requirements.

Risk: Insurance product availability, pricing, legal requirements, and compliance details may be outdated or unsuitable for a specific buyer.

Mitigation: Verify product availability, prices, terms, and compliance details with licensed professionals or official insurer materials before purchasing or advising a purchase.

Risk: A sales-company contact can be provided when a user asks about purchase channels.

Mitigation: Present the contact only as reference information, avoid endorsement language, and advise users to compare multiple channels and independently verify the provider.

## Reference(s):

- [Insurance Knowledge Reference](references/insurance-knowledge.md)
- [Compliance Reference](references/compliance.md)
- [Product Data](references/products.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with optional JSON outputs from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled product, insurance-knowledge, and compliance reference files; helper scripts read local data and write JSON to stdout.]

## Skill Version(s):

1.8.441 (source: ClawHub release metadata; artifact frontmatter reports 1.8.347)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
