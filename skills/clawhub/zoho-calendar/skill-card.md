## Description:

Zoho Calendar API integration with managed OAuth for reading, creating, updating, and deleting calendar events, managing calendars, and scheduling meetings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a Maton-authenticated Zoho Calendar account, inspect calendars and events, and perform approved calendar changes or scheduling workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho Calendar data and Maton credentials can be exposed if API keys, raw responses, or broad OAuth scopes are mishandled.

Mitigation: Prefer Maton OAuth, review OAuth scopes during connection, avoid printing or persisting API keys, and extract only the response fields needed for the task.

Risk: Calendar writes, deletions, connection creation, or connection deletion can alter user data or revoke access.

Mitigation: Default to read and list calls, specify the intended connection when multiple connections exist, and require explicit user confirmation before every write, deletion, or new connection.

Risk: Hosted functions and triggers can create ongoing automation or persistent data forwarding.

Mitigation: Use user-authored or user-reviewed handlers, confirm destinations and forwarded fields, prefer DENY_ALL network policy for functions, and delete automation when it is no longer needed.

## Reference(s):

- [Zoho Calendar API Introduction](https://www.zoho.com/calendar/help/api/introduction.html)
- [Zoho Calendar Events API](https://www.zoho.com/calendar/help/api/events-api.html)
- [Zoho Calendar Calendars API](https://www.zoho.com/calendar/help/api/calendars-api.html)
- [Create Event](https://www.zoho.com/calendar/help/api/post-create-event.html)
- [Get Events List](https://www.zoho.com/calendar/help/api/get-events-list.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Zoho Calendar connection.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
