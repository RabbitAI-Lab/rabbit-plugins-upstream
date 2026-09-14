## Description:

Acuity Scheduling API integration with managed OAuth for managing appointments, calendars, clients, and availability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to help users schedule, reschedule, cancel, and inspect Acuity Scheduling appointments and availability through a Maton-managed Acuity connection. It is also useful when a user explicitly asks to create approved hosted automations around Acuity Scheduling actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and change scheduling data through the user's Acuity Scheduling connection.

Mitigation: Prefer read-only calls first and require explicit user approval before creating connections, writes, deletions, hosted functions, or automations.

Risk: Long-lived API keys and destination headers can expose credentials or sensitive scheduling data.

Mitigation: Prefer OAuth, store credentials only through the Maton credential flow, avoid embedding credentials in trigger destinations, and rotate any key that was printed, pasted, or committed.

Risk: Triggers or hosted destinations can continue forwarding event or scheduling data until removed.

Mitigation: Use trigger destinations only after explicit approval, keep destinations inside the Maton platform when possible, and delete automations when the task is complete.

Risk: Installing the Maton CLI or SDK introduces a residual package supply-chain dependency.

Mitigation: Use pinned reviewed versions and upgrade deliberately after checking release notes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/acuity-scheduling)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Acuity Scheduling API Quick Start](https://developers.acuityscheduling.com/reference/quick-start)
- [Appointments API](https://developers.acuityscheduling.com/reference/get-appointments)
- [Availability API](https://developers.acuityscheduling.com/reference/get-availability-dates)
- [Calendars API](https://developers.acuityscheduling.com/reference/get-calendars)
- [Clients API](https://developers.acuityscheduling.com/reference/clients)
- [Acuity OAuth2 Documentation](https://developers.acuityscheduling.com/docs/oauth2)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON, Python, JavaScript, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Acuity API paths, Maton CLI commands, connection IDs, hosted function examples, trigger configuration, and approval guidance.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
