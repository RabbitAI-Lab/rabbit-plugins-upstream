## Description:

A mainland China insurance advisory skill for personal and family coverage consultation, product comparison, plan design, premium estimates, underwriting compliance guidance, and claims support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to analyze insurance needs, compare insurance products, estimate premiums, design protection plans, and understand general underwriting, compliance, and claims considerations.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may ask users for personal insurance-planning details such as age, income, family structure, existing coverage, health disclosure context, and budget.

Mitigation: Collect only the details needed for the requested analysis, avoid unnecessary identifiers, and handle any shared personal information according to applicable privacy and insurance-compliance requirements.

Risk: Insurance product availability, pricing, and compliance details may differ from the bundled static product data.

Mitigation: Verify current product terms, premiums, availability, and regulatory requirements with official insurers, licensed distributors, or qualified professionals before taking action.

Risk: The skill can generate financial or insurance recommendations that may not fit a user's full circumstances.

Mitigation: Treat outputs as informational planning support and have users review final decisions with qualified insurance or financial professionals.

## Reference(s):

- [Compliance Reference](references/compliance.md)
- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Insurance Product Dataset](references/products.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese Markdown guidance with optional JSON outputs from local analysis scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled static insurance product data and local Python scripts for needs analysis, premium estimates, and plan design.]

## Skill Version(s):

1.8.435 (source: server release metadata; artifact frontmatter lists 1.8.347)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
