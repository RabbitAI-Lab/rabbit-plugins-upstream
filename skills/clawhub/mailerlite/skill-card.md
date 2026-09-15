## Description:

MailerLite API integration with managed OAuth for managing subscribers, groups, campaigns, automations, forms, fields, segments, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate MailerLite through Maton-managed OAuth, including subscriber, group, campaign, automation, form, field, segment, and webhook tasks. It defaults to read and list calls and requires user confirmation for new connections, writes, webhooks, hosted functions, and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes, campaign scheduling, webhooks, hosted functions, and triggers can modify MailerLite data or create persistent automation.

Mitigation: Require explicit user approval for each connection, write, deploy, invocation, webhook, function, trigger, or destination change, including the target resource, payload, intended effect, destination host, and persistence.

Risk: Subscriber, campaign, form, webhook, and trigger data may contain personal or business-sensitive information.

Mitigation: Return only the fields needed for the task and avoid dumping raw responses or event payloads into logs, files, shared surfaces, or third-party destinations.

Risk: Maton credentials or API keys could be exposed when raw HTTP is used or when credentials are passed through the environment.

Mitigation: Prefer OAuth through the Maton CLI, do not print, read, export, or store credentials, and send MATON_API_KEY only to api.maton.ai when the CLI cannot be installed.

Risk: Persistent forwarding to third-party URLs can disclose subscriber, campaign, or event data beyond the intended platform.

Mitigation: Prefer api.maton.ai or *.maton.app destinations, never invent or reuse documentation URLs as destinations, and use only user-supplied, explicitly trusted hosts with minimal payload fields.

## Reference(s):

- [MailerLite API Documentation](https://developers.mailerlite.com/docs/)
- [MailerLite Subscribers API](https://developers.mailerlite.com/docs/subscribers.html)
- [MailerLite Groups API](https://developers.mailerlite.com/docs/groups.html)
- [MailerLite Campaigns API](https://developers.mailerlite.com/docs/campaigns.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [MailerLite Skill Page](https://clawhub.ai/byungkyu/skills/mailerlite)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-approved MailerLite connection for live API calls.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
