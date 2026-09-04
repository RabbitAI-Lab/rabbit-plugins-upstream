## Description:

A China-focused AI insurance advisor that helps individuals and families analyze coverage needs, compare insurance products, estimate premiums, design coverage plans, and understand underwriting, compliance, and claims topics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill for informational insurance planning, including needs analysis, product comparisons, premium estimates, plan design, insurance knowledge, underwriting guidance, and general claims-process support.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Insurance product availability, premiums, and legal or compliance claims may be stale or inaccurate.

Mitigation: Verify recommendations, product details, premiums, and regulatory claims with licensed insurance professionals, insurers, or authoritative sources before acting.

Risk: The bundled datafix utilities can rewrite local product data or patch skill scripts if run intentionally.

Mitigation: Do not run maintenance utilities during normal advisor use; review changes and keep backups before using them to maintain the product database.

Risk: The skill provides informational guidance in a regulated financial domain and may be mistaken for professional advice.

Mitigation: Present outputs as informational support, preserve disclaimers, and route purchase, underwriting, legal, or claims decisions to licensed or authoritative sources.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance Knowledge Base](references/insurance-knowledge.md)
- [Compliance Reference](references/compliance.md)
- [Product Database](references/products.json)
- [Product Database Analysis Report](references/_repo_analysis_2026-08-21.md)
- [Insurance Database Analysis Report 2026-08-26](references/保险资料库分析报告_2026-08-26.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese-language Markdown responses with optional JSON outputs from bundled Python tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call local Python scripts for needs analysis, premium calculation, and plan design; product and compliance outputs should be treated as informational and verified with licensed sources.]

## Skill Version(s):

2.0.75 (source: server release evidence; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
