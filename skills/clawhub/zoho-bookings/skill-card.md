## Description:

Zoho Bookings API integration with managed OAuth for managing appointments, services, staff, and workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Zoho Bookings through Maton, list and manage booking resources, and perform appointment, service, staff, and workspace operations with user confirmation for writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton receives access to the connected Zoho Bookings account.

Mitigation: Install only when that access is intended, prefer OAuth, and choose the narrowest scopes available during authorization.

Risk: Writes can create, cancel, or change appointments, services, staff, and workspaces.

Mitigation: Default to read and list calls, verify the target connection and resource identifiers, and require explicit user confirmation before any modifying request.

Risk: Deleting a connection revokes stored authorization and can break automation using that connection.

Mitigation: List connections first, confirm the exact connection id with the user, and avoid bypassing interactive prompts unless the user has already confirmed the target.

Risk: API responses may contain personal data such as names, email addresses, phone numbers, appointment notes, and booking details.

Mitigation: Extract only the fields needed for the task and avoid logging, persisting, or broadly displaying raw response bodies.

Risk: Using a raw Maton API key exposes a long-lived credential to the process environment.

Mitigation: Use the Maton CLI with OAuth when available; if raw HTTP is necessary, never print or persist the key and send it only to api.maton.ai.

## Reference(s):

- [Zoho Bookings API Documentation](https://www.zoho.com/bookings/help/api/v1/oauthauthentication.html)
- [Book Appointment API](https://www.zoho.com/bookings/help/api/v1/book-appointment.html)
- [Fetch Appointments API](https://www.zoho.com/bookings/help/api/v1/fetch-appointment.html)
- [Fetch Services API](https://www.zoho.com/bookings/help/api/v1/fetch-services.html)
- [Fetch Staff API](https://www.zoho.com/bookings/help/api/v1/fetch-staff.html)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK usage guidance for authenticated Zoho Bookings API calls; API responses may contain personal data and should be minimized.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
