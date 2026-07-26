## Description: <br>
Files, checks, and audits received invoices using OCR and e-invoice XML, duplicate and fraud checks, VAT deduction support, and a searchable local archive. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance operators, and agent-assisted workflows use this skill to capture, validate, file, search, and prepare reports from received invoices, bills, receipts, credit notes, and VAT records. It is intended for maintaining a local invoice archive and related supplier, payment, tax, and accountant handoff records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This skill handles sensitive invoice, supplier, tax, finance, contact, and project records in local Clawic data folders. <br>
Mitigation: Install only when local persistence is acceptable, protect the local data folders, and review important file changes before relying on them. <br>
Risk: Incorrect supplier identities, payment status, tax filings, exports, deletion proposals, or purge proposals could affect financial records. <br>
Mitigation: Review supplier, payment, tax, export, deletion, and purge changes before accepting them, especially when the skill flags anomalies or missing evidence. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/invoices) <br>
- [Clawic Invoices Skill](https://clawic.com/skills/invoices) <br>
- [Clawic](https://clawic.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance and local data-file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local invoice ledgers, supplier records, due-date reminders, finance/contact/project references, and reviewable export or filing notes.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
