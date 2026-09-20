## Description:

整车厂返利与商务政策核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and dealership operations staff use this skill during monthly close, reconciliation, and rebate settlement review to check OEM rebate policy tables for arithmetic mismatches, total-row inconsistencies, duplicates, blanks, and negative values. It reports findings with source row context and states when required material is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes local rebate or finance table data, which may contain commercially sensitive information.

Mitigation: Use it only in environments approved for that data and review the local command output before sharing results.

Risk: Documentation mentions anonymous statistics while the inspected release did not contain implemented network upload code, creating an expectation mismatch for users.

Mitigation: Tell users to rely on the validated release behavior and review future updates before deployment if network behavior matters.

Risk: The free edition omits some rebate policy checks and does not interpret contract, tax, accounting-period, or OEM system data.

Mitigation: Review the listed withheld and out-of-scope checks before using results for settlement, accounting, or commercial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/oem-rebate-policy-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON results from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include executed checks, withheld checks, row-level messages, summary counts, and insufficient-input guidance.]

## Skill Version(s):

1.0.47 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
