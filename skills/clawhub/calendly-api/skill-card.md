## Description:

Calendly API integration with managed OAuth for accessing event types, scheduled events, invitees, availability, booking workflows, and webhook management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and scheduling workflow owners use this skill to inspect Calendly scheduling data, check availability, manage invitees and event types, and build approved scheduling automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendly writes, connection changes, webhooks, or triggers may alter scheduling data or create persistent automation.

Mitigation: Default to read and list calls, and get explicit user approval for each write, new connection, webhook, trigger, hosted function deployment, or invocation.

Risk: Long-lived API keys or exposed environment variables can broaden account access beyond the immediate task.

Mitigation: Prefer OAuth and the operating system credential store, avoid MATON_API_KEY unless the CLI cannot be installed, and revoke unused connections or automations when finished.

Risk: Webhook and trigger destinations can forward future invitee or scheduling data automatically.

Mitigation: Review destination URLs carefully, use least-privilege Calendly scopes, and remove automations that are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/calendly-api)
- [Maton Homepage](https://maton.ai)
- [Calendly Developer Portal](https://developer.calendly.com/)
- [Calendly API Reference](https://developer.calendly.com/api-docs)
- [Calendly API Use Cases](https://developer.calendly.com/api-use-cases)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Calendly connection; defaults to read/list flows and requires explicit approval for writes, webhooks, triggers, and credential-bearing automation.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
