## Description:

Klaviyo API integration with managed OAuth for accessing and managing profiles, lists, segments, campaigns, flows, events, metrics, templates, catalogs, webhooks, tags, coupons, images, forms, reviews, and account settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage Klaviyo marketing and customer engagement workflows through Maton-authenticated API calls. The skill supports read/list workflows by default and documents approval requirements for writes, account connections, hosted functions, triggers, webhooks, and persistent forwarding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Klaviyo access can expose customer and marketing data or enable changes to campaigns, contacts, webhooks, and automations.

Mitigation: Use OAuth where possible, select least-privilege scopes, default to read/list calls, and get explicit user confirmation before writes, new connections, sends, automation, or persistent forwarding.

Risk: Persistent webhooks, triggers, and destinations can continue forwarding future customer, marketing, or event data after setup.

Mitigation: Review the exact destination URL, payload fields, host ownership, and frequency before creation; prefer Maton-controlled destinations where appropriate and delete unused webhooks, triggers, destinations, functions, and connections.

Risk: Raw HTTP mode requires handling a long-lived Maton API key that can leak through logs, shell history, files, or child processes.

Mitigation: Prefer the Maton CLI with OAuth; if raw HTTP is unavoidable, keep MATON_API_KEY in the process environment only, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/klaviyo)
- [Maton Homepage](https://maton.ai)
- [Klaviyo API Documentation](https://developers.klaviyo.com)
- [Klaviyo API Reference](https://developers.klaviyo.com/en/reference/api_overview)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI or API commands and user-approval checkpoints.]

## Skill Version(s):

1.2.6 (source: server release evidence; artifact metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
