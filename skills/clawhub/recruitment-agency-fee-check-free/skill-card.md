## Description:

Checks Chinese-language recruitment agency fee bills and guarantee-period refund tables by recomputing fees, refunds, totals, duplicate candidate charges, rate caps, missing fields, and negative values.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

HR and finance teams use this skill before payment approval or month-end reconciliation to validate recruitment agency fee bills and guarantee-period refunds from tabular text copied from spreadsheets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inputs may contain sensitive HR, recruiting, salary, and finance data.

Mitigation: Provide only the billing fields needed for the check and review outputs before sharing them outside the HR or finance workflow.

Risk: The checker validates table arithmetic and guarantee-period refund calculations, but does not verify salary basis, contract legality, employment records, taxes, invoices, PDFs, or external HR systems.

Mitigation: Confirm source data, contract terms, and employment records with the appropriate HR, finance, or legal records before acting on findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/recruitment-agency-fee-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON results with finding line numbers, severity levels, categories, candidate context, scope, and summary verdict.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local tabular text input and reports insufficient input without issuing a positive or negative conclusion.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
