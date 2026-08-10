## Description:

Use when converting or migrating email templates from another provider (SendGrid, Mailgun, Mandrill, Postmark, Brevo, Amazon SES) to Mailtrap-compatible Handlebars syntax.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mailtrap](https://clawhub.ai/user/mailtrap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and email operations teams use this skill to migrate templates from common email providers into Mailtrap-compatible Handlebars syntax. It supports single-file, bulk-directory, and inline HTML conversion while reporting patterns that require application-level changes or manual review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Template files may contain sensitive customer, transactional, or business content that the agent must read to convert.

Mitigation: Provide only the specific template file or directory intended for migration, and review the converted output and report files before reuse.

Risk: Unsupported or ambiguous provider syntax can produce incomplete migration behavior if ignored.

Mitigation: Resolve every flagged pattern, move unsupported helpers such as date formatting or comparisons into application code, and test migrated templates before sending to real recipients.

Risk: The migration guide includes optional Mailtrap API examples that use tokens and create, update, or delete templates.

Mitigation: Keep tokens in environment variables or a secret manager, confirm account and template identifiers, and review live API changes before executing them.

## Reference(s):

- [Template Conversion Rules](references/conversion-rules.md)
- [How to Migrate Email Templates to Mailtrap](content/how-to-migrate-email-templates.md)
- [Mailtrap Email Templates documentation](https://docs.mailtrap.io/email-api-smtp/email-templates)
- [Mailtrap Sending Domain setup](https://docs.mailtrap.io/email-api-smtp/setup/sending-domain.md)
- [Mailtrap API authentication](https://docs.mailtrap.io/developers/authentication)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, converted HTML template code, text reports, and configuration reminders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes converted template files and report files for file-based conversions; inline conversions can be presented as converted HTML for review.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
