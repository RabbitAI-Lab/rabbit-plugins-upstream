## Description:

Use b24 to read and change a Bitrix24 portal's CRM — deals, leads, contacts (people), companies (organizations), pipelines, stages, products, employees — with the owner's profile and JSON answers; deals and leads are synced into the local WireCat store. Use when a task needs the owner's Bitrix24 sales data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent to work with the owner's Bitrix24 sales data can use this skill to inspect CRM records and perform permitted CRM updates through the owner's configured profile. It also explains how to sync and query deals and leads and how to handle limits in portal data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A CRM write may have an unknown outcome, and retrying it can create a duplicate change.

Mitigation: After outcome_unknown, sync and show the record before attempting the write again.

Risk: CRM records can contain personal contact details.

Mitigation: Keep access within the owner's selected-client scope and show only the specific person or organization needed.

## Reference(s):

- [Bitrix24 Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-b24)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON CRM records and status responses with concise text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CRM reads and writes are limited by the configured profile's permissions and the owner's selected sync scope.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
