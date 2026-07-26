## Description: <br>
Extracts invoice attachments from email, verifies invoices, categorizes expenses, checks invoice headers, and generates reimbursement spreadsheets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ningmengyun12366](https://clawhub.ai/user/ningmengyun12366) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance teams, employees, and business users can use this skill to collect invoice attachments from supported mailboxes, verify invoice records, classify expenses, and prepare reimbursement spreadsheets. It requires mailbox credentials and an invoice verification API key at runtime. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for mailbox authorization codes and an invoice verification API key. <br>
Mitigation: Treat these as sensitive credentials, prefer a dedicated mailbox or limited app password, avoid storing them in files or logs, and rotate or revoke them after use. <br>
Risk: The skill installs and executes external platform-specific binaries from the publisher's download domain. <br>
Mitigation: Install only if the publisher and download domain are trusted, select only the current platform binary, and verify the downloaded file before running it. <br>
Risk: Invoice attachments, intermediate verification spreadsheets, and reimbursement outputs may contain sensitive financial data and persist on disk. <br>
Mitigation: Use an approved local output directory, restrict access to generated files, and remove retained artifacts when business retention requirements allow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ningmengyun12366/skills/invoice-reimbursement-assistant) <br>
- [Installation and Update Guide](https://download.ningmengyun.com/Skills/invoice-reimbursement-assistant/invoice-reimbursement-assistant-install.md) <br>
- [Invoice Verification API Endpoint](https://openapi.nmy.cn/api/v1/skill/national-invoice-check) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON status summaries; the local executable produces XLSX reimbursement files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Handles sensitive mailbox and API credentials at runtime; generated invoice files and spreadsheets may persist locally.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact frontmatter and install guide state 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
