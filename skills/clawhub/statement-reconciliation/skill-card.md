## Description:

Check a vendor statement against the AP log to confirm every invoice is recorded, and draft a request for any that are missing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillsandagentsco](https://clawhub.ai/user/skillsandagentsco)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounts-payable operators use this skill when a vendor statement arrives to compare statement invoice lines against an AP log before payment or period close. It reports reconciled statements, missing invoices, and ambiguous lines that need human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial reconciliation can be wrong if statement identification or match tolerance rules are unclear.

Mitigation: Confirm matching rules in plan mode before the first run and stop rather than defaulting to loose matches.

Risk: Vendor communication could contain incorrect missing-invoice requests.

Mitigation: Keep vendor requests draft-only and require human review before any message is sent.

Risk: Unreadable statement lines or near matches can create false matches.

Mitigation: Flag unreadable or ambiguous lines for confirmation and require matched lines to cite both the statement source and the AP-log row.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillsandagentsco/skills/statement-reconciliation)
- [Statement Reconciliation reference](https://skillsandagents.co/skills/statement-reconciliation/)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text reconciliation report with cited matches, missing-invoice details, confirm lines, and draft vendor reply text when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft-only vendor communication; matched lines should cite both statement source and AP-log row.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
