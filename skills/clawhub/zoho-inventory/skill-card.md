## Description:

Helps agents manage Zoho Inventory items, orders, invoices, bills, contacts, and shipments through an authorized account connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People managing a Zoho Inventory account use this skill to look up and, with approval, create, update, or delete inventory and business records. It also provides guidance for account connections and optional automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized access can expose or change inventory and financial records.

Mitigation: Prefer read-only scopes and confirm each write or deletion against the intended account and record.

Risk: Third-party trigger destinations may forward matching events automatically over time.

Mitigation: Approve each destination separately and verify what data it forwards and for how long.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/byungkyu/skills/zoho-inventory)
- [Maton homepage](https://maton.ai)
- [Zoho Inventory API introduction](https://www.zoho.com/inventory/api/v1/introduction/)
- [Zoho Inventory items API](https://www.zoho.com/inventory/api/v1/items/)
- [Scheduled trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for authorized Zoho Inventory requests and optional automations.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
