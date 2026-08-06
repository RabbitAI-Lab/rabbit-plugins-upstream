## Description:

Guides agents in creating, sending, and debugging Mailtrap-hosted email templates with Handlebars personalization, template UUID API payloads, and transactional or bulk delivery workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mailtrap](https://clawhub.ai/user/mailtrap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and email operations teams use this skill to work with Mailtrap-hosted templates, generate or verify template send payloads, and troubleshoot Handlebars variables before transactional or bulk email delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help prepare Mailtrap API requests that send transactional or bulk email.

Mitigation: Provide API tokens, sender details, and recipient data only when intentionally performing email actions.

Risk: Template or variable changes can affect live email content.

Mitigation: Use Mailtrap sandbox testing and template previews for risky changes before live delivery.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mailtrap/skills/using-email-templates)
- [Mailtrap Templates API](https://docs.mailtrap.io/developers/templates/templates.md)
- [Mailtrap Transactional Email Sending](https://docs.mailtrap.io/developers/email-sending/transactional.md)
- [Mailtrap Bulk Email Sending](https://docs.mailtrap.io/developers/email-sending/bulk.md)
- [Using Handlebars with Email Templates](https://docs.mailtrap.io/email-api-smtp/email-templates/handlebars.md)
- [Testing Templates with Handlebars](https://docs.mailtrap.io/email-api-smtp/email-templates/handlebars.md#testing-templates-with-handlebars)
- [Mailtrap Sandbox Test Emails](https://docs.mailtrap.io/developers/email-sandbox/send-test-emails.md)
- [Mailtrap Node.js SDK](https://github.com/mailtrap/mailtrap-nodejs)
- [Mailtrap Python SDK](https://github.com/mailtrap/mailtrap-python)
- [Mailtrap PHP SDK](https://github.com/mailtrap/mailtrap-php)
- [Mailtrap Ruby SDK](https://github.com/mailtrap/mailtrap-ruby)
- [Mailtrap Java SDK](https://github.com/mailtrap/mailtrap-java)
- [Mailtrap .NET SDK](https://github.com/mailtrap/mailtrap-dotnet)
- [Mailtrap CLI](https://github.com/mailtrap/mailtrap-cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with API payload examples, inline code, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include email template HTML, Handlebars variables, API request bodies, SDK usage guidance, and sandbox testing recommendations.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
