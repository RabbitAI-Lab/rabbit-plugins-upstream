## Description:

Provides Chinese-language insurance needs analysis, product comparison, premium estimates, plan design, compliance prompts, and claims guidance for individuals and families in mainland China.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to evaluate household insurance needs, compare products, estimate premiums, design coverage plans, understand insurance concepts, and prepare for underwriting, compliance, and claims conversations.

### Deployment Geography for Use:

China (Mainland)

## Known Risks and Mitigations:

Risk: Dormant maintenance scripts can alter the local product database or helper scripts if executed.

Mitigation: Run scripts under scripts/datafix only after review, in a controlled workspace, and only when product database maintenance is intended.

Risk: Static insurance product data can be stale, estimated, or partially unverified.

Mitigation: Confirm current product availability, terms, and premiums with the insurer or authorized channel before relying on recommendations.

Risk: Insurance and compliance guidance may be incomplete for a user's facts or current regulation.

Mitigation: Treat outputs as reference guidance and obtain qualified insurance, legal, or compliance review before purchase or claims decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge base](references/insurance-knowledge.md)
- [Regulatory compliance notes](references/compliance.md)
- [Product database](references/products.json)
- [Product database analysis report, 2026-08-26](references/保险资料库分析报告_2026-08-26.md)
- [Product database analysis report, 2026-08-21](references/_repo_analysis_2026-08-21.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese-language Markdown guidance with optional JSON reports from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call bundled Python scripts for needs analysis, premium calculations, and plan design; helper script outputs are JSON.]

## Skill Version(s):

2.0.65 (source: server release evidence; SKILL.md frontmatter lists 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
