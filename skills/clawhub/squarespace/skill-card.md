## Description:

Squarespace Commerce API integration with managed OAuth for managing products, inventory, orders, customer profiles, and transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to a Squarespace store through Maton-managed OAuth, inspect commerce data, and carry out approved store operations. It supports read-first workflows for inventory, orders, products, customer profiles, and transactions, with explicit approval required for writes, new connections, and automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Squarespace commerce data such as customer profiles, orders, transactions, products, and inventory through the user's authorized connection.

Mitigation: Use OAuth where possible, connect only the account and scopes needed for the task, prefer read/list calls first, and avoid logging or forwarding full commerce responses.

Risk: Write operations, new connections, hosted functions, and automations can create persistent or high-impact changes.

Mitigation: Require separate user approval for each write, connection, function deployment or invocation, trigger, and destination; confirm the target resource, payload, and intended effect before execution.

Risk: Trigger destinations can create ongoing data flows to external URLs, including customer, order, transaction, email, or payment data.

Mitigation: Keep triggers and destinations narrowly scoped, prefer Maton-owned destinations, and forward commerce or third-party event data to external hosts only when the user explicitly approves the host and data fields.

Risk: API-key authentication can expose a long-lived credential if it is exported or embedded in commands, files, or destinations.

Mitigation: Prefer Maton OAuth, keep credentials in the operating system credential store, and never print, store, export, or place Maton or provider credentials in destination headers or body templates.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/squarespace)
- [Maton Homepage](https://maton.ai)
- [Squarespace Commerce APIs Overview](https://developers.squarespace.com/commerce-apis/overview)
- [Squarespace Inventory API](https://developers.squarespace.com/commerce-apis/inventory-overview)
- [Squarespace Orders API](https://developers.squarespace.com/commerce-apis/orders-overview)
- [Squarespace Products API](https://developers.squarespace.com/commerce-apis/products-overview)
- [Squarespace Profiles API](https://developers.squarespace.com/commerce-apis/profiles-overview)
- [Squarespace Transactions API](https://developers.squarespace.com/commerce-apis/transactions-overview)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, HTTP examples, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved Squarespace authorization.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
