## Description:

A China mainland insurance assistant for insurance planning, product comparison, critical illness, medical, life, accident, and savings-insurance recommendations, premium calculations, coverage gap analysis, underwriting and compliance guidance, claims questions, social copy, training scripts, and agent sales support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to compare insurance products, estimate premiums, analyze coverage gaps, design insurance plans, and prepare insurance sales or training material. The skill is also useful to insurance agents who need structured Chinese-language reports and scripts backed by local reference files and calculators.

### Deployment Geography for Use:

China mainland

## Known Risks and Mitigations:

Risk: The skill may handle sensitive insurance, health, family, and financial details during conversation.

Mitigation: Avoid sharing unnecessary personal documents or identifiers, and review how sensitive details are handled before using the skill in a production workflow.

Risk: The skill may recommend real insurance products and a specific sales contact based on bundled data and local calculations.

Mitigation: Independently verify product availability, premiums, policy terms, legal or compliance points, and sales contact details before buying insurance.

## Reference(s):

- [Insurance Knowledge Reference](references/insurance-knowledge.md)
- [Compliance Reference](references/compliance.md)
- [Insurance Product Data](references/products.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese Markdown reports and JSON from local Python helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include product freshness disclaimers, premium estimates, coverage-gap analysis, plan recommendations, sales contact prompts, and reminders to verify policy details independently.]

## Skill Version(s):

2.0.3 (source: server release metadata; artifact frontmatter states 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
