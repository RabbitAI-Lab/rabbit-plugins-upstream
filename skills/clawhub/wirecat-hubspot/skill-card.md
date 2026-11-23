## Description:

Use hubspot to read and change a HubSpot account's CRM - deals, leads, pipelines and stages, contacts (people), companies (organizations), owners (users), notes, calls, e-mails, meetings and tasks - with the owner's profile and JSON answers. Deals with their contacts and companies are synced into the local WireCat store and read offline, and `changes list` shows what changed for a morning digest. Use when a question could be answered from the owner's HubSpot sales data (how a deal stands, what is open, what changed, who a client is), to create, update, move or close a deal, change a contact or company, add a note or a task, or to set hubspot up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

HubSpot account owners and their agents use the CLI to review sales CRM data, sync records for offline queries, and create or update deals, contacts, companies, notes, and tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan flagged ticket-management commands beyond the stated sales CRM scope, and its coverage was partial.

Mitigation: Review whether that functionality is needed and inspect the relevant command guidance, especially destructive actions, before installation or use.

## Reference(s):

- [HubSpot CLI skill release](https://clawhub.ai/wirecat/skills/wirecat-hubspot)
- [HubSpot API command groups](artifact/references/api.md)
- [HubSpot API basic commands](artifact/references/api/api-basic.md)
- [HubSpot API batch commands](artifact/references/api/api-batch.md)
- [HubSpot API search commands](artifact/references/api/api-search.md)
- [HubSpot API advanced commands](artifact/references/api/api-advanced.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON CRM results with concise natural-language answers; shell command examples and setup guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers may depend on the local store's sync age, completeness, and reported issues.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
