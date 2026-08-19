## Description:

A Chinese mainland insurance assistant that helps with insurance planning, product comparison, premium estimates, coverage-gap analysis, underwriting and compliance prompts, claims questions, social copy, training scripts, and agent sales support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China and insurance sales or support staff use this skill to discuss personal and family insurance needs, compare static product data, estimate premiums, design coverage plans, and generate Chinese-language insurance explanations or sales-support content.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Users may treat insurance planning output as licensed financial advice.

Mitigation: Use the skill as a planning aid only and confirm recommendations with a qualified insurer, broker, or licensed advisor before purchasing or changing coverage.

Risk: Bundled product data and scripted premium estimates may be stale or differ from current insurer terms.

Mitigation: Verify product availability, policy terms, and exact premiums with official insurer or broker sources before acting on any recommendation.

Risk: The workflow may collect sensitive personal, health, family, and financial details in chat.

Mitigation: Collect only information needed for the insurance task, avoid unnecessary identifiers, and handle any retained conversation data according to applicable privacy requirements.

Risk: The artifact includes behavior that may offer a specific insurance-sales contact when users request contact information.

Mitigation: Disclose the sales-channel nature of any referral and allow users to decline or consult independent multi-company brokers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Compliance Reference](references/compliance.md)
- [Insurance Product Database](references/products.json)
- [Product Data Validation Report](references/validation_report_20260524_090219.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Chinese-language text and Markdown, with JSON reports from local helper scripts when invoked]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static bundled insurance product data and local Python scripts for needs analysis, premium estimates, and plan design.]

## Skill Version(s):

1.8.472 (source: server release evidence; artifact frontmatter reports 1.8.351)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
