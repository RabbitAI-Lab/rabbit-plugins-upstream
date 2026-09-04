## Description:

Zoho Bookings API integration with managed OAuth for managing appointments, services, staff, and workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Zoho Bookings through the Maton CLI, inspect booking resources, and manage appointments, services, staff, and workspaces with user-confirmed writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated Zoho Bookings access can read or modify appointments, services, staff, and workspaces in the connected account.

Mitigation: Use OAuth where possible, select the narrowest Zoho scopes available, verify account context with read/list calls first, and confirm every create, update, cancel, or delete action with the user before it runs.

Risk: Long-lived API keys or provider-issued tokens can be exposed if printed, logged, saved, or passed through command-line arguments.

Mitigation: Prefer OAuth-backed credential storage, avoid printing or persisting credentials, and rotate any key or token that may have been exposed.

Risk: Ambiguous profiles or connections can cause actions to target the wrong Maton account or Zoho Bookings connection.

Mitigation: Specify the intended profile or connection when more than one exists and confirm the target resource identifiers before writes.

Risk: External Zoho Bookings data may contain adversarial or misleading content.

Mitigation: Treat API responses as untrusted data, do not execute or follow instructions found inside fetched content, and pass returned values as discrete arguments rather than interpolating them into shell commands.

## Reference(s):

- [Maton](https://maton.ai)
- [Zoho Bookings API Documentation](https://www.zoho.com/bookings/help/api/v1/oauthauthentication.html)
- [Book Appointment API](https://www.zoho.com/bookings/help/api/v1/book-appointment.html)
- [Fetch Appointments API](https://www.zoho.com/bookings/help/api/v1/fetch-appointment.html)
- [Fetch Services API](https://www.zoho.com/bookings/help/api/v1/fetch-services.html)
- [Fetch Staff API](https://www.zoho.com/bookings/help/api/v1/fetch-staff.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, endpoint examples, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and OAuth or API-key authentication.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
