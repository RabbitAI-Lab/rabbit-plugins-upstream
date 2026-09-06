## Description:

MailerLite API integration with managed OAuth for managing email subscribers, groups, campaigns, automations, forms, fields, segments, and webhooks through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage MailerLite account resources through managed OAuth-backed API calls. It is suited for subscriber management, campaign setup, group maintenance, automation and webhook work, with confirmation before connection creation or data-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MailerLite access is mediated through Maton, so users must be comfortable with Maton acting as the intermediary for account API access.

Mitigation: Install and use the skill only when that intermediary model is acceptable for the connected MailerLite account.

Risk: Writes, campaign scheduling, deletions, webhook changes, and automation changes can alter customer data or trigger downstream effects.

Mitigation: Confirm the exact account, connection, resource identifiers, payload, and intended effect before allowing those actions.

Risk: Long-lived API keys can be exposed through shell history, logs, child processes, or persisted files when the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI; if an API key is required, read it only from the process environment, never print it, and rotate it if exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/mailerlite)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [MailerLite API Documentation](https://developers.mailerlite.com/docs/)
- [MailerLite Subscribers API](https://developers.mailerlite.com/docs/subscribers.html)
- [MailerLite Groups API](https://developers.mailerlite.com/docs/groups.html)
- [MailerLite Campaigns API](https://developers.mailerlite.com/docs/campaigns.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON request examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces MailerLite API paths, Maton CLI calls, request payload examples, and approval guidance; it does not directly execute without user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
