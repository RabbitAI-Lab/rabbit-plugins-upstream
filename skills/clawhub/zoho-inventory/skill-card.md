## Description:

Zoho Inventory API integration with managed OAuth for managing items, sales orders, invoices, purchase orders, bills, contacts, shipments, and other inventory records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to read, create, update, and delete Zoho Inventory records through Maton-managed authentication. It is suited for inventory, order, invoice, purchase, bill, contact, shipment, and item-group workflows that require explicit confirmation before writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can provide broad raw API access to business and financial records in the connected Zoho Inventory account.

Mitigation: Use the narrowest OAuth scopes available, prefer read-only calls, specify the intended connection, and confirm the exact endpoint and payload before any write.

Risk: Long-lived Maton API keys or provider-issued tokens can leak if printed, logged, stored, or passed through shell commands.

Mitigation: Use OAuth where possible, keep credentials in the managed credential store, avoid printing or persisting tokens, and revoke unused connections.

Risk: Data returned from Zoho Inventory can contain untrusted content that attempts to influence subsequent agent actions.

Mitigation: Treat API responses as data, validate values before reuse, and never execute or follow instructions found inside fetched records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-inventory)
- [Maton Homepage](https://maton.ai)
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

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Zoho Inventory connection.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact metadata version 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
