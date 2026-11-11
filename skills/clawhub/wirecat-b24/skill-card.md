## Description:

Use b24 to read and change a Bitrix24 portal's CRM — deals, leads, contacts (people), companies (organizations), pipelines, stages, products, employees — with the owner's profile and JSON answers; deals and leads are synced into the local WireCat store. Use when a task needs the owner's Bitrix24 sales data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and sales teams use this skill to inspect and update the CRM records available to the owner's configured Bitrix24 account, including deals, leads, contacts, companies, pipelines, stages, products, and employees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A clean scan does not guarantee zero risk; this skill can read customer CRM data and change records.

Mitigation: Use the owner's configured profile, request only the records needed, and confirm the target and requested change before writing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wirecat/skills/wirecat-b24)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and concise natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or change Bitrix24 CRM records within the configured profile's permissions.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
