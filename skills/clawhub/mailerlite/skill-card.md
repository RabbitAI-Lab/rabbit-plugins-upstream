## Description:

MailerLite API integration with managed OAuth for managing email subscribers, groups, campaigns, automations, forms, fields, segments, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate MailerLite accounts through Maton OAuth, including subscriber, group, campaign, automation, form, field, segment, and webhook tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MailerLite writes can affect customers or external recipients, especially campaign scheduling, webhooks, subscriber deletion, and automation changes.

Mitigation: Confirm the exact account, connection, target resource, payload, and intended effect before any write operation.

Risk: Credential exposure can occur if API keys or tokens are printed, stored, or passed through shell arguments.

Mitigation: Prefer OAuth through the Maton CLI, avoid raw HTTP fallback unless the CLI cannot be used, and never print or persist credentials.

Risk: Using an ambiguous default account or connection can send changes to the wrong MailerLite workspace.

Mitigation: List and verify available connections first, then specify the intended Maton profile and MailerLite connection for account-sensitive operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/mailerlite)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [MailerLite API Documentation](https://developers.mailerlite.com/docs/)
- [MailerLite Subscribers API](https://developers.mailerlite.com/docs/subscribers.html)
- [MailerLite Groups API](https://developers.mailerlite.com/docs/groups.html)
- [MailerLite Campaigns API](https://developers.mailerlite.com/docs/campaigns.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for Maton CLI and MailerLite API operations; API responses depend on the connected MailerLite account.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
