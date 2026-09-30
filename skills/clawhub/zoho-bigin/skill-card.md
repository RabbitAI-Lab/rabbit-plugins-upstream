## Description:

Helps agents manage Zoho Bigin CRM records and approved sales automations through a Maton-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and their agents use this skill to find and manage Zoho Bigin contacts, companies, pipelines, and products, and to set up explicitly approved CRM automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CRM writes or deletions could change business records unexpectedly.

Mitigation: Default to read-only actions and confirm the exact connection, module, and intended change with the user before writing or deleting.

Risk: Broad OAuth permissions could expose more CRM data than the task requires.

Mitigation: Obtain approval before connecting and select the narrowest available OAuth scopes.

Risk: Functions, triggers, or destinations can continue performing actions or forwarding data after setup.

Mitigation: Require explicit approval for automation and destinations, confirm where data will flow, and remove automations when no longer needed.

## Reference(s):

- [Zoho Bigin skill on ClawHub](https://clawhub.ai/byungkyu/skills/zoho-bigin)
- [Zoho Bigin API documentation](https://www.bigin.com/developer/docs/apis/v2/)
- [Maton](https://maton.ai)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, code, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CRM record summaries and instructions for approved automations.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
