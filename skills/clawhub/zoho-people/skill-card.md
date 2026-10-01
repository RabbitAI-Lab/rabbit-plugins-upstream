## Description:

Helps agents read and manage Zoho People HR records, including employees, leave, attendance, and custom forms, through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to retrieve or update authorized Zoho People HR records, including employees, departments, leave, attendance, and custom forms. Optional user-approved automations can run scheduled or event-triggered actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho People records may contain sensitive employee and HR information.

Mitigation: Access only records the user requests and use the narrowest available OAuth scopes.

Risk: Writes or new connections can modify HR data or broaden access.

Mitigation: Default to reading records; obtain separate explicit approval for each write and new connection.

Risk: Automation or third-party trigger destinations can continually forward data.

Mitigation: Confirm automations separately and avoid third-party destinations unless the user understands what will be forwarded.

## Reference(s):

- [Zoho People skill release](https://clawhub.ai/byungkyu/skills/zoho-people)
- [Maton](https://maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Zoho People API overview](https://www.zoho.com/people/api/overview.html)
- [Zoho People forms API](https://www.zoho.com/people/api/forms-api/fetch-forms.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code]

**Output Format:** [Markdown with commands, API results, and optional function examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Access and results depend on the user's authorized connection and Zoho People scopes.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
