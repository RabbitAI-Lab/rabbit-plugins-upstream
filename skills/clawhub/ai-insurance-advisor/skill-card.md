## Description:

Helps Chinese mainland consumers and families analyze insurance needs, compare local insurance product data, estimate premiums, design coverage plans, answer insurance questions, and surface compliance reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill for insurance education, needs analysis, product comparison, premium estimation, and plan drafting. It is also useful to agents who need structured guidance, but it does not replace licensed underwriting, claims, legal, or compliance review.

### Deployment Geography for Use:

China mainland

## Known Risks and Mitigations:

Risk: The skill may steer insurance recommendations toward specific sales contacts.

Mitigation: Review recommendations for neutrality, disclose the contact-routing basis, and require explicit user intent before showing sales contact details.

Risk: Advertised transparency checks may not be fully supported because referenced product metadata is missing.

Mitigation: Validate product metadata, product availability, and sales-contact claims before deployment or user-facing use.

Risk: Insurance guidance may be mistaken for underwriting, legal, claims, or regulated financial advice.

Mitigation: Keep outputs educational and planning-oriented, and direct users to licensed professionals or insurers for binding decisions.

## Reference(s):

- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Product database](references/products.json)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown responses with optional JSON outputs from local Python tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include needs-analysis summaries, product comparison tables, premium estimates, coverage-plan options, compliance reminders, and product-data disclaimers.]

## Skill Version(s):

2.0.117 (source: server release metadata; artifact frontmatter says 2.0.90)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
