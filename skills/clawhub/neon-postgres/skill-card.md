## Description:

Guides developers working with existing Neon Postgres databases through connections, migrations, performance diagnostics, branching, scaling, replication, and search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure and troubleshoot existing Neon Postgres databases, plan safe schema changes, and implement database search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Database connection strings and environment files may expose credentials.

Mitigation: Confirm the intended project and keep connection strings and environment files out of shared output.

Risk: Migrations, extensions, and indexes can modify a live database.

Mitigation: Review commands and test schema changes on a branch before applying them to production.

Risk: Embedding calls may send private or regulated document text to a provider.

Mitigation: Obtain approval for the provider and data before sending text to generate embeddings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/andrelandgraf/skills/neon-postgres)
- [Neon connection methods](https://neon.com/docs/connect/choose-connection.md)
- [Neon database inspection](https://neon.com/docs/cli/inspect.md)
- [Lakebase Search getting started](https://neon.com/docs/ai/lakebase-search-get-started)
- [Vector search](references/vector-search.md)
- [Full-text search](references/full-text-search.md)
- [Hybrid search](references/hybrid-search.md)
- [Managing Lakebase Search with Drizzle](references/lakebase-search-drizzle.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with SQL, TypeScript, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on the existing Neon project and database configuration.]

## Skill Version(s):

1.0.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
