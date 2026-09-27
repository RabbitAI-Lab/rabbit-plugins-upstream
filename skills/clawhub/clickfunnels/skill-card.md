## Description:

ClickFunnels API integration with managed OAuth for managing contacts, products, orders, courses, forms, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access ClickFunnels through Maton for sales funnel, contact, order, product, course, form, webhook, and automation tasks. It is intended for authenticated account operations where reads are preferred first and writes, new connections, hosted functions, triggers, or forwarding require user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated ClickFunnels access can expose customer and business data through the connected account.

Mitigation: Install only when Maton access is intended, prefer OAuth, review requested scopes, connect only needed accounts, and default to read or list calls before changing data.

Risk: Writes, new connections, hosted functions, triggers, and persistent forwarding can modify data or create continuing data flows.

Mitigation: Require explicit user approval for each write, connection, automation, trigger destination, or forwarding path, and state what data will be sent and for how long.

Risk: Third-party forwarding can disclose customer, payment, mailbox, repository, workspace, or conversation data beyond Maton and ClickFunnels.

Mitigation: Prefer Maton-controlled destinations, use narrow trigger scopes and minimal body templates, and avoid third-party hosts unless the user has approved the exact destination and payload.

Risk: Raw HTTP fallback with MATON_API_KEY uses a long-lived credential that can leak through logs, shell history, or child processes.

Mitigation: Use the Maton CLI with OAuth when possible; if raw HTTP is required, keep the key in a secret-backed environment variable, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/clickfunnels)
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

**Output Format:** [Markdown guidance with CLI commands, HTTP examples, JSON examples, and code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized ClickFunnels connection.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
