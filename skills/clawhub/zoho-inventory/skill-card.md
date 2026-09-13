## Description:

Zoho Inventory API integration with managed OAuth for managing items, sales orders, invoices, purchase orders, bills, contacts, shipments, and related inventory records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read and manage Zoho Inventory business records through Maton-managed OAuth, CLI commands, raw HTTP fallbacks, and optional approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automation features can create persistent workflows that keep acting after the initial request.

Mitigation: Confirm each trigger, destination, hosted function, and --exec watch separately; scope them narrowly and delete them when no longer needed.

Risk: Write operations or connection changes can alter Zoho Inventory business records or authorization state.

Mitigation: Default to read and list calls, and require explicit user confirmation before creating connections or running POST, PUT, PATCH, or DELETE actions.

Risk: Long-lived API keys and unexpected package sources increase credential and install trust risk.

Mitigation: Prefer OAuth through expected Maton package sources and avoid exposing API keys through environment variables unless the CLI cannot be installed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-inventory)
- [Maton Homepage](https://maton.ai)
- [Zoho Inventory API v1 Introduction](https://www.zoho.com/inventory/api/v1/introduction/)
- [Zoho Inventory Items API](https://www.zoho.com/inventory/api/v1/items/)
- [Zoho Inventory Contacts API](https://www.zoho.com/inventory/api/v1/contacts/)
- [Zoho Inventory Sales Orders API](https://www.zoho.com/inventory/api/v1/salesorders/)
- [Zoho Inventory Invoices API](https://www.zoho.com/inventory/api/v1/invoices/)
- [Zoho Inventory Purchase Orders API](https://www.zoho.com/inventory/api/v1/purchaseorders/)
- [Zoho Inventory Bills API](https://www.zoho.com/inventory/api/v1/bills/)
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

**Output Format:** [Markdown with inline shell commands, code snippets, configuration examples, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated API calls, connection setup, hosted function code, and trigger configuration for user-approved Zoho Inventory workflows.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
