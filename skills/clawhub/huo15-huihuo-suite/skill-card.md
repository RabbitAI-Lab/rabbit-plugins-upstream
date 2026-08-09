## Description: <br>
Enables an agent to manage Huo15/Huihuo Cloud Odoo ERP work such as tasks, projects, timesheets, CRM, calendar, documents, sales, purchasing, inventory, accounting, HR, briefings, reminders, and heartbeat checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaobod1](https://clawhub.ai/user/zhaobod1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operators, and administrators use this skill to operate a live Huo15/Huihuo Odoo ERP system from natural-language requests and script-backed commands. It supports day-to-day business workflows, reporting, reminders, and administrative actions across ERP modules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad authority over a live Odoo company database. <br>
Mitigation: Use a dedicated least-privilege Odoo API key and scope the account to only the modules and records needed for the intended workflow. <br>
Risk: Some commands can post invoices or payments, validate stock movements, cancel orders, approve leave or expenses, delete calendar events, or act on another person's records. <br>
Mitigation: Require explicit manual confirmation before executing high-impact writes, approvals, cancellations, postings, validations, deletions, or actions on other users' records. <br>
Risk: Credential setup stores Odoo connection details in a local tools.md file. <br>
Mitigation: Prefer revocable Odoo API keys, keep the credentials file permission-restricted, avoid committing it, and rotate credentials if exposed. <br>
Risk: Heartbeat and cron-style monitoring can broaden continuous access to business activity data. <br>
Mitigation: Enable heartbeat or scheduled checks only when needed, and limit them to the minimum reminder and briefing scope required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhaobod1/skills/huo15-huihuo-suite) <br>
- [Command reference](references/commands.md) <br>
- [Odoo accounting API reference](references/odoo-accounting-api.md) <br>
- [Odoo CRM API reference](references/odoo-crm-api.md) <br>
- [Odoo HR API reference](references/odoo-hr-api.md) <br>
- [Odoo sales, purchase, and stock API reference](references/odoo-sales-purchase-stock-api.md) <br>
- [Odoo activity and calendar API reference](references/odoo-activity-calendar-api.md) <br>
- [Odoo project API reference](references/odoo-project-api.md) <br>
- [Odoo testing API reference](references/odoo-testing-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands, plus script-generated text tables or JSON when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Script behavior depends on Odoo credentials and the permissions of the configured Odoo account.] <br>

## Skill Version(s): <br>
1.7.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
