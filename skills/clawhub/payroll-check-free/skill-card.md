## Description:

A free local payroll-sheet checker that verifies net-pay arithmetic, control totals, duplicate people, and blank or placeholder amounts, with line-cited findings and no network use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

HR, payroll, finance, or accounting staff use this skill before payroll release to check pasted salary-table text for net-pay arithmetic errors, control-total mismatches, duplicate names, and blank or placeholder values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payroll tables can contain sensitive employee compensation data.

Mitigation: Use the skill only in an environment where local access to pasted payroll-sheet text is acceptable, and avoid sharing inputs outside approved payroll workflows.

Risk: The free version performs only four listed checks and does not provide full payroll, tax, or legal validation.

Mitigation: Treat findings as pre-release arithmetic and table-quality checks, then complete normal payroll, tax, policy, and legal review before disbursement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-check-free)
- [Free web checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable findings text by default, or structured JSON when invoked with --json.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers and include severity, message, advice, and evidence; the local script uses exit codes for completed checks, insufficient input, and errors.]

## Skill Version(s):

1.0.0 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
