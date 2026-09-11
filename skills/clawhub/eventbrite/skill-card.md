## Description:

Eventbrite API integration with managed OAuth for managing events, venues, ticket classes, orders, attendees, categories, and related Eventbrite resources through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and manage Eventbrite organizations, events, venues, ticket classes, orders, attendees, and reference data. It is suited to read-first workflows with explicit user approval before account connections or Eventbrite write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned Maton CLI or SDK installation can introduce supply-chain exposure.

Mitigation: Install Maton only from trusted sources, prefer pinned versions or isolated environments, and review installation provenance before use.

Risk: Long-lived API keys can leak through environment variables, logs, command history, or child processes.

Mitigation: Use OAuth where possible; if an API key is unavoidable, keep it out of command arguments, logs, files, and user-visible output.

Risk: Eventbrite write operations can publish, cancel, delete, or alter events, tickets, venues, orders, or attendee-facing state.

Mitigation: Default to read and list calls, confirm the target resource and payload with the user, and require approval before every POST, PUT, PATCH, DELETE, publish, cancel, delete, or ticket change.

Risk: Multiple Maton profiles or Eventbrite connections can cause actions to target the wrong account.

Mitigation: Verify account context first and specify the intended profile or connection when more than one is available.

Risk: External Eventbrite content can contain untrusted or adversarial instructions.

Mitigation: Treat API responses as data, avoid executing or interpolating returned content into shell commands, and validate values before reuse.

## Reference(s):

- [ClawHub Eventbrite Skill](https://clawhub.ai/byungkyu/skills/eventbrite)
- [Maton Homepage](https://maton.ai)
- [Eventbrite API Documentation](https://www.eventbrite.com/platform/api)
- [Eventbrite API Basics](https://www.eventbrite.com/platform/docs/api-basics)
- [Eventbrite API Explorer](https://www.eventbrite.com/platform/docs/api-explorer)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, Python, JavaScript, JSON examples, and Maton API command patterns.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and user approval before creating connections or executing write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
