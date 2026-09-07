## Description:

Cal.com API integration with managed OAuth for managing event types, bookings, schedules, availability, calendars, conferencing, webhooks, teams, verified resources, and user profile.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Cal.com through Maton OAuth and perform scheduling workflows such as checking availability, creating bookings, configuring event types, and managing webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure from package installation, OAuth/API-key handling, or raw HTTP fallback.

Mitigation: Confirm trust in the Maton packages and account connection, prefer OAuth, keep credentials in the approved credential store or secret environment, and never print or persist tokens or API keys.

Risk: Broad API passthrough may reach Cal.com endpoints beyond the documented examples.

Mitigation: Default to read/list operations, use the narrowest Cal.com scopes available, specify the intended connection when multiple accounts exist, and review every write request before execution.

Risk: Webhook subscriptions can send booking and event data, including attendee details, to external URLs.

Mitigation: Confirm the subscriber URL, host ownership, triggers, and intent with the user before creating or updating any webhook.

## Reference(s):

- [Cal.com API Documentation](https://cal.com/docs/api-reference/v2/introduction)
- [Cal.com API Reference](https://cal.com/docs/api-reference/v2)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/cal-com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Cal.com connection.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
