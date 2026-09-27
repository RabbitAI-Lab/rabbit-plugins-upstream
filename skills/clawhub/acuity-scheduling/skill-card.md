## Description:

Acuity Scheduling API integration with managed OAuth for managing appointments, calendars, clients, and availability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Acuity Scheduling through Maton-managed authentication, including checking availability, scheduling or rescheduling appointments, cancelling appointments, and managing clients or calendars. It is intended for user-approved Acuity account operations and related hosted automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on Acuity Scheduling account data through a Maton connection.

Mitigation: Grant access only to the intended account, prefer OAuth, and scope the connection to the current task where scope selection is available.

Risk: Create, update, delete, reschedule, cancel, function, trigger, or forwarding actions can make persistent changes or automation.

Mitigation: Require explicit user confirmation before each write or automation action, review the target connection and action details, and remove unused automation when the task is complete.

Risk: API keys and raw HTTP fallback can expose long-lived credentials if handled broadly.

Mitigation: Use OAuth when possible, avoid exporting long-lived keys to child processes, and use the raw HTTP form only when the CLI cannot be installed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/acuity-scheduling)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Acuity Scheduling API Quick Start](https://developers.acuityscheduling.com/reference/quick-start)
- [Appointments API](https://developers.acuityscheduling.com/reference/get-appointments)
- [Availability API](https://developers.acuityscheduling.com/reference/get-availability-dates)
- [Calendars API](https://developers.acuityscheduling.com/reference/get-calendars)
- [Clients API](https://developers.acuityscheduling.com/reference/clients)
- [OAuth2 Documentation](https://developers.acuityscheduling.com/docs/oauth2)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly trigger catalog](references/calendly/triggers.md)
- [GitHub trigger catalog](references/github/triggers.md)
- [Google Mail trigger catalog](references/google-mail/triggers.md)
- [HubSpot trigger catalog](references/hubspot/triggers.md)
- [Linear trigger catalog](references/linear/triggers.md)
- [Notion trigger catalog](references/notion/triggers.md)
- [Slack trigger catalog](references/slack/triggers.md)
- [Stripe trigger catalog](references/stripe/triggers.md)
- [Time trigger catalog](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on Maton CLI or raw HTTP usage, Acuity Scheduling API operations, and user-approved automation setup.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
