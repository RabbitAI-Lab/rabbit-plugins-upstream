## Description: <br>
Zoho Inventory API integration with managed OAuth for managing items, sales orders, invoices, purchase orders, bills, contacts, and shipments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents supporting inventory workflows use this skill to read, create, update, and delete Zoho Inventory records through Maton-managed OAuth. Write operations should be reviewed with the user before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access and modify records in a connected Zoho Inventory account through Maton-mediated OAuth. <br>
Mitigation: Install only if you trust Maton for this account, use the least-privileged Zoho connection available, and confirm the target resource and intended effect before approving create, update, or delete operations. <br>
Risk: The MATON_API_KEY grants access to Maton-managed connections. <br>
Mitigation: Keep the key private, provide it only in trusted runtime environments, and rotate it if exposure is suspected. <br>
Risk: Multiple active Zoho Inventory connections can cause requests to target the wrong account. <br>
Mitigation: Specify the intended connection with the Maton-Connection header whenever more than one active connection exists. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-inventory) <br>
- [Zoho Inventory API v1 Introduction](https://www.zoho.com/inventory/api/v1/introduction/) <br>
- [Zoho Inventory Items API](https://www.zoho.com/inventory/api/v1/items/) <br>
- [Zoho Inventory Contacts API](https://www.zoho.com/inventory/api/v1/contacts/) <br>
- [Zoho Inventory Sales Orders API](https://www.zoho.com/inventory/api/v1/salesorders/) <br>
- [Zoho Inventory Invoices API](https://www.zoho.com/inventory/api/v1/invoices/) <br>
- [Zoho Inventory Purchase Orders API](https://www.zoho.com/inventory/api/v1/purchaseorders/) <br>
- [Zoho Inventory Bills API](https://www.zoho.com/inventory/api/v1/bills/) <br>
- [Maton API Key Settings](https://maton.ai/settings) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline Python, curl, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and a connected Zoho Inventory account.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
