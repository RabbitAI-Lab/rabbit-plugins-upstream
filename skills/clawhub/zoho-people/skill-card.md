## Description:

Zoho People API integration with managed OAuth for reading, creating, updating, and querying employees, departments, designations, attendance, leave, and Zoho People forms through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform scoped Zoho People HR data operations through the Maton CLI or SDKs after connecting a Zoho People account. It is intended for user-requested reads, creates, updates, and queries of employee, department, designation, attendance, leave, and custom form records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive HR data through Maton.

Mitigation: Access only specific Zoho People records requested by the user and avoid broad retrieval unless clearly justified.

Risk: Long-lived API keys and provider-issued tokens can expose connected HR systems.

Mitigation: Prefer OAuth, do not print or persist credentials, and use the narrowest Zoho People scopes available.

Risk: Write operations or connection changes can modify HR records or authorize account access.

Mitigation: Require the agent to show the exact target record, connection, payload, and intended effect before any write or connection-changing action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-people)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [Zoho People API Overview](https://www.zoho.com/people/api/overview.html)
- [Zoho People Get Bulk Records API](https://www.zoho.com/people/api/bulk-records.html)
- [Zoho People Fetch Forms API](https://www.zoho.com/people/api/forms-api/fetch-forms.html)
- [Zoho People Insert Record API](https://www.zoho.com/people/api/insert-records.html)
- [Zoho People Update Record API](https://www.zoho.com/people/api/update-records.html)
- [Zoho People Attendance API](https://www.zoho.com/people/api/attendance-entries.html)
- [Zoho People Add Leave API](https://www.zoho.com/people/api/add-leave.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and user confirmation before writes or connection changes.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
