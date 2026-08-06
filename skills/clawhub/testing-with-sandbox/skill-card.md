## Description:

Use when capturing outbound email in development or staging without delivering to real recipients, inspecting HTML or headers, running spam or structure checks, or automating tests against a fake inbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mailtrap](https://clawhub.ai/user/mailtrap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and automation agents use this skill to route development, staging, CI, and test email into Mailtrap Email Sandbox, inspect captured messages, and avoid delivering test messages to real recipients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated examples may use sandbox tokens or read captured test inbox contents if the user supplies credentials.

Mitigation: Keep Mailtrap sandbox tokens separate from live Mailtrap API tokens, scope them to the intended sandbox, and avoid using sandbox credentials or endpoints in production.

Risk: Users may expect sandbox messages to reach real recipients or accidentally mix sandbox and transactional endpoints.

Mitigation: Confirm the workflow is for non-production email testing and verify endpoints use Mailtrap sandbox API or SMTP hosts before applying generated configuration.

## Reference(s):

- [Mailtrap developer documentation](https://docs.mailtrap.io/developers/)
- [Sandboxes API](https://docs.mailtrap.io/developers/email-sandbox/sandboxes-inboxes.md)
- [Messages API](https://docs.mailtrap.io/developers/email-sandbox/messages.md)
- [Send test emails](https://docs.mailtrap.io/developers/email-sandbox/send-test-emails.md)
- [Handlebars templates](https://docs.mailtrap.io/email-api-smtp/email-templates/handlebars.md)
- [Email address per sandbox](https://docs.mailtrap.io/email-sandbox/setup/email-address-per-sandbox.md)
- [Mailtrap Node.js SDK](https://github.com/mailtrap/mailtrap-nodejs)
- [Mailtrap Python SDK](https://github.com/mailtrap/mailtrap-python)
- [Mailtrap PHP SDK](https://github.com/mailtrap/mailtrap-php)
- [Mailtrap Ruby SDK](https://github.com/mailtrap/mailtrap-ruby)
- [Mailtrap Java SDK](https://github.com/mailtrap/mailtrap-java)
- [Mailtrap .NET SDK](https://github.com/mailtrap/mailtrap-dotnet)
- [Mailtrap CLI](https://github.com/mailtrap/mailtrap-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code blocks, endpoint examples, tables, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Mailtrap sandbox API or SMTP settings, test-mode code examples, and credential-handling reminders.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
