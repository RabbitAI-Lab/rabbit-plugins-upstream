## Description:

Checks sales commission tables for row-level arithmetic, totals, duplicates, and missing values, with each finding tied to the source line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, payroll, cashier, warehouse, and operations staff use this skill during month-end settlement, payroll, reconciliation, and inventory workflows to check commission calculation tables before acting on them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The embedded paid-upgrade workflow asks an assistant to run mutable remote installer code and initiate purchase steps.

Mitigation: Do not run the optional purchase or install prompt unless the payment package, source, and exact version have been independently verified and the user confirms any wallet or payment action.

Risk: The checker can misreport a skipped commission validation as executed for inputs containing a ladder field.

Mitigation: Do not rely on reports for ladder-based inputs until the skipped-check behavior is fixed or independently verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/commission-check-free)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON report with cited source lines and local Node.js command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld checks, findings, summary totals, insufficient-input guidance, and non-network local execution status.]

## Skill Version(s):

1.1.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
