## Description:

Watch an inbox for vendor invoices, extract the key fields, dedupe against the AP log, log them, forward to the AP system, and file the email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillsandagentsco](https://clawhub.ai/user/skillsandagentsco)

### License/Terms of Use:

MIT-0

## Use Case:

Accounts payable teams use this skill to automate invoice intake from an AP inbox while keeping human review before approval or payment. It extracts invoice fields, deduplicates against the AP log, forwards matching emails to the AP system, files them, and returns a run summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoice attachments and AP logs can contain sensitive vendor, banking, tax, or payment details.

Mitigation: Install the skill only for a dedicated AP inbox or label, restrict access to the AP mailbox and log, and review early run logs.

Risk: Incorrect forwarding could send invoice data to the wrong AP destination.

Mitigation: Confirm the AP system forwarding address or connector before the first run.

Risk: Unreadable scans, conflicting invoice fields, duplicate invoices, or mixed payment patterns could lead to bad AP records if handled silently.

Mitigation: Require cited values, mark unclear fields as uncertain, deduplicate by vendor plus invoice number, and keep every new row in human review before payment.

## Reference(s):

- [AP Invoice Processing on ClawHub](https://clawhub.ai/skillsandagentsco/skills/ap-invoice-processing)
- [AP Invoice Processing publisher reference](https://skillsandagents.co/skills/ap-invoice-processing/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown or text run summary with AP log updates and routing actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces logged, skipped, and uncertain invoice counts; new AP log rows are marked for human review.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
