## Description:

Payroll Disbursement Bank Check (Free) performs a local deterministic review of payroll disbursement and bank receipt tables, citing source lines for arithmetic, totals, duplicate, blank-field, and negative-amount findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and cashiering employees use this skill after monthly payroll disbursement and before payroll close to reconcile payroll payment tables with bank receipt records. It helps identify table-level inconsistencies while clearly listing checks that the free version does not perform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes an embedded upgrade prompt that asks an AI agent to run an unpinned remote installer and begin a paid SkillPay purchase workflow.

Mitigation: Use the local free checker only unless the remote package, version, publisher, and payment flow have been independently verified; keep wallet or payment confirmation under direct user control.

Risk: The free version intentionally omits several payroll and bank receipt checks.

Mitigation: Treat results as limited to the listed free checks and separately review omitted areas such as bank receipt amount mismatches, success-count reconciliation, reissue after failed returns, duplicate bank-account payments, and negative net pay.

Risk: Payroll tables may contain sensitive employee and bank-account information.

Mitigation: Run the checker locally and provide only the table rows needed for reconciliation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-payment-bank-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs cite source lines, report executed and omitted checks, and return an insufficient-input status instead of a conclusion when required table evidence is missing.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
