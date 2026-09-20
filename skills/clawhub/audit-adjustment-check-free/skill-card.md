## Description:

审计调整分录核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and audit teams use this skill during annual audit adjustment reconciliation to check copied audit adjustment tables for arithmetic consistency, totals, duplicate rows, blanks, placeholders, and negative amounts. It supports internal consistency review only and does not decide accounting treatment, materiality, disclosure, or audit conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outputs may be mistaken for accounting, audit, disclosure, or materiality advice.

Mitigation: Use the results only as arithmetic and internal-consistency assistance, and route accounting judgments through the appropriate audit plan, accounting standards, and reviewer process.

Risk: Audit adjustment tables may contain sensitive financial data.

Mitigation: Run the skill only in an appropriate local workspace and provide only the table intended for checking.

Risk: The free version intentionally omits some checks available in a fuller product tier.

Mitigation: Review the listed executed and withheld checks before relying on the output, and do not treat omitted checks as performed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/audit-adjustment-check-free)
- [Artifact skill instructions](artifact/SKILL.md)
- [Sample audit adjustment table input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON from a local command-line run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing-field guidance instead of a clean-result assertion.]

## Skill Version(s):

1.0.57 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
