## Description:

Huo15 Huihuo Suite lets an agent manage a company's Huo15/Huihuo Odoo system for tasks, projects, timesheets, CRM, calendar, knowledge, documents, sales, purchasing, inventory, accounting, HR, reminders, and work briefings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaobod1](https://clawhub.ai/user/zhaobod1)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operations staff use this skill to operate a company Odoo environment through agent-mediated commands for work tracking, sales, purchasing, inventory, accounting, HR, files, and scheduling. It is intended for users who have valid Odoo credentials and authority to perform the requested business actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store Odoo login secrets for a real company account.

Mitigation: Use a revocable API key with the least Odoo permissions needed and protect ~/.huo15/tools.md.

Risk: The skill can perform sensitive business changes, including finance, HR approval, order confirmation, stock validation, RSVP-on-behalf-of-others, and deletion actions.

Mitigation: Require explicit human review before these actions and deploy with narrower triggers, confirmation gates, and record-scope checks.

## Reference(s):

- [Command Reference](references/commands.md)
- [Odoo Todo API](references/odoo-todo-api.md)
- [Odoo Project API](references/odoo-project-api.md)
- [Odoo Timesheet API](references/odoo-timesheet-api.md)
- [Odoo CRM API](references/odoo-crm-api.md)
- [Odoo Activity and Calendar API](references/odoo-activity-calendar-api.md)
- [Odoo Advanced Calendar API](references/odoo-calendar-advanced-api.md)
- [Odoo Knowledge and Documents API](references/odoo-knowledge-documents-api.md)
- [Odoo Sales, Purchase, and Stock API](references/odoo-sales-purchase-stock-api.md)
- [Odoo Accounting API](references/odoo-accounting-api.md)
- [Odoo HR API](references/odoo-hr-api.md)
- [Odoo Testing API](references/odoo-testing-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include operational summaries, command proposals, and script results; sensitive write actions should be reviewed before execution.]

## Skill Version(s):

1.7.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
