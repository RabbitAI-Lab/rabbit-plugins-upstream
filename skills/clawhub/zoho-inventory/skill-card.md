## Description:

Zoho Inventory API integration with managed OAuth for managing items, sales orders, invoices, purchase orders, bills, contacts, shipments, and related inventory records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Zoho Inventory through Maton-managed OAuth, inspect inventory and business records, and perform user-approved CRUD operations or automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify Zoho Inventory business data through a connected account.

Mitigation: Use least-privilege Zoho scopes, default to read and list operations, and require explicit user confirmation before every write or delete.

Risk: Hosted functions, triggers, or destinations can run or forward data persistently after setup.

Mitigation: Create or update automation only after the user approves the exact function, connection, destination host, payload fields, and persistence behavior.

Risk: API keys or OAuth credentials could be exposed if handled outside the documented Maton credential flow.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, and avoid printing, exporting, logging, or embedding secrets in destinations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-inventory)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Inventory API v1 Introduction](https://www.zoho.com/inventory/api/v1/introduction/)
- [Zoho Inventory Items API](https://www.zoho.com/inventory/api/v1/items/)
- [Zoho Inventory Contacts API](https://www.zoho.com/inventory/api/v1/contacts/)
- [Zoho Inventory Sales Orders API](https://www.zoho.com/inventory/api/v1/salesorders/)
- [Zoho Inventory Invoices API](https://www.zoho.com/inventory/api/v1/invoices/)
- [Zoho Inventory Purchase Orders API](https://www.zoho.com/inventory/api/v1/purchaseorders/)
- [Zoho Inventory Bills API](https://www.zoho.com/inventory/api/v1/bills/)
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

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing operational guidance for authenticated Zoho Inventory API calls and optional Maton automation setup.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
