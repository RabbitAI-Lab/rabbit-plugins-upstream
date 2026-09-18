## Description:

审计调整分录核对（免费版）逐项复算审计调整分录核对表，检查借贷差额、科目净影响、合计勾稽、重复行、空缺与负数，并为结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Auditors, finance teams, and external reviewers use this skill during annual audit close work to check copied audit adjustment tables for internal arithmetic consistency and missing or duplicate entries. It supports review of table structure and calculations, not accounting-policy judgments or audit conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paid-upgrade path asks an agent to install and run mutable external purchase tooling.

Mitigation: Use only the bundled local checker for audit-table validation unless the external package source and version are independently trusted and the install runs in an isolated environment.

Risk: The checker only validates arithmetic, duplicate rows, blanks, placeholders, and negative amounts in the free tier.

Mitigation: Treat results as table-consistency findings and keep accounting treatment, materiality, disclosure, and policy judgments with qualified reviewers and the audit plan.

Risk: Downstream agents may overstate incomplete-input runs or text output as a completed audit conclusion.

Mitigation: Prefer --json for agent consumption and preserve the status, executed checks, checks_not_run, and scope fields when summarizing results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/audit-adjustment-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Full-version purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text with optional JSON checker output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs a local Node.js checker against audit adjustment table text or JSON input and reports executed checks, findings, omitted checks, and scope boundaries.]

## Skill Version(s):

1.0.3 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
