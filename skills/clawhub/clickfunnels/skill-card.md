## Description:

ClickFunnels API integration with managed OAuth for managing contacts, products, orders, courses, forms, webhooks, sales funnels, and marketing automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with ClickFunnels sales-funnel data and automations through Maton-managed OAuth. It supports read-first workflows and user-approved changes to contacts, products, orders, courses, forms, webhooks, functions, and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A write, deletion, webhook, function, trigger, or destination can change business data or create an ongoing data flow.

Mitigation: Require explicit user approval for the exact target, payload, intended effect, and persistence before executing the operation.

Risk: Credentials or long-lived API keys can be exposed through environment variables, command lines, logs, files, or stored destination templates.

Mitigation: Prefer OAuth and operating-system credential storage, avoid printing or exporting secrets, and never place Maton or provider credentials in trigger destination headers or bodies.

Risk: Ambiguous accounts or connections can send a read or write to the wrong ClickFunnels workspace.

Mitigation: Confirm the intended Maton account and ClickFunnels connection, use explicit profile and connection selection when more than one exists, and prefer least-privilege scopes.

Risk: External API responses and event payloads may contain untrusted data that could influence follow-up actions.

Mitigation: Treat fetched content as data, validate fields before use, do not execute or interpolate it into shell commands, and require user-reviewed handlers for local or hosted automation.

## Reference(s):

- [ClawHub ClickFunnels Skill](https://clawhub.ai/byungkyu/skills/clickfunnels)
- [Maton Homepage](https://maton.ai)
- [ClickFunnels API Introduction](https://developers.myclickfunnels.com/docs/intro)
- [ClickFunnels API Reference](https://developers.myclickfunnels.com/reference)
- [ClickFunnels Pagination Guide](https://developers.myclickfunnels.com/docs/pagination)
- [ClickFunnels Filtering Guide](https://developers.myclickfunnels.com/docs/filtering)
- [ClickFunnels Webhooks Overview](https://developers.myclickfunnels.com/docs/webhooks)
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

**Output Format:** [Markdown guidance with CLI commands, API request examples, JSON examples, and short code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an approved ClickFunnels connection for live operations.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
