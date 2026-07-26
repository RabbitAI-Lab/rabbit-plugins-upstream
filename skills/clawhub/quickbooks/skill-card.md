## Description: <br>
QuickBooks API integration with managed OAuth for QuickBooks Online accounting administration, including customers, vendors, invoices, payments, and financial reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and authorized accounting administrators use this skill to let an agent access QuickBooks Online through Maton-managed OAuth. It supports querying accounting data and carefully approved changes to customers, invoices, payments, and reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, modify, or delete QuickBooks accounting records. <br>
Mitigation: Default to read-only requests and require explicit user approval after showing the exact endpoint, target record, amount, account context, and consequence for each write or delete action. <br>
Risk: Requests could be sent to the wrong QuickBooks company when multiple Maton connections exist. <br>
Mitigation: Verify the intended connection ID and company before each request and include the Maton-Connection header, especially before write operations. <br>
Risk: The MATON_API_KEY grants access to Maton-managed QuickBooks connections. <br>
Mitigation: Protect the API key as a secret, use a least-privileged QuickBooks account, and revoke unused connections promptly. <br>


## Reference(s): <br>
- [ClawHub QuickBooks Skill](https://clawhub.ai/byungkyu/skills/quickbooks) <br>
- [QuickBooks API Overview](https://developer.intuit.com/app/developer/qbo/docs/get-started) <br>
- [QuickBooks Customer API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/customer) <br>
- [QuickBooks Invoice API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/invoice) <br>
- [QuickBooks Payment API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/payment) <br>
- [QuickBooks Profit and Loss Report API](https://developer.intuit.com/app/developer/qbo/docs/api/accounting/report-entities/profitandloss) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python, JavaScript, shell command, JSON, and SQL-like query examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MATON_API_KEY and an active QuickBooks OAuth connection; write and delete actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
