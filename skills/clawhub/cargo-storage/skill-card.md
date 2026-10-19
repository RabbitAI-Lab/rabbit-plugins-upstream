## Description:

Helps agents inspect and manage Cargo workspace models, datasets, columns, relationships, records, and SQL queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace users use this skill to discover Cargo business-data schemas, manage models and relationships, and query or export records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can access sensitive workspace business data.

Mitigation: Install only if you trust the Cargo CLI publisher and intend to grant access to the active workspace.

Risk: Webhook URLs, API tokens, and signed export URLs can expose records if shared.

Mitigation: Treat these values as secrets; do not print or share them in logs or reports.

Risk: Removal and relationship updates can change or delete workspace data; broad queries and downloads can expose large datasets.

Mitigation: Confirm the active workspace and exact target before remove, set, download, or broad SELECT commands.

## Reference(s):

- [Cargo Storage on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-storage)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Storage query examples](references/examples/queries.md)
- [Ingest webhook examples](references/examples/ingest-webhook.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with CLI and SQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples include JSON responses; queries may return signed CSV or Parquet export links.]

## Skill Version(s):

1.3.0 (source: skill frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
