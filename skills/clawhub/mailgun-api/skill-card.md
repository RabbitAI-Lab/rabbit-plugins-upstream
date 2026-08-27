## Description:

Mailgun API integration with managed OAuth for sending, receiving, tracking email and managing Mailgun resources through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect to a Mailgun account through Maton, inspect account resources, and perform user-approved email, domain, route, template, mailing list, suppression, and webhook operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on a real Mailgun account, including sending email and changing or deleting account resources.

Mitigation: Use OAuth when possible, confirm the active account and connection, default to read or list calls first, and require explicit user approval before any send, create, update, or delete action.

Risk: A long-lived Maton API key can be exposed if the raw HTTP fallback is used carelessly.

Mitigation: Prefer the Maton CLI OAuth flow; when the fallback is required, never print, log, persist, or pass the key on the command line, and send it only to api.maton.ai.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Mailgun API Documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview)
- [Mailgun API Reference](https://mailgun-docs.redoc.ly/docs/mailgun/api-reference/intro/)
- [Mailgun Postman Collection](https://www.postman.com/mailgun/mailgun-s-public-workspace/documentation/ik8dl61/mailgun-api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user confirmation for connection creation or write operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
