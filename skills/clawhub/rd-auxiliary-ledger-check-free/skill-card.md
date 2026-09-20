## Description:

研发费用辅助账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 研发费用辅助账与高新指标核对、研发费用辅助账对不上。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

External finance and R&D management teams at high-tech enterprises use this skill to check Chinese R&D auxiliary ledger tables before monthly cost aggregation, annual high-tech reporting, or certification review. It performs deterministic row, total, duplicate, blank, negative-value, and other-expense-ratio checks and returns source-backed findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The help text includes stale wording about anonymous usage statistics and a --no-stats option, which may confuse users about runtime behavior.

Mitigation: Rely on the server security evidence and inspected artifact behavior before installation; the publisher should update the help text so it matches the shipped code.

Risk: The skill checks table arithmetic and stated high-tech ledger indicators, but it does not decide whether an expense qualifies as R&D cost or replace audit, tax, or certification review.

Mitigation: Use findings as screening guidance and confirm accounting, tax, and high-tech eligibility decisions against official rules, company policy, and supporting source documents.

Risk: Input may contain sensitive financial ledger data.

Mitigation: Run the local Node script only in a trusted environment and review the artifact and scan verdict before using it on confidential materials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/rd-auxiliary-ledger-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON containing findings, severity counts, executed checks, omitted checks, and scope metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on Node.js standard library; sample and input-file modes are supported; material-insufficient cases return explicit missing-input guidance instead of a ledger conclusion.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
