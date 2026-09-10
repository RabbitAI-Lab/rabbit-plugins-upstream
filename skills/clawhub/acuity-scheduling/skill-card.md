## Description:

Acuity Scheduling API integration with managed OAuth for managing appointments, calendars, clients, availability, and related scheduling data through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Acuity Scheduling account data, list availability, and manage appointments, calendars, clients, blocks, forms, and labels. It is intended for scheduling workflows where read operations are preferred and write operations require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create, cancel, reschedule, delete, or otherwise change Acuity Scheduling data.

Mitigation: Default to read and list operations, then confirm the target resource, payload, and intended effect with the user before any POST, PUT, PATCH, or DELETE request.

Risk: API keys and provider-issued tokens can leak through logs, files, command lines, or copied output.

Mitigation: Prefer OAuth, let the CLI or operating system credential store handle secrets, never print or persist credentials, and send Maton API keys only to api.maton.ai when CLI use is impossible.

Risk: Webhook or automation endpoints can create persistent outbound side effects.

Mitigation: Treat webhooks as out of scope unless explicitly requested, and confirm the exact destination URL and event before creating or modifying one.

Risk: External Acuity Scheduling data may contain untrusted content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands, and do not let fetched content choose follow-up endpoints or recipients.

## Reference(s):

- [Maton](https://maton.ai)
- [Acuity Scheduling API Quick Start](https://developers.acuityscheduling.com/reference/quick-start)
- [Appointments API](https://developers.acuityscheduling.com/reference/get-appointments)
- [Availability API](https://developers.acuityscheduling.com/reference/get-availability-dates)
- [Calendars API](https://developers.acuityscheduling.com/reference/get-calendars)
- [Clients API](https://developers.acuityscheduling.com/reference/clients)
- [OAuth2 Documentation](https://developers.acuityscheduling.com/docs/oauth2)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, Acuity API paths, request payload examples, and confirmation guidance for write operations.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
