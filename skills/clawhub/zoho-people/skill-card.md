## Description:

Zoho People API integration with managed OAuth for reading, creating, updating, and querying employees, departments, designations, attendance, leave, and custom HR forms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to help agents work with Zoho People HR records through Maton-managed OAuth. It is suited for targeted HR data retrieval and approved record changes where the user has confirmed the Zoho People account, connection, record, and payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive HR data in Zoho People.

Mitigation: Use it only for specific records the user requests, apply the narrowest Zoho scopes available, and avoid bulk retrieval without a clear need.

Risk: Write operations can change HR records or attendance and leave data.

Mitigation: Require explicit user approval after reviewing the exact target record, payload, connection, and intended effect.

Risk: Multiple Maton or Zoho People connections can route requests to the wrong account.

Mitigation: Confirm the target connection before use and specify the connection when more than one Zoho People connection exists.

Risk: Long-lived Maton API keys can leak through environment variables, logs, command history, or process listings when the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is necessary, feed credentials through stdin, never print or persist them, and send them only to api.maton.ai.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-people)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho People API Overview](https://www.zoho.com/people/api/overview.html)
- [Zoho People Bulk Records API](https://www.zoho.com/people/api/bulk-records.html)
- [Zoho People Fetch Forms API](https://www.zoho.com/people/api/forms-api/fetch-forms.html)
- [Zoho People Insert Records API](https://www.zoho.com/people/api/insert-records.html)
- [Zoho People Update Records API](https://www.zoho.com/people/api/update-records.html)
- [Zoho People Attendance API](https://www.zoho.com/people/api/attendance-entries.html)
- [Zoho People Leave API](https://www.zoho.com/people/api/add-leave.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, JSON examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Zoho People connection]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
