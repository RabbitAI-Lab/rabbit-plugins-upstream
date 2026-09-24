## Description:

Google Calendar API integration with managed OAuth for creating events, listing calendars, checking availability, and managing schedules through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents, developers, and operators use this skill to perform approved Google Calendar reads and writes through a managed Maton connection, including event lookup, calendar listing, availability checks, and schedule updates. Hosted functions and triggers are documented for user-approved automations, not as a default workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth connections and calendar writes can grant or change access to user calendar data.

Mitigation: Confirm every new Google Calendar connection and write action with the user, choose the least-privilege OAuth scopes available, and default to read/list operations until a write is explicitly requested.

Risk: Long-lived API keys can expose a broader credential surface than OAuth-backed CLI profiles.

Mitigation: Prefer Maton OAuth login, avoid exporting MATON_API_KEY except where the CLI cannot be installed, and keep credentials in the operating system credential store whenever possible.

Risk: Hosted functions, triggers, destinations, and local execution can create persistent automation and ongoing data flows.

Mitigation: Create automations only after reviewing the exact code, scope, destination, and data flow with the user, and require separate approval for function deployment, trigger creation, and external destinations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-calendar-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Calendar API Overview](https://developers.google.com/calendar/api/v3/reference)
- [Calendar List API](https://developers.google.com/workspace/calendar/api/v3/reference/calendarList/list)
- [Events List API](https://developers.google.com/workspace/calendar/api/v3/reference/events/list)
- [Events Insert API](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert)
- [Freebusy Query API](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are proposals and commands for the agent to present or run only after required user approval for connections, writes, hosted functions, triggers, and local execution.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
