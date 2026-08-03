## Description: <br>
Accountant helps agents keep local accounting notes for double-entry bookkeeping, reconciliation, period close, financial statements, payroll, sales tax, income tax, audit preparation, and related accounting workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when an agent needs accounting guidance, journal entries, reconciliations, close checklists, filing figures, or durable local bookkeeping notes. It is intended for maintaining defensible books, not for forecasting, fundraising, invoice issuance, document archiving, or bank payment operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill maintains local accounting notes that may include sensitive financial context, account nicknames, last four digits, tax registration numbers, ledger codes, amounts, and filing references. <br>
Mitigation: Keep the configured Clawic data folders access-controlled and backed up appropriately, and store only credential pointers rather than secret values. <br>
Risk: Bookkeeping, payroll, sales tax, and income tax guidance can be jurisdiction-specific, year-specific, and high impact if used for filings or locked periods. <br>
Mitigation: Verify current rules for the relevant filing year and escalate filed-return changes, unpaid withheld payroll taxes, insolvency, ownership changes, and examination issues to a licensed professional. <br>
Risk: Agent-generated postings, write-offs, period changes, or deletions could alter accounting records or local shared boxes in ways the user did not intend. <br>
Mitigation: Require user confirmation for high-impact updates, review named file writes, and use the skill's reconciliation, close, and output gates before relying on results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/accountant) <br>
- [Clawic Accountant skill page](https://clawic.com/skills/accountant) <br>
- [Skill overview and security notes](artifact/SKILL.md) <br>
- [Local memory and file templates](artifact/memory-template.md) <br>
- [Reconciliation workflow](artifact/reconciliation.md) <br>
- [Income tax workflow](artifact/tax.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with accounting entries, checklists, local note updates, and configuration references.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write local Clawic notes under configured paths; evidence reports no hidden code, network transfer, or credential capture.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
