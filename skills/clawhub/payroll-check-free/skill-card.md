## Description:

发薪前核对工资表中的逐人实发工资算术、合计行、重复人员、空白金额和占位符，并为每条发现引用源行。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

HR, payroll, finance, and accounting users can run this skill before salary disbursement to check copied payroll-table text for arithmetic errors, total-row mismatches, duplicate names, missing net pay, and template placeholders. It reports findings with line-level evidence and does not decide whether a person's compensation, tax treatment, or social-insurance basis is correct.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled documentation includes a paid-upgrade path that can steer a user or agent toward external package installation and a payment flow.

Mitigation: Use the free local checks without running the upgrade command or starting any purchase flow unless the package, merchant, and payment process have been independently verified.

Risk: The free checker covers only four payroll checks, so a clean result can be mistaken for a complete payroll audit.

Mitigation: Treat results as scoped arithmetic and table-quality checks only; review omitted items such as tax calculation, gross-pay composition, bank-disbursement totals, and policy compliance separately.

Risk: Payroll sheets contain sensitive compensation data.

Mitigation: Run the skill locally on the minimum necessary payroll-table text and avoid sending inputs or outputs to unverified external services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-check-free)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable text or JSON containing payroll-check findings, severity, source lines, advice, executed checks, and omitted checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on supplied payroll-table text; returns insufficient_input instead of conclusions when required table structure is missing.]

## Skill Version(s):

1.0.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
