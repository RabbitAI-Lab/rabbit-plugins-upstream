## Description:

Use b24 to read and change a Bitrix24 portal's CRM — deals, leads, contacts (people), companies (organizations), pipelines, stages, products, employees — with the owner's profile and JSON answers. Use when a task needs the owner's Bitrix24 sales data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Bitrix24 portal users use this skill to inspect CRM records and create, update, or move records with the b24 CLI, guided by their account profile and permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can create, update, or move CRM records using the configured Bitrix24 profile.

Mitigation: Use the intended account profile with only the permissions needed, preview consequential changes with --dry-run, and retain each operation_id to recover safely from uncertain write outcomes.

Risk: The external @wirecat/bitrix24-cli package was not audited as part of the supplied security review.

Mitigation: Review the CLI package and its permissions before installation, and run it only with the intended Bitrix24 account configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wirecat/skills/wirecat-b24)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands include read and write operations; consequential writes can be previewed with --dry-run.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
