## Description:

发薪前核对工资表中的逐人实发工资算术、合计行、重复人员、金额空缺与占位符，并为每条结论提供行号和原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

HR, payroll, accounting, and cash-management users use this skill before payroll release to catch arithmetic errors, incorrect totals, duplicate employee rows, and missing or placeholder net-pay values in pasted salary tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may misunderstand the documentation around anonymous statistics or network behavior.

Mitigation: Review the release documentation before deployment and clarify whether any anonymous statistics are implemented or disabled.

Risk: Users may treat a clean result as full payroll, tax, labor-law, or audit validation.

Mitigation: Use the output only for the documented arithmetic and table-quality checks, and keep human review for payroll policy, tax, and legal determinations.

Risk: The skill cannot read .xlsx files directly and may return insufficient input when pasted tables lack recognizable headers.

Mitigation: Paste payroll data as text with headers, preferably tab-delimited from Excel, and review insufficient-input messages before drawing conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed free-tier checks, withheld checks, insufficient-input status, severity summaries, and source evidence for findings.]

## Skill Version(s):

1.0.48 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
