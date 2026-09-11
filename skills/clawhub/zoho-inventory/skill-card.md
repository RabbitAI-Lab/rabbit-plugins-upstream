## Description:

Zoho Inventory API integration with managed OAuth for managing items, sales orders, invoices, purchase orders, bills, contacts, and shipments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to connect agents to Zoho Inventory through Maton-managed OAuth, then list, read, create, update, or delete inventory, order, billing, contact, and shipment records with user-confirmed API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho Inventory write operations can create, update, delete, email, or change the status of business records.

Mitigation: Default to read and list calls, then require explicit user confirmation of the exact target, payload, and intended effect before any create, update, delete, email, or status-change operation.

Risk: The Maton API passthrough can reach any Zoho Inventory endpoint allowed by the connected account, including endpoints outside the documented intended surface.

Mitigation: Use OAuth with the narrowest available Zoho scopes, specify the intended connection when multiple accounts exist, and keep calls limited to the user's current task.

Risk: CLI or API-key setup can expose long-lived credentials if handled incorrectly.

Mitigation: Prefer OAuth, keep credentials in the operating system credential store, avoid printing or persisting tokens, and isolate or pin CLI/SDK installation where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-inventory)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
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

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and valid Zoho Inventory authorization; responses may contain business or personal data.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
