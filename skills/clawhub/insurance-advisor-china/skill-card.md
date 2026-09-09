## Description:

Provides Mainland China insurance guidance for individuals and families, including needs analysis, product comparison, plan design, premium calculation, underwriting compliance prompts, and claims guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in Mainland China can use this skill to compare insurance products, estimate premiums, identify protection gaps, and generate family insurance plan options. It also supports insurance knowledge questions, underwriting and compliance reminders, and general claims process guidance.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Financial-product guidance may steer users toward a specific insurance sales channel.

Mitigation: Review outputs for neutrality before use and require clear disclosure that sales-channel contact information is informational, not an endorsement or purchase recommendation.

Risk: Insurance product data is static and may be stale or incomplete.

Mitigation: Require users or reviewers to verify product availability, pricing, terms, and underwriting requirements with official insurer or licensed-channel sources before decisions.

Risk: The skill gives insurance and compliance guidance that may not fit an individual user's circumstances.

Mitigation: Use responses as general guidance and route binding recommendations, legal questions, and purchase decisions to qualified insurance or legal professionals.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [Insurance product database](artifact/references/products.json)
- [Insurance knowledge base](artifact/references/insurance-knowledge.md)
- [Regulatory compliance notes](artifact/references/compliance.md)
- [Product database analysis report](artifact/references/保险资料库分析报告_2026-08-26.md)
- [Repository analysis report](artifact/references/_repo_analysis_2026-08-21.md)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [ClawHub publisher profile](https://clawhub.ai/user/mnetfairy)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese-language Markdown responses with tables and JSON outputs from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static reference files and whitelisted Python helpers; normal runtime has no network access or file writes.]

## Skill Version(s):

2.0.88 (source: server release evidence; SKILL.md frontmatter says 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
