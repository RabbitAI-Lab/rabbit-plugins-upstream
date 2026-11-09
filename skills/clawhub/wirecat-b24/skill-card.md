## Description:

Use b24 to read and change a Bitrix24 portal's CRM — deals, leads, contacts (people), companies (organizations), pipelines, stages, products, employees — with the owner's profile and JSON answers; deals and leads are synced into the local WireCat store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Bitrix24 account owners and their authorized agents use this skill to inspect and manage CRM records through the b24 CLI, with sync scope and changes limited by the selected profile's permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CRM create, update, close, and delete commands can change portal records, and repeated writes after an unclear outcome may create duplicate changes.

Mitigation: Check the selected profile and permissions, confirm the target record before writing, and sync and inspect the record after an unclear outcome before retrying.

## Reference(s):

- [Bitrix24 Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-b24)
- [WireCat publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON CLI answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands for reading CRM data and making permission-scoped CRM changes.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
