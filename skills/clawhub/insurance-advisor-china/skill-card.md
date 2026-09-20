## Description:

Provides Chinese-language insurance needs analysis, product comparison, premium estimation, plan design, compliance guidance, and claims support for mainland China insurance questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China use this skill to explore personal or family insurance needs, compare insurance products, estimate premiums, draft coverage plans, and get general compliance or claims guidance in Chinese.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill may steer insurance recommendation workflows toward a named insurance sales company.

Mitigation: Treat any sales-channel contact as optional reference information, compare multiple insurers and channels independently, and verify all products before making financial decisions.

Risk: Manual maintenance scripts can alter local product or skill files if intentionally run.

Mitigation: Do not run maintenance scripts during normal advisory use; run them only with explicit authorization, review the intended file changes, and keep backups.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/insurance-advisor-china)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Insurance product database analysis](references/保险资料库分析报告_2026-08-26.md)
- [Product database](references/products.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese-language Markdown guidance with JSON tool outputs when local scripts are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static local product, knowledge, and compliance references; users should verify product availability, pricing, and sales channels before purchase.]

## Skill Version(s):

2.0.120 (source: ClawHub release evidence; artifact frontmatter says 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
