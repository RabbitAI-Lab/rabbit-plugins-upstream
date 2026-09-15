## Description:

Provides mainland China insurance consultation, product comparison, plan design, premium estimates, coverage gap analysis, underwriting compliance guidance, and claims guidance for individuals and families.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China can use this skill to understand insurance needs, compare local products, estimate premiums, design family protection plans, and receive general compliance or claims guidance. Outputs should be treated as reference material and verified against current official policy documents and licensed professionals.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Insurance advice may be biased because the skill repeatedly surfaces one specific sales company phone number.

Mitigation: Tell users the contact is not an endorsement, encourage comparison across multiple channels, and review responses for undue steering before deployment.

Risk: Product recommendations, renewal guarantees, premium estimates, or coverage claims may be unreliable or out of date.

Mitigation: Require users to verify advice against current official policy documents, insurer calculations, and a licensed insurance professional before purchase or renewal decisions.

## Reference(s):

- [Skill definition](SKILL.md)
- [Insurance product database](references/products.json)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Regulatory compliance notes](references/compliance.md)
- [Product database analysis report](references/_repo_analysis_2026-08-21.md)
- [Insurance database analysis report](references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, JSON]

**Output Format:** [Chinese Markdown responses with structured JSON outputs from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static product, knowledge, and compliance files; runtime helper scripts return JSON for needs analysis, premium calculation, and plan design.]

## Skill Version(s):

2.0.110 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
