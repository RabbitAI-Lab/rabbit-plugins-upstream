## Description:

AI Insurance Advisor helps mainland China insurance users compare products, estimate premiums, analyze coverage gaps, design plans, answer insurance questions, and generate compliant sales or training guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to receive insurance needs analysis, product comparisons, premium estimates, plan options, compliance reminders, claims guidance, and Chinese-language sales or training copy. Agents using the skill can call local helper scripts that return structured JSON for needs analysis, premium calculation, and plan design.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill can request sensitive family, income, health, and existing-policy details.

Mitigation: Collect only the minimum needed information, get clear user consent, avoid retaining or sharing personal data, and review outputs before use.

Risk: Product and premium recommendations rely on a static local database.

Mitigation: Verify product availability, terms, premiums, and suitability with licensed professionals and current insurer materials before any purchase decision.

Risk: The skill can steer users toward a named sales contact.

Mitigation: Disclose referral context clearly and offer neutral alternatives such as licensed local brokers or direct insurer channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Compliance reference](artifact/references/compliance.md)
- [Product database](artifact/references/products.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown responses and JSON outputs from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a static local product database; final insurance decisions should be verified against current insurer materials.]

## Skill Version(s):

2.0.75 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
