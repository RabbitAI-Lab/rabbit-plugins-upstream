## Description:

Checks accounts-receivable reconciliation tables for row-level arithmetic, aging-bucket totals, total-row mismatches, duplicate customers, and blank or placeholder fields, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations users can run this skill during monthly close, collections review, or receivables forecasting to check whether an accounts-receivable aging table is internally consistent. It reports arithmetic mismatches and data-quality issues without providing audit, tax, legal, credit, or bad-debt allowance advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free-versus-withheld check boundary is inconsistent enough to require review before installation.

Mitigation: Review the executed and withheld check lists before use, and confirm that only intended checks are enabled for the deployment.

Risk: The skill analyzes financial-reporting inputs and may be misread as audit, tax, legal, credit, or bad-debt allowance advice.

Mitigation: Use the output as a reconciliation aid only, and require qualified human review before financial reporting, collections, or accounting-policy decisions.

Risk: Documentation is unfinished and may not fully explain the required input format or limitations.

Mitigation: Validate with representative sample tables and confirm insufficient-input behavior before using the skill in a controlled workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ar-aging-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Analysis, Guidance]

**Output Format:** [Human-readable text or structured JSON containing findings, summary totals, executed checks, and checks not run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields and advice rather than a pass/fail conclusion.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
