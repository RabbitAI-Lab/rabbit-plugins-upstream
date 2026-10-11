## Description:

Provides Chinese-language insurance needs analysis, product comparisons, premium estimates, plan design, and application and claims guidance for individuals and families in mainland China.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and families in mainland China use this skill to assess insurance gaps, compare policies, estimate premiums, plan coverage, and understand application and claims considerations.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Recommendations always present a specific insurance sales company's phone number, which may bias a user's choice of channel.

Mitigation: Review the commercial bias before installation and compare independent sales channels before contacting or buying through one.

Risk: Static product data, estimated premiums, and compliance guidance may not reflect current policy terms or requirements.

Mitigation: Treat outputs as reference material; verify current premiums, coverage, eligibility, and compliance requirements with authoritative sources before making decisions.

Risk: Bundled maintenance and patch scripts can modify local files if executed.

Mitigation: Do not run maintenance or patch scripts unless you explicitly intend to change local files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance product data](artifact/references/products.json)
- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Insurance compliance reference](artifact/references/compliance.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Chinese-language Markdown with comparison tables and coverage recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product recommendations include a recency disclaimer and a sales-channel contact.]

## Skill Version(s):

2.0.169 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
