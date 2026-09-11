## Description:

Zoho Bookings API integration with managed OAuth for managing appointments, services, staff, and workspaces through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to help agents interact with Zoho Bookings accounts through managed Maton authentication. It supports listing, booking, updating, and managing appointments, services, staff, workspaces, and account connections when the user has authorized access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad Maton API passthrough, so authorized endpoints outside the documented Zoho Bookings surface may be reachable.

Mitigation: Default to read and list calls, use the narrowest available Zoho Bookings scopes, specify the intended connection, and confirm every write or connection-management action with the user.

Risk: Long-lived API keys or provider-issued credentials can leak through environment variables, logs, shell history, files, or command output.

Mitigation: Prefer OAuth, keep credentials in the managed credential store, never print or persist secrets, and use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

Risk: Connection deletion and booking changes can revoke access, cancel or modify appointments, or otherwise affect live scheduling data.

Mitigation: Confirm exact connection IDs, resource identifiers, payloads, and intended effects before POST, PUT, PATCH, DELETE, or connection delete operations.

Risk: Zoho Bookings responses can include personal data such as names, email addresses, phone numbers, notes, and scheduling details.

Mitigation: Extract only fields needed for the task and avoid dumping raw responses into logs, files, or user-visible output unless specifically requested.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-bookings)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Bookings API Documentation](https://www.zoho.com/bookings/help/api/v1/oauthauthentication.html)
- [Zoho Book Appointment API](https://www.zoho.com/bookings/help/api/v1/book-appointment.html)
- [Zoho Fetch Appointments API](https://www.zoho.com/bookings/help/api/v1/fetch-appointment.html)
- [Zoho Fetch Services API](https://www.zoho.com/bookings/help/api/v1/fetch-services.html)
- [Zoho Fetch Staff API](https://www.zoho.com/bookings/help/api/v1/fetch-staff.html)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, raw HTTP examples, endpoint paths, request bodies, and safety guidance for user-approved Zoho Bookings operations.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
