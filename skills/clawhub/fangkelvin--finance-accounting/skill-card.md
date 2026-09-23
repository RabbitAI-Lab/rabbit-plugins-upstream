## Description:

Finance Accounting helps agents support bookkeeping, bank-statement import, tax calculations, and financial report generation for finance workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fangkelvin](https://clawhub.ai/user/fangkelvin)

### License/Terms of Use:


## Use Case:

Developers, finance operators, and business users can use this skill to record transactions, import bank statements, calculate VAT and income tax, and generate accounting reports from local CSV and YAML data. Users should review outputs before business, tax, audit, or filing use.

### Deployment Geography for Use:

Global; tax and accounting configuration should be reviewed for the user's jurisdiction.

## Known Risks and Mitigations:

Risk: The skill handles sensitive business, tax, invoice, and bank-statement data.

Mitigation: Use private local storage, restrict access, add encryption and backups appropriate to the deployment, and avoid using real data until controls are reviewed.

Risk: Generated finance reports and exports may be sensitive plaintext.

Mitigation: Treat CSV, JSON, PDF, and XLSX outputs as confidential records and review storage, retention, and sharing paths before use.

Risk: External sharing and automation guidance is under-scoped for finance workflows.

Mitigation: Do not sync financial data to GitHub or connect bank, tax, ERP, payment, or automation systems until data flows and approvals are confirmed.

Risk: Accounting and tax calculations may not match the user's jurisdiction or filing requirements.

Mitigation: Have qualified finance or tax reviewers validate configuration, calculations, and reports before operational, audit, or filing use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fangkelvin/skills/finance-accounting)
- [Publisher profile](https://clawhub.ai/user/fangkelvin)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and generated CSV, JSON, PDF, or XLSX finance artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local finance records, configuration files, reports, and imported bank-statement data depending on the command used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
