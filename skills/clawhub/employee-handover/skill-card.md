## Description:

Employee Handover helps an agent collect authorized handover inputs, organize task ledgers, chats, contacts, and local file locations, and produce a structured departing-employee handover package.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bz-ai](https://clawhub.ai/user/bz-ai)

### License/Terms of Use:

Proprietary

## Use Case:

Employees, managers, HR teams, and operations staff use this skill to create a signable employee departure handover from authorized task records, chat exports, local folders, and stakeholder information. It is intended to help disclose source coverage gaps and produce a main handover table plus appendices for unfinished tasks, data locations, contacts, and checklist items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive HR, employee, chat, task, contact, and file-location data.

Mitigation: Limit inputs to data the user is authorized to provide, define the time and participant scope before collection, confirm output recipients, and treat generated files and intermediates as sensitive workplace records.

Risk: Automated collection could exceed the intended authorization scope if connectors or exports are used without review.

Mitigation: Confirm data range, platform, participant scope, and recipient scope before using any API, CLI, or MCP connector, and do not bypass platform permissions, audit controls, export limits, or organization policy.

Risk: Manual exports, screenshots, OCR, or pasted chat records can be incomplete or inaccurate.

Mitigation: Record the source and time range for each input, label unverified or OCR-derived data, disclose coverage gaps, and ask the user to review key dates, amounts, identifiers, and commitments.

Risk: Generated handover workbooks can misstate task counts, ownership, or file locations if not checked.

Mitigation: Reopen and validate the workbook, confirm sheet structure and row counts, sample key cells against source data, reconcile completed and unfinished task totals, and include coverage-gap disclosures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bz-ai/skills/employee-handover)
- [Publisher profile](https://clawhub.ai/user/bz-ai)

## Skill Output:

**Output Type(s):** [files, markdown, csv, code, shell commands, guidance]

**Output Format:** [Excel workbook with Markdown and CSV fallback instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated spreadsheet files, source-coverage notes, validation checklists, and environment-specific assembly commands.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
