## Description:

Helps agents inspect and manage Cargo workspace storage, including models, datasets, columns, relationships, records, unification, webhook-fed models, and SQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide agents through Cargo workspace storage tasks such as discovering schemas, creating or updating models and columns, defining relationships, querying records, and configuring unification or webhook ingestion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Cargo CLI access can expose or use workspace API tokens.

Mitigation: Use a dedicated low-privilege token where possible, avoid printing tokens in transcripts, and rotate any token that is displayed or shared.

Risk: The skill can guide high-impact storage changes such as creating, updating, removing, or unifying models, columns, relationships, and records.

Mitigation: Confirm backups, dependencies, identifiers, and intended changes before executing write commands.

Risk: Relationship updates replace the dataset relationship set and can remove existing relationships if they are omitted from the payload.

Mitigation: List existing relationships first and send back the complete relationship array, preserving existing UUIDs.

## Reference(s):

- [Cargo Storage skill page](https://clawhub.ai/cargo-ai/skills/cargo-storage)
- [Cargo publisher profile](https://clawhub.ai/user/cargo-ai)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [Model examples](references/examples/models.md)
- [Column examples](references/examples/columns.md)
- [Storage query examples](references/examples/queries.md)
- [Ingest webhook examples](references/examples/ingest-webhook.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Cargo CLI commands that read or change workspace storage; command results are JSON on stdout and errors are JSON with non-zero exit status.]

## Skill Version(s):

1.2.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
