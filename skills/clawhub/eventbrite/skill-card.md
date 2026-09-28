## Description:

Eventbrite API integration with managed OAuth for managing events, venues, ticket classes, orders, attendees, and event categories through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate an authorized Eventbrite account from an agent, starting with read/list calls and escalating to event, venue, ticket, order, attendee, or automation changes only after explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Eventbrite business data through a connected Maton account.

Mitigation: Use OAuth where possible, review requested scopes, select the least privileged account/connection, and revoke unused connections.

Risk: Write, delete, hosted function, trigger, or destination operations can change resources or establish ongoing automation.

Mitigation: Require explicit user approval for each operation, including the target resource, payload, intended effect, schedule, destination host, and persistence.

Risk: Raw Maton API keys are long-lived credentials that can leak through process environments, logs, shell history, or pasted output.

Mitigation: Prefer the Maton CLI credential store; when raw HTTP is unavoidable, read the key only from the environment, never print or persist it, and rotate it if exposed.

Risk: Third-party API responses or trigger payloads may contain untrusted content.

Mitigation: Treat fetched content as data, validate it before use, and never let external data choose commands, endpoints, recipients, destinations, or follow-up actions.

## Reference(s):

- [ClawHub Eventbrite Skill](https://clawhub.ai/byungkyu/skills/eventbrite)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Eventbrite API Documentation](https://www.eventbrite.com/platform/api)
- [Eventbrite API Basics](https://www.eventbrite.com/platform/docs/api-basics)
- [Eventbrite API Explorer](https://www.eventbrite.com/platform/docs/api-explorer)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, API paths, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated Maton CLI/API calls and user-approved hosted function or trigger setup steps.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
