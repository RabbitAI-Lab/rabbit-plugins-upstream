## Description:

Helps developers add or migrate transactional email sending to Mailfully, test delivery, and prepare sending-domain DNS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gbourne1](https://clawhub.ai/user/gbourne1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to connect an app's transactional emails to Mailfully or migrate existing transactional send paths from another provider, while retaining the old provider for rollback and bulk mail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to transactional email code and dependencies can affect production sending.

Mitigation: Review proposed files and package changes; keep existing sending paths available until the migration is approved.

Risk: A test send or DNS record change may have unintended effects.

Mitigation: Review the test send and DNS records, and approve any Cloudflare or Route 53 writes before execution.

Risk: Exposure of API keys or webhook secrets.

Mitigation: Enter real secrets only in the intended local or hosting environment, not in chat.

## Reference(s):

- [Mailfully homepage](https://mailfully.com)
- [ClawHub skill release](https://clawhub.ai/gbourne1/skills/add-mailfully)
- [Mailfully API essentials](references/api-essentials.md)
- [REST client examples](references/rest-clients.md)
- [DNS provider setup](references/dns-providers.md)
- [Webhook setup](references/webhooks.md)
- [Provider migration guides](references/migrate-sendgrid.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a setup report and a test-send result when a test key is available.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
