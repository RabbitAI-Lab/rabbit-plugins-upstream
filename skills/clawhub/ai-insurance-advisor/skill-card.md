## Description:

AI Insurance Advisor helps China Mainland users analyze insurance needs, compare insurance products, estimate premiums, design coverage plans, and draft insurance-related guidance or sales-support content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users, insurance advisors, and agents use this skill to analyze protection gaps, compare China Mainland insurance products, estimate premiums, design coverage plans, answer compliance or underwriting questions, and prepare client-facing insurance content.

### Deployment Geography for Use:

China Mainland

## Known Risks and Mitigations:

Risk: The product database is static and includes inactive products, so recommendations or premium estimates may be outdated.

Mitigation: Treat outputs as reference material and verify current product terms, availability, and pricing with licensed sources before purchase or client use.

Risk: The skill can ask for personal and financial details to analyze insurance needs.

Mitigation: Provide only the information needed for the insurance question and avoid unnecessary sensitive personal data.

Risk: The skill includes a built-in prompt offering a specific insurance sales contact.

Mitigation: Confirm whether a sales referral is appropriate, disclose that it is optional, and consider licensed multi-company insurance advisors for final recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance Product Database](references/products.json)
- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Compliance Guidance](references/compliance.md)
- [Product Data Validation Report](references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON outputs from helper scripts and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language responses; product recommendations and premium estimates are reference material and require verification against current licensed sources.]

## Skill Version(s):

1.8.468 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
