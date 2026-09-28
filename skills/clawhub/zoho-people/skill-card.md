## Description:

Zoho People API integration with managed OAuth for reading, creating, updating, and querying employees, departments, designations, attendance, leave, and custom HR forms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to connect an agent to Zoho People through Maton, inspect HR data, and perform approved HR record changes. It also documents how to turn approved Zoho People actions into narrowly scoped hosted functions or trigger-driven automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change sensitive HR records through a user's Zoho People connection.

Mitigation: Use OAuth where possible, default to read and list calls, access only records the user explicitly requests, and require explicit approval for every write.

Risk: Hosted functions and triggers can turn an approved one-time action into continuing automation over sensitive HR data.

Mitigation: Create functions or triggers only after user approval, keep scopes and destinations narrow, prefer no outbound network for hosted functions, and delete automation that is no longer needed.

Risk: API keys and raw response bodies can expose long-lived credentials or personal HR data if copied into the environment, logs, files, or third-party destinations.

Mitigation: Prefer managed OAuth credentials, avoid exporting long-lived keys, forward only required fields, and avoid logging or relaying raw HR responses unless the user explicitly asks.

## Reference(s):

- [ClawHub Zoho People Skill](https://clawhub.ai/byungkyu/skills/zoho-people)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho People API Overview](https://www.zoho.com/people/api/overview.html)
- [Zoho People Fetch Forms API](https://www.zoho.com/people/api/forms-api/fetch-forms.html)
- [Zoho People Insert Record API](https://www.zoho.com/people/api/insert-records.html)
- [Zoho People Update Record API](https://www.zoho.com/people/api/update-records.html)
- [Zoho People Attendance API](https://www.zoho.com/people/api/attendance-entries.html)
- [Zoho People Leave API](https://www.zoho.com/people/api/add-leave.html)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Code, Configuration, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit approval for writes, connection changes, hosted functions, and triggers.]

## Skill Version(s):

1.2.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
