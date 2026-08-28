## Description:

Chinese-language insurance assistant for mainland China insurance planning, product comparison, premium estimates, coverage-gap analysis, compliance prompts, claims questions, and agent sales-support content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China can use this skill to ask Chinese-language insurance planning questions, compare bundled product data, estimate premiums, analyze protection gaps, and draft insurance-related sales or training content. Agents can use it to produce structured guidance, tables, JSON calculator outputs, and compliance reminders that should be reviewed against current insurer terms.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance recommendations and premium estimates may be stale or incomplete because they rely on bundled static product data.

Mitigation: Verify product availability, premiums, coverage, exclusions, and policy terms with licensed professionals or insurers before making financial decisions.

Risk: The skill may provide financial or compliance guidance that is not a substitute for professional advice.

Mitigation: Treat outputs as decision support and review recommendations with qualified insurance, legal, or compliance professionals.

Risk: The skill includes a disclosed referral path to a specific insurance sales company when users ask for contact information.

Mitigation: Disclose the referral context and compare options from multiple licensed insurance agencies or brokerages before purchasing.

## Reference(s):

- [Insurance Compliance Reference](references/compliance.md)
- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Insurance Product Database](references/products.json)
- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese-language Markdown responses, comparison tables, and JSON calculator outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled static insurance product and compliance references; product availability, premiums, and terms require external verification.]

## Skill Version(s):

2.0.63 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
