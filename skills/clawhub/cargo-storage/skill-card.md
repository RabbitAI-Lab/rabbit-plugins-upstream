## Description:

Manage models, datasets, columns, and relationships and query workspace storage with SQL using the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and modify Cargo workspace storage: models, datasets, columns, relationships, records, SQL queries, exports, and ingest webhook flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Cargo CLI storage commands can delete models or columns and export workspace data.

Mitigation: Require explicit confirmation of the workspace, target identifiers, operation, and expected data impact before destructive or export tasks.

Risk: Webhook URLs, API tokens, and signed download URLs can expose workspace data or write access if shared.

Mitigation: Treat these values as secrets; avoid placing them in tickets, commits, logs, reports, or shared chats, and prefer token headers when supported.

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

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference Cargo CLI command output, SQL snippets, identifiers, signed download URLs, webhook URLs, and API token handling guidance.]

## Skill Version(s):

1.2.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
