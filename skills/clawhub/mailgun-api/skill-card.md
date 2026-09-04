## Description:

Mailgun API integration with managed OAuth for sending, receiving, and tracking email, and for managing domains, routes, templates, mailing lists, suppressions, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to make Mailgun API calls through Maton-managed OAuth for transactional email operations, account resource management, reporting, and troubleshooting. It is suited for read/list workflows by default and for write operations after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailgun access is mediated through Maton, so the user must trust Maton with the connected Mailgun account.

Mitigation: Install only when Maton is an acceptable intermediary and confirm the intended Mailgun account or connection before use.

Risk: Write operations can send email, alter domains, routes, templates, lists, suppressions, webhooks, or credentials.

Mitigation: Default to read/list calls and require explicit user confirmation of the target resource, payload, and expected effect before POST, PUT, PATCH, or DELETE.

Risk: The documented gateway defaults to the Mailgun US API region, which may be unsuitable for EU-region or regulated email data.

Mitigation: Do not use the default flow for EU-region or regulated data unless the gateway region and compliance posture have been confirmed.

Risk: Long-lived API keys can leak through logs, shell history, command arguments, or persisted files when the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI; if an API key is necessary, keep it in the process environment, never print or persist it, and rotate it if exposed.

## Reference(s):

- [ClawHub Mailgun Skill](https://clawhub.ai/byungkyu/skills/mailgun-api)
- [Maton Homepage](https://maton.ai)
- [Mailgun API Documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview)
- [Mailgun API Reference](https://mailgun-docs.redoc.ly/docs/mailgun/api-reference/intro/)
- [Mailgun Postman Collection](https://www.postman.com/mailgun/mailgun-s-public-workspace/documentation/ik8dl61/mailgun-api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, configuration steps, and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands or SDK examples; API responses are expected from Mailgun through the Maton gateway.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
