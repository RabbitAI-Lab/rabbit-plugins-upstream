## Description:

Zoho CRM API integration with managed OAuth for reading, creating, updating, deleting, searching, and managing CRM records, organization settings, users, and module metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, sales operations teams, and developers use this skill to work with Zoho CRM records and metadata through Maton-managed OAuth. It supports read-first CRM lookup workflows and user-approved create, update, and delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on mutable third-party Maton CLI and SDK packages and routes Zoho CRM access through Maton.

Mitigation: Install only when Maton is trusted for the connected CRM account, and pin or review Maton CLI and SDK package versions in sensitive environments.

Risk: Zoho CRM write and delete operations can modify or remove business records.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user approval for every POST, PUT, PATCH, or DELETE operation.

Risk: API keys or provider-issued tokens could be exposed if printed, logged, persisted, or passed through shell commands.

Mitigation: Prefer OAuth with operating-system credential storage, avoid printing or persisting credentials, and send Maton API keys only to api.maton.ai when the CLI cannot be used.

## Reference(s):

- [ClawHub Zoho CRM Skill](https://clawhub.ai/byungkyu/skills/zoho-crm)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho CRM API v8 Documentation](https://www.zoho.com/crm/developer/docs/api/v8/)
- [Zoho CRM Get Records API](https://www.zoho.com/crm/developer/docs/api/v8/get-records.html)
- [Zoho CRM Insert Records API](https://www.zoho.com/crm/developer/docs/api/v8/insert-records.html)
- [Zoho CRM Update Records API](https://www.zoho.com/crm/developer/docs/api/v8/update-records.html)
- [Zoho CRM Delete Records API](https://www.zoho.com/crm/developer/docs/api/v8/delete-records.html)
- [Zoho CRM Search Records API](https://www.zoho.com/crm/developer/docs/api/v8/search-records.html)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and user approval for new connections and write operations.]

## Skill Version(s):

1.2.0 (source: server release evidence; artifact frontmatter version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
