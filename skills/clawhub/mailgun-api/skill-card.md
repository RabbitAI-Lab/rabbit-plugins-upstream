## Description:

Mailgun API integration through Maton managed OAuth for sending, receiving, tracking, and managing email resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Mailgun through the Maton gateway for transactional email, domain, route, template, mailing list, suppression, event, webhook, tracking, and credential workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence identifies unpinned CLI or SDK installation and persistent authentication as the main caution.

Mitigation: Prefer OAuth, use the narrowest Mailgun scopes available, and install reviewed or pinned versions in an isolated environment where possible.

Risk: Email sends, deletions, webhook changes, and credential changes can affect external recipients or account state.

Mitigation: Default to read and list operations, then confirm the target resource, payload, and effect before any write operation.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key.

Mitigation: Use the CLI OAuth path when available; when raw HTTP is necessary, do not print, persist, or pass the key on a command line, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Mailgun Skill](https://clawhub.ai/byungkyu/skills/mailgun-api)
- [Maton](https://maton.ai)
- [Mailgun API Documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview)
- [Mailgun API Reference](https://mailgun-docs.redoc.ly/docs/mailgun/api-reference/intro/)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include command examples, endpoint paths, request bodies, connection guidance, and safety checks for Mailgun operations.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
