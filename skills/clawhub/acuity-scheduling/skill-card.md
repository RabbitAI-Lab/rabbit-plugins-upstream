## Description:

Acuity Scheduling API integration with managed OAuth for managing appointments, calendars, clients, and availability through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and scheduling administrators use this skill to let an agent check Acuity availability, inspect calendars and clients, and create, reschedule, cancel, or otherwise manage appointments after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access appointment, calendar, client, and availability data in the connected Acuity Scheduling account.

Mitigation: Install only when Maton-mediated Acuity access is acceptable, connect only intended accounts, and specify the intended connection when more than one exists.

Risk: Appointment creation, cancellation, rescheduling, client changes, block changes, and connection deletion can modify operational scheduling data.

Mitigation: Default to read and list calls first, then require explicit confirmation of the target resource, payload, and intended effect before any write or delete operation.

Risk: Credentials or provider-issued tokens could be exposed if printed, persisted, or passed outside the intended authentication path.

Mitigation: Use OAuth where possible, let the Maton CLI and operating system credential store handle credentials, and do not print, log, persist, or transmit tokens outside the approved request path.

Risk: Webhook or other persistent side-effect endpoints could send data to an unintended external destination.

Mitigation: Treat webhooks as out of scope unless explicitly requested, and confirm the exact endpoint, event, and destination URL before acting.

## Reference(s):

- [Acuity Scheduling API Quick Start](https://developers.acuityscheduling.com/reference/quick-start)
- [Appointments API](https://developers.acuityscheduling.com/reference/get-appointments)
- [Availability API](https://developers.acuityscheduling.com/reference/get-availability-dates)
- [Calendars API](https://developers.acuityscheduling.com/reference/get-calendars)
- [Clients API](https://developers.acuityscheduling.com/reference/clients)
- [Acuity OAuth2 Documentation](https://developers.acuityscheduling.com/docs/oauth2)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/acuity-scheduling)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Acuity API calls through Maton; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
