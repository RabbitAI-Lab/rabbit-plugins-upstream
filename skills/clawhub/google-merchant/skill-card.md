## Description:

Google Merchant Center API integration with managed OAuth for reading and, with explicit user approval, modifying Merchant Center products, inventories, data sources, promotions, account settings, conversions, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to query and administer Google Merchant Center accounts through Maton-authenticated CLI or HTTP calls. It supports approved automations that run Merchant Center actions on schedules or supported source events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete Google Merchant Center business data through authenticated write operations.

Mitigation: Require explicit user approval with exact resource identifiers, payload, and intended effect before any POST, PUT, PATCH, or DELETE operation.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or command-line arguments when raw HTTP is used.

Mitigation: Prefer OAuth through the Maton CLI and use raw HTTP only when the CLI cannot be installed; never print, persist, or pass the API key on a command line.

Risk: Triggers and destinations can create persistent automated forwarding or unattended actions.

Mitigation: Use platform-owned destinations by default, disclose destination host and payload fields, require separate approval for each persistent destination, and delete unused automations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-merchant)
- [Maton Homepage](https://maton.ai)
- [Merchant API Overview](https://developers.google.com/merchant/api/overview)
- [Merchant API Reference](https://developers.google.com/merchant/api/reference/rest)
- [Products Guide](https://developers.google.com/merchant/api/guides/products/overview)
- [Data Sources Guide](https://developers.google.com/merchant/api/guides/data-sources/overview)
- [Reports Guide](https://developers.google.com/merchant/api/guides/reports/overview)
- [Product Data Specification](https://support.google.com/merchants/answer/7052112)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, HTTP, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, raw HTTP examples, OAuth and API key handling guidance, and approval checkpoints for write-capable operations.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
