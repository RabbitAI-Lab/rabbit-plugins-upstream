## Description:

Checks payroll disbursement and bank receipt reconciliation tables locally for row arithmetic, totals, duplicate rows, blank placeholders, and evidence-backed findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and cashiering employees use this skill during monthly payroll reconciliation to check payroll disbursement and bank receipt tables before close or follow-up. It highlights deterministic table issues such as arithmetic mismatches, duplicate rows, blanks, and unsupported free-tier checks without making conclusions when required source material is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payroll reconciliation inputs can contain sensitive payroll and bank-account data.

Mitigation: Run the checker locally on controlled materials, avoid sharing input files externally, and confirm future releases still avoid sending source materials over the network.

Risk: Security evidence notes inconsistent telemetry wording compared with the reviewed implementation.

Mitigation: Review and re-scan future updates before deployment, especially for any new network behavior or telemetry claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-payment-bank-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Analysis]

**Output Format:** [Human-readable text or JSON reconciliation results, with shell commands for local execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing-material guidance instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.48 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
