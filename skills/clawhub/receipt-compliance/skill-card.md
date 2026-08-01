## Description: <br>
Receipt Compliance helps agents process invoices and receipts with OCR, verification links, reimbursement form generation, approval integration, classification, and accounting voucher generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance and operations teams use this skill to extract invoice data, verify receipts, prepare reimbursement files, submit configured approval requests, classify expenses, and generate accounting voucher outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles invoice, reimbursement, and approval data and may send it to configured verification, approval, or custom services despite local-only claims in the artifact text. <br>
Mitigation: Audit configured endpoints before use and disable external verification or approval integrations unless they are required. <br>
Risk: Configuration files can contain API credentials for tax, approval, or custom enterprise systems. <br>
Mitigation: Protect configuration files, prefer environment variables or managed secrets, rotate credentials, and run the skill in a controlled workspace. <br>
Risk: OCR, classification, voucher generation, and approval submission outputs can affect financial workflows. <br>
Mitigation: Require human review before using generated accounting outputs or submitting any approval request. <br>


## Reference(s): <br>
- [Setup Guide](artifact/references/setup-guide.md) <br>
- [API Endpoints](artifact/references/api-endpoints.md) <br>
- [Risk Declaration](artifact/references/risk-declaration.md) <br>
- [Tax Rules](artifact/references/tax-rules.md) <br>
- [Expense Rules](artifact/references/expense_rules.md) <br>
- [Account Mapping](artifact/references/account_mapping.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated artifacts may include JSON, spreadsheet, voucher, and approval-result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [External verification and approval behavior depends on enterprise configuration and credentials.] <br>

## Skill Version(s): <br>
4.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
