## Description:

Use b24 to read and change a Bitrix24 portal's CRM — deals, leads, contacts (people), companies (organizations), pipelines, stages, products, employees — with the owner's profile and JSON answers; deals and leads are synced into the local WireCat store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

People working with a Bitrix24 sales portal can use this skill to inspect CRM records and pipelines, sync deals and leads for offline reading, and create or update records within the selected profile's permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retrying a write after an unknown outcome can create a duplicate CRM record.

Mitigation: Sync the local store and show the record to confirm whether the first write succeeded before retrying.

Risk: CRM reads and writes use the selected profile's webhook permissions and may expose or change portal data.

Mitigation: Check the active session and permissions, select the intended profile, and use the command's dry-run option where available before writes.

## Reference(s):

- [Bitrix24 Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-b24)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration instructions, CRM data]

**Output Format:** [JSON results and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deals and leads can be read from the locally synced store; write commands can change CRM records according to the selected profile's permissions.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
