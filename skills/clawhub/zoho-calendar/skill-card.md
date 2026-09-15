## Description:

Zoho Calendar API integration with managed OAuth for reading, creating, updating, and deleting calendars and events through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and calendar operators use this skill to manage Zoho Calendar calendars and events through authenticated Maton CLI, SDK, or raw HTTPS calls. It supports read-first calendar workflows, scheduling changes, and user-approved automation around hosted functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar writes or deletions can create, change, cancel, or remove meetings and notify participants.

Mitigation: Default to read and list calls, verify identifiers and current state, and require explicit user approval for each POST, PUT, PATCH, or DELETE operation.

Risk: Calendar event descriptions, attendee lists, and locations can expose sensitive or personal information.

Mitigation: Return only fields needed for the task, avoid dumping full responses, and prefer SDK or raw HTTPS calls over shell commands when local command exposure is a concern.

Risk: API keys and OAuth tokens can leak through environment variables, command lines, logs, or copied output.

Mitigation: Prefer OAuth-backed Maton CLI credentials, never print or persist secrets, and send Maton API keys only to api.maton.ai when raw HTTPS is required.

Risk: Hosted functions, triggers, and destinations can continue running or forwarding matching events until removed.

Mitigation: Review every function, trigger, destination, scope, and network policy with the user before creation or update, and delete automation that is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-calendar)
- [byungkyu publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Calendar API Introduction](https://www.zoho.com/calendar/help/api/introduction.html)
- [Zoho Calendar Events API](https://www.zoho.com/calendar/help/api/events-api.html)
- [Zoho Calendar Calendars API](https://www.zoho.com/calendar/help/api/calendars-api.html)
- [Zoho Calendar Create Event](https://www.zoho.com/calendar/help/api/post-create-event.html)
- [Zoho Calendar Get Events List](https://www.zoho.com/calendar/help/api/get-events-list.html)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-facing Maton CLI, SDK, and HTTPS call guidance; normal write operations require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release evidence; frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
