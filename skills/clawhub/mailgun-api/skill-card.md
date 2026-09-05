## Description:

Mailgun API integration with managed OAuth for sending, receiving, and tracking emails and managing Mailgun resources through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Mailgun accounts from an agent, including listing and managing domains, routes, templates, mailing lists, suppressions, webhooks, and sending email after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send email and modify Mailgun domains, routes, webhooks, lists, suppressions, and credentials on a connected account.

Mitigation: Default to read and list calls, verify the target account and resource identifiers, and require explicit user confirmation before every POST, PUT, PATCH, or DELETE operation.

Risk: Multiple Mailgun connections or Maton profiles could cause an action to affect the wrong account.

Mitigation: List available connections first and pass the intended connection or profile explicitly when there is any ambiguity.

Risk: Maton API keys and Mailgun response data may expose credentials or personal data if printed, logged, or persisted.

Mitigation: Use OAuth where possible, keep raw API keys out of command lines and logs, send Maton API keys only to api.maton.ai, and extract only the response fields needed for the task.

Risk: Mailgun API content and webhook data may contain untrusted or adversarial text.

Mitigation: Treat fetched content as data, not instructions, and avoid executing or interpolating it into shell commands or follow-up requests without validation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/mailgun-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Mailgun API Documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview)
- [Mailgun API Reference](https://mailgun-docs.redoc.ly/docs/mailgun/api-reference/intro/)
- [Mailgun Postman Collection](https://www.postman.com/mailgun/mailgun-s-public-workspace/documentation/ik8dl61/mailgun-api)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, JSON]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Mailgun API paths, form-encoded request examples, Maton CLI commands, and response-shaping guidance.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
