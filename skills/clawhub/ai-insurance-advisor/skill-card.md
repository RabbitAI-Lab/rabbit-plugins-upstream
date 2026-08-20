## Description:

AI Insurance Advisor helps users in mainland China with insurance planning, product comparison, premium estimates, coverage gap analysis, underwriting and claims questions, and agent-facing sales or training copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External consumers, families, and insurance agents in mainland China use this skill to analyze coverage needs, compare insurance products, estimate premiums, design plan options, and generate Chinese insurance guidance or sales-support copy.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance recommendations, product availability, or premium estimates may be stale or incomplete because the skill uses static reference data.

Mitigation: Treat outputs as informational guidance and verify current product terms, availability, and premiums with official insurance providers before decisions.

Risk: The skill includes an opt-in prompt that can provide a specific insurance sales-company phone number.

Mitigation: Provide sales contact information only after user confirmation and review whether the contact workflow fits applicable compliance requirements.

Risk: Needs analysis may involve sensitive family, financial, and health-related context.

Mitigation: Collect only information needed for the task, get appropriate user consent, and avoid unnecessary sharing or retention of personal information.

## Reference(s):

- [Insurance compliance reference](artifact/references/compliance.md)
- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Insurance product dataset](artifact/references/products.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with JSON from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static product reference data; product availability and premiums should be verified with official providers.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
