## Description:

Calendly API integration with managed OAuth for accessing event types, scheduled events, invitees, availability, and webhook workflows through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to view Calendly scheduling data, check availability, book or cancel meetings, and manage webhook subscriptions. It is best suited for agents that need read-first Calendly API guidance with explicit approval before write operations or new account connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendly and Maton credentials could be exposed if tokens or API keys are printed, logged, persisted, or passed on a command line.

Mitigation: Prefer OAuth through the Maton CLI, let the operating system credential store hold secrets, check authentication with `maton whoami`, and never print or persist credential values.

Risk: Write operations can create, cancel, delete, or trigger scheduling and webhook changes with external side effects.

Mitigation: Default to read and list calls, verify resource identifiers first, and require explicit user confirmation before POST, PUT, PATCH, DELETE, connection creation, cancellation, deletion, or webhook actions.

Risk: Multiple Maton profiles or Calendly connections can cause requests to affect the wrong account.

Mitigation: Specify the intended profile and Calendly connection when more than one account or connection exists.

Risk: Calendly API content and webhook payloads may contain untrusted data.

Mitigation: Treat returned content as data, validate it before reuse, and do not execute, eval, or let fetched content choose endpoints, recipients, commands, or follow-up actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/calendly-api)
- [Maton Homepage](https://maton.ai)
- [Calendly Developer Portal](https://developer.calendly.com/)
- [Calendly API Reference](https://developer.calendly.com/api-docs)
- [Calendly API Use Cases](https://developer.calendly.com/api-use-cases)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline shell commands, code examples, and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Calendly API guidance and command examples; destructive or webhook-related operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
