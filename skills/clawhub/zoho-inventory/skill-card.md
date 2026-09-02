## Description:

Zoho Inventory API integration with managed OAuth for managing items, sales orders, invoices, purchase orders, bills, contacts, and shipments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Zoho Inventory records through Maton-managed OAuth, including reading, creating, updating, and deleting inventory, ordering, billing, contact, and shipment data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may gain access to a Zoho Inventory account through Maton.

Mitigation: Install only when that access is intended, prefer OAuth, review requested Zoho scopes, and create connections only after explicit user approval.

Risk: Write, delete, email, billing, or status-changing operations can modify business records or notify external parties.

Mitigation: Default to read/list calls first and require explicit approval after checking exact record IDs, payloads, and intended effects.

Risk: Long-lived API keys or provider tokens can leak through logs, shell history, files, or command-line arguments.

Mitigation: Use OAuth and the operating system credential store when possible; do not print, persist, or pass credentials on command lines, and use the raw HTTP fallback only when the CLI is unavailable.

Risk: Requests may target the wrong Maton account or Zoho Inventory connection when multiple profiles or connections exist.

Mitigation: Specify the intended connection and profile whenever more than one is available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-inventory)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Inventory API v1 Introduction](https://www.zoho.com/inventory/api/v1/introduction/)
- [Zoho Inventory Items API](https://www.zoho.com/inventory/api/v1/items/)
- [Zoho Inventory Invoices API](https://www.zoho.com/inventory/api/v1/invoices/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a valid Zoho Inventory connection.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
