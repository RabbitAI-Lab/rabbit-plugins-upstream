## Description:

Manage Cargo workspace data by inspecting and modifying models, datasets, columns, relationships, records, and SQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Cargo workspace operators use this skill to inspect and manage storage data, including models, datasets, schema, relationships, records, and SQL queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webhook setup can expose an existing workspace API token without confirming that its permissions are appropriate.

Mitigation: Choose a dedicated token with no unnecessary permissions, prefer header authentication where supported, and keep credentials out of shared transcripts and logs.

Risk: Storage changes or reset operations may affect the wrong workspace, delete data, or incur additional costs.

Mitigation: Confirm the active workspace and review deletions and reset costs before running write or reset commands; pin a reviewed CLI version.

## Reference(s):

- [Cargo Storage release on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-storage)
- [Cargo Skills project homepage](https://github.com/getcargohq/cargo-skills)
- [Model examples](references/examples/models.md)
- [Dataset examples](references/examples/datasets.md)
- [Column examples](references/examples/columns.md)
- [Storage query examples](references/examples/queries.md)
- [Webhook ingestion examples](references/examples/ingest-webhook.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, SQL queries, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, SQL, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and examples are tailored to the user's Cargo workspace and requested data task.]

## Skill Version(s):

1.5.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
