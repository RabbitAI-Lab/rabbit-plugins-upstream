## Description:

Zoho Inventory API integration with managed OAuth for managing items, sales orders, invoices, purchase orders, bills, contacts, shipments, and related inventory records through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Zoho Inventory business records through Maton-managed OAuth or, where the CLI cannot be installed, direct Maton API calls. It is suited for account-connected inventory workflows that need read, create, update, delete, status-change, email, payment, credit, and shipment operations with user confirmation for writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a connected Zoho Inventory account and modify business records through Maton.

Mitigation: Use the narrowest available Zoho scopes, prefer read-only access where possible, and require explicit confirmation before every create, update, delete, email, payment, credit, or status-change action.

Risk: Multiple Maton profiles or Zoho Inventory connections could send a request to the wrong account.

Mitigation: Specify the intended profile and connection when more than one exists, and verify resource identifiers with read or list calls before writes.

Risk: Long-lived Maton API keys can be exposed through environment variables, logs, shell history, or command output when the CLI is unavailable.

Mitigation: Prefer OAuth through the Maton CLI; if raw HTTP is necessary, read the key only from the process environment, never print or persist it, and rotate it if exposed.

Risk: Zoho Inventory responses can contain personal, financial, or business-sensitive data.

Mitigation: Return only fields needed for the task and avoid dumping raw responses into logs, files, or user-visible output unless explicitly requested.

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

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes API endpoint paths, request examples, credential-handling guidance, and confirmation requirements for write operations.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
