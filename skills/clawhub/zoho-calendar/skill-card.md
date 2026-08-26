## Description:

Zoho Calendar API integration with managed OAuth for reading, creating, updating, and deleting calendar events, managing calendars, and scheduling meetings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate on a connected Zoho Calendar account through Maton, including calendar discovery, event lookup, and confirmed scheduling changes. It is intended for workflows that need managed OAuth access, read-first behavior, and user approval before writes or new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granting Maton access to Zoho Calendar can expose calendar data or allow changes within the selected account.

Mitigation: Install only if comfortable granting that access, prefer OAuth over API keys, connect only the needed account and scopes, and revoke unused Maton connections when finished.

Risk: Calendar creation, update, deletion, cancellation, or rescheduling can change scheduling data or notify participants.

Mitigation: Default to read and list calls, then confirm every write with the target calendar or event, payload, and intended effect before execution.

Risk: Using the API key fallback introduces long-lived credential handling risk.

Mitigation: Prefer OAuth; when the raw HTTP fallback is unavoidable, avoid printing, logging, or persisting the key and rotate it if it is exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-calendar)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Calendar API Introduction](https://www.zoho.com/calendar/help/api/introduction.html)
- [Zoho Calendar Events API](https://www.zoho.com/calendar/help/api/events-api.html)
- [Zoho Calendar Calendars API](https://www.zoho.com/calendar/help/api/calendars-api.html)
- [Zoho Calendar Create Event](https://www.zoho.com/calendar/help/api/post-create-event.html)
- [Zoho Calendar Get Events List](https://www.zoho.com/calendar/help/api/get-events-list.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API path guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Zoho Calendar connection.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
