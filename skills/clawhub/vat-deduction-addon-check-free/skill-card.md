## Description:

Checks Chinese VAT add-on deduction ledgers by recalculating supported totals and balance relationships, detecting duplicates and blanks, and citing source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Accounting and tax operations users use this skill before VAT filing to check whether supported Chinese VAT add-on deduction ledger totals, balances, actual credits, duplicates, and required fields are internally consistent. It does not determine tax-policy eligibility, replace filing, or provide legal or tax advice.

### Deployment Geography for Use:

Global, for workflows involving Chinese VAT add-on deduction ledger materials.

## Known Risks and Mitigations:

Risk: The skill processes tax and accounting ledger material that may contain sensitive business information.

Mitigation: Provide only the specific ledger text or file needed for the check and run it locally as described by the artifact and security guidance.

Risk: Users may treat arithmetic consistency findings as legal, tax, or filing advice.

Mitigation: Review results with the applicable tax authority guidance or a qualified tax professional; the skill only checks supported table relationships and explicitly does not determine policy eligibility or replace VAT filing.

Risk: Incomplete or unrecognized inputs can prevent meaningful checks.

Mitigation: Include ledger headers and required rows; when material is insufficient, the skill reports missing inputs instead of producing an all-clear conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/vat-deduction-addon-check-free)
- [Artifact skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; results include executed checks, withheld checks, findings, missing-input messages, and cited evidence.]

## Skill Version(s):

1.0.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
