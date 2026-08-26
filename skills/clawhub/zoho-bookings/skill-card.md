## Description:

Zoho Bookings API integration with managed OAuth for managing appointments, services, staff, and workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to help agents connect to Zoho Bookings through Maton, inspect availability and booking data, and manage appointments, services, staff, and workspaces with user-confirmed changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Zoho Bookings data after a Maton connection is authorized.

Mitigation: Only approve connection creation and write actions when the target account, resource, payload, and expected effect are clear.

Risk: Credentials could be exposed if tokens or API keys are printed, persisted, or passed through command-line arguments.

Mitigation: Use Maton OAuth and credential-store flows, avoid printing or exporting credentials, and use the stdin-based raw HTTP fallback only when the CLI cannot be installed.

Risk: Zoho Bookings API responses may contain untrusted external content.

Mitigation: Treat fetched content as data, validate resource identifiers before follow-up calls, and do not let response content choose endpoints or commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-bookings)
- [Maton Homepage](https://maton.ai)
- [Zoho Bookings API Documentation](https://www.zoho.com/bookings/help/api/v1/oauthauthentication.html)
- [Book Appointment API](https://www.zoho.com/bookings/help/api/v1/book-appointment.html)
- [Fetch Appointments API](https://www.zoho.com/bookings/help/api/v1/fetch-appointment.html)
- [Fetch Services API](https://www.zoho.com/bookings/help/api/v1/fetch-services.html)
- [Fetch Staff API](https://www.zoho.com/bookings/help/api/v1/fetch-staff.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, JSON payload examples, and confirmation prompts for connection creation or write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
