## Description:

Use when integrating, configuring, or troubleshooting Mailtrap live email sending over Email API or SMTP, including wiring outbound mail from an application or choosing how to send.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mailtrap](https://clawhub.ai/user/mailtrap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and implement Mailtrap live email sending through platform integrations, SDKs, HTTP Email API, or SMTP. It helps distinguish transactional, bulk, batch, and campaign sending paths and avoid common configuration mistakes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated sending code or shell examples can deliver real email to recipients.

Mitigation: Review generated code before running it and test with safe recipients or sandbox flows where appropriate.

Risk: Mailtrap API tokens may be overexposed or over-permissioned.

Mitigation: Use scoped Mailtrap tokens, store them in environment variables or a secrets manager, and rotate them when needed.

Risk: Bulk or batch examples can send many messages quickly.

Mitigation: Confirm the intended stream, recipient list, and rate-limit handling before using bulk or batch sends.

## Reference(s):

- [Mailtrap Transactional Email Sending](https://docs.mailtrap.io/developers/email-sending/transactional.md)
- [Mailtrap Bulk Email Sending](https://docs.mailtrap.io/developers/email-sending/bulk.md)
- [Mailtrap Suppressions](https://docs.mailtrap.io/developers/email-sending/suppressions.md)
- [Mailtrap Node.js SDK](https://github.com/mailtrap/mailtrap-nodejs)
- [Mailtrap Python SDK](https://github.com/mailtrap/mailtrap-python)
- [Mailtrap PHP SDK](https://github.com/mailtrap/mailtrap-php)
- [Mailtrap Ruby SDK](https://github.com/mailtrap/mailtrap-ruby)
- [Mailtrap Java SDK](https://github.com/mailtrap/mailtrap-java)
- [Mailtrap .NET SDK](https://github.com/mailtrap/mailtrap-dotnet)
- [Mailtrap CLI](https://github.com/mailtrap/mailtrap-cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tables, JSON examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live email API and SMTP examples that should be reviewed before execution.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
