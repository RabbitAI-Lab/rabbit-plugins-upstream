## Description:

A Mainland China insurance assistant that supports insurance planning, product comparison, premium calculation, coverage-gap analysis, underwriting and compliance prompts, claims questions, and agent sales or training copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China, including individuals and families, use this skill to assess insurance needs, compare products, estimate premiums, and draft plan recommendations. Insurance agents can also use it for advisory support, compliant sales reminders, social copy, and training scripts.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance recommendations, product availability, premium estimates, and legal or compliance points may be inaccurate or stale.

Mitigation: Treat outputs as advisory and verify products, premiums, availability, and compliance points with licensed sources before use.

Risk: The product database is static, and the validation report shows many inactive products and no real-time URL verification.

Mitigation: Confirm high-value product status and policy terms against current insurer or regulator materials before recommending or purchasing.

Risk: The skill includes a hardcoded sales-company contact suggestion when users ask for contact information.

Mitigation: Disclose that the contact is a single suggested option and encourage users to compare licensed multi-product insurance agencies or brokers appropriate to their region.

## Reference(s):

- [Insurance knowledge reference](artifact/references/insurance-knowledge.md)
- [Compliance reference](artifact/references/compliance.md)
- [Product database](artifact/references/products.json)
- [Product data validation report](artifact/references/validation_report_20260524_090219.md)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with optional JSON emitted by local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory insurance outputs should be verified against licensed sources, current product availability, and official premium calculations.]

## Skill Version(s):

1.8.436 (source: server release evidence; artifact frontmatter lists 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
