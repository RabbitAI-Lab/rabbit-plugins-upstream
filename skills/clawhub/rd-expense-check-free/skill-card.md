## Description:

A local Node.js skill for checking R&D super-deduction collection worksheets, including row recalculation, total cross-checks, duplicate and blank-field detection, with source line citations for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business users, finance teams, and tax-preparation reviewers use this skill to check R&D expense collection tables before quarterly prepayment or annual settlement workflows. It performs deterministic worksheet checks and reports missing materials instead of making unsupported tax conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive R&D expense tables on a local machine.

Mitigation: Run it only in a trusted local Node.js environment and provide the minimum worksheet content needed for the check.

Risk: The inspected help text mentions anonymous usage statistics while the security evidence reports no matching outbound network-call implementation in this version.

Mitigation: Review the installed version before use and rely on the security evidence for this release when assessing network behavior.

Risk: The output is an arithmetic worksheet check, not tax advice or a complete paid-version compliance review.

Mitigation: Use findings as review support and have qualified personnel validate tax treatment, scope exclusions, and final filings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/rd-expense-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Console text or JSON reports with executed checks, withheld checks, findings, missing-input guidance, and source line references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided worksheet text or JSON input; material-insufficient cases return missing fields and do not claim no issues were found.]

## Skill Version(s):

1.0.33 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
