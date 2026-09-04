## Description:

Zoho People API integration with managed OAuth for managing employees, departments, designations, attendance, leave, and arbitrary Zoho People forms, including custom forms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to read, create, update, or query Zoho People HR records through Maton-managed OAuth. It is intended for targeted HR operations where the user has authorized the connected account and confirmed any write action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Zoho People HR data through Maton.

Mitigation: Use OAuth with the narrowest Zoho scopes available, access only records the user explicitly requests, and avoid bulk retrieval unless clearly justified.

Risk: Write operations can create, update, or delete HR records in the connected Zoho People account.

Mitigation: Default to read and list calls, confirm the target account and resource, and require explicit user approval before any POST, PUT, PATCH, or DELETE request.

Risk: Long-lived API keys can be exposed through environment variables, logs, shell history, or copied output.

Mitigation: Prefer Maton OAuth, never print or persist credentials, and rotate any key that was printed, committed, or pasted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-people)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho People API Overview](https://www.zoho.com/people/api/overview.html)
- [Zoho People Bulk Records API](https://www.zoho.com/people/api/bulk-records.html)
- [Zoho People Fetch Forms API](https://www.zoho.com/people/api/forms-api/fetch-forms.html)
- [Zoho People Insert Record API](https://www.zoho.com/people/api/insert-records.html)
- [Zoho People Update Record API](https://www.zoho.com/people/api/update-records.html)
- [Zoho People Attendance API](https://www.zoho.com/people/api/attendance-entries.html)
- [Zoho People Leave API](https://www.zoho.com/people/api/add-leave.html)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request paths, JSON payload guidance, and confirmation prompts for write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
