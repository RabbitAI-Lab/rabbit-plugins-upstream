## Description:

Manage models, datasets, columns, and relationships and query workspace storage with SQL using the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and modify Cargo workspace storage, including models, datasets, columns, relationships, records, and SQL queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward destructive storage changes such as model or column deletion.

Mitigation: Require explicit user confirmation before deletion or other irreversible storage changes.

Risk: The skill can guide agents to create or expose token-bearing ingest webhook URLs.

Mitigation: Prefer scoped or newly created low-permission ingest tokens, avoid logging token-bearing URLs, and rotate any token that may have been exposed.

Risk: The skill can guide broad data exports from workspace storage.

Mitigation: Use scoped queries and exports only when needed, and review output destinations before sharing signed download URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-storage)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)
- [Model examples](references/examples/models.md)
- [Dataset examples](references/examples/datasets.md)
- [Column examples](references/examples/columns.md)
- [Storage query examples](references/examples/queries.md)
- [Ingest webhook examples](references/examples/ingest-webhook.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline bash, JSON, SQL, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Cargo CLI commands that inspect, change, export, or query workspace storage.]

## Skill Version(s):

1.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
