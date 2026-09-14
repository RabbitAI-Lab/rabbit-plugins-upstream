## Description:

Zoho Bookings API integration with managed OAuth for managing appointments, services, staff, and workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external service teams, and developers use this skill to work with Zoho Bookings through Maton-managed OAuth, including booking appointments, checking availability, and managing services, staff, and workspaces. It can also guide approved hosted functions and trigger-based automation that run Zoho Bookings actions through the user's Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton credentials and Zoho Bookings OAuth grants may expose scheduling or business data if they are over-scoped, long-lived, or shared across unrelated app connections.

Mitigation: Use Maton OAuth where possible, avoid long-lived API keys, choose only needed Zoho Bookings scopes, and prefer a dedicated Maton account with only the required connection for hosted automation.

Risk: Write operations can modify appointments, services, staff, workspaces, or downstream workflows.

Mitigation: Default to read and list calls, then get explicit user approval for each POST, PUT, PATCH, DELETE, connection creation, function deployment, trigger creation, or automation change.

Risk: Hosted functions and trigger destinations can create persistent automation or data forwarding paths.

Mitigation: Keep function network policy at DENY_ALL unless named hosts are explicitly required and approved, route this skill's trigger output only to its approved hosted function, and review or remove persistent destinations when no longer needed.

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

**Output Format:** [Markdown guidance with shell commands, API request examples, code snippets, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a valid Maton-managed Zoho Bookings connection.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
