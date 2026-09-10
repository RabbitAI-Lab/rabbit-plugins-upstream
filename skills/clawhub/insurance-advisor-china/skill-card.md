## Description:

Provides mainland China insurance consultation for individuals and families, including needs analysis, product comparisons, plan design, premium calculation, underwriting compliance guidance, and claims guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to understand insurance needs, compare local insurance products, estimate premiums, design coverage plans, and receive general compliance or claims guidance. Review is recommended before relying on recommendations because the release evidence reports channel bias toward a named insurance sales company.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Product comparisons and plan-design responses may steer users toward one named insurance sales company instead of remaining neutral.

Mitigation: Require reviewer approval for sales-channel language and instruct operators to present multiple independent channels before deployment.

Risk: Premium calculators may mishandle invalid inputs or produce estimates that differ from insurer quotes.

Mitigation: Validate user inputs before calling helper scripts and label all premium outputs as estimates requiring insurer confirmation.

Risk: Static product data can be stale in a fast-changing insurance market.

Mitigation: Surface product freshness disclaimers and require users to verify current product status, terms, and premiums with insurers or licensed professionals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Publisher Profile](https://clawhub.ai/user/mnetfairy)
- [Insurance Knowledge](artifact/references/insurance-knowledge.md)
- [Compliance Guidance](artifact/references/compliance.md)
- [Product Database](artifact/references/products.json)
- [Insurance Database Analysis Report](artifact/references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese prose, Markdown tables, and JSON from local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal runtime uses local static insurance product, knowledge, and compliance files; evidence reports no network or credential behavior.]

## Skill Version(s):

2.0.90 (source: server release metadata and artifact changelog; artifact frontmatter says 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
