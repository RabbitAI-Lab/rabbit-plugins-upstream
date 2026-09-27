## Description:

Zoho Bookings API integration with managed OAuth for managing appointments, services, staff, and workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect a Maton-authenticated Zoho Bookings account, inspect scheduling data, and manage workspaces, services, staff, and appointments. It is also used to create approved Maton functions or triggers that run Zoho Bookings actions through the user's authorized connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho Bookings operations can expose or change appointment, service, staff, and workspace data through the user's connected account.

Mitigation: Default to read and list calls, use least-privilege OAuth scopes, and require explicit user approval before creating connections or running POST, PUT, PATCH, or DELETE requests.

Risk: Long-lived API keys and raw HTTP fallback can broaden credential exposure compared with OAuth-backed CLI use.

Mitigation: Prefer Maton OAuth, store credentials in the operating system credential store, and use raw HTTP with MATON_API_KEY only when the CLI cannot be installed.

Risk: Hosted functions, triggers, and destinations can create persistent automation or data forwarding.

Mitigation: Require separate approval for hosted code, trigger destinations, and invocations; prefer DENY_ALL network policy and approved Maton endpoints unless the user names and approves another host.

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
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for Maton CLI/API usage, OAuth connection management, Zoho Bookings API calls, and approved automation setup.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
