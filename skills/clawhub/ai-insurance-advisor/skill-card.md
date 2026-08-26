## Description:

A mainland China insurance assistant for needs analysis, insurance plan design, product comparison, premium estimation, compliance prompts, claims guidance, and insurance-agent sales or training support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China can use this skill to analyze insurance needs, compare products, estimate premiums, design coverage plans, and understand compliance or claims considerations. Insurance agents can use it to draft Chinese-language sales copy, training scripts, and customer-facing explanation material.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill asks users for sensitive personal, family, health, and financial details to produce insurance advice.

Mitigation: Collect only the information needed for the immediate task, avoid sharing unnecessary identifying details, and handle any retained outputs as sensitive financial and personal information.

Risk: Insurance product recommendations and premium estimates rely on a bundled static product database and may be stale or incomplete.

Mitigation: Independently verify product availability, premiums, policy terms, and sales-company contact details with insurers or qualified insurance professionals before making decisions.

Risk: The skill can produce financial, compliance, and claims guidance that may be mistaken for final professional advice.

Mitigation: Treat outputs as planning support, keep the skill's product freshness and legal-advice disclaimers visible, and consult licensed insurance or legal professionals for binding decisions.

## Reference(s):

- [Insurance Product Database](references/products.json)
- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Regulatory Compliance Notes](references/compliance.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese-language Markdown and text responses, with JSON output from helper scripts when invoked]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured needs reports, premium comparison tables, plan options, product disclaimers, compliance reminders, and sales or training copy.]

## Skill Version(s):

2.0.52 (source: ClawHub release evidence; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
