## Description:

Front API integration with managed OAuth for managing conversations, messages, contacts, tags, inboxes, teammates, and teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Customer support and operations teams use this skill to work with Front conversations, messages, contacts, tags, inboxes, teammates, and teams through an authenticated Maton connection. Developers and automation builders can also use it to create approved hosted functions and triggers that run Front actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mediate access to Front workspace data through Maton.

Mitigation: Install only when that access is intended, review requested OAuth scopes, and prefer read-only access where possible.

Risk: Write operations and automation setup can change messages, connections, functions, triggers, or destinations.

Mitigation: Confirm every message send, delete, update, new connection, hosted function, trigger, and persistent automation before execution.

Risk: Persistent trigger destinations may forward business data outside the immediate task flow.

Mitigation: Create trigger destinations only after confirming what data will be forwarded and where.

## Reference(s):

- [ClawHub Front Skill](https://clawhub.ai/byungkyu/skills/front-api)
- [Maton](https://maton.ai)
- [Front API Reference](https://dev.frontapp.com/reference/introduction)
- [Front API Authentication](https://dev.frontapp.com/docs/authentication)
- [Front API Rate Limits](https://dev.frontapp.com/docs/rate-limiting)
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

**Output Format:** [Markdown with inline shell, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Front requests require network access, a Maton account, and an approved Front connection; writes and automation setup require explicit user confirmation.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
