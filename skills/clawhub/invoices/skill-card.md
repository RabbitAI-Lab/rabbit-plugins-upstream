## Description: <br>
Files, checks, and audits received invoices by extracting invoice data, checking duplicates and fraud signals, evaluating VAT treatment, and maintaining a searchable local archive. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and finance operators use this skill to capture received invoices, validate supplier and tax details, file the original documents locally, prepare VAT or accountant exports, and answer archive searches about suppliers, periods, payments, disputes, and missing invoices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill maintains local accounting memory and invoice archives that can include supplier tax IDs, invoice history, open items, and last-four bank details. <br>
Mitigation: Review the declared Clawic data folders before installation, keep local backups and device protections appropriate for accounting records, and confirm any export or sharing request before data leaves the machine. <br>
Risk: Incorrect invoice validation, VAT treatment, duplicate handling, or bank-detail checks can affect payments, deductions, and period-close outputs. <br>
Mitigation: Review flagged duplicates, changed bank details, tax math discrepancies, non-deductible items, and filing outputs with the user or an accountant before relying on them for payment, tax filing, deletion, or audit responses. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/invoices) <br>
- [Clawic Invoices Skill](https://clawic.com/skills/invoices) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with local file paths, ledger rows, archive instructions, due tables, and CSV-style export examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintains local invoice records under the declared Clawic data folders when durable work is requested; outputs should state boundaries for totals, exclusions, and any confirmation needed before payment, deletion, sharing, or filing.] <br>

## Skill Version(s): <br>
1.0.3 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
