## Description:

Cal.com API integration with managed OAuth for managing event types, bookings, schedules, availability, calendars, conferencing, webhooks, teams, verified resources, and user profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Cal.com scheduling workflows, including availability checks, booking creation, event type configuration, and webhook management through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access or change Cal.com scheduling data through the user's Maton connection.

Mitigation: Default to read and list calls, and require explicit user approval for every write, new connection, target resource, payload, and intended effect.

Risk: Webhook and trigger destinations can create persistent forwarding of booking, event, or connected-app payload data to a URL.

Mitigation: Before creation or update, confirm the exact destination URL, who controls it, what data will flow, that delivery is persistent, and whether credentials are present.

Risk: Maton credentials and connected-account authorizations can expose scheduling data if mishandled.

Mitigation: Prefer OAuth and the operating system credential store, avoid printing or embedding credentials, use least-privilege connections, and remove unused functions, triggers, webhooks, or connections.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/cal-com)
- [Maton Homepage](https://maton.ai)
- [Cal.com API Documentation](https://cal.com/docs/api-reference/v2/introduction)
- [Cal.com API Reference](https://cal.com/docs/api-reference/v2)
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

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API calls]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples, endpoint guidance, trigger configuration guidance, and approval checkpoints.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
