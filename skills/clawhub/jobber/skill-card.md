## Description:

Jobber API integration with managed OAuth for managing clients, jobs, invoices, quotes, properties, and team members for field service businesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and field service operators use this skill to access Jobber through the Maton gateway, retrieve scheduling and business records, and manage clients, jobs, quotes, invoices, properties, requests, users, and custom fields. It is intended for authenticated Jobber accounts and requires explicit approval before creating new connections or modifying data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify important Jobber business data, including customers, jobs, quotes, and invoices.

Mitigation: Use OAuth where possible, select the narrowest Jobber scopes available, specify the intended connection when multiple accounts exist, and approve writes only after reviewing the exact target and payload.

Risk: A new Jobber connection could authorize broader or unintended account access.

Mitigation: Create connections only after explicit user approval and connect only the account needed for the current task.

Risk: Long-lived API keys or provider-issued tokens can be exposed if printed, logged, persisted, or passed through command lines.

Mitigation: Prefer OAuth and the operating system credential store; do not print, persist, export, or pass credentials on command lines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/jobber)
- [Maton homepage](https://maton.ai)
- [Jobber Developer Documentation](https://developer.getjobber.com/docs/)
- [Jobber Getting Started Guide](https://developer.getjobber.com/docs/getting_started/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway related skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown guidance with shell commands, GraphQL JSON payloads, and SDK examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and a connected Jobber account.]

## Skill Version(s):

1.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
